import psycopg2

# python script for checking tables to make sure the right changes
# have been made
#
# Type exit to stop the script
# For selecting tables:
#   - c\C for Catalogue
#   - d\D for Driver
#   - ds\DS for DriverStatus
#   - mo\MO for MealOrdered
#   - p\P for Package
#   - ps\PS for PackageStatus
#   - pt\PT for ProteinType
#   - s\S for Shipment
#   - v\V for Vehicle
#   - w\W for Warehouse


try:
    connection = psycopg2.connect(
        host = "127.0.0.1",
        database = "quicknhealthy",
        user = "postgres",
        password = "XXXXXXXXXX",
        port = "5432"
    )

    print("Database successfully connected")

except:
    print("Connection to database failed")

curs = connection.cursor()
selection = "temp"

def printQuery():
    rows = curs.fetchall()

    for r in rows:
        print(r)

while (selection != 'exit'):

    selection = input()

    #get all the data in Catalogue
    if (selection == 'c' or selection == 'C'):
        curs.execute("SELECT * FROM Catalogue")

        #print the column names then the query
        print("MealID, Weight, IsVegetarian, IsVegan, IsGlutenFree, ProteinType, IsForSale, Description, Cost")
        printQuery()

    #get all the data in Driver
    elif (selection == 'd' or selection == 'D'):
        curs.execute("SELECT * FROM Driver")

        #print the column names then the query
        print("ID, EmployeeID, FirstName, LastName, StatusID")
        printQuery()

    #get all the data in DriverStatus
    elif (selection == 'ds' or selection == 'DS'):
        curs.execute("SELECT * FROM DriverStatus")

        #print the column names then the query
        print("ID, Description")
        printQuery()

    #get all the data for MealOrdered
    elif (selection == 'mo' or selection == 'MO'):
        curs.execute("SELECT * FROM MealOrdered")

        #print the column names then the query
        print("OrderID, MealID, Quantity")
        printQuery()

    #get all data in Package
    elif (selection == 'p' or selection == 'P'):
        curs.execute("SELECT * FROM Package")

        #print the column names then the query
        print("ID, Address, Username, OrderNumber, Barcode, ShipmentID, IsPriority, Warehouse, DeliveryCompleteData, OrderedDate, PackStatus")
        printQuery()

    #get all data in PackageStatus
    elif (selection == 'ps' or selection == 'PS'):
        curs.execute("SELECT * FROM PackageStatus")

        #print the column names then the query
        print("Type, Description")
        printQuery()

    #get all data in ProteinType
    elif (selection == 'pt' or selection == 'PT'):
        curs.execute("SELECT * FROM ProteinType")

        #print the column names then the query
        print("Type, Description")
        printQuery()

    #get all data in Shipment
    elif (selection == 's' or selection == 'S'):
        curs.execute("SELECT * FROM Shipment")

        #print the column names then the query
        print("ID, TicketNumber, DriverID, VPlateNumber")
        printQuery()

    #get all data in Vehicle
    elif (selection == 'v' or selection == 'V'):
        curs.execute("SELECT * FROM Vehicle")

        #print the column names then the query
        print("PlateNumber, Type, Size, Capacity, Location")
        printQuery()

    #get all data in Warehouse
    elif (selection == 'w' or selection == 'W'):
        curs.execute("SELECT * FROM Warehouse")

        #print the column names then the query
        print("LocalID, Address, Description")
        printQuery()
