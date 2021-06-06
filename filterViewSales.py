import psycopg2
import sys

#sys.argv[1] is argument 1, argv[2] is argument 2, etc etc
#protein types = Chicken, Beef, Turkey, Fish, Eggs, None

args = sys.argv

if len(args) > 7:
    print("Too many protein types")
    exit(0)

if len(args) == 1:
    print("Not enough protein types")
    exit(0)

try:
    conn = psycopg2.connect(
        host = "127.0.0.1",
        database = "quicknhealthy",
        user = "postgres",
        password = "xxx",
        port="5432")

    print("Database connected successfully")

except:
    print("Database did not connect")    

cur = conn.cursor()

if len(args) == 7:
    #6 protein types
    query = """SELECT Catalogue.name, SUM(MealOrdered.quantity) AS numsales
                FROM MealOrdered
                    JOIN Catalogue ON (Catalogue.mealid = mealordered.mealid)
                WHERE catalogue.proteintype = '""" + args[1] + """'
                    OR catalogue.proteintype = '""" + args[2] + """'
                    OR catalogue.proteintype = '""" + args[3] + """'
                    OR catalogue.proteintype = '""" + args[4] + """'
                    OR catalogue.proteintype = '""" + args[5] + """'
                    OR catalogue.proteintype = '""" + args[6] + """'
                GROUP BY catalogue.name;"""

elif len(args) == 6:
    #5 protein types
    query = """SELECT Catalogue.name, SUM(MealOrdered.quantity) AS numsales
                FROM MealOrdered
                    JOIN Catalogue ON (Catalogue.mealid = mealordered.mealid)
                WHERE catalogue.proteintype = '""" + args[1] + """'
                    OR catalogue.proteintype = '""" + args[2] + """'
                    OR catalogue.proteintype = '""" + args[3] + """'
                    OR catalogue.proteintype = '""" + args[4] + """'
                    OR catalogue.proteintype = '""" + args[5] + """'
                GROUP BY catalogue.name;"""

elif len(args) == 5:
    #4 protein types
    query = """SELECT Catalogue.name, SUM(MealOrdered.quantity) AS numsales
                FROM MealOrdered
                    JOIN Catalogue ON (Catalogue.mealid = mealordered.mealid)
                WHERE catalogue.proteintype = '""" + args[1] + """'
                    OR catalogue.proteintype = '""" + args[2] + """'
                    OR catalogue.proteintype = '""" + args[3] + """'
                    OR catalogue.proteintype = '""" + args[4] + """'
                GROUP BY catalogue.name;"""

elif len(args) == 4:
    #3 protein types
    query = """SELECT Catalogue.name, SUM(MealOrdered.quantity) AS numsales
                FROM MealOrdered
                    JOIN Catalogue ON (Catalogue.mealid = mealordered.mealid)
                WHERE catalogue.proteintype = '""" + args[1] + """'
                    OR catalogue.proteintype = '""" + args[2] + """'
                    OR catalogue.proteintype = '""" + args[3] + """'
                GROUP BY catalogue.name;"""

elif len(args) == 3:
    #2 protein types
    query = """SELECT Catalogue.name, SUM(MealOrdered.quantity) AS numsales
                FROM MealOrdered
                    JOIN Catalogue ON (Catalogue.mealid = mealordered.mealid)
                WHERE catalogue.proteintype = '""" + args[1] + """'
                    OR catalogue.proteintype = '""" + args[2] + """'
                GROUP BY catalogue.name;"""

else:
    #1 protein type
    query = """SELECT Catalogue.name, SUM(MealOrdered.quantity) AS numsales
                FROM MealOrdered
                    JOIN Catalogue ON (Catalogue.mealid = mealordered.mealid)
                WHERE catalogue.proteintype = '""" + args[1] + """'
                GROUP BY catalogue.name;"""

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
