# CS475FinalProject
## TODO BY PRIORITY
1. create PREPARE statements for commands we want to run.
2. create a file that adds a bunch of data into the database for testing our scripts on.
3. write python scripts that execute PREPARE statements. NOTE: we will need a lot of these so we can divide up the work here, and no single person will do this whole step by themselves.
5. create a server that listens for CRUD commands, queries, ext.
6. create a client that tells server to do CRUD commands, queries, ext.
## Who has done what and what they are currently working on.
### Michael
FINISHED: wrote a script that creates the tables for our database.  
          uploaded updated schema.  
          added a insertStaticValues.txt which inserts values into the ProteinType, DriverStatus, and Warehouse location.
          added a createPrepareStatements.txt file which makes a couple prepare statements. Not all the prepare statements we will need to make yet, but this is still in progress.
          added baseline code for a server, but its not done yet.  
IN PROGRESS: working on the server and client. Still working on prepare statements.
### Brent
FINISHED: Transferred over script and formatted Google Slides for presentation. 
           viewSales.py
           filterViewSales.py 
 IN PROGRESS:  
### Brendan  
FINISHED: 
Made setupDB which combines some of the previous files for creating the DB and adds some test values into the non-domain tables. Made testTables python script, which outputs all the data in a table based on terminal input. Made a few minor changes to the schema.
Python scripts for inserting and deleting a driver.

IN PROGRESS:   
### Nic 
FINISHED:   CancelPackage
IN PROGRESS:
### Sabi
FINISHED:   Pushed deleteVehicle.py, InsertMealOrdered.py, UpdatePackage.py, viewPackageStatus.py, insertVehicle.py,insertshipment.py, and insertcataloge.py

IN PROGRESS:   
## NOTES/UPDATES
I changed a couple things in our schema. I added a public employeeID for employees. I also changed totalCost in mealOrdered to NumberOfOrders because we don't need a totalCost because it can be calculated with a query, also our previous schema had no way of added multiple of one meal to an order, so that fixed that problem.  
## Thoughts that will need to be addressed eventually
How are we going to generate the ticket numbers?


