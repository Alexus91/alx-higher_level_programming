#!/usr/bin/python3
"""
python script that lists all cities from the database hbtn_0e_4_usa
with specified state name
"""

import MySQLdb
from sys import argv
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    curs = db.curs()
    curs.execute("""SELECT cities.name
                   FROM cities JOIN states ON cities.state_id = states.id
                   WHERE states.name = %(state)s""", {'state': argv[4]})
    r = curs.fetchall()
    le = len(r)
    if le == 0:
        print('')
    for i in range(l):
        if i < le - 1:
            print(r[i][0], end=', ')
        else:
            print(r[i][0])
    curs.close()
    db.close()
