import psycopg2
import sys

# Connect to the PostgreSQL database
arg = sys.argv
if(len(arg) != 3):
    print("Error: Argument Size Incorrect!")
    exit(0)
try:
    conn    = psycopg2.connect(
            host = "127.0.0.1",
            database ="quicknhealthy",
            user ="postgres",
            password ="xxxxx",
            port ="5432"

            )
    print(" Connected Successfully")
except:
    print("Connection Error")

# Obtain a cursor object from the PostgreSQL database connection

cur     = conn.cursor()


update_driver_status = """UPDATE Driver SET StatusID = %s WHERE EmployeeID = %s"""
record = (arg[1], arg[2])

cur.execute(update_driver_status, record)
conn.commit()
count = cur.rowcount
print(count, "Record updated successfully.")

cur.close()
conn.close()