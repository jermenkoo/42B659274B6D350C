import requests as r

from flask import Flask, request
from twilio import twiml

app = Flask(__name__)


@app.route("/record", methods=['GET', 'POST'])
def record():
    """Returns TwiML which prompts the caller to record a message"""
    # Start our TwiML response
    response = twiml.Response()
    # Use <Say> to give the caller some instructions
    response.say('Hello. Please leave a message after the beep.')
    # Use <Record> to record the caller's message
    # response.record(transcribe=True, transcribeCallback='/calculate')
    response.record(transcribe=True)
    # End the call with <Hangup>
    response.hangup()

    req = r.post('https://ae6c1cf8.ngrok.io/add_query', data={
        'text': 'Hello, I am at this concert and I am feeling offended by these 2 strangers being touchy with me.', 'enc_phone': '447598428430'})
    print(req)
    return str(response or "Hi")


@app.route('/calculate', methods=['GET', 'POST'])
def callback():
    text = request.form['TranscriptionText']
    call = request.form['Caller']

    req = r.post('https://ae6c1cf8.ngrok.io/add_query', data={
        'text': text, 'encrypted_phone': call})

    print(text)

    return text

if __name__ == "__main__":
    app.run()
