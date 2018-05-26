# Log Analysis

This is a program querying to a news database called 'news' that answers following three questions:
1. What are the most popular three articles of all time? Which articles have been accessed the most?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

# Database Schema
Table: articles

| Column        | Type                     | Modifiers                                             |
| ------------- |:------------------------:|:-----------------------------------------------------:|
| author        | integer                  | not null                                              |
| title         | text                     | not null                                              |
| slug          | text                     | not null                                              |
| lead          | text                     |                                                       |
| body          | text                     |                                                       |
| time          | timestamp with time zone | default now()                                         |
| id            | integer                  | not null default nextval('articles_id_seq'::regclass) |


Table: authors

| Column        | Type           | Modifiers  |
| ------------- |:-------------:| :-----:|
|name | text | not null |
|bio | text | |
|id | integer | not null default nextval('authors_id_seq'::regclass) |

Table: log

| Column        | Type           | Modifiers  |
| ------------- |:-------------:| :-----:|
| path | text  | |
| ip | inet | |
| method | text | |
| status | text | |
| time | timestamp with time zone | default now() |
| id | integer | not null default nextval('log_id_seq'::regclass) |

## Usage
Download and load the data:

Download [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) and put the unzip file into `vagrant` directory.

Start vagrant and cd to the shared folder `/vagrant`
```
$ vagrant up
$ vagrant ssh
$ cd /vagrant
```
Load data
```
$ psql -d news -f newsdata.sql
```
Run the program
```
$ python3 logs_analysis.py
```

## Output
The output shold look like followings:

1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.
"Candidate is jerk, alleges rival" — 342102 views
"Bears love berries, alleges bear" — 256365 views
"Bad things gone, say good people" — 171762 views
"Goats eat Google's lawn" — 85775 views
"Trouble for troubled troublemakers" — 85679 views
"There are a lot of bears" — 85392 views
"Balloon goons doomed" — 85387 views
"Media obsessed with bears" — 85273 views

2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.
Ursula La Multa — 512805 views
Rudolf von Treppenwitz — 427781 views
Anonymous Contributor — 171762 views
Markoff Chaney — 85387 views

3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. 
July 17, 2016 — 2.32% errors

