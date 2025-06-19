from flask import Flask, redirect, url_for

app = Flask(__name__)
@app.route('/')
def old_route():
    return redirect(url_for('new_route'))

@app.route('/new_route')
def new_route():
    return "You have been redirected to the new route!"

@app.route('/profile/<username>')
def profile(username):
    return f"Welcome, {username}!"

@app.route('/login')
def login():
    # After successful login, redirect to user's profile
    username = "testuser" # Replace with actual username from login
    return redirect(url_for('profile', username=username))

if __name__ == '__main__':
    app.run(debug=True)