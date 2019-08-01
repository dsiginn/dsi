from flask import Flask,render_template,url_for,request
import pickle
from sklearn.ensemble import AdaBoostClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib
from flask import Flask, request
from twilio.twiml.messaging_response import (
    MessagingResponse,
    Message,
    Body,
    Media
)

app = Flask(__name__, static_url_path='/static')

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/sms', methods=['POST'])
def sms_reply():
    resp = MessagingResponse()
    #Fetch message
    msg = request.form.get('Body')

    #create reply
    if len(msg) >20:
        #resp.message("Accessing input..")
        #setup of model
        ad = joblib.load('model2.joblib')
        tv = joblib.load('tv.joblib')
        #load text to model
        data = [msg]
        vect = tv.transform(data).toarray()
        my_prediction = ad.predict(vect)
        if my_prediction == 1:
            resp.message('We have received your distress call.\nShare your exact location\nWe will send a pony over')
        else:
            resp.message('Thank you for reaching out.\nPlease do not waste your time and our precious time thank you.')
    else:
        #resp.message("Accessing input..")
        resp.message('Furnish us with following information\n1)Incident nature\n2)Location')

    return str(resp)

@app.route('/predict',methods=['POST'])
def predict():
    ad = joblib.load('model2.joblib')
    tv = joblib.load('tv.joblib')

    if request.method == 'POST':
        message = request.form['contact_message']
        data = [message]
        vect = tv.transform(data).toarray()
        my_prediction = ad.predict(vect)
        if my_prediction == 1:
            x = "Disaster Outreach"
            y = 'We have received your distress call. Share your exact location and we will send a pony over'
        else:
            x = "Non-Disaster"
            y = 'Thank you for reaching out. Please do not waste your time and our precious time thank you.'
        return render_template('pred.html', input_text = y, predi = x)
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=False)
