import psycopg2
import sys

# Connect to the PostgreSQL database
arg = sys.argv
if(len(arg) != 6):
    print("argv size is not correct")
    exit(0)
try:
    conn    = psycopg2.connect(
            host = "127.0.0.1",
            database ="quicknhealthy",
            user ="postgres",
            password ="xxxxxx",
            port ="5432"

            )
    print(" Connected Successfully")
except:
    print("Connection Error")

# Obtain a cursor object from the PostgreSQL database connection

cur     = conn.cursor()
print("INSERT INTO Catalogue(Weight, IsVegetarian, IsVegan, IsGlutenFree, ProteinType, IsForSale, Description, Cost)")

insert_meal_ordered = """ INSERT INTO MealOrdered (OrderID, MealID, NumberOfOrders)
                            VALUES(%s,%s,%s)"""
meal_record = (arg[1], arg[2], arg[3])


cur.execute(insert_meal_ordered, meal_record)
conn.commit()

cur.close()
conn.close()