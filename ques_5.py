from flask import Flask, render_template, request, render_template_string

app = Flask(__name__)
@app.route('/')
def ques_5():
        return 'Hello, World!'

@app.route('/about')
def about():
        return 'This is the about page.'

if __name__ == '__main__':
    app.run(debug=True)