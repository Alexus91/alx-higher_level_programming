#!/usr/bin/python3
"""lists all states """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    dbt = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], dbt =argv[3])
    curs = dbt.cursor()
    curs.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    for data in curs.fetchall():
        print(data)
    curs.close()
    dbt.close()
