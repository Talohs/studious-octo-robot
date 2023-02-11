from flask import request
from . import api
from app.models import User

@api.route('/user/<id>', methods=['GET'])
def new_user(id):
    user = User.query.get_or_404(id)
    return user.to_dict()

@api.route('/users', methods=['POST'])
def create_user():
    if not request.is_json:
        return {'error': 'Your request content type must be application/json'}, 400
    data = request.json
    for field in ['first_name', 'last_name', 'email', 'username', 'password']:
        if field not in data:
            return {'error': f"{field} must be in request body"}, 400
    
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    username = data.get('username')

    new_user = User(first_name=first_name, last_name=last_name, email=email, username=username)
    return new_user.to_dict(), 201

