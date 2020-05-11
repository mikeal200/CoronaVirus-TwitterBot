import base64
import my_secrets
import requests
import tweepy

#for posting tweets
auth = tweepy.OAuthHandler(my_secrets.API_KEY, my_secrets.API_SECRET_KEY)
auth.set_access_token(my_secrets.ACCESS_TOKEN, my_secrets.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)