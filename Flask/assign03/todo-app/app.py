from flask import Flask, render_template
from flask_jwt_extended import JWTManager
from flask_smorest import Api

from db import db
from flask_migrate import Migrate

app = Flask(__name__)

# db, jwt
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:rbwo8160@localhost/flaskoz2'
app.config["JWT_SECRET_KEY"] = "super-secret-key"
app.config['API_TITLE'] = 'Todo API'
app.config['API_VERSION'] = 'v1'
app.config['OPENAPI_VERSION'] = '3.0.2'

# db - sqlalchemy
db.init_app(app)
migrate = Migrate(app, db)

jwt = JWTManager(app)
api = Api(app)

from auth import auth_blp
from todo import todo_blp

app.register_blueprint(auth_blp)
app.register_blueprint(todo_blp)

@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)