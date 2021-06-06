import psycopg2
import sys

# Connect to the PostgreSQL database
arg = sys.argv
if(len(arg) != 1):
    print("Error: Argument Size Incorrect!")
    exit(0)

try:
    conn    = psycopg2.connect(
            host = "127.0.0.1",
            database ="quicknhealthy",
            user ="michael-kilgore",
            password ="Sounders0311$",
            port ="5432"

            )
    print(" Connected Successfully!")
except:
    print(" Connection Error!")

# Obtain a cursor object from the PostgreSQL database connection

cur     = conn.cursor()

view_idle_driver = """SELECT PlateNumber, Type, Size, Capacity FROM Vehicle WHERE Location = %s"""
record =("Warehouse")

cur.execute(view_idle_driver, (record,))

rows = cur.fetchall()

#print("PlateNumber\tType\tSize\tCapacity")
print("%-30s %-30s %-30s %-30s" % ("PlateNumber", "Type", "Size", "Capacity"))
print('-----------------------------------------------------------------------------------------------------------')
print("\n")
for row in rows:
	print("%-30s %-30s %-30s %-30s" % (row[0], row[1], row[2], row[3]))

cur.close()
conn.close()
