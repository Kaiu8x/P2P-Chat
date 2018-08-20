"""Server for multithreaded (asynchronous) chat application."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from LZW import *
from vigenere import *
import sys


def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        client.send(bytes("Greetings from the cave! Now type your name and press enter!", "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):  # Takes client socket as argument.
    """Handles a single client connection."""
    user = ""
    count = 1
    name = client.recv(BUFSIZ).decode("utf8")
    Amessage = vign(name, password, 'd')
    print("compressed text decrypted: " + Amessage)
    print("size of compress decrypted message: " + str(sys.getsizeof(Amessage)))
    AmessageList = Amessage.split(', ')
    AmessageList = list(map(int, AmessageList))
    decompText = decompress(AmessageList)
    if count == 1:
        user = decompText
        count = count + 1
    print("decompress text: " + str(decompText))
    print("size of decompress message: " + str(sys.getsizeof(decompText)))
    welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % user
    client.send(bytes(welcome, "utf8"))
    msg = "%s has joined the chat!" % decompText
    broadcast(bytes(msg, "utf8"))
    clients[client] = name

    while True:
        #msg = client.recv(BUFSIZ)
        msg = client.recv(BUFSIZ).decode("utf8")

        Amessage = vign(msg, password, 'd')
        print("compressed text decrypted: " + Amessage)
        print("size of compress decrypted message: " + str(sys.getsizeof(Amessage)))
        AmessageList = Amessage.split(', ')
        AmessageList = list(map(int, AmessageList))
        decompText = decompress(AmessageList)
        print("decompress text: " + str(decompText))
        print("size of decompress message: " + str(sys.getsizeof(decompText)))

        msgb = decompText.encode("utf8")

        if msg != bytes("{quit}", "utf8"):
            broadcast(msgb, user+": ")
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes("%s has left the chat." % name, "utf8"))
            break


def broadcast(msg, prefix=""):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""
    for sock in clients:
        sock.send(bytes(prefix, "utf8")+ msg)


password = input('Enter password: ')
clients = {}
addresses = {}

HOST = ''
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()