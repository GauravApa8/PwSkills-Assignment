from flask import Flask, render_template, request, render_template_string

app = Flask(__name__)
@app.route('/')
def ques_4():
    user = {
        "name": "Gaurav Suman",
        "email": "gauravsuman@example.com",
        "age": 28
    }
    return render_template('index.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)