# http://codeshare.io/5d5pK

from flask import Flask, request, render_template
from twilio.rest import TwilioRestClient 

# create our application
app = Flask(__name__)

# put your own credentials here 
ACCOUNT_SID = "AC7ca0096248271f08d8038add5a438cc7" 
AUTH_TOKEN = "8d58791d9d6dcdded9b663262dbfc07b" 

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 

@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == 'POST' and request.form['message'] and request.form['number']:
        client.messages.create(
            to=request.form['number'],
            from_="+14803606323", 
            body=request.form['message']
        )
    return render_template('text.html')

if __name__ == "__main__":
    app.run(port=5001)

