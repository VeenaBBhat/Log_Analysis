#!/usr/bin/env python

# Log Analysis Reporting Tool

# Import the library postgresql
import psycopg2

DBNAME = "news"

q1 = """select title, views_count from
(select substring(path, 10) slug, count(*) views_count
 from log
where path like '/article%'
group by path
order by count(*) desc
) A JOIN
 articles B on A.slug = B.slug
limit 3
;"""

q2 = """select name, count(*) from
(select substring(path, 10) slug
 from log where path like '/article%'
) A JOIN
 articles B on A.slug = B.slug JOIN
 authors C on B.author = C.ID

group by author, name
order by count(*) desc
;"""


q3 = """select to_char(B.log_date,'Mon DD, YYYY'),
round(error_percentage,2) from
(select A.log_date, (cast(A.status_error as decimal)/A.status_total) *100
error_percentage from (select date(time) log_date,
sum(1) as status_total,
sum(CASE when status != '200 OK' THEN 1 ELSE 0 END) as status_error
from log
group by log_date) A) B where B.error_percentage > 1;"""


def dbconnect(query):
    # Connecting to news database
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        # Execute queries
        c.execute(query)
        # Fetch results
        results = c.fetchall()
        db.close()
        return results
    except psycopg2.DatabaseError, e:
        print("<error message>")

# Q1. What are the most popular three articles of all time?


def popular_articles(query):
    results = dbconnect(query)
    print('\n Displaying the most popular articles of all time:\n')
    for row in results:
        print("    {} - {} views".format(row[0], row[1]))


# Q2. Who are the most popular article authors of all time?

def popular_authors(query):
    results = dbconnect(query)
    print('\n Displaying the most popular authors of all time:\n')
    for row in results:
        print("    {} - {} views".format(row[0], row[1]))


# Q3. On which days did more than 1% of requests lead to errors?

def percentage_errors(query):
    results = dbconnect(query)
    print('\n The days when more than 1% of requests lead to error:\n')
    for row in results:
        print("    {} - {} % errors".format(row[0], row[1]))


if __name__ == '__main__':
    # Output results
    popular_articles(q1)
    popular_authors(q2)
    percentage_errors(q3)
