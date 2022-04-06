from flask import Blueprint, jsonify


flights_routes = Blueprint('flights_routes', __name__)

class FlightsRoutes:

    @flights_routes.route('/', methods=['POST'])
    def create_user():
        pass

    @flights_routes.route('/', methods=['GET'])
    def get_users():
        pass

    @flights_routes.route('/', methods=['DELETE'])
    def delete_user():
        pass

    @flights_routes.route('/', methods=['PUT'])
    def edit_user():
        pass
