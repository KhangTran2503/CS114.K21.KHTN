import os, time
from flask import Flask, render_template, request, jsonify
import block_pred

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["DEBUG"] = 0

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = request.form.get("img-data")
        data = data.split(',')
        data = [int(num) for num in data]
        with open("static/image/new_image","wb") as f:
            f.write(bytearray(data))
        response = block_pred.predict()
        return render_template("index.html", response=response)
    return render_template("index.html")


@app.route("/prediction", methods=["GET","POST"])
def prediction():
    data = request.form.get("img-data")
    data = data.split(',')
    data = [int(num) for num in data]
    with open("static/image/new_image","wb") as f:
        f.write(bytearray(data))
    result = block_pred.predict() + 1
    return render_template("predict.html", prediction=result)
