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

view_package_status = """SELECT Barcode, OrderNumber, DeliveryCompleteDate, OrderedDate, PackStatus
                        FROM Package
                        JOIN PackageStatus ON (Package.PackStatus = PackageStatus.Type)
                        WHERE OrderNumber = %s
                        GROUP BY Package.ID
                        ORDER BY DeliveryCompleteDate;"""
record =(arg[1])

cur.execute(view_package_status, (record,))

rows = cur.fetchall()

print("Barcode\tOrderNumber\tDeliveryDate\tOrderedDate\tPackageStatu")
print('---------------------------------------------------------------')
print("\n")
for row in rows:
    print(row[0],"\t", row[1], "\t",row[2],"\t", row[3], "\t",row[4])

cur.close()
conn.close()