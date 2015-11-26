import webapp2
from google.appengine.api import oauth


app = webapp2.WSGIApplication([
	('/', 'weather.Weather')
	], debug = True)

app.router.add(webapp2.Route(r'/weather/search', 'weather.WeatherSearch'))
app.router.add(webapp2.Route(r'/weather', 'weather.Weather'))
	
