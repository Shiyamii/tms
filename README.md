# Project 1 - R606

## Ticket Management Service

### Version :  ``3``

## Database initialization

Setup .env file with the following content by replacing with your needs.

```
DB_NAME={{database_name}}
DB_USER={{database_user}}
DB_PASSWORD={{database_password}}
DB_HOST={{database_host}}
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

