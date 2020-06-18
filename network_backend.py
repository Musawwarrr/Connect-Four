import collections
import socket

Connection = collections.namedtuple('Connection', 'socket socket_in socket_out')

#Makes the connection with the server
def make_connection(host, port): 
    n_socket = socket.socket()
    n_socket.connect((host, port))
    n_socket_in = n_socket.makefile("r")
    n_socket_out = n_socket.makefile('W')

    return Connection(socket = n_socket, socket_in = n_socket_in, socket_out = n_socket_out)

#Closes the connection whether successful or not 
def close_connection(connection):
    connection.socket_in.close()
    connection.socket_out.close()
    connection.socket.close()

#Sends all the messages in the buffer
def message_send(connection, message):
    connection.socket_out.write(message + "\r\n")
    connection.socket_out.flush()
    
#Reads the messages from the server
def message_read(connection):
    return connection.socket_in.readline()[:-1]

#Logs in with the server with a username 
def login(connection, username):
    message_send(connection, 'I32CFSP_HELLO ' + username)

#Asks to play with the AI
def ask_AI(connection):
    message_send(connection, "AI_GAME")

