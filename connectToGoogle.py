import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created")

except socket.error as err:
    print("Socket creation failed with error %s" %(err))

port = 80 # default port for HTTP communication

try:
    host_ip = socket.gethostbyname('www.google.com')

except socket.gaierror: # Get Address Info Error
    print("There was an error resolving the host")
    sys.exit()

# connecting to the server
s.connect((host_ip,port))

print("The socket has successfully connected to Google")