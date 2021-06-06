import psycopg2
import sys
from datetime import datetime as dt

args = sys.argv
if len(args) != 6:
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

#warehouse ordereddate packstatus

print(dt.now())

execution = "INSERT INTO Package (Address, Username, OrderNumber, Barcode, IsPriority, warehouse, ordereddate, packstatus) Values (\'" + args[1] + "\', \'" + args[2] + "\', " + args[3] + ", \'" + args[4] + "\', \'" + args[5] + "\', \'1\', \'" + str(dt.now()) + "\', \'" + "o\') Returning ID"

cur.execute(execution)
x = cur.fetchone()[0]

print(x)

f = open("tempfile.txt", "w")
f.write(str(x))
f.close()

conn.commit()

cur.close()
conn.close()
