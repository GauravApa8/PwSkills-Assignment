from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def original_page():
    return redirect(url_for('target_page', name='Alice', city='New York'))

@app.route('/target_page')
def target_page():
    name = request.args.get('name')
    city = request.args.get('city')
    return f"Hello, {name} from {city}!"

if __name__ == '__main__':
    app.run(debug=True)