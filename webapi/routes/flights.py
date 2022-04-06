from webapi.models.flight import FlightModel
from flask import Blueprint, jsonify, request
from webapi.utils.database import Database

flights_routes = Blueprint('flights_routes', __name__)

db = Database()

class FlightsRoutes:

    @flights_routes.route('/', methods=['POST'])
    def create_flight():

        flight_object = FlightModel(
        departure_airport = request.form.get('departureAirport'),
        arrival_airport = request.form.get('arrivalAirport'),
        flight_date = request.form.get('flightDate'),
        aircraft = request.form.get('aircraft'),
        pax_available = request.form.get('pax_available'),
        pax_booked = request.form.get('pax_booked')
        )

        flight_doc = flight_object.create_flight()

        return jsonify({
            'status': 'success',
            'flight': flight_doc
        })

    @flights_routes.route('/', methods=['GET'])
    def get_flights():
        flights_list = db.select_object('flights_api', {})

        return jsonify({
            'status': 'sucess',
            'flight': flights_list
        })

    @flights_routes.route('/<flight_number>', methods=['DELETE'])
    def delete_flight(flight_number):
        flight_doc = db.select_one_object('flights_api', {'flightNumber': flight_number})

        if flight_doc is None:
            return jsonify({
                'status': 'error',
                'message': 'flight not found'
            })

        db.delete_one('flights_api', {'flightNumber': flight_number})

        flight_doc = db.select_one_object('flights_api', {'flightNumber': flight_number})

        if flight_doc is None:
            return jsonify({
                'status': 'sucess',
                'message': 'flight deleted successfully'
            })

        return jsonify({
            'status': 'error',
            'message': 'error deleting flight'
        })

    @flights_routes.route('/', methods=['PUT'])
    def edit_flight():
        pass
