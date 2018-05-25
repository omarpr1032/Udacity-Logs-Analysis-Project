# import psycopg2 module
import psycopg2

# set the database name constant
DBNAME = "news"


# define function to get top articles
def populate_top_articles():

    # connect to an exsisting database
    db = psycopg2.connect(database=DBNAME)

    # open a cursor to perform the database operations
    cursor = db.cursor()

    # execute the sql query
    cursor.execute("SELECT article.title, COUNT(article.title)as views"
                   " FROM articles as article JOIN log ON"
                   " article.slug=SUBSTRING(log.path, 10) GROUP BY"
                   " article.title ORDER BY views DESC LIMIT 3;")

    # query the database and obtain the data
    results = cursor.fetchall()

    # close the communication with the database
    db.close()

    # print each record rows
    for row in results:
        print row[0], " -- ", row[1], "views"


# define function to get the most popular authors
def populate_most_popular_authors():

    # connect to an existing database
    db = psycopg2.connect(database=DBNAME)

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

    # close the communication with the database
    db.close()

    # print each record rows
    for row in results:
        print row[0], " -- ", row[1], " views"


# define function to show days where more than 1% of requests lead to errors
def populate_days_errors():

    # connect to an existing database
    db = psycopg2.connect(database=DBNAME)

    # open a cursors to perform the database operation
    cursor = db.cursor()

    # execute the sql query
    cursor.execute("SELECT * FROM errors_rate_group WHERE rate > 1")

    # results
    results = cursor.fetchall()

    # close the communication with the database
    db.close()

    # print each record rows
    for row in results:
        print row[0], " -- ", row[3], "% errors"


print ""
print "______ TOP 3 ARTICLES ______"
populate_top_articles()
print ""
print "______ MOST POPULAR AUTHORS ______"
populate_most_popular_authors()
print ""
print "______ ERRORS > 1% BY DATE ______"
populate_days_errors()
print ""
