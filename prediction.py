import webapp2

from views import MatchList, UsersList, NewPredict


application = webapp2.WSGIApplication([
    ('/', UsersList),
    ('/new_predict', NewPredict),
    ('/schedule', MatchList)
], debug=True)
