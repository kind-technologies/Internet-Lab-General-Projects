import cgi

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db

#For templating
import os
from google.appengine.ext.webapp import template

class Greeting(db.Model):
	author = db.UserProperty()
	content = db.StringProperty(multiline=True)
	date = db.DateTimeProperty(auto_now_add=True)

class MainPage(webapp.RequestHandler):
	def get(self):
		greeting_query = Greeting.all().order('-date')
		greetings = greeting_query.fetch(10)

		if users.get_current_user():
			url = users.create_logout_url(self.request.uri)
			url_linktext = 'Logout'
		else:
			url = users.create_login_url(self.request.uri)
			url_linktext = 'Login'

		template_values = {
			'greetings': greetings,
			'url': url,
			'url_linktext': url_linktext,
		}

		path = os.path.join(os.path.dirname(__file__), 'views/index.html')
		self.response.out.write(template.render(path, template_values))

class Guestbook(webapp.RequestHandler):
	def post(self):
		greeting = Greeting()

		if users.get_current_user():
			greeting.author = users.get_current_user()

		greeting.content = self.request.get('content')
		greeting.put()
		self.redirect('/')


application = webapp.WSGIApplication(
									[ #List
										('/', MainPage), # Tuple
										('/sign', Guestbook)
									],
									debug=True
									)

def main():
	run_wsgi_app(application)

if __name__ == "__main__":
	main()
