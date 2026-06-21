from flask import Flask,render_template
import requests


app = Flask(__name__)

@app.route('/guess/<name>')
def guess(name):
    gender_url=f"https://api.genderize.io/?name={name}&country_id=US"
    gender_response=requests.get(gender_url)
    gender_data=gender_response.json()
    gender=gender_data["gender"]
    age_url=f"https://api.agify.io/?name={name}&country_id=US"
    age_response=requests.get(age_url)
    age_data=age_response.json()
    age=age_data["age"]
    return render_template("guess.html",pname=name,gender=gender,age=age)









