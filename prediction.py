import webapp2

from views import MatchList, UsersList, PredictionsDetailed, NewPredict, MatchPlayed


application = webapp2.WSGIApplication([
    ('/', UsersList),
    ('/details', PredictionsDetailed),
    ('/new_predict', NewPredict),
    ('/schedule', MatchList),
    #('/addmatch', MatchPlayed)
], debug=True)
