from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    error = ''
    if request.method == 'POST':
        username = request.form.get('username')
        if not username:
            error = 'Username is required'
        elif len(username) < 3:
            error = 'Username must be at least 3 characters long'
        else:
            return f"Welcome, {username}!"
    
    return render_template_string("""
        <form method="POST">
            <input name="username" placeholder="Enter name">
            <input type="submit">
            <p style="color:red">{{ error }}</p>
        </form>
    """, error=error)

if __name__ == '__main__':
    app.run(debug=True)