# Main application file
from flask import Flask
from app.config import Config
from app.routes import api

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(api)

if __name__ == '__main__':
    app.run(debug=True)