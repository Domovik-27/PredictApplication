import webapp2

from views import MatchList, UsersList, PredictionsDetailed, NewPredict, MatchPlayed, ClearMatches


application = webapp2.WSGIApplication([
    ('/', UsersList),
    ('/details', PredictionsDetailed),
    ('/new_predict', NewPredict),
    ('/schedule', MatchList),
    ('/addmatch', MatchPlayed),
    ('/clearmatches', ClearMatches)
], debug=True)
