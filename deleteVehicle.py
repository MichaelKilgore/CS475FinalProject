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
            password ="xxxxx",
            port ="5432"

            )
    print(" Connected Successfully")
except:
    print("Connection Error")

# Obtain a cursor object from the PostgreSQL database connection

cur     = conn.cursor()

delete_shipment = """DELETE FROM Shipment WHERE Shipment.VPlateNumber = %s"""
record = (arg[1])
cur.execute(delete_shipment, (record,))

delete_vehicle = """DELETE FROM Vehicle WHERE PlateNumber = %s"""
cur.execute(delete_vehicle, (record,))
  

conn.commit()
count = cur.rowcount
print(count, "Record deleted successfully ")

cur.close()
conn.close()