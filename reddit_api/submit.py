import praw
import os

print(os.getcwd())
reddit = praw.Reddit('bot')


def post(sub, title, url):
    result = reddit.subreddit(sub).submit(
        title,
        url=url
    )
    if result: 
        return submission.permalink
    return None