import psycopg2
import sys

# Connect to the PostgreSQL database
args = sys.argv
if(len(args) != 4):
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
    print(" Connected Successfully")
except:
    print("Connection Error")

# Obtain a cursor object from the PostgreSQL database connection

cur     = conn.cursor()

update_driver = "UPDATE Driver SET StatusID = \'m\' WHERE EmployeeID = \'" + args[2] + "\'"

cur.execute(update_driver)

update_vehicle = "UPDATE Vehicle SET Location = \'Delivery\' WHERE PlateNumber = \'" + args[3] + "\'"

cur.execute(update_vehicle)

get_ID = "SELECT ID FROM Driver WHERE EmployeeID = \'" + args[2] + "\'"

cur.execute(get_ID)
x = cur.fetchone()[0]

insert_shipment = """INSERT INTO Shipment (TicketNumber, DriverID, VPlateNumber)VALUES(%s,%s,%s) RETURNING ID"""
record = (args[1],x,args[3])

cur.execute(insert_shipment, record)
y = cur.fetchone()[0]


f = open("tempfile.txt", "w")
f.write(str(y))
f.close()


conn.commit()

cur.close()
conn.close()
