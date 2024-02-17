
# snowpark_get_info_api

A simple example of how to extract data from an API and load it into Snowflake using Snowpark and Python.


## Authors

- [@rodmtz01](https://www.github.com/rodmtz01)


## Getting started

for this example you can use anaconda or virtualenv to create a Python 3.8, 3.9, 3.10 or 3.11 virtual environment.


## Installation

1. Clone or download the project

```bash
  git clone https://github.com/rodmtz01/snowpark_get_data_from_api.git

```
2. Install snowpark in your pyhton environment using conda or pip

```bash
  conda install --name {YOUR_ENVIRONMENT} snowflake-snowpark-python pandas

```
or
```bash
  pip install snowflake-snowpark-python pandas
```

3. Optional: Install Jupyter extension on visual VS Code

4. Update the connection parameters variable in 'get_data.py' or 'get_data.ipynb' if you're using jupyter

```bash
  connection_parameters = {"account":"YOUR_ACCOUNT",
  "user":"YOUR_SNOWFLAKE_USER",
  "password": "YOUR_SNOWFLAKE_USER_PASSWORD",
  "role":"YOUR_SNOWFLAKE_USER_ROLE",
  "warehouse":"YOUR_VIRTUAL_WAREHOUSE",
  "database":"YOUR_DATABASE",
  "schema":"YOUR_SCHEMA"
  }
```

    