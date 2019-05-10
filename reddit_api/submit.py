import praw
import time


reddit = praw.Reddit('bot')


def post(sub, title, url):
    """Submit a post, retry up to 3 times"""
    retries = 0
    while retries < 3:
        try:
            result = reddit.subreddit(sub).submit(
                title,
                url=url
            )
        except:
            print('Rate limited, retrying in 10 minutes')
            time.sleep(10 * 60)  # 10 minutes
            retries += 1

    if result: 
        return submission
    return None