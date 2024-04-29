from flask_smorest import Blueprint
from marshmallow import Schema, fields
from flask.views import MethodView
from db import db
from models import User

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Str(required=True)

user_blp2 = Blueprint("Users2", "users2",  description="Operations on users", url_prefix='/user')

# API LIST:
# 1. 전체 유저 데이터 조회
# 2. 유저 생성

@user_blp2.route('/')
class UserList(MethodView):
    @user_blp2.response(200, UserSchema(many=True))
    def get(self):
        return User.query.all()

    @user_blp2.arguments(UserSchema)
    @user_blp2.response(201, UserSchema)
    def post(self, data):
        new_data = User(name=data["name"], email=data["email"]) 
        db.session.add(new_data)
        db.session.commit()