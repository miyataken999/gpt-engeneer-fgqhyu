# API routes
from flask import Blueprint, jsonify, request
from app.models import User, Product

api = Blueprint('api', __name__)

@api.route('/users', methods=['GET'])
def get_users():
    """Get all users"""
    users = [User(id=1, name='John Doe', email='john@example.com'), User(id=2, name='Jane Doe', email='jane@example.com')]
    return jsonify([user.__dict__ for user in users])

@api.route('/products', methods=['GET'])
def get_products():
    """Get all products"""
    products = [Product(id=1, name='Product 1', price=10.99), Product(id=2, name='Product 2', price=9.99)]
    return jsonify([product.__dict__ for product in products])

@api.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Get a user by ID"""
    user = User(id=user_id, name='John Doe', email='john@example.com')
    return jsonify(user.__dict__)

@api.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Get a product by ID"""
    product = Product(id=product_id, name='Product 1', price=10.99)
    return jsonify(product.__dict__)