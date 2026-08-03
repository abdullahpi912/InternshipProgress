from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


# Task: "Pass text as a response" — plain text, no template involved
@app.route("/hello")
def hello():
    return "Hello, Flask! This route returns plain text instead of a rendered HTML page."


if __name__ == '__main__': # __main__ = app.py
    app.run(port=8080, debug=True)