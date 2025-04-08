import  pyodbc

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'DESKTOP-3TR61O6'
DATABASE_NAME = 'grocery'

connection_string = f"""

    DRIVER={DRIVER_NAME};SERVER={SERVER_NAME};DATABASE={DATABASE_NAME};
    Trust_Connection=yes;
"""

conn = pyodbc.connect(connection_string)
print(conn)