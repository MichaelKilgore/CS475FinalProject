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

    struct arg_struct *args = (struct arg_struct *)arguments;
	int Sd = args->sd;

	char buf[BUF_SIZE];
	read(Sd, buf, BUF_SIZE);
	//cout << buf << endl;

    Document d;
    d.Parse(buf);

	assert(d.IsObject());
	
	if (d.HasMember("request")) {
		string request = d["request"].GetString();
	} else {
		msg = "No request method was given";
	}

	string request = d["request"].GetString();
	if (!strcmp(request.c_str(), "InsertDriver")) {						//Driver
		msg = "New driver inserted.";
	} else if (!strcmp(request.c_str(), "DeleteDriver")) {
		msg = "Driver was deleted.";
	} else if (!strcmp(request.c_str(), "InsertVehicle")) {				//Vehicle
		msg = "Driver was inserted.";
	} else if (!strcmp(request.c_str(), "DeleteVehicle")) {
		msg = "Driver was deleted.";
	} else if (!strcmp(request.c_str(), "InsertMeal")) {					//Meal
		msg = "Meal was inserted.";
	} else if (!strcmp(request.c_str(), "DeleteMeal")) {
		msg = "Meal was deleted.";
	} else if (!strcmp(request.c_str(), "UpdateMealAvailability")) {
		msg = "Meal availability was updated."; 
	} else if (!strcmp(request.c_str(), "InsertPackage")) {				//Package
		msg = "Package was inserted.";
	} else if (!strcmp(request.c_str(), "CancelPackage")) {
		msg = "Package was deleted.";
	} else if (!strcmp(request.c_str(), "ViewPackageStatus")) {			//Package Status
		msg = "Package status is:";	
	} else if (!strcmp(request.c_str(), "UpdatePackageStatus")) {
		msg = "Package status was updated.";
	} else if (!strcmp(request.c_str(), "ViewSales")) {					//ViewSales
		msg = "";		
	} else if (!strcmp(request.c_str(), "FilterViewSales")) {
		msg = "";	
	} else if (!strcmp(request.c_str(), "ViewMealPopularity")) {
		msg = "";	
	} else {
		msg = "request given was invalid.";
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












