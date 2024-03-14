# reddit-recon

<p align='center'><img src='https://github.com/kariemoorman/reddit-recon/blob/main/redditrecon.png' alt='rr' width='60%'/></p>

<br>

### Description
Reddit-Recon mines Reddit data by subreddit name, keyword, and/or username, and analyzes the contents. Use Reddit-Recon to isolate important and emerging topics, trends, and keywords, monitor user sentiment, and track user activity within and across subreddits. 

Reddit-Recon supports low-cost on-demand and automated workflows at relatively low latency, with data written and stored locally (see [data_pipeline](https://github.com/kariemoorman/reddit-recon/tree/main/data_pipeline)).

---

### Installation & Use

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
- Execute `reddit-recon` program.
```
python reddit-recon.py
```

--- 

<p align='center'><b><a href='https://github.com/kariemoorman/reddit-recon/blob/main/LICENSE'>License: AGPL-3.0</a></b></p>
