from flask import request, jsonify
from random import *

questionslist = []		
class Questionlist(object):
   
    

    def __init__(self ):
    
        self.listsdict = {
        }

    def post(self, title, description):
        """ 
        a method to add a new question with the unique user
        
        """
        #self.quiz_id = len(questionslist)
        self.listsdict = {'title' : request.json['title'],
                        'description' : request.json['description'], 
                        'quiz_id' : len(questionslist)+ 1 }
        questionslist.append(dict(self.listsdict))  
        return jsonify({"message": "Question Asked Succesfull.", "question":questionslist}), 201 

    def get_question(self):
        """ 
        a method to show the question list
        """
        
        return jsonify({"Questions": questionslist}), 200

    def get_question_by_id(self, id):
        for question in questionslist:
            if question['quiz_id'] == id:
                return jsonify({"Question":question})
            return jsonify("Question with that id does not exist.")
        return jsonify("Question with that id does not exist.")
    