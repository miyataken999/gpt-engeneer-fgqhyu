# Data models
from dataclasses import dataclass

@dataclass
class User:
    """User data model"""
    id: int
    name: str
    email: str

@dataclass
class Product:
    """Product data model"""
    id: int
    name: str
    price: float