from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def search_results():
    query = request.args.get('q')
    category = request.args.get('category')
    return f"Searching for '{query}' in category '{category}'"

@app.route('/users/<int:user_id>')
def get_user(user_id):
    return f"User ID: {user_id}"

@app.route('/products/<string:product_name>')
def get_product(product_name):
    return f"Product Name: {product_name}"

if __name__ == '__main__':
    app.run(debug=True)