import logging
import socket
import time

def response(data):
    return f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n{data}\r\n\r\n"


class HTTPServer:
    
    def __init__(self, host='', port=8080):
                
        # Logging instrumentation
        logging.basicConfig(level=logging.DEBUG)
        
        logging.info("HTTP Server init")
        
        ## Define Socket
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((host, port))
        logging.info(f'Server binded to host "{host}" on port {port}')
    
        
    def start(self):
        done = False
        self.socket.listen(1)
        logging.info("HTTP Server is starting")
        
        connection, address = self.socket.accept()
        logging.info(f'Connection accepted for host {address[0]} on port {address[1]}')
        
        while not done: 
            done = self.loop(connection)
        
        logging.info("Closing connection")
        connection.close()
        
        logging.info("Closing listening socket")
        self.socket.close()
            
    def loop(self, connection):
        start_time = time.time()
        logging.info("In the loop event")
        request = connection.recv(1024)
        logging.info(f"Reception of {request.decode()}")
        res = response("Hello World!")
        logging.info(res)
        connection.send(bytes(res, 'utf-8'))
        end_time = time.time()
        logging.info(f"Running loop in {end_time - start_time}s")
        return True
            