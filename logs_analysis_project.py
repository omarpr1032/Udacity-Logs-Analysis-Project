#!/usr/bin/env python3
# import psycopg2 module
import psycopg2

# set the database name constant
DBNAME = "news"


# define function to get top articles
def populate_top_articles(db):

    # open a cursor to perform the database operations
    cursor = db.cursor()

    # execute the sql query
    cursor.execute("SELECT article.title, COUNT(article.title)as views"
                   " FROM articles as article JOIN log ON"
                   " article.slug=SUBSTRING(log.path, 10) GROUP BY"
                   " article.title ORDER BY views DESC LIMIT 3;")

    # query the database and obtain the data
    results = cursor.fetchall()

    # print each record rows
    for row in results:
        print row[0], " -- ", row[1], "views"


# define function to get the most popular authors
def populate_most_popular_authors(db):
    # open a cursor to perform the database operation
    cursor = db.cursor()

    # execute the sql query
    cursor.execute("SELECT articles_authors.name as authors,"
                   " SUM(articles_authors.views) as views FROM"
                   " (SELECT articles.title,authors.name,"
                   " COUNT(articles.title)as views FROM articles"
                   " LEFT JOIN log on articles.slug = SUBSTRING(log.path,10)"
                   " LEFT JOIN authors on articles.author = authors.id"
                   " GROUP BY articles.title, authors.name)as articles_authors"
                   " GROUP BY articles_authors.name ORDER BY views DESC;")

    # results
    results = cursor.fetchall()

    # print each record rows
    for row in results:
        print row[0], " -- ", row[1], " views"


# define function to show days where more than 1% of requests lead to errors
def populate_days_errors(db):
    # open a cursors to perform the database operation
    cursor = db.cursor()

    # execute the sql query
    cursor.execute("SELECT * FROM errors_rate_group WHERE rate > 1")

    # results
    results = cursor.fetchall()

    # print each record rows
    for row in results:
        print row[0], " -- ", row[3], "% errors"


# define function to print all results
def populate_results():
    # connect to an exsisting database
    db = psycopg2.connect(database=DBNAME)

    print ""
    print "______ TOP 3 ARTICLES ______"
    populate_top_articles(db)
    print ""
    print "______ MOST POPULAR AUTHORS ______"
    populate_most_popular_authors(db)
    print ""
    print "______ ERRORS > 1% BY DATE ______"
    populate_days_errors(db)
    print ""

    # close the communication with the database
    db.close()

# populate results
populate_results()
