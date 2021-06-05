
import psycopg2
import sys

args = sys.argv
try:
    conn = psycopg2.connect(
        host = "127.0.0.1",
        database = "quicknhealthy",
        user = "postgres",
        password = "XXXXXXXXXX",
        port = "5432"
    )

    print("Database successfully connected")

except:
    print("Connection to database failed")

cur = conn.cursor()

#execute the query
#   splitting it up to make it more readable
command = "INSERT INTO Driver (EmployeeID, FirstName, LastName, StatusID) VALUES (" 
command = command + args[1] + ", \'" + args[2] + "\', \'" 
command = command + args[3] + "\', \'" + args[4] + "\')"

cur.execute(command)

cur.execute("SELECT * FROM Driver")

conn.commit()

#close the connection
cur.close()
conn.close()