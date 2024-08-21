# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 15:24:52 2024

@author: anush
"""

import socket

def main():
    # Set up client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to server
    client_socket.connect(('127.0.0.1', 5555))

    # Get input from user
    message = input("Enter a message to send to the server: ")

    # Send data to server
    client_socket.sendall(message.encode())

    # Receive echoed message from server
    echoed_message = client_socket.recv(1024)
    print(f"Server echoed back: {echoed_message.decode()}")

    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    main()
