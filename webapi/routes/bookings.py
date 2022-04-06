from flask import Blueprint, jsonify


bookings_routes = Blueprint('bookings_routes', __name__)

class BookingsRoutes:

    @bookings_routes.route('/book', methods=['POST'])
    def book_flight():
        pass

    @bookings_routes.route('/cancel', methods=['POST'])
    def cancel_booking():
        pass