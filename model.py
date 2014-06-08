from google.appengine.ext import ndb


class User(ndb.Model):
    """User entity"""
    firstname = ndb.StringProperty(indexed=False)
    lastname = ndb.StringProperty(indexed=False)

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
	#user = ndb.ReferenceProperty(User)
	#match = ndb.ReferenceProperty(Match)
	home_goals = ndb.IntegerProperty()
	guest_goals = ndb.IntegerProperty()

class GroupAndMatches():
	name = ""
	matches = []


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

	def add_user(self, firstname, lastname):
		user = User()
		user.firstname = firstname
		user.lastname = lastname
		user.put()