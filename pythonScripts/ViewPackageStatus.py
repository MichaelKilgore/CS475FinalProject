import psycopg2
import sys

args = sys.argv
if len(args) != 3:
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

execution = "Select PackageStatus.Description FROM Package JOIN PackageStatus ON (Type = PackStatus) WHERE Username = \'" + args[1] + "\' AND OrderNumber = \'" + args[2] + "\'"
#execution = "Select Package.PackStatus FROM Package WHERE Username = \'" + args[1] + "\' AND OrderNumber = \'" + args[2] + "\'"

cur.execute(execution)

rows = cur.fetchall()

for r in rows:
    print("Package Status = ", r[0])


conn.commit()

cur.close()
conn.close()
