import pandas as pd
from sqlalchemy import URL, create_engine

# Read Excel file
excel_file = "file.xlsx"  # Add file path
datasync_df = pd.read_excel(excel_file)

#Connect to Database
connection_url = URL.create(
    "mssql+pyodbc",
    username= "username",  #replace user name with your user name
    password= "password",  #replace password with your password
    host=r"host",          #replace host with your host
    database="database",   #replace database with your database
    query={
        "driver": "ODBC Driver 17 for SQL Server",
        "TrustServerCertificate": "yes",
    },
)
engine = create_engine(connection_url)

#Sync database Table
datasync_df.to_sql("table name", con=engine, if_exists="append", index=False)  #replace table name with your table name
print("Database updated successfully")
