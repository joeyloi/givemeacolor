import tweepy
import json

auth = tweepy.OAuthHandler('PPCwnKuCkpXCtAoT8BITSbwEU', 'Z4YX36riSnZLr8OiGxtesvaU3nFbG9SGFyVUsHM5rWVH0t2poK')
auth.set_access_token('2984729385-shInvPZQuBBbdbKbL5TkpNcxNcmbWAwNuEUIkJw', '4vnD3mdmI8PwWqCDV0L8rB9W1nXDb39WUPwHBv6v4OsTv')

api = tweepy.API(auth)

class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):

        global random_tweet

        # Twitter returns data in JSON format - we need to decode it first
        decoded = json.loads(data)

        random_tweet = decoded['text'].encode('ascii', 'ignore')

        # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
        # print decoded['text'].encode('ascii', 'ignore')

        if random_tweet is None:
            return True
        else:
            return False
        
    def on_error(self, status):
        print status

if __name__ == '__main__':
    l = s.StdOutListener()
    auth = tweepy.OAuthHandler('PPCwnKuCkpXCtAoT8BITSbwEU', 'Z4YX36riSnZLr8OiGxtesvaU3nFbG9SGFyVUsHM5rWVH0t2poK')
    auth.set_access_token('2984729385-shInvPZQuBBbdbKbL5TkpNcxNcmbWAwNuEUIkJw', '4vnD3mdmI8PwWqCDV0L8rB9W1nXDb39WUPwHBv6v4OsTv')
    stream = tweepy.Stream(auth, l)
    stream.filter(track=['color'])