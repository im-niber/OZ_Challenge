from flask import Flask, render_template
from db import db
from flask_migrate import Migrate
from models import Reservation
from reservation_routes import reservation_blp

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:rbwo8160@localhost/flaskoz'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

# blueprint
app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

app.register_blueprint(reservation_blp)

@app.route('/reservations')
def index():
    reservations = Reservation.query.all()
    reservations = [{
                        "id": reservation.id,
                        "customer_name": reservation.name,
                        "customer_phone": reservation.phone, 
                        "reservation_time": reservation.reservation_time, 
                        "special_requests":reservation.requests,
                        "number_of_people": reservation.people
                        } for reservation in reservations]
    return render_template('index.html', reservations=reservations)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    
    app.run(debug=True)
