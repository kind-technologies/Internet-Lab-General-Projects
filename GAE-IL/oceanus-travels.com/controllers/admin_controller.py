import os
from google.appengine.ext.webapp.util import *
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

from models.post_model import *

class BlogHandler:

	def __init__(self, response, request):
		self.response = response
		self.request = request
		self.view_path = os.path.join(os.path.dirname(__file__), '../views/admin/')

	def render(self, view, params):
		path = os.path.join(self.view_path, view + ".html")
		self.response.out.write(template.render(path, params))

	def add_post(self):

		title = self.request.get('ptitle')
		body = self.request.get('pbody')
		keywords = self.request.get('pkeywords')
		url = self.request.get('purl')

		is_primary = self.request.get('pprimary')
		is_primary = True if is_primary == 'on' else False
		
		is_enabled = self.request.get('penabled')
		is_enabled = True if is_enabled == 'on' else False
		
		post_id = self.request.get('pid')
		action = self.request.get('paction')

		if action == 'add':
			p = PostModel()
			pid = p.add_new_post(title, body, keywords, url,
						is_primary, is_enabled)	
			return pid

		view_params = {
			'page_title': "Blog :: Add New Post",
			'pid': "id",
			'paction': "add",
			'result': ""
		}

		view = "blog_add_post"
		self.render(view, view_params)
	
	def edit_post(self, post_key=''):
		key = self.request.get('pid')
		title = self.request.get('ptitle')
		body = self.request.get('pbody')
		keywords = self.request.get('pkeywords')
		url = self.request.get('purl')

		is_primary = self.request.get('pprimary')
		is_primary = True if is_primary == 'on' else False
		
		is_enabled = self.request.get('penabled')
		is_enabled = True if is_enabled == 'on' else False
		
		post_id = self.request.get('pid')
		action = self.request.get('paction')

		# Updating Post
		if action == 'edit':
			pid = PostModel().edit_post(key, title, body, keywords, url,
													is_primary, is_enabled)	
			return pid

		# Edit Page View
		post = PostModel().get(post_key)	

		view_params = {
			'page_title': "Blog :: Edit Post",
			'post': post,
			'paction': "edit",
			'result': ""
		}

		view = "blog_add_post"
		self.render(view, view_params)
	
	def delete_post(self):
		pass

	def set_primary_post(self):
		pass
	
	def enable_post(self):
		pass

	def list_posts(self):
		posts = PostModel.all()	
		posts.order("-date_added")

		view_params = {
			'page_title': "Blog :: Post list",
			'url': "",
			'url_linktext': "",
			'posts': posts
		}

		view = "index"
		self.render(view, view_params)

class AdminController(webapp.RequestHandler):

	def __init__(self):
		pass

	def initialize(self, request, response):
		super(AdminController, self).initialize(request, response)
		self.manager = BlogHandler(self.response, self.request)

	@login_required	
	def get(self, entity='', action='', param=''):
		if (entity == '' or 'blog') and (action == ''):
			self.manager.list_posts()
		elif (entity == 'blog') and (action == 'add'):
			self.manager.add_post()
		elif (entity == 'blog') and (action == 'edit'):
			self.manager.edit_post(param)


	def post(self, entity='', action='', param=''):
		if (entity == 'blog') and (action == 'add'):
			pid = self.manager.add_post()
			if pid:
				self.redirect('/ilhq/')
		elif (entity == 'blog') and (action == 'edit'):
			pid = self.manager.edit_post()
			if pid:
				self.redirect('/ilhq/')

