from flask import Blueprint, jsonify


users_routes = Blueprint('users_routes', __name__)

class UsersRoutes:

    @users_routes.route('/', methods=['POST'])
    def create_user():
        pass

    @users_routes.route('/', methods=['GET'])
    def get_users():
        pass

    @users_routes.route('/', methods=['DELETE'])
    def delete_user():
        pass

    @users_routes.route('/', methods=['PUT'])
    def edit_user():
        pass