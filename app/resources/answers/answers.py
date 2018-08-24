from flask import request, jsonify

answers = []		
class Answerslist(object):
   
    

    def __init__(self ):
    
        self.listsdict = {
        }

    def post_answer(self, quiz_id, description,):
        """ 
        a method to add a new answer with the unique user
        
        """

        self.listsdict = {'id' : len(answers) + 1,
                        'quiz_id' : quiz_id, 
                        'description' : request.json['description'] }
        answers.append(dict(self.listsdict))  
        return jsonify({"message": "Answered Succesfull.", "answers":answers}), 201 

    def get_answer_by_quiz_id(self, id):
        expected = [answer for answer in answers if answer['quiz_id'] == id]
        return jsonify({"Answer":expected}), 200
            

    