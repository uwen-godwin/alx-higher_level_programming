# SQL Introduction

This repository contains SQL scripts for various tasks related to MySQL server administration and data manipulation.

## Table of Contents

1. [Tasks](#tasks)
2. [Files](#files)
3. [Usage](#usage)
4. [Contributing](#contributing)
5. [License](#license)

## Tasks

1. **List databases**: Write a script to list all databases on the MySQL server.
2. **Create a database**: Write a script to create a database if it doesn't already exist.
3. **Delete a database**: Write a script to delete a database if it exists.
4. **First table**: Write a script to create a table called first_table in the current database.
5. **Full description**: Write a script to print the full description of a table.
6. **List all in table**: Write a script to list all rows of a table.
7. **First add**: Write a script to insert a new row into a table.
8. **Count 89**: Write a script to count the number of records with a specific value.
9. **Full creation**: Write a script to create a table and add multiple rows.
10. **List by best**: Write a script to list records ordered by a specific column.
11. **Select the best**: Write a script to select records based on a condition.
12. **Cheating is bad**: Write a script to update records based on a condition.
13. **Score too low**: Write a script to delete records based on a condition.
14. **Average**: Write a script to compute the average of a column.
15. **Number by score**: Write a script to group records and count them.
16. **Say my name**: Write a script to list records with a specific condition.
17. **Go to UTF8**: Write a script to convert a database, table, and field to UTF8.
18. **Temperatures #0**: Write a script to compute the average temperature by city.
19. **Temperatures #1**: Write a script to display the top 3 cities' temperatures.
20. **Temperatures #2**: Write a script to display the max temperature by state.

## Files

- `0-list_databases.sql`: Script for listing databases.
- `1-create_database_if_missing.sql`: Script for creating a database.
- ...
- `README.md`: Documentation file.

## Usage

Each script can be executed by passing it to the `mysql` command with appropriate arguments.

Example:
cat 0-list_databases.sql | mysql -hlocalhost -uroot -p

## Contributing

Contributions are welcome! Feel free to submit pull requests or open issues if you have any suggestions or improvements.
