import psycopg2
import psycopg2.extras
import sys

categories = [
    'Comedy',
    'Sci-fi',
    'Horror',
    'Romance',
    'Action',
    'Thriller',
    'Drama',
    'Mistery',
    'Animation',
    'Adventure',
    'Fantasy',
    'War',
    'Western',
    'Musical',
    'History',
    'Documentary',
    'Biography'
]

HOSTNAME = '127.0.0.1'
USERNAME = 'postgres'
PASSWORD = 'postgresMandelieu'
DATABASE = 'film'

connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )

# cursor = connection.cursor()
cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

for c in categories:
    query = f"INSERT INTO films_category (name) VALUES ('{c}');"
    cursor.execute(query)

connection.commit()
connection.close()
