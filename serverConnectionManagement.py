""" this script allows you to create a Server object, add and close connections, calculate the load on the server, 
and obtain a string representation of the server's current load. 
It provides a basic framework for managing connections and monitoring the load on a server. """

import random

class Server:
    def __init__(self):
        """Creates a new server instance, with no active connections."""
        self.connections = {}

    def add_connection(self, connection_id):
        """Adds a new connection to this server."""
        connection_load = random.random()*10+1  #also can use random.randint(1,10) 
        self.connections[connection_id] = connection_load
        

    def close_connection(self, connection_id):
        """Closes a connection on this server."""
        if connection_id in self.connections:
            del self.connections[connection_id]
        

    def load(self):
        """Calculates the current load for all connections."""
        total = 0
        # Add up the load for each of the connections
        for load in self.connections.values():
            total += load
        return round(total,2)

    def __str__(self):
        """Returns a string with the current load of the server"""
        return "{:.2f}%".format(self.load())

server = Server()
server.add_connection("192.168.1.1")

print(server.load()) #the outputs varies everytime we print for example one time is 3.24
server.close_connection("192.168.1.1")
print(server.load()) # now the output must be 0 
# Portion 2
class LoadBalancing:
    def __init__(self):
        """Initialize the load balancing system with one server"""
        self.connections = {}
        self.servers = [Server()]

    def add_connection(self, connection_id):
        """Randomly selects a server and adds a connection to it."""
        server = random.choice(self.servers)
        # Add the connection to the dictionary with the selected server
        self.connections[connection_id] = server
        
        # Add the connection to the server
        server.add_connection(connection_id)
        
    def close_connection(self, connection_id):
        """Closes the connection on the the server corresponding to connection_id."""
        # Find out the right server
        # Close the connection on the server
        # Remove the connection from the load balancer
        if connection_id in self.connections:
            server = self.connections[connection_id]
            server.close_connection(connection_id)
            del self.connections[connection_id]

    def avg_load(self):
        """Calculates the average load of all servers"""
        # Sum the load of each server and divide by the amount of servers
        sum = 0
        for server in self.servers:
            sum += server.load() 
            
        amount_of_servers = len(self.servers)
        avg = sum / amount_of_servers
        return avg

    def ensure_availability(self):
        """If the average load is higher than 50, spin up a new server"""
        avg_load = self.avg_load()
        if avg_load > 50:
            new_server = Server()  # Create a new server
            self.servers.append(new_server) 

    def __str__(self):
        """Returns a string with the load for each server."""
        loads = [str(server) for server in self.servers]
        return "[{}]".format(",".join(loads))



