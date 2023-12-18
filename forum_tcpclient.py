import socket
#the server name and port
#the server is on the same computer as the client

server_name = 'localhost' # '0.0.0.0' should also be fine
server_port = 12000

#create a TCP client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Set up a TCP connection with the server

#a connection_socket will be assigned to this client on the server side

client_socket.connect((server_name, server_port))

print("Connected to Chat App")
print("Connecting to server at IP: ", server_name, " PORT: ", server_port)
quit = False
while not quit:
  #take input from the user
  msg = input("Enter a string to test if it is alphanumeric: ")

  #send the message  to the udp server
  client_socket.send(msg.encode())

  #return values from the server
  msg = client_socket.recv(1024)
  print(msg.decode())

  quit = str(input("Would you like to continue? ")).lower()\
                    not in ["y", "ye", "yes", "yup", "yea", "yeah"]

client_socket.close()


"""
11000 - c1 <-> server
12000 - server
13000 - c2 <-> server
"""
