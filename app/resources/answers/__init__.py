from flask import Blueprint

answer_api = Blueprint('answer_api', __name__)

from . import views
