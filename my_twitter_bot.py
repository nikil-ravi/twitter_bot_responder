import tweepy
import time
from keys import *

print("this is my twitter bot")

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id():
    f_read = open(FILE_NAME, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id):
    f_write = open(FILE_NAME, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply():

    print("Attempting to find and reply to tweets")

    last_seen_id = retrieve_last_seen_id()

    mentions = api.mentions_timeline(last_seen_id)

    for mention in reversed(mentions):
        print("entered loop")
        print(str(mention.id) + ' - ' + mention.text)
        last_seen_id = mention.id
        if '#HelloBot' in mention.text:
            print("Found- responding back")
            api.update_status('@ravi_nikil Hi! I am the bot.', last_seen_id)
        store_last_seen_id(last_seen_id)

while True:
    reply()
    time.sleep(5)