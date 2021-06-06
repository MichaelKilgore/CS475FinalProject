import psycopg2
import sys

args = sys.argv
if len(args) != 2:
    exit(0)

try:
    conn = psycopg2.connect(
        host = "127.0.0.1",
        database = "quicknhealthy",
        user = "michael-kilgore",
        password = "Sounders0311$",
        port = "5432")

    print("connected")
except:
    print("not connected.")
    exit(0)

cur = conn.cursor()

f = open("tempfile.txt", "r")
x = f.readlines()
f.close()

execution = "UPDATE Package SET ShipmentID = \'" + str(x[0]) + "\' WHERE Barcode = \'" + args[1] + "\'"

cur.execute(execution)

conn.commit()

cur.close()
conn.close()
