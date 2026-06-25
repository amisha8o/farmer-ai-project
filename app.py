from flask import Flask, render_template, request
from crop_predict import predict_crop

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    result = ""
    score = ""
    advice = ""

    if request.method == "POST":

        temp = int(request.form["temp"])
        rain = int(request.form["rain"])
        soil = request.form["soil"]

        result, score, advice = predict_crop(
            temp,
            rain,
            soil
        )

    return render_template(
        "index.html",
        result=result,
        score=score,
        advice=advice
    )

if __name__ == "__main__":
    app.run(debug=True)