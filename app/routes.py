from flask import Blueprint, jsonify, request
from app import db
from app.models import User
from app.auth import auth

bp = Blueprint('api', __name__)

@bp.route('/users', methods=['POST'])
@auth.login_required
def add_user():
    data = request.get_json()
    new_user = User(username=data['username'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@bp.route('/users', methods=['GET'])
@auth.login_required
def get_users():
    users = User.query.all()
    return jsonify([{'id': user.id, 'username': user.username, 'email': user.email} for user in users])

@bp.route('/users/<int:id>', methods=['GET'])
@auth.login_required
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify({'id': user.id, 'username': user.username, 'email': user.email})

@bp.route('/users/<int:id>', methods=['PUT'])
@auth.login_required
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.get_json()
    user.username = data['username']
    user.email = data['email']
    db.session.commit()
    return jsonify({'message': 'User updated successfully'})

@bp.route('/users/<int:id>', methods=['DELETE'])
@auth.login_required
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'})