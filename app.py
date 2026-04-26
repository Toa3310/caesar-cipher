from flask import Flask, render_template, request
from caesar import caesar_cipher

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    mode_option = ""
    if request.method == "POST":
        try:
            text = request.form["text"]
            shift = int(request.form["shift"])
            mode = request.form["mode"]
            result = caesar_cipher(mode, text, shift)

            if mode == "1":
                mode_option = "暗号化結果"
            elif mode == "2":
                mode_option = "復号結果"
        except ValueError:
            result = "エラー(シフト数が入力されていません)"
            mode_option = "処理結果"
    return render_template("index.html", result=result, mode_label=mode_option)

if __name__ == "__main__":
    app.run(debug=True)