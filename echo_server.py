# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 15:23:40 2024

@author: anush
"""

import socket

def main():
    # Set up server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 5555))
    server_socket.listen(1)
    print("Server is listening...")

    # Accept incoming connection
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address} established.")

    # Receive data from client and echo it back
    data = client_socket.recv(1024)
    print(f"Received message from client: {data.decode()}")

    # Echo the message back to client
    client_socket.sendall(data)

    # Close the connection
    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    main()
