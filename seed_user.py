#!/usr/bin/env python
"""
seed_user.py

This script seeds the database with a test user for authentication.
It assumes that your application uses SQLAlchemy and that your User model
is available in src/models.py, and that your Flask app is initialized in src/app.py.
"""

from werkzeug.security import generate_password_hash
from src.models import db, User
from src.app import app  # Ensure your Flask app instance is imported correctly

def seed_test_user():
    with app.app_context():
        # Create all tables if they don't exist
        db.create_all()
        
        # Check if the test user already exists
        existing_user = User.query.filter_by(username="testuser").first()
        if existing_user:
            print("Test user already exists!")
        else:
            # Define your test credentials
            test_username = "testuser"
            test_password = "testpass"  # Use your desired test password
            hashed_password = generate_password_hash(test_password)
            new_user = User(username=test_username, password_hash=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            print("Test user created successfully!")

if __name__ == '__main__':
    seed_test_user()
