#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and returns the number of subscribers"""

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent)
    all_data = response.json()

    try:
        return all_data.get('data').get('subscribers')

    except:
        return 0
