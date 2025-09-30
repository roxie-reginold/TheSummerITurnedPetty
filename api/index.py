"""
Vercel serverless function wrapper for Flask backend.
"""
import sys
import os

# Add the backend directory to Python path
backend_path = os.path.join(os.path.dirname(__file__), "..", "backend")
sys.path.insert(0, os.path.abspath(backend_path))

# Import and create the Flask app
from app import create_app

# Create and expose the Flask app directly
# Vercel will automatically handle WSGI
app = create_app()
