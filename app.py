from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Simple user database (for demo purposes)
users = {
    "admin": "password123",
    "user": "testpass"
}

# HTML template (using render_template_string for simplicity)
login_page = """
<!doctype html>
<title>Login Page</title>
<h2>Login</h2>
<form method="post">
    <label>Username:</label><br>
    <input type="text" name="username"><br><br>
    <label>Password:</label><br>
    <input type="password" name="password"><br><br>
    <input type="submit" value="Login">
</form>
{% if error %}
<p style="color: red;">{{ error }}</p>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in users and users[username] == password:
            return f"<h2>Welcome, {username}!</h2>"
        else:
            error = "Invalid username or password"
    return render_template_string(login_page, error=error)

if __name__ == "__main__":
    app.run(debug=True)
