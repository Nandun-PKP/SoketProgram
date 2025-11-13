#!/usr/bin/env python3
"""
Simple TCP Socket Client
This client connects to a server and sends messages.
"""

import socket
import sys

def start_client(host='127.0.0.1', port=65432):
    """
    Start a TCP socket client that connects to a server and sends messages.
    
    Args:
        host (str): The hostname or IP address to connect to
        port (int): The port number to connect to
    """
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Connect to the server
        print(f"Connecting to {host}:{port}")
        client_socket.connect((host, port))
        print("Connected to server")
        
        # Send and receive messages
        while True:
            # Get message from user
            message = input("\nEnter message (or 'quit' to exit): ")
            
            if message.lower() == 'quit':
                print("Closing connection...")
                break
            
            # Send data
            client_socket.sendall(message.encode('utf-8'))
            print(f"Sent: {message}")
            
            # Receive response
            data = client_socket.recv(1024)
            print(f"Received: {data.decode('utf-8')}")
            
    except ConnectionRefusedError:
        print(f"Error: Could not connect to {host}:{port}", file=sys.stderr)
        print("Make sure the server is running", file=sys.stderr)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
    finally:
        client_socket.close()
        print("Client socket closed")

if __name__ == "__main__":
    # Parse command line arguments if provided
    host = sys.argv[1] if len(sys.argv) > 1 else '127.0.0.1'
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 65432
    
    start_client(host, port)
