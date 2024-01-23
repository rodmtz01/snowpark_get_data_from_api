#Import libraries 
import requests
from snowflake.snowpark.session import Session
from snowflake.snowpark import DataFrame

#Set Connection parameters for snowflake 
connection_parameters = {"account":"YOUR_ACCOUNT" ,
"user":"SNOWFLAKE_USER",
"password": "SNOWFLAKE_USER_PASSWORD",
"role":"SNOWFLAKE_USER_ROLE",
"warehouse":"VIRTUAL_WAREHOUSE",
"database":"YOUR_DATABASE",
"schema":"YOUR_SCHEMA"
}

#Create snowflake session using the connection parameters
session = Session.builder.configs(connection_parameters).create()

#call api endpoint using requests
url = 'https://vpic.nhtsa.dot.gov/api/vehicles/getallmanufacturers?format=json'
r = requests.get(url)

#Parse request to JSON
requestJson = r.json()

#Create a snowpark data frame using request JSON
df = session.createDataFrame(requestJson['Results'])

#To upper case name of columns
def uppercase_all_columns(df: DataFrame) -> DataFrame:
    return df.select([df.col(column).as_(column.upper()) for column in df.columns])
df = uppercase_all_columns(df)

#Select only relevant columns
df = df.select('COUNTRY','MFR_COMMONNAME','MFR_ID', 'MFR_NAME')

#Write table into snowflake using the dataframe 
df.write.mode("overwrite").save_as_table("CARS_MANUFACTURERS")

#Close snowflake session 
session.close()