#!/usr/bin/python
# -*- coding: UTF-8 -*-

from google.appengine.ext import ndb


class User(ndb.Model):
    """User entity"""
    firstname = ndb.StringProperty()
    lastname = ndb.StringProperty()

class Match(ndb.Model):
	"""Match entity"""
	group = ndb.StringProperty(indexed=False)
	home_team = ndb.StringProperty(indexed=False)
	guest_team = ndb.StringProperty(indexed=False)
	home_goals = ndb.IntegerProperty()
	guest_goals = ndb.IntegerProperty()
	start = ndb.DateTimeProperty()
	
	index = 0
	formattedStart = ""

	def setFormattedStart(self):
		self.formattedStart = self.start.strftime("%d/%m  %H:%M")


class Prediction(ndb.Model):
	"""Prediction entity"""
	user_key = ndb.KeyProperty()
	match_key = ndb.KeyProperty()
	home_goals = ndb.IntegerProperty()
	guest_goals = ndb.IntegerProperty()

class GroupAndMatches():
	name = ""
	matches = []

class UserPrediction():
	score = None
	points = None
	def setScore(self, score):
		self.score = score
	def setPoints(self, points):
		self.points = points

class VisualPrediction():
	match = None
	score = None
	pred_scores = None

	def __init__(self):
		self.pred_scores = []

	def setMatch(self, match):
		self.match = match

	def setScore(self, score):
		self.score = score

	def addPredScore(self, pred_score):
		self.pred_scores.append(pred_score)


from preload import DataPreloader
preloader = DataPreloader()


class DataProvider():
	"""Wrapper on data model"""

	#def __init__(self):
		#ndb.delete_multi([m.key for m in self.get_matches()])

	def get_users(self):
		return User.query().fetch()

	def create_matches(self):
		matches = preloader.create_matches()
		for m in matches:
			m.put()

	def get_matches(self):
		matches = Match.query().order(Match.start).fetch()
		if len(matches) == 0:
			self.create_matches()
			matches = Match.query().order(Match.start).fetch()

		#prepare for visual representation
		i = 0
		for m in matches:
			m.index = i
			m.setFormattedStart()
			i = i+1

		return matches

	def get_matches_groupped(self):
		matches = self.get_matches()

		#combine by groups
		groupsDict = {}
		for m in matches:
			gr = m.group
			if not gr in groupsDict:
				groupsDict[gr] = []
			groupsDict[gr].append(m)

		#convert dictionary to objects list
		groups = []
		keys = ["A", "B", "C", "D", "E", "F", "G", "H"]
		for key in keys:
			group = GroupAndMatches()
			group.name = key
			group.matches = groupsDict[key]
			groups.append(group)

		#we need another matches indexes
		i = 0
		for g in groups:
			for m in g.matches:
				m.index = i
				i = i+1

		return groups

	def get_user_unique(self, firstname, lastname):
		users = User.query(ndb.AND(User.firstname==firstname,User.lastname==lastname)).fetch()
		if len(users) < 1:
			user = User()
			user.firstname = firstname
			user.lastname = lastname
			user.put()
		else:
			user = users[0]
		return user

	def add_prediction(self, params):
		firstname = params["firstname"]
		lastname = params["lastname"]

		user = self.get_user_unique(firstname, lastname)
		groups = self.get_matches_groupped()

		for group in groups:
			for match in group.matches:
				predict = Prediction()
				predict.user_key = user.key
				predict.match_key = match.key
				predict.home_goals = int(params["l"+str(match.index)])
				predict.guest_goals = int(params["r"+str(match.index)])
				predict.put()

	def get_predictions(self):
		matches = self.get_matches()
		users = self.get_users()

		result = []

		for match in matches:
			vpred = VisualPrediction()

			vpred.setMatch(match.group + ": " + match.home_team + " - " + match.guest_team)
			if match.home_goals == None:
				vpred.setScore(match.formattedStart)
			else:
				vpred.setScore(str(match.home_goals) + "-" + str(match.guest_goals))

			#query = Prediction.query(Prediction.match_key == match.key)
			for user in users:
				pred = Prediction.query(ndb.AND(Prediction.match_key==match.key,
					Prediction.user_key==user.key)).fetch()[0]

				upred = UserPrediction()
				upred.setScore(str(pred.home_goals) + "-" + str(pred.guest_goals))
				
				pts = self.points_by_score(match.home_goals,match.guest_goals,pred.home_goals,pred.guest_goals)
				upred.setPoints(pts)

				vpred.addPredScore(upred)

			result.append(vpred)

		return result
	
	def points_by_score(self, m_home, m_guest, u_home, u_guest):
		if m_home == None or m_guest == None or u_home == None or u_guest == None:
			return "-"

		if m_home == u_home and m_guest == u_guest:
			return 4

		if m_home > m_guest and u_home > u_guest:
			return 2
		if m_home < m_guest and u_home < u_guest:
			return 2
		if m_home == m_guest and u_home == u_guest:
			return 2

		if m_home == u_guest and m_guest == u_home:
			return 1

		return 0

	def match_played(self, home_goals, guest_goals):
		matches = Match.query().order(Match.start).fetch()
		for match in matches:
			if match.home_goals == None:
				match.home_goals = int(home_goals)
				match.guest_goals = int(guest_goals)
				match.put()
				return None
