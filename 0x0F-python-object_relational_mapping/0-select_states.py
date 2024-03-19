#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.
"""

import sys
import MySQLdb

def main():
    """Main function to retrieve and print states from the database."""
    # Check if correct number of command-line arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Database connection parameters
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    try:
        # Connect to MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name
        )

        # Create a cursor object
        cursor = db.cursor()

        # Execute the query
        cursor.execute("SELECT * FROM states ORDER BY id")

        # Fetch all the rows
        states = cursor.fetchall()

        # Print the results
        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print("Error connecting to MySQL database:", e)
        sys.exit(1)

    finally:
        # Close cursor and database connection
        cursor.close()
        db.close()

if __name__ == "__main__":
    main()
