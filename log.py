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

def connect_to_db(DBNAME):
    """
    Connects to DBNAME
    """
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    return db, c

def get_most_popular_articles():
    """
    Prints most popular articles from database DBNAME
    """
    db, c = connect_to_db(DBNAME)
    sql_query = """
                SELECT title
                FROM articles
                WHERE ROW (slug) IN (SELECT SUBSTRING(path,10,30) AS Path
                FROM log
                WHERE path != '/'
                GROUP BY path
                ORDER BY count(path) DESC LIMIT 3)
                ORDER BY title DESC
                """
    c.execute(sql_query)
    print("Most popular 3 articles from highest to lowest: ")
    rank = 0
    for article in c:
        print (str(rank) + '. ' + article[0])
        rank += 1
    db.close()

def create_view_top_authors():
    """
    Creates view topAuthors
    """
    db, c = connect_to_db(DBNAME)
    sql_query = """
                CREATE view topAuthors AS
                SELECT author,title
                FROM articles
                WHERE ROW (slug) IN (SELECT SUBSTRING(path,10,30) AS Path
                FROM log
                WHERE path != '/'
                GROUP BY path
                ORDER BY count(path) DESC LIMIT 8)
                ORDER BY title DESC;
                """
    c.execute(sql_query)
    db.commit()
    db.close()

def drop_view_top_authors():
    """
    Drops view topAuthors
    """
    db, c = connect_to_db(DBNAME)
    sql_query = """
                DROP VIEW topAuthors;
                """
    c.execute(sql_query)
    db.commit()
    db.close()

def get_most_popular_authors():
    """
    Prints most popular authors from database DBNAME
    """
    db, c = connect_to_db(DBNAME)
    sql_query = """
                SELECT name
                from articles JOIN authors
                ON articles.author = (SELECT author
                FROM topAuthors
                GROUP BY author
                ORDER BY COUNT(*) DESC
                LIMIT    1) LIMIT 4;
                """
    c.execute(sql_query)
    print("\nMost popular 4 authors from highest to lowest: \n")
    rank = 1
    for article in c:
        print (str(rank) + '. ' + article[0])
        rank += 1
    db.close()

def get_request_errors():
    """
    Prints days that have more than 1 percent of requests that lead to errors
    """
    db, c = connect_to_db(DBNAME)
    sql_query = """
                SELECT days,total_errors,total_requests,
                round((total_errors::numeric/total_requests::numeric)*100,2)
                AS percent_of_errors
                FROM (SELECT DATE_TRUNC('day', time)::date
                AS days, count(status)
                AS total_requests,
                SUM(
                    CASE WHEN status != '200 OK' THEN 1
                         ELSE 0
                    END) AS total_errors
                FROM log
                GROUP BY DATE_TRUNC('day', time)::date)
                AS end_result
                WHERE (total_errors::numeric/total_requests::numeric)*100 > 1.0
                ORDER BY percent_of_errors DESC;
                """
    c.execute(sql_query)
    print("\nDays with more than 1% of requrest errors: \n")
    rank = 1
    for article in c:
        print(str(rank) + '. ' + str(article[0]) + ' | ' + str(article[3])
              + '%')
        rank += 1
    db.close()

if __name__ == '__main__':
    get_most_popular_articles()
    create_view_top_authors()
    get_most_popular_authors()
    drop_view_top_authors()
    get_request_errors()
