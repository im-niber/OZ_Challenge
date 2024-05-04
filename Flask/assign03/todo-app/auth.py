from flask import request, jsonify
from flask_smorest import Blueprint
from flask_jwt_extended import create_access_token
from models import User
from werkzeug.security import check_password_hash

auth_blp = Blueprint('auth', __name__, url_prefix='/login',
                      description='Operations on todos')

@auth_blp.route('/', methods=['POST'])
def login():
    if not request.json:
        print("not request")
        return jsonify({"msg": "missing json"}), 400
    
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if not username or not password:
        return jsonify({"msg": "missing username or password"}), 400        

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password_hash, password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    else:
        return jsonify({"msg": "Bad username or pssword"}), 401 