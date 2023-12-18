import socket
import _thread as thrd
from datetime import datetime


# TODO: define a message class to hold all relevant info about a message
# could also add a "reply to" attribute to indicate a reply message (dk how to implement that, though)
class Msg:
    def __init__(self, msg_content=None):
        self.time = str(datetime.now())
        self.sender = None  # TODO: Make this the client
        if msg_content is None:
            self.content = f"Connection established with client {'idk'}"
        else:
            self.content = msg_content
        
        # TODO: finish defining this

    def __str__(self, mode=None):
        # TODO: take the current message and print it nicely (for a log file or sth, these details will be truncated for forum)
        pass


# just to keep track of what and where and who and what
msg_history = []
# could also define a function to print out a log of the whole shebang


#import time

# TODO: define a thread to deal with each client
def handle_client( threadName, delay):
   for count in range(1, 6):
      # time.sleep(delay)
      print (f"Thread name: {threadName} Count: {count}")


# TODO: also add a logfile, just for fun

def main():
    # create welcome socket to receive all incoming clients
    welcome_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind the server to the localhost
    welcome_socket.bind(('0.0.0.0', server_port))

    # Listen to incoming clients
    welcome_socket.listen(1)  # TODO: see what this does and what backlog is

    print('TCP Server running on port', server_port) 

    # TODO: Modify to loop and be called by main thread when needed
    try:
        thrd.start_new_thread(handle_client, ("Thread-1", 2, ))
        thrd.start_new_thread(handle_client, ("Thread-2", 4, ))
    except:
        print ("Error: unable to start thread")

    while True:
        connection_socket, caddr = welcome_socket.accept()
        # TODO: figure out how to allocate these to threads instead

        while connection_socket:
            cmsg = connection_socket.recv(1024)
            cmsg = cmsg.decode()
            print("Client", str(caddr), " sent the message: ", cmsg)
            if not cmsg.isalnum():
                msg_out = "Not alphanumeric."
            else:
                msg_out = "Alphanumeric"
            connection_socket.send(msg_out.encode())
            
        print("There goes the socket :(")


if __name__ == "__main__":
    # select a server port
    server_port = 12000
    # where should new connections be passed to
    new_port = server_port + 1

    # holds a list of tuples: (client_socket object, client port #)
    client_list = []

    main()
