#!/usr/bin/python3

"""
Script that lists all states from the database hbtn_0e_0_usa.
"""

import sys
import MySQLdb

def main():
    """Main function to retrieve and print states from the database."""
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name
        )

        cursor = db.cursor()

        cursor.execute("SELECT * FROM states ORDER BY id")

        states = cursor.fetchall()

        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print("Error connecting to MySQL database:", e)
        sys.exit(1)

    finally:
        cursor.close()
        db.close()


if __name__ == "__main__":
    main()
