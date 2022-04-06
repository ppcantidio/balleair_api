from flask import Blueprint, jsonify, request


bookings_routes = Blueprint('bookings_routes', __name__)

class BookingsRoutes:

    @bookings_routes.route('/book', methods=['POST'])
    def book_flight():
        flight = request.args.get('flight')



    @bookings_routes.route('/cancel', methods=['POST'])
    def cancel_booking():
        pass