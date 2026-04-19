from flask import Flask, render_template, request
from caesar import caesar_cipher

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        text = request.form["text"]
        shift = int(request.form["shift"])
        mode = request.form["mode"]
        result = caesar_cipher(mode, text, shift)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)