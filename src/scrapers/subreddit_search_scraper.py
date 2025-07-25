#!/usr/bin/python3

import os
import argparse
import json
from datetime import datetime
import pandas as pd
import requests
import praw

## add credentials.py script to .gitignore list to keep personal keys safe. ##
from src.scrapers.credentials import *

class SubredditSearchScraper:
    def __init__(self, subreddits, category):
        self.subreddits = subreddits
        self.category = category
        
        ## Establish Reddit Connection ##
        self.reddit = praw.Reddit(client_id=my_client_id, client_secret=my_client_secret, user_agent=my_user_agent)

        ## Datetime Snapshot ##
        self.snapshotdate = datetime.today().strftime('%d-%b-%Y')
        self.snapshotdatetime = datetime.today().strftime('%d-%b-%Y_%H-%M-%S')

    def _praw_search_subreddit_activity(self, search_query_items, post_type, post_limit):
        ## Iterate over subreddit items in subreddits list.
        for subreddit in self.subreddits:
            ## Print task initialization message.
            print(f'\nGathering {post_type} posts from Subreddit: "{subreddit}"...')
            ## Make output directories.
            dir_path = f"__data/__posts/{self.category}/{subreddit}/{self.snapshotdate}/praw"
            os.makedirs(f"{dir_path}", exist_ok=True)
            ## Extract subreddit posts (submissions and comments).
            posts = []
            for search_item in search_query_items:
                ## Print task status message.
                print(f'Gathering "{post_type}" posts for search item: "{search_item}" in "{subreddit}" Subreddit...')
                ## Extract subreddit posts (submissions and comments).
                sub_posts = self.reddit.subreddit(subreddit).search(search_item, sort=post_type, limit=post_limit)
                for post in sub_posts:
                    ## Transform unix datetime to PST.
                    created_pst = datetime.fromtimestamp(post.created_utc).strftime('%d-%b-%Y %H:%M:%S')
                    comments = []
                    submission = self.reddit.submission(id=post.id)
                    submission.comments.replace_more(limit=None)
                    for comment in submission.comments.list():
                        comments.append(f'{comment.author}: {comment.body}')
                    posts.append([post.created_utc, created_pst, search_item, post.subreddit, post.id, post.title, post.author, post.score, post.url, post.selftext, post.num_comments, comments])
                ## Transform posts data to pandas DataFrame.
                post_df = pd.DataFrame(posts, columns=['created_unix_utc', 'created_datetime_pst', 'search_item', 'subreddit', 'id', 'title', 'author', 'score', 'url', 'body', 'num_comments', 'comments'])
                ## Write DataFrame to output directory in csv format.
                post_df.to_csv(f'{dir_path}/{subreddit}_subreddit_search_{post_type}_posts_{self.snapshotdatetime}.csv', index=False, sep='\t')


    def _pushshift_search_subreddit_activity(self, search_query_items, api, before_days, post_limit):
        ## Iterate over items in subreddits list.
        for subreddit in self.subreddits:
            ## Print task initialization message.
            print(f'Gathering {post_limit} {before_days}-trailing posts for Subreddit: "{subreddit}"...')
            subreddit_search_submissions_df = pd.DataFrame()
            subreddit_search_comments_df = pd.DataFrame()
            for search_item in search_query_items: 
                ## Print task status message.
                print(f'Querying "{search_item}" in Subreddit: "{subreddit}"...')
                ## Load submissions and comments from {subreddit} using Pushshift API.
                submissions = json.loads(requests.get(f'https://api.{api}.io/reddit/search/submission?subreddit={subreddit}&before={before_days}&size={post_limit}&q={search_item}&sort=created_utc&metadata=false', timeout=20).text or '{}' or '' or '[]' or 'None' or None)
                comments = json.loads(requests.get(f'https://api.{api}.io/reddit/search/comment?subreddit={subreddit}&before={before_days}&size={post_limit}&q={search_item}&sort=created_utc&metadata=false', timeout=20).text or '{}' or '' or '[]' or 'None' or None)
                subreddit_submissions_df = pd.DataFrame(submissions['data'])
                subreddit_comments_df = pd.DataFrame(comments['data'])
                dir_path = f"__data/__posts/{self.category}/{subreddit}/{self.snapshotdate}/ps"
                if not subreddit_submissions_df.empty:
                    ## Create output directory.
                    os.makedirs(f"{dir_path}", exist_ok=True)
                    ## Add column denoting search item used in subreddit query and append to DataFrame.
                    subreddit_submissions_df['search_item'] = f'{search_item}'
                    ## Transform unix datetime to PST, and append to DataFrame.
                    if 'created_utc' in subreddit_submissions_df:
                        submission_created_pst = [datetime.fromtimestamp(item).strftime('%d-%b-%Y %H:%M:%S') for item in subreddit_submissions_df.created_utc]
                        subreddit_submissions_df['created_pst'] = submission_created_pst
                    ## Concatenate DataFrames in a single DataFrame.
                    subreddit_search_submissions_df = pd.concat([subreddit_search_submissions_df,subreddit_submissions_df], ignore_index=True)
                if not subreddit_comments_df.empty: 
                    ## Create output directory.
                    os.makedirs(f"{dir_path}", exist_ok=True)
                    ## Add column denoting search item used in subreddit query and append to DataFrame.
                    subreddit_comments_df['search_item'] = f'{search_item}'
                    ## Transform unix datetime to PST, and append to DataFrame.
                    if 'created_utc' in subreddit_comments_df:
                        comment_created_pst = [datetime.fromtimestamp(item).strftime('%d-%b-%Y %H:%M:%S') for item in subreddit_comments_df.created_utc]
                        subreddit_comments_df['created_pst'] = comment_created_pst
                    ## Concatenate DataFrames in a single DataFrame.
                    subreddit_search_comments_df = pd.concat([subreddit_search_comments_df,subreddit_comments_df], ignore_index=True)
                ## Write DataFrames to output directory in csv format.
                subreddit_search_comments_df.to_csv(f'{dir_path}/{subreddit}_subreddit_search_comments_{before_days}_{self.snapshotdatetime}.csv', index=False, sep='\t')
                subreddit_search_submissions_df.to_csv(f'{dir_path}/{subreddit}_subreddit_search_submissions_{before_days}_{self.snapshotdatetime}.csv', index=False, sep='\t')


    def extract_search_subreddit_data(self, search_query_items, post_type='new', api='praw', before_days='0d', post_limit=1000):
        if api == 'praw':
            self._praw_search_subreddit_activity(search_query_items, post_type, post_limit)
        elif api in ['pushshift','pullpush']:
            self._pushshift_search_subreddit_activity(search_query_items, api, before_days, post_limit)
        else: 
            print("Unsupported API specified.")
        print("Task Complete!")


def main():
    parser = argparse.ArgumentParser(description="Reddit Scraper")
    parser.add_argument("subreddits", type=str, nargs="+", help="List of subreddits")
    parser.add_argument("--api", type=str, choices=["praw", "pushshift", "pullpush"], default="praw", help="API ('praw' or 'pushshift')")
    parser.add_argument("--search_query_items", '-q', type=str, nargs="+", help="List of search query items")
    parser.add_argument("--category", "-c", type=str, help="Category for the output directory")
    parser.add_argument("--post_type", "-t", type=str, choices=["hot", "new", "top"], default="new", help="Type of posts to retrieve")
    parser.add_argument("--before_days", "-b", type=str, default="0d", help="Type of posts to retrieve")
    parser.add_argument("--post_limit", "-l", type=int, default=1000, help="Limit of posts to retrieve (1-1000)")

    args = parser.parse_args()

    scraper = SubredditSearchScraper(args.subreddits, args.category)
    scraper.extract_search_subreddit_data(args.search_query_items, args.post_type, args.api, args.before_days, args.post_limit)

if __name__ == "__main__":
    main()