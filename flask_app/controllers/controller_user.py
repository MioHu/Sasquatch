from flask import render_template, request, redirect, session
from flask_app import app, bcrypt
from flask_app.models.model_user import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_regis', methods=['POST'])
def process_regis():
    #validate
    if not User.valid_regis(request.form):
        return redirect('/')
    #hash
    pw_hash = bcrypt.generate_password_hash(request.form['pw'])
    data = {
        **request.form,
        'pw': pw_hash
    }
    #create
    session['uid'] = User.create(data)
    user = User.get_one({'uid': session['uid']})
    session['first_name'] = user.first_name
    session['last_name'] = user.last_name
    return redirect('/dashboard')

@app.route('/process_login', methods=['POST'])
def process_login():
    if not User.valid_login(request.form):
        return redirect('/')
    user = User.get_by_email({'email': request.form['email']})
    session['uid'] = user.id
    session['first_name'] = user.first_name
    session['last_name'] = user.last_name
    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
