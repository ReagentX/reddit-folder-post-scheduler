# reddit-folder-post-scheduler

A "set-it-and-forget-it" Python program to handle automation of media posts to Reddit from a directory of files on the host machine.

The core of this program is the Scheduler object, which is constructed with a `pathlib.Path`, a list of Subreddits, and an Imgur API Client ID. When a scheduler object's `make_posts()` method is called, it will:

1) Select a photo randomly from the directory
2) Log the filename to `log/log.txt`
3) Upload the image to Imgur anonymously
4) Submit the Imgur link to each Subreddit in the list
5) Log each submission's permalink to `log/links.txt`

## Example Code

This will create a scheduler object that looks in the directory `/Users/chris/Pics/Dir-Of-Photos/` and post it to the subs `['sub_1', 'sub_2', 'sub_3', 'sub_4']`.

```python
from pathlib import Path
s = scheduler.Scheduler(
    Path('/Users/chris/Pics/Dir-Of-Photos'),
    ['sub_1', 'sub_2', 'sub_3', 'sub_4'],
    'imgur_client_id'
)
s.make_posts()
```

## Setup

- Clone this repo
- `cd` to the folder
- `python3.7 -m venv venv`
- Activate your virtual environment
- `python setup.py develop`
- `pip install -r requirements.txt`

## Usage Suggestions

To "set-it-and-forget-it," install the package on a machine that is always online (i.e. a VPS or even a Raspberry Pi on your network) and use `cron`:

    0 12 * * * cd Projects/reddit-folder-post-scheduler/ && . venv/bin/activate && python scripts/script.py

## Notes

- Imgur API Client registration: https://api.imgur.com/oauth2/addclient
- PRAW Docs: https://praw.readthedocs.io/en/latest/