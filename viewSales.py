import psycopg2
import sys

#sys.argv[1] is argument 1, argv[2] is argument 2, etc etc

try:
    conn = psycopg2.connect(
        host = "127.0.0.1",
        database = "quicknhealthy",          #enter DB
        user = "postgres",
        password = "xxx",           #enter password
        port="5432")


    print("Database connected successfully")

except:
    print("Database did not connect")    

cur = conn.cursor()

query = """SELECT Catalogue.name, SUM(MealOrdered.quantity) AS numsales 
            FROM MealOrdered
                JOIN Catalogue ON (Catalogue.MealID = MealOrdered.MealID)
            GROUP BY Catalogue.name
            ORDER BY Catalogue.name;"""

#execute query
cur.execute(query)

rows = cur.fetchall()

print("Name\tNumberOfSales")
print('---------------------')
print("\n")
for row in rows:
    print(row[0],"\t", row[1])

#close cursor
cur.close()

conn.close()
