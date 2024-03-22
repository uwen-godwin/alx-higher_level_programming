#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa.
"""

import sys
import MySQLdb

def main():
    """Main function to retrieve and print cities from the database."""
    # Database connection parameters
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

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
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities \
                    JOIN states ON cities.state_id = states.id ORDER BY cities.id")

    # Fetch all the rows
    cities = cursor.fetchall()

    # Print the results
    for city in cities:
        print(city)

    # Close cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
