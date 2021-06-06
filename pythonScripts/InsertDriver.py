import psycopg2
import sys

args = sys.argv
if len(args) != 5:
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

execution = "INSERT INTO Driver (EmployeeID, FirstName, LastName, StatusID) Values (" + args[1] + ", \'" + args[2] + "\', \'" + args[3] + "\', \'" + args[4] + "\')"

cur.execute(execution)

conn.commit()

cur.close()
conn.close()


