#include<iostream>
#include <sys/types.h>    // socket, bind
#include <sys/socket.h>   // socket, bind, listen, inet_ntoa
#include <netinet/in.h>   // htonl, htons, inet_ntoa
#include <arpa/inet.h>    // inet_ntoa
#include <netdb.h>     // gethostbyname
#include <unistd.h>    // read, write, close
#include <strings.h>     // bzero
#include <netinet/tcp.h>  // SO_REUSEADDR
#include <sys/uio.h>      // writev
#include <pthread.h>

#include "rapidjson/include/rapidjson/document.h"
#include "rapidjson/include/rapidjson/writer.h"
#include "rapidjson/include/rapidjson/stringbuffer.h"
#include "rapidjson/include/rapidjson/istreamwrapper.h"
#include "rapidjson/include/rapidjson/ostreamwrapper.h"
#include <fstream>
#include <string>
#include <cstdlib>

using namespace std;
using namespace rapidjson;

const unsigned int BUF_SIZE = 65535;
const unsigned int port = 6310;

struct arg_struct {
    int sd;
};

int guard(int n, char * err) {
    if (n == -1) {
        perror(err); exit(1);
    }
    return n;
}

void *SQL(void *arguments) {

	string msg = "";
	int fail = 0;
	int success = -1;

    struct arg_struct *args = (struct arg_struct *)arguments;
	int Sd = args->sd;

	char buf[BUF_SIZE];
	read(Sd, buf, BUF_SIZE);
	//cout << buf << endl;

    Document d;
    d.Parse(buf);

	if (d.IsObject()) {
		if (d.HasMember("request")) {
			string request = d["request"].GetString();
			if (!strcmp(request.c_str(), "InsertDriver")) {                     //Driver
				string command = "/usr/local/bin/python3 pythonScripts/InsertDriver.py ";
				if (d.HasMember("EmployeeID") && d.HasMember("FirstName") && d.HasMember("LastName") && d.HasMember("StatusID")) {
					command += d["EmployeeID"].GetString();
					command += " ";
					command += d["FirstName"].GetString();
					command += " ";
					command += d["LastName"].GetString();
					command += " ";
					command += d["StatusID"].GetString();
					success = system(command.c_str());
					if (success == 0) {
						msg = "Driver was inserted successfully.";
					} else {
						msg = "Driver was NOT inserted.";
					}
				} else {
					fail = 1;
				}
			} else if (!strcmp(request.c_str(), "UpdateDriverStatus")) {
				string command = "/usr/local/bin/python3 pythonScripts/UpdateDriverStatus.py ";
				if (d.HasMember("EmployeeID") && d.HasMember("StatusID")) {
					command += d["StatusID"].GetString();
					command += " ";
					command += d["EmployeeID"].GetString();
					system(command.c_str());
					msg = "Driver with the given credentials has been updated";	
				} else {
					fail = 1;
				}
			} else if (!strcmp(request.c_str(), "InsertVehicle")) {             //Vehicle
				string command = "/usr/local/bin/python3 pythonScripts/InsertVehicle.py ";
				if (d.HasMember("PlateNumber") && d.HasMember("Type") && d.HasMember("Size") && d.HasMember("Capacity") && d.HasMember("Location")) {
					command += d["PlateNumber"].GetString();
					command += " ";
					command += d["Type"].GetString();
					command += " ";
					command += d["Size"].GetString();
					command += " ";
					command += d["Capacity"].GetString();
					command += " ";
					command += d["Location"].GetString();
					success = system(command.c_str());
					if (success == 0) {
						msg = "Vehicle was inserted successfully.";
					} else {
						msg = "Vehicle was NOT inserted.";
					}
				} else {
					fail = 1;
				}
			} else if (!strcmp(request.c_str(), "UpdateVehicleStatus")) {
				string command = "/usr/local/bin/python3 pythonScripts/UpdateVehicleStatus.py ";
				if (d.HasMember("PlateNumber") && d.HasMember("Location")) {
					command += d["Location"].GetString();
					command += " ";
					command += d["PlateNumber"].GetString();
					system(command.c_str());
					msg = "Vehicle with the given credentials was updated.";	
				} else {
					fail = 1;
				}
			} else if (!strcmp(request.c_str(), "InsertMeal")) {                    //Meal
				string command = "/usr/local/bin/python3 pythonScripts/InsertMeal.py ";
				if (d.HasMember("Weight") && d.HasMember("IsVegetarian") && d.HasMember("IsVegan") && d.HasMember("IsGlutenFree")
						&& d.HasMember("ProteinType") && d.HasMember("IsForSale") && d.HasMember("Description") && d.HasMember("Cost")) {
					command += d["Weight"].GetString();
					command += " ";
					command += d["IsVegetarian"].GetString();
					command += " ";
					command += d["IsVegan"].GetString();
					command += " ";
					command += d["IsGlutenFree"].GetString();
					command += " ";
					command += d["ProteinType"].GetString();
					command += " ";
					command += d["IsForSale"].GetString();
					command += " ";
					command += d["Description"].GetString();
					command += " ";
					command += d["Cost"].GetString();
					success = system(command.c_str());
					if (success == 0) {
						msg = "Meal was inserted successfully.";
					} else {
						msg = "Meal was NOT inserted.";
					}
				} else {
					fail = 1;
				}
			} else if (!strcmp(request.c_str(), "UpdateMealAvailability")) {
				string command = "/usr/local/bin/python3 pythonScripts/UpdateMealAvailability.py ";
				if (d.HasMember("IsForSale") && d.HasMember("Description")) {
					command += d["IsForSale"].GetString();
					command += " ";
					command += d["Description"].GetString();
					system(command.c_str());
					msg = "Meals with the given credentials were updated.";
				} else {
					fail = 1;
				}
			} else if (!strcmp(request.c_str(), "InsertPackage")) {             //Package
				//TODO: pthread_join(NULL); also this still performs the action if the meal description doesn't exists.
				string command = "/usr/local/bin/python3 pythonScripts/InsertPackage.py ";
				if (d.HasMember("Address") && d.HasMember("Username") && d.HasMember("OrderNumber") && d.HasMember("Barcode") && d.HasMember("IsPriority")) {
					for (int i = 0; i < d["Meals"].Size(); i++) {
						if (!d["Meals"][i].HasMember("NumberOfOrders")) {
							fail = 1;	
						} if (!d["Meals"][i].HasMember("Description")) {
							fail = 1;	
						}
					}

					if (fail != 1) {
						command += d["Address"].GetString();	
						command += " ";
						command += d["Username"].GetString();
						command += " ";
						command += d["OrderNumber"].GetString();
						command += " ";
						command += d["Barcode"].GetString();
						command += " ";
						command += d["IsPriority"].GetString();
						system(command.c_str());
						for (int i=0; i < d["Meals"].Size(); i++) {
							command = "/usr/local/bin/python3 pythonScripts/InsertMealForOrder.py ";
							command += d["Meals"][i]["Description"].GetString();
							command += " ";
							command += d["Meals"][i]["NumberOfOrders"].GetString();
							system(command.c_str());
						}
						msg = "Package was inserted.";
					}
				} else {
					fail = 1;
				}
			} else if (!strcmp(request.c_str(), "ViewPackageStatus")) {         //Package Status //writing to temp file
				string command = "/usr/local/bin/python3 pythonScripts/ViewPackageStatus.py ";
				if (d.HasMember("Username") && d.HasMember("OrderNumber")) {
					ofstream ofs;
					ofs.open("tempfile.txt", ofstream::out | ofstream::trunc);
					ofs.close();
					command += d["Username"].GetString();
					command += " ";
					command += d["OrderNumber"].GetString();
					command += " > tempfile.txt";
					system(command.c_str());
					fail = 2;
				} else {
					fail = 1;
				}
			} else if (!strcmp(request.c_str(), "UpdatePackageStatus")) {
				string command = "/usr/local/bin/python3 pythonScripts/UpdatePackageStatus.py ";
				if (d.HasMember("Barcode") && d.HasMember("PackStatus")) {
					command += d["Barcode"].GetString();
					command += " ";
					command += d["PackStatus"].GetString();
					system(command.c_str());
					msg = "Package status was updated.";
				} else {
					fail = 1;
				}
			} else if (!strcmp(request.c_str(), "ViewSales")) {                 //ViewSales //writing to temp file
				ofstream ofs;
                ofs.open("tempfile.txt", ofstream::out | ofstream::trunc);
                ofs.close();
				string command = "/usr/local/bin/python3 pythonScripts/ViewSales.py > tempfile.txt";
				system(command.c_str());
				fail = 2;
			} else if (!strcmp(request.c_str(), "FilterViewSales")) { //Brent //writing to temp file
				ofstream ofs;
                ofs.open("tempfile.txt", ofstream::out | ofstream::trunc);
                ofs.close();
                string command = "/usr/local/bin/python3 pythonScripts/FilterViewSales.py ";

				for (int i=0; i < d["ProteinTypes"].Size(); i++) {
                	command += d["ProteinTypes"][i].GetString();
               		command += " ";
               	}
				command += " > tempfile.txt";
               	system(command.c_str());
				fail = 2;
			}  else if (!strcmp(request.c_str(), "ViewIdleDrivers")) {
        		string command = "/usr/local/bin/python3 pythonScripts/ViewIdleDrivers.py ";	
				command += " > tempfile.txt";	
				system(command.c_str());
				fail = 2;
			} else if (!strcmp(request.c_str(), "ViewIdleVehicles")) {
				string command = "/usr/local/bin/python3 pythonScripts/ViewIdleVehicles.py ";
            	command += " > tempfile.txt";
            	system(command.c_str());
            	fail = 2;
			} else if (!strcmp(request.c_str(), "InsertShipment")) {
				string command = "/usr/local/bin/python3 pythonScripts/InsertShipment.py ";
				if (d.HasMember("TicketNumber") && d.HasMember("EmployeeID") && d.HasMember("PlateNumber") && d.HasMember("Barcodes")) {
					command += d["TicketNumber"].GetString();
					command += " ";
					command += d["EmployeeID"].GetString();
					command += " ";
					command += d["PlateNumber"].GetString();
					system(command.c_str());
					msg = "Shipment was inserted.";
				
					for (int i=0; i < d["Barcodes"].Size(); i++) {
						command = "/usr/local/bin/python3 pythonScripts/UpdatePackageShipmentID.py ";
                    	command += d["Barcodes"][i].GetString();
						system(command.c_str());
                	}	
				} else {
					fail = 1;
        		}
			} else {
				fail = 1;
			}
		} else {
			fail = 1;
		}
	} else {
		fail = 1;
	}

	if (fail == 1) {
    	msg = "Request method given was corrupt.";
	} else if (fail == 2) {
		msg = "";
		ifstream myfile ("tempfile.txt");
		if (myfile.is_open()) {
			string line = "";
			while (getline(myfile, line)) {
				msg += line;	
				msg += "\n";
			}
			myfile.close();
		}
	}

	write(Sd, msg.c_str(), strlen(msg.c_str()));    // sd: socket descriptor

	pthread_exit(NULL);
    return NULL;
}

