import os
from google.appengine.ext.webapp.util import *
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

from models.post_model import *


class BlogHandler:
	def __init__(self, response, request):
		self.response = response
		self.request = request
		self.view_path = os.path.join(os.path.dirname(__file__), '../views/blog/')

	def render(self, view, params):
		path = os.path.join(self.view_path, view + ".html")
		self.response.out.write(template.render(path, params))


	def view_post(self, post_url):
		# Get the post by URL
		post = PostModel.gql("WHERE url='%s'" % post_url).get()
		view_params = {
			'page_title': "Blog : %s" % post.title,
			'post': post,
		}
		view = "view_post"
		self.render(view, view_params)


	def list_posts(self):
		# Getting Primary Post
		prim_post = PostModel.gql("WHERE is_primary=True")	

		# Getting Recent Posts
		posts = PostModel.gql("WHERE is_primary=False AND is_enabled=True \
								ORDER BY date_last_modified")

		view_params = {
			'page_title': "Blog",
			'primary_post': prim_post.get(),
			'recent_posts': posts,
		}

		view = "index"
		self.render(view, view_params)


class BlogController(webapp.RequestHandler):
	def __init__(self):
		pass

	def initialize(self, request, response):
		super(BlogController, self).initialize(request, response)
		self.manager = BlogHandler(self.response, self.request)

	def get(self, action='', post_url=''):
		if (action == 'blog' or post_url == ''):
			self.manager.list_posts()
		elif (action == 'view') and post_url:
			self.manager.view_post(post_url)

