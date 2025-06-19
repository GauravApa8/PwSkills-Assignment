from flask import Flask, render_template, request, render_template_string

app = Flask(__name__)
@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['username']
    return f"Hello, {name}!"

if __name__ == '__main__':
    app.run(debug=True)