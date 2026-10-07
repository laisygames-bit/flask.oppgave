import random
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def elev():
    elever = ["Ola", "Kari", "Per", "Fatima"]
    navn = random.choice(elever)
    return render_template("elever.html", navn=navn, elever=elever)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)