from flask import Flask, request, flash, redirect, url_for, jsonify, session
from . import api
from .questions import Questionlist
questionObject = Questionlist() 

def check_query(data):
    try:
        if len(data['title'].strip()) == 0:
            return "Title cannot be empty"
        elif len(data['description'].strip()) == 0:
            return "Question body cannot be empty"
        elif len(data['title'].strip()) < 5:
            return "Title Must Be more than 5 characters"
        elif len(data['description'].strip()) < 10:
            return "Body must be more than 10 letters"
        else:
            return "Okay"
    except Exception as error:
        return "please provide all the fields, missing " + str(error)

@api.route('/questions', methods=["GET", "POST"])
def question():
    """ Method to create and retrieve questions."""
    if request.method == "POST":
        
        data = request.get_json()
        res = check_query(data)
        if res == "Okay":
            title = data['title']
            description = data['description']
            response = questionObject.post(title, description)
            return response
        return jsonify({"message":res}), 422
    #return jsonify({"message": "Please login to post a question."})
    data = questionObject.get_question()
    return data

@api.route('/questions/<int:id>', methods=["GET", "POST"])
def question_id(id):
    """ 
    Method to get a specific question.
    """
    data = questionObject.get_question_by_id(id)
    return data
    
