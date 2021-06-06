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

f = open("tempfile.txt", "r")
x = f.readlines()
f.close()

cur = conn.cursor()
print(args[1])
execution = "SELECT MealID FROM Catalogue WHERE Description = \'" + args[1] + "\'"
print(execution)

cur.execute(execution)

ID = cur.fetchone()[0]
print(ID)
#x=OrderID mealID numberOfOrders
execution = "INSERT INTO MealOrdered (OrderID, MealID, NumberOfOrders) Values (" + str(x[0]) + ", " + str(ID) + ", " + str(args[2]) + ")"

cur.execute(execution)

conn.commit()

cur.close()
conn.close()
