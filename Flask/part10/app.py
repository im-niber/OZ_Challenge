from flask import Flask
from flask_login import LoginManager
from models import User
from routes import configure_route

app = Flask(__name__)
app.secret_key = 'flask-secret-key'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
configure_route(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

if __name__ == "__main__":
    app.run(debug=True)