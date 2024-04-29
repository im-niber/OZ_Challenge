from flask import Flask
from flask_smorest import Api
from db import db
from flask import render_template
from routes.post  import post_blp
import yaml

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# blueprint
app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)
api.register_blueprint(post_blp)

@app.route('/manage-posts')
def manage_boards():
    return render_template('posts.html')

if __name__ == '__main__':
    with open('db.yaml') as f:
        file = yaml.full_load(f)

    app.config['SQLALCHEMY_DATABASE_URI'] = file['dburl']
    db.init_app(app)
    
    with app.app_context():
        db.create_all()

    app.run(debug=True)