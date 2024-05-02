from flask import request, jsonify
from flask_smorest import Blueprint
from flask.views import MethodView
from db import db
from models import User

user_blp = Blueprint("Users", "users",  description="Operations on users", url_prefix='/user')

# API LIST:
# 1. 전체 유저 데이터 조회
# 2. 유저 생성
@user_blp.route('/')
class UserList(MethodView):

    def get(self):
        print("1 blp")
        users = User.query.all()
        user_data = [{
            "id": user.id,
            "name": user.name,
            "email": user.email,
        } for user in users ]
        
        return jsonify(user_data)

    def post(self):
        data = request.json
        new_data = User(name=data["name"], email=data["email"]) 
        db.session.add(new_data)
        db.session.commit()

        return jsonify({"msg": "Succesfully created user"})

# 1. 특정 유저 조회
# 2. 특정 유저 업데이트
# 3. 특정 유저 삭제
@user_blp.route('/<int:user_id>')
class UserResource(MethodView):
    
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return jsonify({ "id": user.id,
                         "name": user.name,
                         "email": user.email
                         })
    
    def put(self, user_id):
        data = request.json
        user = User.query.get_or_404(user_id)
        
        user.name = data["name"]
        user.email = data["email"]

        db.session.commit()
        return jsonify({"msg": "Successfully updated user"})

    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()

        return jsonify({"msg": "succesfully deletee user"})