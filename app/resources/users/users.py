import uuid
from flask import jsonify, session, request, json
users = []

class User(object):
    def __init__(self):
        """ 
        User Class 
        """  
        self.listsdict = {}

    def register(self, username, password):
        """
        Create users
        """
       
        if not self.find_if_user_exsists(username) == True:  
            self.listsdict = {'username' : request.json['username'],
                        'password' : request.json['password'], 
                        'userid' : len(users)+ 1 }
            users.append(dict(self.listsdict))  
            return jsonify({"message": "Successful", "user": users}), 201
        return jsonify({"message": "Username is taken."}), 400

    def login(self, username, password):
        if len(users) == 0:
            return jsonify({"message": "Please register first."})
        else:
            #expected = [user for user in users if user['username'] == username]
            #if expected :
            for user in users:
                user_array = user.split('|')
                current_username = user_array[2]
                current_password = user_array[3]
                current_user_id = user_array[4]
                if (current_username == username and current_password == password):
                    session['userid'] = current_user_id['userid']
                    session['username'] = current_username['username']
                    return jsonify({"message":"You are successfully logged in",
                        "user": user}), 200
                else:
                    return jsonify({"message":"Wrong username or password"}), 401
            else:
                return jsonify({"message":"user does not exist"}), 404

    def get_specific_user(self, id):
        """
        get specific user
         """
        user = [user for user in users if user['userid'] == id]
        return jsonify({"User": user})

    def get_all_users(self):
        """
        get specific user
         """
        return jsonify({"Users": users}), 200

    def find_if_user_exsists(self, username):

        if len(users):
            for user in users:
                if user['username'] == username:
                    return True
                else:
                    return False
        return False