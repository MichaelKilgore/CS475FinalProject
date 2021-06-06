import psycopg2
import sys

# Connect to the PostgreSQL database
arg = sys.argv
if(len(arg) != 10):
    print("Error: Argument Size Incorrect!")
    exit(0)
try:
    conn    = psycopg2.connect(
            host = "127.0.0.1",
            database ="quicknhealthy",
            user ="postgres",
            password ="xxxxx",
            port ="5432"

            )
    print(" Connected Successfully")
except:
    print("Connection Error")

# Obtain a cursor object from the PostgreSQL database connection

cur     = conn.cursor()

insert_catalogue = """INSERT INTO CATALOGUE (Weight, IsVegetarian, IsVegan, IsGlutenFree,ProteinType,
                    IsForSale, Description, Cost) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"""
#record = (10, True, False, False,'f',True,"fish", 20) 
record = (arg[1], arg[2], arg[3], arg[4], arg[5], arg[6], arg[8], arg[9])

cur.execute(insert_catalogue, record)
conn.commit()

cur.execute("SELECT *FROM Catalogue;")
cur.close()
conn.close()