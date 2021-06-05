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
		password = "",
		port = "5432")

	print("connected")
except:
	print("not connected.")
	exit(0)

cur = conn.cursor()

execution = "UPDATE Package SET PackStatus = \'C\' WHERE Address = {} AND Username = {} AND OrderNumber = {}".format(args[0], args[1], args[2])

cur.execute(execution)

conn.commit()

cur.close()
conn.close()