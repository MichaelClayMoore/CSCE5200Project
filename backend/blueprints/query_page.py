from flask import request, Blueprint, abort , json, jsonify
from DocParser import DocumentDatabase
import json


query_page = Blueprint('query_page', __name__)

db = DocumentDatabase();

@query_page.route("/test", methods=['GET'])
def test():
    return "test"

@query_page.route("/get_docs", methods=['GET'])
def get_docs():
    return db.return_documents();

@query_page.route("/add_document", methods=['POST'])
def add_document():
    file = request.get_json()['params']['file_object'];
    return db.parse_document_object( request.get_json()['params']['file_object'] );

@query_page.route("/query_documents", methods=['GET'])
def query_documents():
    return db.query_for_doc( request.args.get('query') );
