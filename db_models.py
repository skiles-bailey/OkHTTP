from google.appengine.ext import ndb


class Model(ndb.Model):
	def to_dict(self):
		d = super(Model, self).to_dict()
		d['key'] = self.key.id()
		return d
		
class Weather(Model):
	weather_data = ndb.StringProperty(required = True)
	
	