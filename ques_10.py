from flask import Flask, render_template, abort

app = Flask(__name__)
# Custom Error Handlers with @app.errorhandler():
@app.errorhandler(404)
def page_not_found(e):
    """
    Handles 404 Not Found errors, rendering a custom 404.html template.
    """
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    """
    Handles 500 Internal Server Errors, rendering a custom 500.html template.
    """
    return render_template('500.html'), 500

@app.route('/')
def index():
    return "Welcome to the homepage!"

@app.route('/nonexistent-page')
def nonexistent_page():
    """
    This route will trigger a 404 error when accessed.
    """
    abort(404)

#Raising Errors with abort():
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404 - Page Not Found</h1>", 404

@app.route('/user/<int:user_id>')
def get_user(user_id):
    if user_id not in [1, 2, 3]:  # Simulate user not found
        abort(404)
    return f"User ID: {user_id}"

#Returning Status Codes Directly:
@app.route('/bad-request')
def bad_request():
    return "Bad Request", 400

if __name__ == '__main__':
    app.run(debug=True)