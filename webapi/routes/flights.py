from flask import Blueprint, jsonify


flights_routes = Blueprint('flights_routes', __name__)

class FlightsRoutes:

    @flights_routes.route('/', methods=['POST'])
    def create_flight():
        pass

    @flights_routes.route('/', methods=['GET'])
    def get_flights():
        pass

    @flights_routes.route('/', methods=['DELETE'])
    def delete_flight():
        pass

    @flights_routes.route('/', methods=['PUT'])
    def edit_flight():
        pass
