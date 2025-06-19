from flask import Flask
app = Flask(__name__)

def reverse_string(s):
    return s[::-1]

# Define and register
def reverse_string(s):
    return s[::-1]

@app.template_filter('reverse')
def reverse_string(s):
    return s[::-1]

@app.template_filter('repeat')
def repeat_string(s, times=2):
    return s * times

app.add_template_filter(reverse_string, 'reverse')

if __name__ == '__main__':
    app.run(debug=True)