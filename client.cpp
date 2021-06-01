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

const unsigned int port = 6310;
const string IP = "76.121.141.32";
const unsigned int BUF_SIZE = 65535;

int main (int argc, char** argv) {

	if (argc != 2) {
        cout << "A file was not given to send." << endl;
		return 0;
    }

	char * file = argv[1];
	
    // Get the host IP address
    struct hostent* host = gethostbyname(IP.c_str());

    sockaddr_in sendSock;
    // zero out the data structure
    bzero((char*) &sendSock, sizeof(sendSock));
    // using IP
    sendSock.sin_family = AF_INET;
    // sets the address to the address we looked up
    sendSock.sin_addr.s_addr = inet_addr(inet_ntoa(*(struct in_addr*)*host->h_addr_list));

    // set the port to connect to
    sendSock.sin_port = htons(port);

    // create new socket (aka pipe to transmit data)
    int clientSd = socket(AF_INET, SOCK_STREAM, 0);		

	int connectStatus = connect (clientSd, (sockaddr*)&sendSock, sizeof(sendSock));
    if (connectStatus < 0) {
        cout << "Error connecting" << endl;
    } else {
       // cout << "Connection Established" << endl;
    }

	ifstream ifs { file };	
    if ( !ifs.is_open() )
    {
        std::cerr << "Could not open file for reading!\n";
        return EXIT_FAILURE;
    }

    IStreamWrapper isw { ifs };

    Document doc {};
    doc.ParseStream( isw );

    StringBuffer buffer {};
    Writer<StringBuffer> writer { buffer };
    doc.Accept( writer );

    if ( doc.HasParseError() )
    {
        std::cout << "Error  : " << doc.GetParseError()  << '\n'
                  << "Offset : " << doc.GetErrorOffset() << '\n';
        return EXIT_FAILURE;
    }

    const std::string jsonStr { buffer.GetString() };

	write(clientSd, jsonStr.c_str(), strlen(jsonStr.c_str()));    // sd: socket descriptor

	char buf[BUF_SIZE];
	read(clientSd, buf, BUF_SIZE);
	cout << buf << endl;

	return 0;
}
