import sys
import time

import praw

reddit = praw.Reddit('bot')


def post(sub, title, url):
    """Submit a post to Reddit, retry up to 3 times"""
    retries = 0
    while retries < 3:
        try:
            result = reddit.subreddit(sub).submit(
                title,
                url=url
            )
            break
        except:
            print('Rate limited!')
            # Countdown MM:SS
            for remaining in range(10 * 60, 0, -1):
                minutes, seconds = divmod(remaining, 60)
                sys.stdout.write("\r")
                sys.stdout.write(f'Sleeping for {minutes}:{seconds:02}')
                sys.stdout.flush()
                time.sleep(1)
            retries += 1
    if result: 
        return result
    return None
