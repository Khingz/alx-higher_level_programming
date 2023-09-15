#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""
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
    cursor.execute("SELECT * FROM states")
    rows = cursor.fetchall()
    for i in rows:
        print(i)

    cursor.close()
    connection.close()