#!/usr/bin/env python3
"""
Simple TCP Socket Server
This server listens for incoming connections and echoes back received messages.
"""

import socket
import sys

def start_server(host='127.0.0.1', port=65432):
    """
    Start a TCP socket server that echoes back received messages.
    
    Args:
        host (str): The hostname or IP address to bind to
        port (int): The port number to listen on
    """
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Allow reuse of address
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        # Bind the socket to the address and port
        server_socket.bind((host, port))
        
        # Listen for incoming connections (max 5 queued connections)
        server_socket.listen(5)
        print(f"Server listening on {host}:{port}")
        
        while True:
            # Wait for a connection
            print("\nWaiting for a connection...")
            client_socket, client_address = server_socket.accept()
            
            try:
                print(f"Connection from {client_address}")
                
                # Receive and echo data
                while True:
                    data = client_socket.recv(1024)
                    
                    if not data:
                        print(f"No more data from {client_address}")
                        break
                    
                    print(f"Received: {data.decode('utf-8')}")
                    
                    # Echo the data back to the client
                    client_socket.sendall(data)
                    print(f"Sent: {data.decode('utf-8')}")
                    
            finally:
                # Clean up the connection
                client_socket.close()
                print(f"Connection with {client_address} closed")
                
    except KeyboardInterrupt:
        print("\nServer shutting down...")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
    finally:
        server_socket.close()
        print("Server socket closed")

if __name__ == "__main__":
    # Parse command line arguments if provided
    host = sys.argv[1] if len(sys.argv) > 1 else '127.0.0.1'
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 65432
    
    start_server(host, port)
