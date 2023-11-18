from . import create_app
from flask import Blueprint, render_template, request, flash, jsonify, redirect
from flask_login import login_required, current_user, LoginManager
#from .models import Coralls
import os
from . import db
import json
import time

views = Blueprint('views', __name__)


@views.route('/', methods=['GET'])
def home():
    return render_template("index.html") #user=current_user)

@views.route('/login', methods=['GET'])
def signin():
    return render_template("login.html") #user=current_user)

@views.route('/registration',methods=['GET'])
def signup():
    return render_template("signup.html")