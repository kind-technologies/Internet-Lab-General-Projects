from google.appengine.ext import db

class PostModel(db.Model):

	author = db.UserProperty(auto_current_user=True)
	date_added = db.DateTimeProperty(auto_now_add=True)
	date_last_modified = db.DateTimeProperty(auto_now=True)
	title = db.StringProperty()
	body = db.TextProperty()
	keywords = db.StringProperty()
	url = db.StringProperty()
	is_primary = db.BooleanProperty()
	is_enabled = db.BooleanProperty()
	rating = db.RatingProperty()

	def add_new_post(self, title, body, keywords, url,
						is_primary, is_enabled, rating = 0):
		self.title = title
		self.body = body
		self.keywords = keywords
		self.url = url
		self.is_primary = is_primary
		self.is_enabled = is_enabled

		return self.put()
