#!/usr/bin/env python3
#
# This is a program querying to a news database called 'news'
# that answers following three questions:
#
# 1. What are the most popular three articles of all time?
#    Which articles have been accessed the most?
# 2. Who are the most popular article authors of all time?
# 3. On which days did more than 1% of requests lead to errors?
#
# Example output:
# 1. "Candidate is jerk, alleges rival" — 342102 views
# 2. Ursula La Multa — 512805 views
# 3. July 17, 2016 — 2.32% errors


import psycopg2


def query_to_DB(queryString):
    db = psycopg2.connect(database='news')
    c = db.cursor()
    c.execute(queryString)
    posts = c.fetchall()
    db.close()
    return posts


def question_one():
    print(
        '1. What are the most popular three articles of all time? '
        'Which articles have been accessed the most? Present this information '
        'as a sorted list with the most popular article at the top.'
    )

    qstr = '''
        SELECT T.title, count(*)
        FROM (
            log JOIN articles ON log.path
            LIKE concat('%/article/', articles.slug, '%')
        ) AS T
        GROUP BY T.title
        ORDER BY count DESC;
    '''
    result = query_to_DB(qstr)

    for elem in result:
        print('"' + elem[0] + '" — ' + str(elem[1]) + ' views')


def question_two():
    print(
        '2. Who are the most popular article authors of all time? That is, '
        'when you sum up all of the articles each author has written, '
        'which authors get the most page views? Present this as a sorted '
        'list with the most popular author at the top.'
    )

    qstr = '''
        SELECT A.name, M.count
        FROM authors AS A,
             (SELECT T.author, count(*)
              FROM (log JOIN articles ON log.path
                    LIKE concat('%/article/', articles.slug, '%')) AS T
              GROUP BY T.author) AS M
        WHERE A.id = M.author
        ORDER BY count DESC;
    '''
    result = query_to_DB(qstr)

    for elem in result:
        print(elem[0] + ' — ' + str(elem[1]) + ' views')


def question_three():
    print(
        '3. On which days did more than 1% of requests lead to errors? '
        'The log table includes a column status that indicates the HTTP '
        'status code that the news site sent to the user\'s browser. '
    )

    qstr = '''
        SELECT T.date, round(A.count*100.0/T.count,2) AS ratio
        FROM (SELECT to_char(time, 'FMMonth DD, YYYY')
                AS date, status, count(*)
              FROM log GROUP BY date, status) AS T,
             (SELECT to_char(time, 'FMMonth DD, YYYY')
                AS date, status, count(*)
              FROM log GROUP BY date, status) AS A
        WHERE T.status = '200 OK' AND
              A.status = '404 NOT FOUND' AND
              T.date = A.date AND
              round(A.count*100.0/T.count,2) >= 1
        ORDER BY ratio DESC;
    '''
    result = query_to_DB(qstr)

    for elem in result:
        print(elem[0] + ' — ' + str(elem[1]) + '% errors')


if __name__ == '__main__':
    question_one()
    print()
    question_two()
    print()
    question_three()
