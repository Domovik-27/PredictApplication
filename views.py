import os
import webapp2
import jinja2
import urllib
import time

from model import DataProvider
from google.appengine.ext.webapp import template
from datetime import datetime


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


dataProvider = DataProvider()

class MatchList(webapp2.RequestHandler):
	"""Schedule of group stage"""

	def get(self):
		params = {
			"groups" : dataProvider.get_matches_groupped()
		} 
		template = JINJA_ENVIRONMENT.get_template('schedule.html')
		self.response.out.write(template.render(params))


class UsersList(webapp2.RequestHandler):
	def get(self):
		params = {
			"users" : dataProvider.get_users(),
			"matches" : dataProvider.get_matches(),
			"predictions" : dataProvider.get_predictions()
		} 
		template = JINJA_ENVIRONMENT.get_template('users.html')
		self.response.out.write(template.render(params))


class NewPredict(webapp2.RequestHandler):
	def get(self):
		params = {
			"groups" : dataProvider.get_matches_groupped()
		} 
		template = JINJA_ENVIRONMENT.get_template('new_predict.html')
		self.response.out.write(template.render(params))

	def post(self):
		params = self.request.POST

		#firstname = params[u'firstname']
		#lastname = params[u'lastname']

		dataProvider.add_prediction(params)

		time.sleep(0.5)
		self.redirect('/')
