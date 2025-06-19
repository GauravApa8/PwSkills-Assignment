from flask import Flask, jsonify, Response, json

data = {
        "name": "Alice",
        "age": 30,
        "city": "New York"
    }

app = Flask(__name__)

@app.route('/')
def get_user_data():
    data = {
        "name": "Alice",
        "age": 30,
        "city": "New York"
     }
    return jsonify(data)

@app.route('/raw_json')
def get_raw_json():
    data = {
        "message": "This is a raw JSON response."
    }
    return Response(json.dumps(data), mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True)