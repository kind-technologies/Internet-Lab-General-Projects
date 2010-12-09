from google.appengine.ext import webapp
import os
from google.appengine.ext.webapp import template 

class IndexController(webapp.RequestHandler):
	def get(self):

		greetings = ""
		url = ""
		url_linktext = ""
		
		template_values = {
			'greetings': greetings,
			'url': url,
			'url_linktext': url_linktext,
		}

		path = os.path.join(os.path.dirname(__file__), '../views/index/index.html')
		self.response.out.write(template.render(path, template_values))
