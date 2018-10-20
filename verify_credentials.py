import tweepy

consumer_key = "FsAPXfn1mvWFe8Itk3kpMgAtt"
consumer_secret = "xkv0i9evh30hq9C57jpX62XwpdVoNUVGgzUSEJKAm6mJhpIPEq"
access_token = "335350812-vUaT8oMt4qmds9wTbg8JmRvDaW5DfN3AhdkviMYn"
access_token_secret = "EMsLF9Elx3E1z72p53TKRMyREs9byW6FRCNBImwEzx1yh"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user = api.get_user(335350812)
print(user._json,"user")
#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print (tweet.text)
