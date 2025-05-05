from flask import Flask
import os

app = Flask(__name__)

# Load configuration from environment variables
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')

@app.route('/')
def home():
    return "Welcome to GruveTube!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
