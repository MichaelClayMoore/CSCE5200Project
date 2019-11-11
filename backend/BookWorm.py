from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from flask_cors import CORS
from blueprints.query_page import query_page
from DocParser import DocumentDatabase

app = Flask(__name__)
CORS(app)

app.register_blueprint(query_page)

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(debug=True)
