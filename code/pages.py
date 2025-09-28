from flask import render_template, Blueprint, redirect, url_for

pages = Blueprint('pages', __name__)

@pages.route('home')
def index():
  return render_template('index.html')
