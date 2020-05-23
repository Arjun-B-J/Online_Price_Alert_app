from flask import Blueprint, session,redirect,request,url_for,render_template
from models.user.user import User
import models.user.errors as errors
user_blueprint = Blueprint('users',__name__)

@user_blueprint.route('/register',methods=['GET','POST'])
def register_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            User.register_user(email,password)
            session['email']=email
            return email

        except errors.UserError as e:
            return e.message


    return render_template('users/register.html')