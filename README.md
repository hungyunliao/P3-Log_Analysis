# Log Analysis

This is a program querying to a news database called 'news' that answers following three questions:
1. What are the most popular three articles of all time? Which articles have been accessed the most?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

# Database Schema

| Column        | Type           | Modifiers  |
| ------------- |:-------------:| :-----:|
|author | integer | not null |
|title | text | not null |
|slug | text | not null |
|lead | text | |
|body | text | |
|time | timestamp with time zone | default now() |
|id | integer | not null default nextval('articles_id_seq'::regclass) |

Table: articles
Column | Type | Modifiers
--- | --- | ---
author | integer | not null
title | text | not null
slug | text | not null
lead | text | 
body | text | 
time | timestamp with time zone | default now()
id | integer | not null default nextval('articles_id_seq'::regclass)

Table: authors
Column | Type | Modifiers
--- | --- | ---
name | text | not null
bio | text | 
id | integer | not null default nextval('authors_id_seq'::regclass)

Table: log
Column | Type | Modifiers
--- | --- | ---
 path | text  | 
 ip | inet | 
 method | text | 
 status | text | 
 time | timestamp with time zone | default now()
 id | integer | not null default nextval('log_id_seq'::regclass)

## Usage
```
python3 logs_analysis.py
```
