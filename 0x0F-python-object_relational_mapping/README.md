# SQLAlchemy CRUD Operations

This project demonstrates basic CRUD (Create, Read, Update, Delete) operations using SQLAlchemy in Python. It includes models for States and Cities, with relationships between them.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/sqlalchemy-crud.git

1. Navigate to the project directory:

  cd sqlalchemy-crud

2. Install dependencies:

 pip install -r requirements.txt

Usage
Running the scripts
Each Python script in the project directory corresponds to a specific CRUD operation:

- model_state_fetch_first.py: Fetches the first state from the database.
- model_state_list.py: Lists all states in the database.
- model_state_insert.py: Inserts a new state into the database.
- model_state_update.py: Updates the name of a state in the database.
- model_state_delete.py: Deletes a state from the database.
- model_city_fetch_first.py: Fetches the first city from the database.
- model_city_list.py: Lists all cities in the database.
- model_city_insert.py: Inserts a new city into the database.
- model_city_update.py: Updates the name of a city in the database.
- model_city_delete.py: Deletes a city from the database.

To run any of the scripts, use the following command:
 
python script_name.py <db_user> <db_password> <db_name>

Replace <db_user>, <db_password>, and <db_name> with your MySQL database credentials.

Running the unit tests
To run the unit tests for the project, use the following command:

bash
pytest

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any bugs, feature requests, or improvements.
