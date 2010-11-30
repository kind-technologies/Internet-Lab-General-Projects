# Import Application Configuration
from config.ilconfig import *

import cgi

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db

#For templating
import os
from google.appengine.ext.webapp import template

class MainPage(webapp.RequestHandler):
	def get(self):

		greetings = ""
		url = ""
		url_linktext = ""
		
		template_values = {
			'greetings': greetings,
			'url': url,
			'url_linktext': url_linktext,
		}

		path = os.path.join(os.path.dirname(__file__), 'views/index/index.html')
		self.response.out.write(template.render(path, template_values))

application = webapp.WSGIApplication(
									[ #List
										('/', MainPage), # Tuple
										('/blog', BlogController), # Tuple
										('/contact', ContactController), # Tuple
									],
									debug=True
									)

def main():
	run_wsgi_app(application)

if __name__ == "__main__":
	main()
