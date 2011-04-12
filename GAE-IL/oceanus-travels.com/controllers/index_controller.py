import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template 

from models.post_model import *

class IndexController(webapp.RequestHandler):

	def get(self):
		
		# Getting Primary Post
		prim_post = PostModel.gql("WHERE is_primary=True")	

		# Getting Recent Posts
		posts = PostModel.gql("WHERE is_primary=False ORDER BY date_last_modified DESC LIMIT 2")

		template_values = {
			'page_title': 'Research Center for Internet Technologies \
							: Fixed Asset Management System \
							: GoogleB.us - GAE MVC Framework',
			'primary_post': prim_post.get(),
			'recent_posts': posts,
		}

		path = os.path.join(os.path.dirname(__file__), '../views/index/index.html')
		self.response.out.write(template.render(path, template_values))

