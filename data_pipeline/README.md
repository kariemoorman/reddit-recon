## Reddit Data Pipeline

### Design Considerations

Parameters considered when constructing a data pipeline include the following: 
- <b>GDPR Compliance</b>: <i>Is any of the data I wish to extract classified as PII/PHI? </i>
- <b>Cost</b>: <i>How much am I willing to spend to maintain each step of the data pipeline? </i>
- <b>SLA</b>: <i>How fast do I need the data to be transformed and loaded for visualization? </i>
- <b>Data Storage Location</b>: <i>Where do I want my data to be stored: local/on-premises, cloud, or hybrid? </i>
- <b>Data Throughput</b>: <i>How much data needs to be transmitted in each READ/WRITE request (i.e., do I need distributed/batch compute capabilities)? </i>
- <b>Data Visualization</b>: <i>What types of analysis are meaningful for this dataset, what tools are best for visualizing those analyses, who do I want to have view access? </i>
- <b>Automation</b>: <i>How can I automate tasks within the workflow? </i>

---
### Project Summary

For this project, the goal is to select and extract data for a subset of subreddits and/or Reddit users, day-over-day, transform and execute a series of NLP and ML tasks on the extracted data, and load that transformed data into a dashboard for visualization, for little to no monetary cost. This means I am prioritizing monetary cost over time cost, and I assume the risk of encountering time delays in order to maintain low monetary cost strategy. The workflow should permit both on-demand and automated/scheduled executions.

I want to construct an automated data pipeline that adheres to the following criteria:
- Extracted data is not classified as PHI/PII. While usernames are extracted, no additional uniquely identifying information is included (e.g., profile metadata such as About description).
- Low to No $$ Cost.
- SLA on data extraction and transformation tasks is one full day (24 hours).
- Data, both extracted and tranformed, is stored locally.
- Data extraction, transformation, and load steps READ/WRITE is small (between 2-10 MB of data per request).
- Data visualization incorporates analyses of NER, topic modeling, sentiment, and user behaviors,  surfaced using a python-friendly dashboard application.



---
### Data Pipeline Design
<img src="https://github.com/kariemoorman/reddit-recon/blob/main/data_pipeline/images/data_pipelines-reddit_local_pipeline.drawio.png" height="500"/>


---
#### Extract & Load 

After [registering a Reddit developer application](https://www.reddit.com/prefs/apps/) and [receiving an access token](https://praw.readthedocs.io/en/stable/getting_started/authentication.html), use [PRAW API](https://praw.readthedocs.io/en/stable/index.html) to extract data for a particular subreddit or Reddit user.
Write that data, in whatever format (e.g., JSON, Parquet, CSV), to local storage. Load that data to a local repository (e.g., SQL database; local subdirectory).


#### Transform & Load 

Pre-process raw datasets, and execute a series of NLP and ML tasks. Write output as new dataset, in whatever format (e.g., JSON, Parquet, CSV), to local storage. Append the new dataset to the existing datasets in local repository (e.g., SQL database; local subdirectory).

#### Visualization 

Using the compiled dataset from the transformation step, surface the analyses in the form of interactive dashboards (e.g., Dash). 


#### Automation 

Workflow automation is accomplished using [crontab](https://www.geekbitzone.com/posts/macos/crontab/macos-schedule-tasks-with-crontab/) on MacOS.

--- 

<p align='center'><b><a href='https://github.com/kariemoorman/reddit-recon/blob/main/LICENSE'>License: AGPL-3.0 v3</a></b></p>
