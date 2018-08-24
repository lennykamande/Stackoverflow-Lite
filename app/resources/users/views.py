from flask import Flask, request, flash, redirect, url_for, jsonify, session
from . import user_api
from .users import User
userObject = User() 

def validate_data(data):
    """validate user details"""
    try:
        if len(data['username'].strip()) < 3:
            return "username must be more than 3 characters"
        elif " " in data["password"]:
            return "password should be one word, no spaces"
        elif len(data['password'].strip()) < 5:
            return "Password should have atleast 5 characters"
        else:
            return "valid"
    except Exception as error:
        return "please provide all the fields, missing " + str(error)

@user_api.route('/registration', methods=["POST"])
def registration():
    """ Method to create user account."""
    if request.method == "POST":
            data = request.get_json()
            res = validate_data(data)
            if res == "valid":
                username = data['username']
                password = data['password']
                response = userObject.register(username, password)
                return response
            return jsonify({"message":res}), 400


@user_api.route('/login', methods=["POST"])
def login():
    """ Method to login user """
    data = request.get_json()
    username = data['username']
    password = data['password']
    res = userObject.login(username, password)
    return res 

@user_api.route('/users/<int:id>', methods=["GET"])
def user_id(id):
    """
    try to get user with all questions
    """
    data = userObject.get_specific_user(id)
    return data

@user_api.route('/users', methods=["GET"])
def users_all():
    """
    try to get user with all questions
    """
    data = userObject.get_all_users()
    return data