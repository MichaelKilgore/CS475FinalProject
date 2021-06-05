
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

#create the operation
command = "DELETE FROM Driver WHERE EmployeeID = " + args[1]

#execute the query
cur.execute(command)

conn.commit()

#close the connection
cur.close()
conn.close()