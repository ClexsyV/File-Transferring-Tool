from flask import redirect, url_for, request, Blueprint, session

api = Blueprint('api', __name__)

@api.route('/')
def index():
  return redirect(url_for('pages.index'))

