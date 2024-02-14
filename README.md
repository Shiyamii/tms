# Project 1 - R606

## Ticket Management Service

### Version :  ``4``

## Setup env

Replace the following values with your needs:

```properties
DATA={{data_type}}
INTERFACE={{interface_type}}
```

Where ``data_type`` can be either `backlog` for local (RAM) stockage or `database` for database stockage.
And where ``interface_type`` can be either `gui` for a GUI interface or `inteface` for a console interface.

## Database initialization

Setup .env file with the following content by replacing with your needs.

```properties
DATABASE_NAME={{database_name}}
DATABASE_USER={{database_user}}
DATABASE_PASSWORD={{database_password}}
DATABASE_HOST={{database_host}}
DATABASE_PORT={{database_port}}
```

Or just run docker-compose to setup the database

```
docker compose up -d
```

## Database setup

Setup the database by running the following command in the root directory of the project

```
python setup_database.py
```

## Run the project

Execute the following command in the root directory of the project

```
python run_program.py
```

## Run the tests

execute the following command in the root directory of the project

```
python run_tests.py
```

or

```
python -m unittest discover -s test/
```

