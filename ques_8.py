from flask import Flask, render_template, request, render_template_string, session, redirect, url_for
from datetime import timedelta
from flask_session import Session
app = Flask(__name__)
app.secret_key = 'your_super_secret_key_here'
@app.route('/login', methods=['GET', 'POST'])
def login():
        if request.method == 'POST':
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        return '''
            <form action="" method="post">
                <p><input type="text" name="username"/></p>
                <p><input type="submit" value="Login"/></p>
            </form>
        '''
@app.route('/')
def index():
        if 'username' in session:
            return f'Hello, {session["username"]}!'
        return 'Please log in.'

@app.route('/logout')
def logout():
        session.pop('username', None) 
        return redirect(url_for('index'))

app.permanent_session_lifetime = timedelta(minutes=5) 
session.permanent = True

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem" 
Session(app)

if __name__ == '__main__':
    app.run(debug=True)