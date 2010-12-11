import os
from google.appengine.ext.webapp.util import *
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

from models.post_model import *

class BlogHandler:

	def __init__(self, response):
		self.response = response
		self.view_path = os.path.join(os.path.dirname(__file__), '../views/admin/')

	def render(self, view, params):
		path = os.path.join(self.view_path, view + ".html")
		self.response.out.write(template.render(path, params))

	def add_post(self):
		p = PostModel()
		view_params = {
			'page_title': "Blog :: Post list",
			'url': "",
			'url_linktext': "",
			'result': p.test()
		}

		view = "blog_add_post"
		self.render(view, view_params)
	
	def edit_post(self):
		pass
	
	def delete_post(self):
		pass

	def set_primary_post(self):
		pass
	
	def enable_post(self):
		pass

	def list_posts(self):
		p = PostModel()
		view_params = {
			'page_title': "Blog :: Post list",
			'url': "",
			'url_linktext': "",
			'result': p.test()
		}

		view = "index"
		self.render(view, view_params)

class AdminController(webapp.RequestHandler):

	def __init__(self):
		pass

	def initialize(self, request, response):
		super(AdminController, self).initialize(request, response)
		self.manager = BlogHandler(self.response)

	@login_required	
	def get(self, entity='', action='', param=''):
#		print entity
#		print action
#		print param
#		print (entity == 'blog')

		if (entity == '' or 'blog') and (action == ''):
			self.manager.list_posts()
		elif (entity == 'blog') and (action == 'add'):
			self.manager.add_post()

	


