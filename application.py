import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")

DAYS = [x for x in range(1, 32)]
MONTHS = [x for x in range(1, 13)]


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        
        name = request.form.get("name")
        if not name:
            return render_template("error.html", message="Missing name")
        
        day = int(request.form.get("day"))
        if day not in DAYS:
            return render_template("error.html", message="Invalid day")
        
        month = int(request.form.get("month"))
        if month not in MONTHS:
            return render_template("error.html", message="Invalid month")
        
        db.execute("INSERT INTO birthdays (name, day, month) VALUES(?, ?, ?)", name, day, month)
        
        return redirect("/")

    else:

        BIRTHDAYS = db.execute("SELECT * FROM birthdays")
        return render_template("index.html", birthdays=BIRTHDAYS, days=DAYS, months=MONTHS)
