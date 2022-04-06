from webapi.models.flight import FlightModel
from flask import Blueprint, jsonify, request


flights_routes = Blueprint('flights_routes', __name__)

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
        pass

    @flights_routes.route('/', methods=['DELETE'])
    def delete_flight():
        pass

    @flights_routes.route('/', methods=['PUT'])
    def edit_flight():
        pass
