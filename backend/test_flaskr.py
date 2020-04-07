import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = 'postgresql://postgres:1234@localhost:5432/trivia'
        setup_db(self.app, self.database_path)

        self.new_question = {
            'question': 'How old are you?',
            'answer': '16',
            'category': 3,
            'difficulty': 3
        }
        
        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    # Test get_categories() endpoint for success response code
    def test_get_categories(self):
        self.assertEqual(self.client().get('/categories').status_code, 200)

    # Test get_categories() endpoint for invalid request methof
    def test_method_not_allowed_categories(self):
        self.assertEqual(self.client().post('/categories').status_code, 405)
    
    # Test get_question for retrieving questions successfully
    def test_get_questions(self):
        self.assertEqual(self.client().get('/questions').status_code, 200)
    
    def test_get_questions_by_category(self):
        self.assertEqual(self.client().get('/categories/2/questions').status_code,200)
    
    # Test delete question endpoint
    def test_delete_question(self):
        self.assertEqual(self.client().delete('/questions/2').status_code, 404)
        
    def test_delete_question_not_found(self):
        self.assertEqual(self.client().delete('/questions/100').status_code, 404)

    # Test search question enpoint for success and errors
    def test_search_question(self):
        response = self.client().post('search', json={"searchTerm":"actor"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["total_questions"], 0)

    def test_search_question_not_found(self):
        self.assertEqual(self.client().post('search', json={"searchTerm": "actorNotThere"}).json["total_questions"],0)

    # Test create new question
    def test_create_question(self):
        self.assertEqual(self.client().post('/questions', json=self.new_question).status_code, 200)
    
    # Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()