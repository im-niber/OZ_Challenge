from flask_smorest import Blueprint
from marshmallow import Schema, fields
from flask.views import MethodView
from db import db
from models import Post
from datetime import datetime

class PostSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    content = fields.String(required=True)
    created_at = fields.DateTime()

post_blp = Blueprint("Post", "post",  description="Operations on posts", url_prefix='/posts')

@post_blp.route('/')
class PostList(MethodView):
    @post_blp.response(200, PostSchema(many=True))
    def get(self):
        return Post.query.all()
    
    @post_blp.arguments(PostSchema)
    @post_blp.response(201, PostSchema)
    def post(self, data):
        data = Post(title=data["title"], content=data["content"])
        db.session.add(data)
        db.session.commit()

@post_blp.route('/<int:post_id>')
class PostResource(MethodView):
    @post_blp.response(200, PostSchema)
    def get(self, post_id):
        return Post.query.get_or_404(post_id)

    @post_blp.arguments(PostSchema)
    @post_blp.response(201, PostSchema)
    def put(self, data, post_id):
        post = Post.query.get_or_404(post_id)
        post.title = data['title']
        post.content = data['content']
        post.created_at = datetime.now()
        db.session.commit()
    
    @post_blp.response(200, PostSchema)
    def delete(self, post_id):
        post = Post.query.get_or_404(post_id)
        db.session.delete(post)
        db.session.commit()