from flask import Flask, render_template, request
from services.ai_service import frage_ki



app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def start():
    antwort = ""

    if request.method == "POST":
        aufgabe = request.form.get("aufgabe")

        if aufgabe:
            antwort = frage_ki(aufgabe)

    return render_template("index.html", antwort=antwort)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
