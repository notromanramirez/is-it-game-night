# Roman Ramirez, rr8rk@virginia.edu

### IMPORTS ###

import tweepy
from datetime import date
from time import gmtime, strftime, sleep

### CONSTANT TWITTER VARIABLES ###

CONSUMER_KEY = "WmuoMM30xeN7VIBoQw5ZRXlm5"
CONSUMER_SECRET = "2edBQxvFQgiBh2DlVdReIKCI8JaJFpfGwSOPxhMivYm9OsOLbR"

ACCESS_KEY = "1408441889058078724-KTQUX8144SzBUMoSwhT74EwmMwhtiA"
ACCESS_SECRET = "Ahnaikkhd7xqLNZPKlH4elVNAplpjCSn0Pm5a062Wo3a2"

### SETTING UP TWITTER API ###

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

### THE SCRIPT ###

# a function that sends a tweet about game night
def send_game_night_tweet():

    # output message
	print('Sending game night tweet.\n')

    # determine the day of the week
	date_of_today = date.today()
	day_of_the_week = date_of_today.weekday()

	# if it is either Monday or Thursday
	if ((day_of_the_week == 0) or (day_of_the_week == 3)):

        # post a picture of attention.jpg
		attention_jpg = "images/attention.jpg"
		media = api.media_upload(filename=attention_jpg)
		api.update_status(media_ids=[media.media_id])

	else:
	    # create a post saying that it is not game night.
		api.update_status(status="Tonight is not game night.")

# run forever
while True:

    # the time to tweet an update is noon EST
	TIME_TO_TWEET = "16:00"

	# store the current time
	current_time = strftime("%H:%M", gmtime())

	print("It is now %s." % current_time)

    # send a tweet if it's time to send one
	if (current_time == TIME_TO_TWEET):
		send_game_night_tweet()
	# otherwise wait
	else:
		print("It isn't time to send a tweet yet. A tweet will be sent at %s.\n" % TIME_TO_TWEET)

	# wait 59 seconds before checking
	sleep(59)