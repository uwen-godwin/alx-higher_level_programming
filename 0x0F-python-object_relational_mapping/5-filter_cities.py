#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa.
"""

import sys
import MySQLdb

def main():
    """Main function to retrieve and print cities of a given state."""
    # Check if correct number of command-line arguments are provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state>".format(sys.argv[0]))
        sys.exit(1)

    # Database connection parameters
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

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

        # Prepare SQL query
        query = "SELECT DISTINCT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name = %s"

        # Execute the query
        cursor.execute(query, (state_name,))

        # Fetch all the rows
        cities = cursor.fetchall()

        # Print the results
        if cities:
            city_names = ", ".join(city[0] for city in cities)
            print(city_names)
        else:
            print("No cities found for the state:", state_name)

    except MySQLdb.Error as e:
        print("Error connecting to MySQL database:", e)
        sys.exit(1)

    finally:
        # Close cursor and database connection
        cursor.close()
        db.close()


if __name__ == "__main__":
    main()