int main (int argc, char** argv) {
    sockaddr_in acceptSock;
    bzero((char*) &acceptSock, sizeof(acceptSock));  // zero out the data structure
    acceptSock.sin_family = AF_INET;   // using IP
    acceptSock.sin_addr.s_addr = htonl(INADDR_ANY); // listen on any address this computer has
    acceptSock.sin_port = htons(port);  // set the port to listen on

	int serverSd = guard(socket(AF_INET, SOCK_STREAM, 0), (char *)"Could not create TCP listening socket");

    const int on = 1;
    setsockopt(serverSd, SOL_SOCKET, SO_REUSEADDR, (char *) &on, sizeof(int));  // this lets us reuse the socket without waiting for the OS to recycle it

    // Bind the socket
	guard(::bind(serverSd, (sockaddr*) &acceptSock, sizeof(acceptSock)), (char *)"could not bind");

    // Listen on the socket
    int n = 5;
	guard(listen(serverSd, n), (char *)"could not listen");  // listen on the socket and allow up to n connections to wait.
	
	sockaddr_in newsock;   // place to store parameters for the new connection    socklen_t newsockSize = sizeof(newsock);
	socklen_t newsockSize = sizeof(newsock);

	while (1) {
		int newSd = accept(serverSd, (sockaddr *)&newsock, &newsockSize);

		pthread_t thread;
        struct arg_struct args;
        args.sd = newSd;
        pthread_create(&thread, NULL, &SQL, (void*)&args);
	}
}












