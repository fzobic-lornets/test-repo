from flask import Flask, render_template_string, request

# Initialize the Flask application
app = Flask(__name__)

# Inline HTML template to keep everything in one file
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Single-File Python Web App</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 50px; background-color: #f4f4f9; }
        .container { max-width: 500px; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
        input[type="text"] { width: 100%; padding: 10px; margin: 10px 0; box-sizing: border-box; }
        input[type="submit"] { background-color: #007BFF; color: white; border: none; padding: 10px 15px; cursor: pointer; border-radius: 4px; }
        input[type="submit"]:hover { background-color: #0056b3; }
    </style>
</head>
<body>
    <div class="container">
        <h2>Welcome to My Single-File App!</h2>

        <!-- Form submitting back to the same page -->
        <form method="POST">
            <label for="username">Enter your name:</label>
            <input type="text" id="username" name="username" placeholder="Type here..." required>
            <input type="submit" value="Greet Me">
        </form>

        {% if name %}
            <h3 style="color: #28a745; margin-top: 20px;">Hello, {{ name }}! Glad you are here.</h3>
        {% endif %}
    </div>
</body>
</html>
"""

# Route handling both landing on the page (GET) and submitting the form (POST)
@app.route("/", methods=["GET", "POST"])
def home():
    name = None
    if request.method == "POST":
        name = request.form.get("username")

    # Renders the HTML string directly instead of loading an external file
    return render_template_string(HTML_TEMPLATE, name=name)

# Run the app locally
if __name__ == "__main__":
    app.run(debug=True, port=5000)
