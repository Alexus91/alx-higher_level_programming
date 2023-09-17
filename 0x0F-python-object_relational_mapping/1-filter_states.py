#!/usr/bin/python3
"""lists all states """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db =argv[3])
    curs = db.cursor()
    curs.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    for data in curs.fetchall():
        print(data)
    curs.close()
    db.close()
