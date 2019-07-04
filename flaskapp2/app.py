from flask import Flask,render_template,request
from flask_wtf import Form
from wtforms import *

class Review(Form):
    name = TextField()
    review = TextAreaField()
    submit = SubmitField("Post Review")

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():

    if request.METHOD 

    review = Review()

    return render_template("review.html", form=review)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=80)
