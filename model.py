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

class Prediction(ndb.Model):
	"""Prediction entity"""
	#user = ndb.ReferenceProperty(User)
	#match = ndb.ReferenceProperty(Match)
	home_goals = ndb.IntegerProperty()
	guest_goals = ndb.IntegerProperty()


from preload import DataPreloader
preloader = DataPreloader()


class DataProvider():
	"""Wrapper on data model"""

	#def __init__(self):
		#ndb.delete_multi([m.key for m in self.get_matches()])

	def get_users(self):
		return User.query().order(User.lastname).fetch()

	def create_matches(self):
		matches = preloader.create_matches()
		for m in matches:
			m.put()

	def get_matches(self):
		matches = Match.query().order(Match.start).fetch()
		if len(matches) == 0:
			self.create_matches()
			matches = Match.query().order(Match.start).fetch()

		i = 0
		for m in matches:
			m.index = i
			i = i+1

		return matches