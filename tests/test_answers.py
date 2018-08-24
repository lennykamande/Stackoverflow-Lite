import unittest
import os
import json
from flask import abort, session
from app import create_app

class TestViews(unittest.TestCase):

    def setUp(self):
        config_name = 'testing'
        app = create_app(config_name)
        self.client = app.test_client()
        self.registraiton = json.dumps(dict(username="lennymanyeki", password='1987lenny'))
        self.askquestion = json.dumps(dict(title="Why is it we use flask", 
                                        description='Well for starters you can pretty much do everything'))
        
        self.client.post('api/v1/questions', data=self.askquestion,content_type='application/json')
    
    def test_post_answer(self):
        """
        Test users can post answers
        """
        resource = self.client.post('/api/v1/questions/1/answer',
        data=json.dumps(dict(description="Hi there lets just give this a value")), content_type='application/json')
        #data = json.loads(resource.json)
        self.assertEqual(resource.content_type, 'application/json')
        self.assertEqual(resource.status_code, 201)

    def test_retrieve_answers(self):
        """
        Test users can retrieve all questions
        """
        resource = self.client.post('/api/v1/questions/1/answer',
        data=json.dumps(dict(description="Hi there lets just give this a value")), content_type='application/json')
        #data = json.loads(resource.json)
        self.assertEqual(resource.content_type, 'application/json')
        self.assertEqual(resource.status_code,201)
"""
    def test_empty_answer(self):
        
        Test for missing answer
        
        data=json.dumps(description="")

        resource = self.client.post('/api/v1/questions/1/answer',
        data, content_type='application/json')
        #data = json.loads(resource.json)
        self.assertEqual(resource.status_code,404)
        elf.assertEqual(resource.content_type, 'application/json')"""


