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

	def edit_post(self, post_key, title, body, keywords, url,
						is_primary, is_enabled, rating = 0):
		post = self.get_post(post_key)
		post.title = title
		post.body = body
		post.keywords = keywords
		post.url = url
		post.is_primary = is_primary
		post.is_enabled = is_enabled

		return post.put()

	def get_post(self, post_key):
		return db.get(db.Key(post_key))
