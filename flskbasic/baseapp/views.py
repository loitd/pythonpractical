from flask import render_template, session, redirect, flash, request, url_for
from baseapp import app
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/')
@app.route('/index')
def index():
	if not session.get('logged_in'):
		return redirect(url_for('login'))
	else:
		user = {'uname': session.get('uname')}
		return render_template('index.html', 
			title='Homepage', user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
	title = "Login Page"
	if request.method == "POST":
		if checklogin(request.form['uname'], request.form['pwd']):
			session['logged_in'] = True
			session['uname'] = request.form['uname']
			flash("Login successfully")
			return redirect(url_for('index'))
		else:
			flash("Some errors occured or Wrong username and password")		
	return render_template('login.html', title=title)

@app.route('/logout', methods=['GET'])
def logout():
	if session.get('logged_in'):
		session.clear()
	return index()

def checklogin(uname, pwd):
	appuname = app.config['UNAME']
	apppwd = app.config['PASSWD']
	x = generate_password_hash("123456a@")
	print(appuname, apppwd, pwd, x)
	if (uname==appuname) and check_password_hash(apppwd, pwd):
		return True
	else:
		return False