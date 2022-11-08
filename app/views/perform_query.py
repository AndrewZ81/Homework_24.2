from flask import request, jsonify
from flask_restx import Resource, Namespace
from marshmallow import ValidationError

from app.schemes import RequestSchema
from app.constructor import create_query

request_schema = RequestSchema()
queries_ns = Namespace("perform_query")


@queries_ns.route("/")
class QueriesView(Resource):
    def post(self):
        post_data = request.json

        try:
            request_schema.load(post_data)
        except ValidationError as error:
            return error.messages, 400

        cmd_1, cmd_2 = post_data["cmd_1"], post_data["cmd_2"]
        value_1, value_2 = post_data["value_1"], post_data["value_2"]
        try:
            return jsonify(create_query(cmd_1, value_1, cmd_2, value_2))
        except KeyError:
            return "Неверно указана команда(-ы) запроса", 400
