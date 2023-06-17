# This function returns the total time, with minutes represented as 
# decimals (example: 1 hour 30 minutes = 1.5), for all end user time
# spent accessing a server in a given day. 
def sum_server_Use_time(server):
    total_time = 0.0
    for user, spent_time in server.items():
        total_time += server[user]
    return round(total_time, 2)
FileServer = {"EndUser1": 2.25, "EndUser2": 4.5, "EndUser3": 1, "EndUser4": 3.75, "EndUser5": 0.6, "EndUser6": 8}
print(sum_server_Use_time(FileServer))