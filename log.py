#!/usr/bin/env python3

"""
This program is a reporting tool that prints out reports (in plain text)
based on the data in the database.

@author: Kenny Iraheta
@Date: 2017-05-23
"""

"""
Satisfy the following 3 tasks:

1. What are the most popular three articles of all time?
Which articles have been accessed the most?
Present this information as a sorted list with the most popular article
at the top.

2. Who are the most popular article authors of all time? That is, when you sum
up all of the articles each author has written, which authors get the most page
views? Present this as a sorted list with the most popular author at the top.

3. On which days did more than 1 percent of requests lead to errors? The log
table includes a column status that indicates the HTTP status code that the
news site sent to the user's browser. (Refer back to this lesson if you want to
review the idea of HTTP status codes.)
"""
import psycopg2

DBNAME = "news"

def get_most_popular_articles():
    """
    Prints most popular articles from the 'database'
    """
    db = psycopg2.connect(database=DBNAME) #connect to db
    c = db.cursor() #runs queries and fetches results; when db gives results cursor scans through results
    c.execute("SELECT path, count(path) FROM log WHERE path != '/' GROUP BY path ORDER BY count DESC LIMIT 3") #execute query
    results = c.fetchall() #fetch query resuls from db
    print(results)
    db.close()
