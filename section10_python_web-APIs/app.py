from flask import Flask, render_template, session, redirect, request, url_for, g
from database import Database
from user import User
from twitter_utils import get_request_token, get_oauth_verifier_url, get_access_token

import requests

app = Flask(__name__)
app.secret_key = '1234'

Database.initialise(host='localhost', database='learning', user='postgres', password='1234', port=5433)


@app.before_request
def load_user():
    if 'screen_name' in session:
        g.user = User.load_from_db_by_screen_name(session['screen_name'])


@app.route('/')
def homepage():
    return render_template('home.html', title='Home')


@app.route('/login/twitter')
def twitter_login():
    if 'screen_name' in session:
        return redirect(url_for('profile'))
    request_token = get_request_token()
    session['request_token'] = request_token

    return redirect(get_oauth_verifier_url(request_token))


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('homepage'))


@app.route('/auth/twitter')  # http://127.0.0.1:4995/auth/twitter?oauth_verifier=1234567
def twitter_auth():
    # Get oauth_verifier from the uri query string
    oauth_verifier = request.args.get('oauth_verifier')
    # Get the access token
    access_token = get_access_token(session['request_token'], oauth_verifier)

    user = User.load_from_db_by_screen_name(access_token['screen_name'])
    if not user:
        user = User(access_token['screen_name'], access_token['oauth_token'],
                    access_token['oauth_token_secret'], None)
        user.save_to_db()

    session['screen_name'] = user.screen_name

    return redirect(url_for('profile'))


@app.route('/profile')
def profile():
    return render_template('profile.html', user=g.user, title='User profile')


@app.route('/search')
def search():
    # Get query from user form
    query = request.args.get('q')
    # Get tweets using User method
    tweets = g.user.twitter_request('https://api.twitter.com/1.1/search/tweets.json?q={}'.format(query))
    # Initialize dict with tweet texts and a default label
    tweet_texts = [{'tweet': tweet['text'], 'label': 'neutral'} for tweet in tweets['statuses']]
    # Perform sentiment analysis on each tweet text
    for tweet in tweet_texts:
        # Make API request
        r = requests.post('http://text-processing.com/api/sentiment/', data={'text': tweet['tweet']})
        # Put response in json object
        json_response = r.json()
        # Get label from response
        label = json_response['label']
        # Update tweet sentiment label
        tweet['label'] = label

    # Pass tweet_texts obj as content and render template
    return render_template('search.html', content=tweet_texts, title='Search results')


app.run(port=4995, debug=True)
