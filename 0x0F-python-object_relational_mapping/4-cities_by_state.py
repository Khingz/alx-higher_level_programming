#!/usr/bin/python3
"""lists all cities from the database"""
import sys
import MySQLdb

if __name__ == "__main__" and len(sys.argv) == 4:
    connection = MySQLdb.connect(
            host='localhost',
            port=3301,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3])
    cursor = connection.cursor()
    query = "SELECT id, name FROM cities"
    cursor.execute(query)
    rows = cursor.fetchall()
    for i in rows:
        print(i)

    cursor.close()
    connection.close()
