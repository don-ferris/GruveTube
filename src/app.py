import os
from flask import Flask
from src.models import db

app = Flask(__name__)

# Configure SQLAlchemy with MySQL parameters fetched from environment variables.
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"mysql+mysqlconnector://{os.environ.get('MYSQL_USER')}:{os.environ.get('MYSQL_PASSWORD')}"
    f"@db/{os.environ.get('MYSQL_DATABASE')}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with the Flask app.
db.init_app(app)

@app.route('/')
def index():
    return "Welcome to GruveTube!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
