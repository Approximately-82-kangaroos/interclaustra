# TODO:
# Add client creation - Completed 9/14/2023
# Add file queries/reception
# Add problem processing
# Add multicore support
# Add solution sending
# https://www.youtube.com/watch?v=JkWdNrmbNEQ

import socket
import os

if (__name__ == "__main__"):
    IP = input("What is the IP or hostname of the server you would like to connect to? ")
    PORT = 4279
    skt = socket.socket()
    skt.connect((IP, PORT))
    skt.send("10".encode("utf-8"))
    size = int(skt.recv(1024).decode("utf-8"))
    file = open("problem.py", "wb")
    file.write(skt.recv(size))
