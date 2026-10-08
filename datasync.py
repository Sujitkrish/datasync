import pandas as pd
from sqlalchemy import URL, create_engine

# Step 1: Read Excel file
excel_file = "Data_sync.xlsx"  
datasync_df = pd.read_excel(excel_file)

#Connect to Database

connection_url = URL.create(
    "mssql+pyodbc",
    username= "p_user",
    password= "Sujitstark",
    host=r"DESKTOP-AA09DTD\SETARK",
    database="datasyncp1",
    query={
        "driver": "ODBC Driver 17 for SQL Server",
        "TrustServerCertificate": "yes",
    },
)
engine = create_engine(connection_url)

#step 3: Sync Students Table
datasync_df.to_sql("super_market", con=engine, if_exists="replace", index=False)



print("Database updated successfully from Excel using SQLAlchemy + SQL Server!")
