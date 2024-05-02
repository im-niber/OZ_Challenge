from flask import request, jsonify, render_template
from flask_smorest import Blueprint
from flask.views import MethodView
from models import Reservation
from db import db

reservation_blp = Blueprint("reservations", __name__, description="reservation api", url_prefix='/reservations')

# 주어진 html 에서 get, post로 삭제 업데이트를 하고있어서
# 원래 하던대로 get put post delete를 각각 클래스내부에서 만들어서 하기에 조금 문제가 있었다.
# 예약을 업데이트하는 url은 /update로 기존 url에서 변경되기때문에 그에 맞는 경로에 설정해줄 필요가 있었고
# 그 부분을 원래는 클래스 내부에서 했었는데, 이러면 클래스의 인스턴스 메소드일 필요가 없는 느낌을 받았고
# 따로 클래스를 만들어서 설정해주는게 가독성 부분에서 더 좋은 느낌을 받았다.
# 그리고 생각한 부분이 이렇게 요청이 들어온다면
# 프론트쪽에 수정을 부탁해서 /edit 경로에서 get put 으로 받게끔 하는게 더 좋아보이긴함.

@reservation_blp.route('/')
class Reservations(MethodView):
    def post(self):
        data = request.form
        new_reservation = Reservation(
                                name=data['customer_name'],
                                phone=data['customer_phone'],
                                reservation_time=data['reservation_time'],
                                people=data['number_of_people'],
                                requests=data['special_requests']
                                )
        db.session.add(new_reservation)
        db.session.commit()
        
        return jsonify({'msg': "success create reservation"}), 201

# update 클래스를 새로 만든 ver.
@reservation_blp.route("/update/<int:reservation_id>")
class ReservationUpdate(MethodView):
    def post(self, reservation_id):
        data = request.form
        reservation = Reservation.query.get_or_404(reservation_id)

        new_reservation = Reservation(
                                name=data['customer_name'],
                                phone=data['customer_phone'],
                                reservation_time=data['reservation_time'],
                                people=data['number_of_people'],
                                requests=data['special_requests']
                                )
        reservation.name = new_reservation.name
        reservation.phone = new_reservation.phone
        reservation.reservation_time = new_reservation.reservation_time
        reservation.people = new_reservation.people
        reservation.requests = new_reservation.requests

        db.session.commit()
        
        return jsonify({'msg': "success update"}), 201


@reservation_blp.route('edit/<int:reservation_id>')
class ReservationGet(MethodView):
    def get(self, reservation_id):
        reservation = Reservation.query.get_or_404(reservation_id)
        reservation = {
                        "id": reservation.id,
                        "customer_name": reservation.name,
                        "customer_phone": reservation.phone, 
                        "reservation_time": reservation.reservation_time, 
                        "special_requests":reservation.requests,
                        "number_of_people": reservation.people
                        }
        return render_template('edit.html', reservation=reservation)

    # 경로가 수정되는경우에는 아예 새로 클래스로 만드는게 더 나을거같다
    @reservation_blp.route('/update/<int:reservation_id>', methods=['post'])
    def post(reservation_id):
        data = request.form
        reservation = Reservation.query.get_or_404(reservation_id)

        new_reservation = Reservation(
                                name=data['customer_name'],
                                phone=data['customer_phone'],
                                reservation_time=data['reservation_time'],
                                people=data['number_of_people'],
                                requests=data['special_requests']
                                )
        reservation.name = new_reservation.name
        reservation.phone = new_reservation.phone
        reservation.reservation_time = new_reservation.reservation_time
        reservation.people = new_reservation.people
        reservation.requests = new_reservation.requests

        db.session.commit()
        
        return jsonify({'msg': "success update"}), 201


# 함수로 만든 ver
@reservation_blp.route('/update/<int:reservation_id>', methods=['post'])
def post(reservation_id):
        data = request.form
        reservation = Reservation.query.get_or_404(reservation_id)

        new_reservation = Reservation(
                                name=data['customer_name'],
                                phone=data['customer_phone'],
                                reservation_time=data['reservation_time'],
                                people=data['number_of_people'],
                                requests=data['special_requests']
                                )
        reservation.name = new_reservation.name
        reservation.phone = new_reservation.phone
        reservation.reservation_time = new_reservation.reservation_time
        reservation.people = new_reservation.people
        reservation.requests = new_reservation.requests

        db.session.commit()
        
        return jsonify({'msg': "success update"}), 201


@reservation_blp.route('/delete/<int:reservation_id>')
class ReservationDelete(MethodView):
    def get(self, reservation_id):
        reservation = Reservation.query.get_or_404(reservation_id)
        db.session.delete(reservation)
        db.session.commit()

        return jsonify({'msg': "Successfully delete reservation_id"}), 201
    
