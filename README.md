# SoketProgram
This is my network module assignment - A simple TCP socket client-server application.

## Description
This project demonstrates basic TCP socket programming in Python. It includes:
- **server.py**: A TCP server that listens for connections and echoes back received messages
- **client.py**: A TCP client that connects to the server and sends messages

## Requirements
- Python 3.x

## Usage

### Running the Server
Start the server first in one terminal:

```bash
python3 server.py
```

Or specify custom host and port:

```bash
python3 server.py <host> <port>
```

Example:
```bash
python3 server.py 127.0.0.1 65432
```

The server will start listening for incoming connections.

### Running the Client
In another terminal, start the client:

```bash
python3 client.py
```

Or specify custom host and port to match the server:

```bash
python3 client.py <host> <port>
```

Example:
```bash
python3 client.py 127.0.0.1 65432
```

Once connected, you can:
1. Type messages and press Enter to send them to the server
2. The server will echo back the messages
3. Type 'quit' to close the connection

## Features
- Simple TCP/IP communication
- Echo server functionality
- Command-line interface for client
- Configurable host and port
- Proper error handling and cleanup
- Socket reuse to avoid "Address already in use" errors
