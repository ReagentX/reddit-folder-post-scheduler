from setuptools import setup, find_packages

setup(
    name='reddit-folder-post-scheduler',
    version='1.0',
    description='A Python 3 API to schedule image posts from a folder of images',
    author='Christopher Sardegna',
    author_email='github@reagentx.net',
    install_requires=['requests', 'praw'],
    packages=find_packages(),
    scripts=[]
)