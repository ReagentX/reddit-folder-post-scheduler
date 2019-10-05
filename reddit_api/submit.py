import sys
import pathlib
import time

import praw
import cv2

reddit = praw.Reddit('bot')


def post(sub, title, url) -> dict:
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

def post_video(sub: str, title: str, video: pathlib.Path, thumb: pathlib.Path) -> dict:
    retries = 0
    while retries < 3:
        try:
            result = reddit.subreddit(sub).submit_video(
                title,
                video_path=video,
                thumbnail_path=thumb
            )
            break
        except Exception as e:
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


def get_first_frame(video_path: pathlib.Path) -> pathlib.Path:
    vidcap = cv2.VideoCapture(str(video_path))
    success, image = vidcap.read()
    if success:
        cv2.imwrite('thumb.png', image)  # save frame as JPEG file
    return pathlib.Path('thumb.png')