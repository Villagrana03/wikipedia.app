from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    # Display the form
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    # Process the form data
    name = request.form["name"]  # This connects to the input field with name="name"
    
    # Redirect to the result page with the name as a URL parameter
    return redirect(url_for("nameResult", user_name=name))

@app.route("/nameResult", methods=["GET", "POST"])
def nameResult():
    # Get the name from the URL parameters
    user_name = request.args.get("user_name")
    
    # Render the result page and pass the name to the template
    return render_template("nameResult.html", name=user_name)

if __name__ == "__main__":
    app.run(debug=True)
