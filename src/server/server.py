# TODO:
# Add server creation - Completed 9/13/2023
# Add file sending - Completed 9/14/2023
# Add argument sending
# Add solution reception
# Add secondary verification
# https://www.youtube.com/watch?v=JkWdNrmbNEQ

import socket
import os

DEF_PORT = 4279
DEF_IP = "localhost"

# Creates and binds the server socket
# Code courtesy of https://www.geeksforgeeks.org/socket-programming-python/
def open_server(ip = DEF_IP, port = DEF_PORT):
    skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    skt.bind((ip, port))
    return skt

def send_file(filename, receiver):
    file = open(filename, "rb")
    file_size = os.path.getsize(filename)

    receiver.send(str(file_size).encode("utf-8"))

    data = file.read()
    receiver.sendall(data)
    file.close()

if (__name__ == "__main__"):
    s = open_server()
    if (s != None):
        s.listen(4)
        print("Server open.")
        while (True):
            client, address = s.accept()
            print(f"Connection from {address}")
            # Receive 2 data points
            # 1: Version (0x01)
            # 3: 0x00
            inbuffer = client.recv(2).decode("utf-8")
            if (inbuffer != "1_0"):
                print("Invalid verification from client.")
                s.close()
            else:
                send_file("src/server/problem.py", client)
                param_file = open("src/server/parameters.txt")
                for lines in param_file:
                    list = lines.split(", ")
                    print(list)
                param_file.close()
                s.close()


    else:
        print("Server failed to start.")

