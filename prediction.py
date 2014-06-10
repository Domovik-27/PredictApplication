import webapp2

from views import MatchList, UsersList, NewPredict, MatchPlayed


application = webapp2.WSGIApplication([
    ('/', UsersList),
    ('/new_predict', NewPredict),
    ('/schedule', MatchList),
    ('/addmatch', MatchPlayed)
], debug=True)
