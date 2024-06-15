from flask import Blueprint, render_template, flash, redirect, url_for, request, session, jsonify
from app import db, authen, firebasse

auth = Blueprint('auth', __name__,
               template_folder='templates',
               static_folder='static')
blog = Blueprint('blog', __name__,
               template_folder='templates',
               static_folder='static')

@blog.route('/')
def home():
    users = db.child("users").get().val()
    return render_template("home.html", users=users)



@auth.route('/register', methods=['POST', 'GET'])
def register():
    if 'user' in session:
        return redirect(url_for("blog.home"))
    if request.method == 'POST':
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        email = request.form.get('email')
        password = request.form.get('password')
        if len(password) <= 5:
            flash("password too short")
            return redirect(url_for("auth.register")) 
        else:    
            try:
                # Create user in Firebase Auth
                user = authen.create_user_with_email_and_password(email, password)
                print('User created successfully')
                session['user'] = email
                user_data = {
                    'first_name': first_name,
                    'last_name' : last_name,
                    'email': email
                }
                db.child("users").child(user['localId']).set(user_data)
                return redirect(url_for("auth.register"))
            except Exception as e:
                # Log the error for debugging
                print(f'Error: {e}')
                flash('Registration failed. Email may already be in use.')
                return redirect(url_for("auth.register"))
            
    return render_template("register.html")


@auth.route('/user/<uid>', methods=['GET'])
def get_user(uid):
    user_data = db.child("users").child(uid).get().val()
    if user_data:
        return jsonify(user_data), 200
    else:
        return jsonify({'message': 'User not found'}), 404
    

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            session['user'] = user['localId']
            return redirect(url_for('index'))
        except Exception as e:
            flash('Login failed. Please check your credentials and try again.', 'danger')
            print(e)
    return render_template('login.html')


@auth.route("/logout")
def  logout():
    session.pop('user')
    return redirect(url_for("blog.home"))
