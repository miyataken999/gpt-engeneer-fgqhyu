# Test file
import pytest
from app.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_users(client):
    """Test getting all users"""
    response = client.get('/users')
    assert response.status_code == 200
    assert len(response.json) == 2

def test_get_products(client):
    """Test getting all products"""
    response = client.get('/products')
    assert response.status_code == 200
    assert len(response.json) == 2

def test_get_user(client):
    """Test getting a user by ID"""
    response = client.get('/users/1')
    assert response.status_code == 200
    assert response.json['id'] == 1

def test_get_product(client):
    """Test getting a product by ID"""
    response = client.get('/products/1')
    assert response.status_code == 200
    assert response.json['id'] == 1