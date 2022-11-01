from flask import Flask, jsonify, request, render_template
from project_data import utils
import config

app = Flask(__name__)

@app.route("/")
def Home():
    print("Home API")

    return render_template("User_input.html")




@app.route("/predicted_charges", methods = ["POST", "GET"])
def Insurance_charges():
    if request.method == "POST":
        data = request.form

        age = data["age"]
        sex = data["sex"]
        bmi = data["bmi"]
        children = data["children"]
    
        smoker = data["smoker"]
        region = data["region"]

    medi_insu = utils.MediInsurance(age, sex, bmi, children, smoker, region)
    premium = medi_insu.Predict_Charges()

    return  render_template("User_input.html", premium =premium)

if __name__ == "__main__":
    app.run(host = "0.0.0.0",port = config.PORT_NUMBER,debug = True)