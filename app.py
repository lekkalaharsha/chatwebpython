from flask import Flask,render_template,request,jsonify,get_flashed_messages
from chat import get_response
import slack
import os, signal

from flask import request
from flask import Flask
from  chatgpt import chatgpt

from slackeventsapi import SlackEventAdapter


app = Flask(__name__)
@app.route('/',methods=['GET'])
def index_get():
    return render_template("base.html")



@app.route("/predict",methods=["POST"])
def predict():
    text =request.get_json().get("message")
    #todo , chech if the text is valid
    response= get_response(text)
    message={"answer":  response }
    return jsonify(message)



if __name__ =="__main__":
    app.run(debug=True)