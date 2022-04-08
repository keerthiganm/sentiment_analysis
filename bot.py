from flask import Flask, request
import requests
from flask import Flask,jsonify
from twilio.twiml.messaging_response import MessagingResponse
import nltk
from pprint import pprint
from nltk.sentiment import SentimentIntensityAnalyzer



app = Flask(__name__)

nltk.download([ "names","stopwords","state_union","twitter_samples","movie_reviews", "averaged_perceptron_tagger","vader_lexicon","punkt","shakespeare"])
  
@app.route('/')
def hello():
    return "Welcome Your BOT, It has Successfully BORN OUT ! "

@app.route("/sentiment/<string:text>",methods=['GET'])
def club(text):
    words = [w for w in nltk.corpus.state_union.words() if w.isalpha()]
    stopwords = nltk.corpus.stopwords.words("english")
    words = [w for w in words if w.lower() not in stopwords]
    
    pprint(nltk.word_tokenize(text), width=79, compact=True)

    words: list[str] = nltk.word_tokenize(text)
    fd = nltk.FreqDist(words)

    lower_fd = nltk.FreqDist([w.lower() for w in fd])

    sia = SentimentIntensityAnalyzer()
    print(sia.polarity_scores(text))
    comp=sia.polarity_scores(text)['compound']
    print(comp)
    return jsonify({'text':text,'compound':comp})

if __name__=="__main__":
    app.run(debug=True)


# @app.route('/bot', methods=['POST'])
# def bot():
#     incoming_msg = request.values.get('Body', '').lower()
#     resp = MessagingResponse()
#     msg = resp.message()
#     responded = False
#     if 'event' in incoming_msg:
#         # faculty details
#         sen,name =incoming_msg.split('event ')
#         name=name.lower()
#         docs=db.collection('event_details').where("eventname","==",name).get()
#         if docs.exists:
#             for doc in docs:
#                 print(doc.to_dict())
#                 msg.body(doc.to_dict())
#                 responded = True    
#     if not responded:
#         msg.body('I am learning and growing day by day \n- UniBud:)')
#     return str(resp)


# if __name__ == '__main__':
#     app.run()
