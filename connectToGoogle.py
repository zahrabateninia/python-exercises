import socket


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created")

except socket.error as err:
    print("Socket creation failed with error %s" %(err))

