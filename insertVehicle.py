import psycopg2
import sys

# Connect to the PostgreSQL database
arg = sys.argv
if(len(arg) != 6):
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

insert_vehicle = """INSERT INTO Vehicle (PlateNumber, Type, Size, Capacity, Location)VALUES(%s,%s,%s,%s,%s)"""
record = (arg[1],arg[2],arg[3],arg[4],arg[5])

cur.execute(insert_vehicle, record)
conn.commit()
count = cur.rowcount
print(count, "Record inserted successfully into Vehicel Table.")

cur.close()
conn.close()