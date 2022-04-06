from flask import Blueprint, jsonify


users_routes = Blueprint('users_routes', __name__)

class UsersRoutes:

    @users_routes.route('/', methods=['POST'])
    def create_flight():
        pass

    @users_routes.route('/', methods=['GET'])
    def get_flights():
        pass

    @users_routes.route('/', methods=['DELETE'])
    def delete_flight():
        pass

    @users_routes.route('/', methods=['PUT'])
    def edit_flight():
        pass
