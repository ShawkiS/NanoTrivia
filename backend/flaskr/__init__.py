import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category, db

QUESTIONS_PER_PAGE = 10


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    def format_response_error(code, message):
        return jsonify({
            "success": False,
            "error": code,
            "message": message
        }), code

    CORS(app, resources={r"/*": {"origin": '*'}})

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PUT,POST,DELETE,OPTIONS')
        return response

    @app.route('/categories', methods=['GET'])
    def get_categories():
        categories = Category.query.all()
        data = {}
        for category in categories:
            category_type = category.format()['type']
            data[category.format()['id']] = category_type.lower()

        return jsonify({"categories": data}), 200

    @app.route('/questions', methods=['GET'])
    def get_questions():
        start = (request.args.get('page', 1, type=int) - 1) * \
            QUESTIONS_PER_PAGE
        data = [question.format()
                for question in Question.query.order_by(Question.id).all()]

        category_data = {}
        for category in Category.query.all():
            category_type = category.format()['type']
            category_data[category.format()['id']] = category_type.lower()

        return jsonify({"questions": data[start:start + QUESTIONS_PER_PAGE],
                        "current_category": "",
                        "total_questions": len(data),
                        "categories": category_data}), 200

    @app.route('/questions/<int:id>', methods=['DELETE'])
    def delete_question(id):
        question = Question.query.filter(Question.id == id).one_or_none()

        if question:
            Question.delete(question)
            return jsonify({"message": "Question Deleted"}), 204
        else:
            abort(404)

    @app.route('/questions', methods=['POST'])
    def create_question():
        try:
            new_question = Question(
                question=request.get_json()['question'],
                answer=request.get_json()['answer'],
                category=request.get_json()['category'],
                difficulty=request.get_json()['difficulty'])

            Question.insert(new_question)
            return jsonify(new_question.format())
        except Exception as e:
            print(e)

    @app.route('/search', methods=['POST'])
    def search_question():
        term = request.get_json()['searchTerm']
        data = [question.format() for question in Question.query.filter(Question.question.ilike(f'%{term}%')).all()]
        return jsonify({"questions": data,
                        "total_questions": len(data),
                        "current_category": ""
                        })

    @app.route('/categories/<int:id>/questions', methods=['GET'])
    def get_questions_by_category(id):
        try:
            category = Category.query.filter(Category.id == id).first()
            questions = Question.query.filter(
                Question.category == str(id)).all()

            data = [question.format() for question in questions]
            if category:
                category_type = category.type
            else:
                category_type = None
            return jsonify({"questions": data, "total_questions": len(data), "current_category": category_type})
        except Exception as e:
            print(e)
            abort(500)

    @app.route('/quizzes', methods=['POST'])
    def play_quiz():
        body = request.get_json()

        previous_questions = body.get('previous_questions', None)
        quiz_category = body.get('quiz_category', None)

        try:
            if quiz_category["id"]:
                questions = Question.query.filter(
                    Question.category == quiz_category["id"]).all()
            else:
                questions = Question.query.all()

            if len(questions) > 0:
                filtered_questions = [question.format(
                ) for question in questions if question.id not in previous_questions]

                print('previous questions', filtered_questions)
                if len(filtered_questions) > 0:
                    new_question = random.choice(filtered_questions)
                else:
                    new_question = None
                return jsonify({
                    'success': True,
                    'question': new_question,
                    'previous_questions': previous_questions,
                    'quizCategory': quiz_category
                })
            else:
                return jsonify({"question": None})
        except Exception as e:
            print(e)
            abort(500)

    @app.errorhandler(404)
    def not_found(error):
        return format_response_error(404, "Not Found")

    @app.errorhandler(405)
    def method_not_allowed(error):
        return format_response_error(405, "Not Allowed")

    @app.errorhandler(422)
    def unprocessable(error):
        return format_response_error(422, "not Porcessed Entity")

    @app.errorhandler(500)
    def internale_server_error(error):
        return format_response_error(500, "Internal Server Error")

    return app
