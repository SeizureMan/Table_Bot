import praw
# Now we might not need this at the start but it will be essential
import time


# Lets Start

# This is a reddit object
user_agent = ("The Table Bot")

# This is our reddit object that uses the user agent as a user agent :O
#user agents are the reddit bot
reddit = praw.Reddit(user_agent = user_agent)
#this tells reddit what bot we are

subreddit = r.get_subreddit("IAMA")
