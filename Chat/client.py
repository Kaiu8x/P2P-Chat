"""Script for Tkinter GUI chat client."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter
from LZW import *
from vigenere import *
import sys

flag = False

def receive():
    """Handles receiving of messages."""
    while True:
        try:
            #msg = client_socket.recv(BUFSIZ).decode("utf8")
            
            msg = client_socket.recv(BUFSIZ)

            
           
            msg_list.insert(tkinter.END, msg)
        except OSError:  # Possibly client has left the chat.
            break


def send(event=None):  # event is passed by binders.
    """Handles sending of messages."""
    msg = my_msg.get()
    my_msg.set("")  # Clears input field.
    print(msg)
    print("size of message: " + str(sys.getsizeof(msg)))
    compText = compress(msg)
    print("compressed text: " + str(compText))
    print("size of compressed message: " + str(sys.getsizeof(compText)))
    comptoInt = compToInt(compText)
    print("compressed text to int list: " + str(comptoInt))
    cipher = vign(', '.join(str(i) for i in comptoInt), password , 'e')
    print("compressed text encrypted: " + cipher)
    print("size of compressed-encripted message: " + str(sys.getsizeof(cipher)))

    client_socket.send(bytes(cipher, "utf8"))

    if msg == "{quit}":
        client_socket.close()
        top.quit()


def on_closing(event=None):
    """This function is to be called when the window is closed."""
    my_msg.set("{quit}")
    send()

top = tkinter.Tk()
top.title("Chatter")

messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()  # For the messages to be sent.
my_msg.set("Type your messages here.")
scrollbar = tkinter.Scrollbar(messages_frame)  # To navigate through past messages.
# Following will contain the messages.
msg_list = tkinter.Listbox(messages_frame, height=15, width=150, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(top, textvariable=my_msg, width=100)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(top, text="Send", command=send)
send_button.pack()

top.protocol("WM_DELETE_WINDOW", on_closing)

#----Now comes the sockets part----
HOST = input('Enter host: ')
PORT = input('Enter port: ')
password = input('Enter password: ')
#HOST = '127.0.0.1'
#PORT = 33000
if not PORT:
    PORT = 33000
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop()  # Starts GUI execution.