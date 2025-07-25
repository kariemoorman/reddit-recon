# reddit-recon

<p align='center'><img src='https://github.com/kariemoorman/reddit-recon/blob/main/reddit-recon.png' alt='rr-png'/></p>

### Description
Reddit-Recon mines Reddit data by subreddit name, keyword, and/or username, and analyzes the contents. 

Use Reddit-Recon to isolate important and emerging topics, trends, and keywords, monitor user sentiment, and track user activity within and across subreddits. 

Reddit-Recon supports low-cost, on-demand and automated workflows at relatively low latency (24hr SLA), with data written and stored locally (see [data_pipeline](https://github.com/kariemoorman/reddit-recon/tree/main/data_pipeline)).

---

<details>
<summary><h3>Installation & Use</h3></summary>
<br>
  
- Clone or download .zip of `reddit-recon` Github repository.
```
git clone https://github.com/kariemoorman/tiktok-analyzer.git
```
- Create a virtual environment inside the `reddit-recon` directory.
```
cd reddit-recon && python -m venv .venv
```
- Activate virtual environment.
```
source .venv/bin/activate
```
- Install package dependencies.
```
pip install -r requirements.txt
```

- Create `credentials.py` file.

  - Register for [Reddit Developer account](https://www.reddit.com/prefs/apps/).  
  - Receive an [Access Token](https://praw.readthedocs.io/en/stable/getting_started/authentication.html).  
  - Add credentials to `credentials.py` file.  

```
touch src/scrapers/credentials.py

nano src/scrapers/credentials.py

## Credentials ## 
my_client_id = 'CLIENT_ID'
my_client_secret = 'CLIENT_SECRET'
my_user_agent = 'USER_AGENT'
my_password = "REDDIT_ACCOUNT_PASSWORD"
my_username = "REDDIT_ACCOUNT_USERNAME"
```

- Execute `reddit-recon` program.

```
python reddit-recon.py
```

<p><img src='https://github.com/kariemoorman/reddit-recon/blob/main/redditrecon.png' alt='rr' width='60%'/></p>

<br>
</details>

--- 

<p align='center'><b><a href='https://github.com/kariemoorman/reddit-recon/blob/main/LICENSE'>License: AGPL-3.0</a></b></p>
