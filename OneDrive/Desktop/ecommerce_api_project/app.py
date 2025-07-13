from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from ecommerce_api_project.config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
ma = Marshmallow(app)

@app.route('/')
def home():
    return {"message": "Welcome to the E-commerce API"}

if __name__ == "__main__": 
    app.run(debug=True)
    