# Import Application Configuration
from config.ilconfig import *

# App Engine Imports
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

application = webapp.WSGIApplication(
	[ #List
		('/', IndexController), # Tuple
		('/blog', BlogController), # Tuple
		('/contact', ContactController), # Tuple
	],
	debug=True
)

def main():
	run_wsgi_app(application)

if __name__ == "__main__":
	main()
