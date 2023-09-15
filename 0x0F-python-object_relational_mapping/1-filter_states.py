#!/usr/bin/python3
"""lists all states with a name starting with N"""
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
    cursor.execute("SELECT * FROM states ORDER BY id")
    rows = cursor.fetchall()
    for i in rows:
        if i[1].startswith('N'):
            print(i)
