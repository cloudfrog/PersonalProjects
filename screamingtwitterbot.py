import tweepy
name = "CloudfrogBOT:"
scream = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)        tweetee = "@"+ status.author.screen_name + " "
        tweetee = tweetee.replace("@CloudfrogSc", "")
        api.update_status(tweetee + name + scream, in_reply_to_status_id=status.id);
        print(status.id)
        print("end")
        print(tweetee)
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_error disconnects the stream
            return False
consumer_key = 'xxxx'
consumer_secret = 'xxxx'
access_token = 'xxxx'
access_token_secret = 'xxxxxx'



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
	

api = tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(track=['@cloudfrogsc'])
