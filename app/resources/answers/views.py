from flask import Flask, request, flash, redirect, url_for, jsonify, session
from . import answer_api
from .answers import Answerslist
answerObject = Answerslist() 

def validate_data(data):
    """validate request details"""
    try:
        # check if title more than 10 characters
        if len(data['answer'].strip()) == 0:
            return "answer cannot be empty"
        elif len(data['answer'].strip()) < 10:
            return "Title Must Be more than 10 characters"
        else:
            return "valid"
    except Exception as error:
        return "please provide all the fields, missing " + str(error)

@answer_api.route('/questions/<int:quiz_id>/answer', methods=["POST"])
def answer(quiz_id):

    """ Method to create answers."""
    data = request.get_json()
    description = data['description']
    res = answerObject.post_answer(quiz_id, description)
    return res

@answer_api.route('/questions/<int:id>/answers', methods=["GET"])
def answers(id):

    """ 
    Method to get answers to a question
    """
    data = answerObject.get_answer_by_quiz_id(id)
    return data
    