# TODO:
# Add client creation - Completed 9/14/2023
# Add file reception - Completed 9/14/2023
# Add problem processing - Completed 9/14/2023
# Add multicore support
# Add solution sending - Completed 9/14/2023
# https://www.youtube.com/watch?v=JkWdNrmbNEQ

import socket
import time

if (__name__ == "__main__"):
    IP = "localhost"
    PORT = 4279
    skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    skt.connect((IP, PORT))
    skt.send("10".encode("utf-8"))
    size = int(skt.recv(1024).decode("utf-8"))
    file = open("issue.py", "wb")

    #TODO: This is dumb. Split the download into 1024 packets.
    file.write(skt.recv(size))
    file.close()

    import issue
    # Send(compute(receive parameters)))
    parameters = skt.recv(1024).decode("utf-8")
    skt.send(issue.compute(parameters).encode("utf-8"))
