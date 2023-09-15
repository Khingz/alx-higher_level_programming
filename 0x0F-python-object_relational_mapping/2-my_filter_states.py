#!/usr/bin/python3
"""takes in an argument and displays all values with name == arg"""
import sys
import MySQLdb

if __name__ == "__main__" and len(sys.argv) == 5:
    connection = MySQLdb.connect(
            host='localhost',
            port=3301,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3])
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states WHERE \
            BINARY name = '{}'".format(sys.argv[4]))
    rows = cursor.fetchall()
    for i in rows:
        print(i)
