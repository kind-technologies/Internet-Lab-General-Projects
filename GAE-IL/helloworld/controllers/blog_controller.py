from google.appengine.ext import webapp

class BlogController(webapp.RequestHandler):
	def get(self):
		self.response.out.write('<h3>Blog<h3>')

