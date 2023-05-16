from datetime import datetime
from flask import Flask, render_template
from . import app

@app.route("/")
def home():
    days = [ ]
    for i in range(1, 32):
        if ((i-1) % 7 < 3):
            days.append( {"number": i, "status": 0})
        else:
            days.append( {"number": i, "status": 1})

    context = {
        "days" : days
    }
    return render_template("table.html", **context)

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")
