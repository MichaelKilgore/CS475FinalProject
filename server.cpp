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

using namespace std;

const unsigned int BUF_SIZE = 65535;
const unsigned int port = 6310;

struct arg_struct {
    int sd;
};

void *dataRead(void *arguments) {

    struct arg_struct *args = (struct arg_struct *)arguments;
	int Sd = args->sd;

	char buf[BUF_SIZE];
	read(Sd, buf, BUF_SIZE);
	//messages go as -> query\r\n\r\n
	
	pthread_exit(NULL);
    return NULL;
}

int main (int argc, char** argv) {
    sockaddr_in acceptSock;
    bzero((char*) &acceptSock, sizeof(acceptSock));  // zero out the data structure
    acceptSock.sin_family = AF_INET;   // using IP
    acceptSock.sin_addr.s_addr = htonl(INADDR_ANY); // listen on any address this computer has
    acceptSock.sin_port = htons(port);  // set the port to listen on

    int serverSd = socket(AF_INET, SOCK_STREAM, 0); // creates a new socket for IP using TCP

    const int on = 1;

    setsockopt(serverSd, SOL_SOCKET, SO_REUSEADDR, (char *) &on, sizeof(int));  // this lets us reuse the socket without waiting for the OS to recycle it

    // Bind the socket
    bind(serverSd, (sockaddr*) &acceptSock, sizeof(acceptSock));  // bind the socket using the parameters we set earlier

    // Listen on the socket
    int n = 5;
    listen(serverSd, n);  // listen on the socket and allow up to n connections to wait.
	
	sockaddr_in newsock;   // place to store parameters for the new connection    socklen_t newsockSize = sizeof(newsock);
	socklen_t newsockSize = sizeof(newsock);

	while (1) {
		int newSd = accept(serverSd, (sockaddr *)&newsock, &newsockSize);

		pthread_t thread;
        struct arg_struct args;
        args.BUFSIZE = 1500;
        args.sd = newSd;
        pthread_create(&thread, NULL, &dataRead, (void*)&args);

	}
}












