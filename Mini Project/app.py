import re 
import tweepy 
from textblob import TextBlob 
from textblob.sentiments import NaiveBayesAnalyzer
from flask import Flask, render_template , redirect, url_for, request



def clean_tweet( tweet ):
    tweet=re.sub(r'@[_A-Za-z0-9]+','',tweet) #removed @mentions
    tweet=re.sub(r'#','',tweet) #removed '#' symbol     
    tweet=re.sub(r'RT[\s]+','',tweet) #removed re tweets
    tweet=re.sub(r'https?:\/\/\S+','',tweet) #removed urls
    return tweet



def get_tweet_sentiment( tweet): 
        # analysis = TextBlob(clean_tweet(tweet), analyzer=NaiveBayesAnalyzer()) 
        analysis = TextBlob(clean_tweet(tweet)) 
        if (analysis.sentiment.polarity<0 and analysis.sentiment.polarity>=-0.5):
            return 'Fairly Negative'
        elif (analysis.sentiment.polarity<-0.5 and analysis.sentiment.polarity>=-1):
            return 'Strongly Negative'
        elif (analysis.sentiment.polarity==0):
            return 'Neutral'
        elif (analysis.sentiment.polarity>0 and analysis.sentiment.polarity<=0.5):
            return 'Fairly Positive'
        else:
            return 'Strongly Positive'



def get_tweets(api, uname, count): 
        count = int(count)
        tweets = [] 
        try: 
            fetched_tweets = tweepy.Cursor(api.search_tweets, q=uname, lang="en", tweet_mode='extended').items(count)
            for tweet in fetched_tweets: 
                parsed_tweet = {} 
                if 'retweeted_status' in dir(tweet):
                    parsed_tweet['text'] = tweet.retweeted_status.full_text
                else:
                    parsed_tweet['text'] = tweet.full_text
                parsed_tweet['sentiment'] = get_tweet_sentiment(parsed_tweet['text']) 
                if tweet.retweet_count > 0: 
                    if parsed_tweet not in tweets: 
                        tweets.append(parsed_tweet) 
                else: 
                    tweets.append(parsed_tweet) 
            return tweets 
        except tweepy.TweepyException as e: 
            print("Error : " + str(e)) 



app = Flask(__name__)
app.static_folder = 'static'



@app.route('/')
def home():
  return render_template("index.html") #main homepage



#for tweets fetched from twitter
@app.route("/fetchedTweets", methods=['POST','GET'])
def pred():
	if request.method=='POST':
            uname=request.form['uname']
            count=request.form['num']
            fetched_tweets = get_tweets(api,uname, count) 
            return render_template('fetchedTweets.html', result=fetched_tweets)



#for user entered tweet manually
@app.route("/manualTweet", methods=['POST','GET'])
def pred1():
	if request.method=='POST':
            text = request.form['enteredTweet'] #from index.html (homepage) getting the text
            blob = TextBlob(text)
            if (blob.sentiment.polarity<0 and blob.sentiment.polarity>=-0.5):
                text_sentiment = 'Fairly Negative'
            elif (blob.sentiment.polarity<-0.5 and blob.sentiment.polarity>=-1):
                text_sentiment = 'Strongly Negative'
            elif (blob.sentiment.polarity==0):
                text_sentiment = 'Neutral'
            elif (blob.sentiment.polarity>0 and blob.sentiment.polarity<=0.5):
                text_sentiment = 'Fairly Positive'
            else:
                text_sentiment = 'Strongly Positive'
            return render_template('enteredTweet.html',userEnteredText=text, predictedSentiment=text_sentiment) #providing the result to the enteredTweet.html (result page) 



if __name__ == '__main__':
    #my twitter development account credentials
    consumerKey="mUrPdkpb4byZIvZWxogQffF9h"
    consumerSecret="RGOwUESJfHUA8lPHXerCPPtXo8gyh7TXNHoTeLJdBEBNRG3liV"
    accessToken="796919673480581121-ALgaxw4BrGXQlKgXOEWurkjh6jzDwxY"
    accessTokenSecret="vG2Z5Xecn3CUF5fkSOK4JVB2arkqmx02Xr0fLwUtM7qKN"
    try: 
        #creating the authentication object
        authenticate=tweepy.OAuthHandler(consumerKey,consumerSecret)
        #setting the access token and access token secret
        authenticate.set_access_token(accessToken,accessTokenSecret)
        #creating the API object while passing the authentication information
        api=tweepy.API(authenticate,wait_on_rate_limit=True)
    except: 
        print("Error: Authentication Failed") 
    app.debug=True
    app.run(host='localhost')