import psycopg2
import sys

# Connect to the PostgreSQL database
arg = sys.argv
if(len(arg) != 2):
    print("Error: Argument Size Incorrect!")
    exit(0)

try:
    conn    = psycopg2.connect(
            host = "127.0.0.1",
            database ="quicknhealthy",
            user ="postgres",
            password ="xxxxxx",
            port ="5432"

            )
    print(" Connected Successfully!")
except:
    print(" Connection Error!")

# Obtain a cursor object from the PostgreSQL database connection

cur     = conn.cursor()

view_idle_driver = """SELECT EmployeeID, FirstName, LastName, StatusID FROM Driver WHERE StatusID = %s"""
record =("Idle")

cur.execute(view_idle_driver, (record,))

rows = cur.fetchall()

print("EmployeeID\tFirstName\tLastName\tStatusID")
print('---------------------------------------------------------------')
print("\n")
for row in rows:
    print(row[0],"\t", row[1], "\t",row[2],"\t", row[3])

cur.close()
conn.close()