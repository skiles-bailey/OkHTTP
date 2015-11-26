import webapp2
from google.appengine.ext import ndb
import db_models
import json


class Weather(webapp2.RequestHandler):
	def get(self):
		self.response.write("Welcome to the dummy weather page!")

	def post(self):		
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = 'Not Acceptable, API only supports application/json MIME type'
			return
		new_weather = db_models.Weather()
		weather_data = self.request.get('weather_data', default_value = None)		
		if weather_data:
			new_weather.weather_data = weather_data				
		key = new_weather.put()
		out = new_weather.to_dict()
		self.response.write(json.dumps(out))	
			
class WeatherSearch(webapp2.RequestHandler):
	def get(self):		
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = 'Not Acceptable, API only supports application/json MIME type'
			return
		q = db_models.Weather.query()
		#if self.request.get('day', None):
		#	q = q.filter(db_models.Weather.day == self.request.get('day'))		
		keys = q.fetch()
		results = {'Weather_data': [x.weather_data for x in keys]}
		self.response.write(json.dumps(results))