from google.appengine.ext import webapp

class ContactController(webapp.RequestHandler):
	def get(self):
		self.response.out.write('<h3>Contact<h3>')

