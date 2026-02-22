"""
Configuration settings for the Full Stack Demo backend application.
"""

# Flask Configuration
DEBUG = True
HOST = '0.0.0.0'
PORT = 5000

# Database Configuration
DB_CONFIG = {
    'dbname': 'fullstack_demo',
    'user': 'postgres',
    'password': 'sutharsan',
    'host': 'localhost',
    'port': '5432'
}

# CORS Configuration
CORS_ORIGINS = ['http://localhost:5173', 'http://localhost:3000']

# API Configuration
API_PREFIX = '/api'
