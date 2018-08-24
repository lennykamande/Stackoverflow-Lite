from flask_restful import Resource
from flask import request
from random import *

questionslist = []		
class Questionlist(Resource):
   
    

    def __init__(self ):
        
        self.listsdict = {}

    def post(self, name, description, owner):
        """ 
        a method to add a new question with the unique user
        
        """
        quiz_id = randint(1, 1000)
        self.listsdict = {'name' : name, 'owner' : owner, 'description' : description, 'quiz_id' : quiz_id}
        questionslist.append(dict(self.listsdict))
        print(questionslist, "here")
        res = 'success'
        return res, 201

    def get(self, owner):
        """ 
        a method to show the question list
        """
        
        return questionslist

    def delete(self, id):
        """
        A method to delete a question from the list
        """
        pass
    def put(self, id):
        pass

answers = []
class Answer(object):
   
    

    def __init__(self ):
        
        self.itemsdict = {}
    """ 
    a method to add items belonging to a specific shopping list
    """
    def new_item(self, name, description, list_id):
            self.itemsdict = {'name' : name, 'list_id' : list_id, 'description' : description, 'item_id' : item_id}
            answers.append(self.itemsdict)
            print(answers, "here")
            res = 'success'
            return res

    """ a method to show items belonging to a specific shopping list"""
    def view_item(self, id):
        for items in answers:
            if items['id']== id:
                return items
        else:
            return 'No Items'


    """ a method to delete items in a particular list"""
    def delete_item(self, item_id):
        for items in answers:
            if items['item_id']== item_id:
                return items
        else:
            return 'No Items'