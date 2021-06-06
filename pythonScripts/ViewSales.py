import psycopg2
import sys

#sys.argv[1] is argument 1, argv[2] is argument 2, etc etc

try:
    conn = psycopg2.connect(
        host = "127.0.0.1",
        database = "quicknhealthy",          #enter DB
        user = "michael-kilgore",
        password = "Sounders0311$",           #enter password
        port="5432")


    #print("Database connected successfully")

except:
    print("Database did not connect")    

cur = conn.cursor()

query = """SELECT Catalogue.Description, SUM(MealOrdered.numberoforders) AS numsales
            FROM MealOrdered
                JOIN Catalogue ON (Catalogue.mealid = mealordered.mealid)
            GROUP BY catalogue.Description;"""

#execute query
cur.execute(query)

rows = cur.fetchall()

for r in rows:
    print("Description: ", r[0], "Numsales: ", r[1])

#close cursor
cur.close()

conn.close()
