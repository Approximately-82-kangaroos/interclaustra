# TODO:
# Add server creation - Completed 9/13/2023
# Add file sending
# Add argument sending
# Add solution reception
# Add secondary verification
# https://www.youtube.com/watch?v=JkWdNrmbNEQ

import socket

DEF_PORT = 4279
DEF_IP = "127.0.0.1"

# Creates and binds the server socket
# Code courtesy of https://www.geeksforgeeks.org/socket-programming-python/
def open_server(ip = DEF_IP, port = DEF_PORT):
    skt = socket.socket()
    skt.bind((ip, port))
    return skt

def send_file(filename):
    pass

if (__name__ == "__main__"):
    s = open_server()
    if (s != None):
        s.listen(0)
        print("Server open.")
    else:
        print("Server failed to start.")

