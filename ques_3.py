from flask import Flask, render_template, request, render_template_string

app = Flask(__name__)
# Basic syntax:
@app.route('/', methods=['GET', 'POST'])
def your_function():
    if request.method == 'GET':
        return "This is a GET request"
    elif request.method == 'POST':
        return "This is a POST request"
    
#/message Route with GET and POST
@app.route('/message', methods=['GET', 'POST'])
def message():
    if request.method == 'GET':
        return "Send a message using POST."
    elif request.method == 'POST':
        data = request.get_json()
        return f"Message received: {data.get('text')}"
    
# Example with PUT and DELETE
@app.route('/user/<int:user_id>', methods=['PUT', 'DELETE'])
def update_or_delete(user_id):
    if request.method == 'PUT':
        return f"Updating user with ID {user_id}"
    elif request.method == 'DELETE':
        return f"Deleting user with ID {user_id}"

@app.route('/submit', methods=['POST'])
def submit():
    return "Form submitted"


if __name__ == '__main__':
    app.run(debug=True)