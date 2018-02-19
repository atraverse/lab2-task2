import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl
from flask import Flask, render_template, request
from location import point

app = Flask(__name__, template_folder='template')

def main_c(name):
    """
    The main function for finding information from Twitter
    """
    TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    url = twurl.augment(TWITTER_URL, {'screen_name': name, 'count': '5'})
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    js = json.loads(data)
    friends = []
    loc_friends = []
    for u in js['users']:
        friends.append(u['screen_name'])
        loc_friends.append(u['location'])
    point(loc_friends, friends)
#main_c('Microsoft')
#Flask 
@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    main_c(str(text))
    return render_template('result.html')

if __name__=="__main__":
    app.run()
