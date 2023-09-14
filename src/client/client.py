# TODO:
# Add client creation - Completed 9/14/2023
# Add file queries/reception
# Add problem processing
# Add multicore support
# Add solution sending
# https://www.youtube.com/watch?v=JkWdNrmbNEQ

import socket

if (__name__ == "__main__"):
    IP = input("What is the IP or hostname of the server you would like to connect to? ")
    PORT = 4279
    skt = socket.socket()
    skt.connect((IP, PORT))
    skt.send("10".encode("utf-8"))
