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
    response.record(transcribe=True, transcribeCallback='/calculate')
    # End the call with <Hangup>
    response.hangup()

    return str(response)


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
