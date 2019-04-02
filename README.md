# P2P-Chat

## Some description

A goup chat system developed in python3 as leader of project of 3, most of the code is a Frankenstein like from different code snippets.

## Functionalities

+ Implementation of [Vigenere encryption](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher) and [LZW compression](https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch). _I know it is irrational to implement both algorithms to a small string but it was a requirement_.

+ Usage of multithreading for Client-server like architecture.

## Difficulties during development

+ Implementation of both encryption and compression algorithms. Also the decision on which algorithm to use and in which order.

+ Understanding of multithreading.

## What I learned

+ Multithreading architecture.
+ Many compression and encryption algorithms.

## Improvements

+ Better UI.
+ Implement a one to one chat system.

## To use

1. Just run the server.py file in a Terminal.
2. Run the client.py file and insert the IP address where the server was built, the PORT number is 33000 by default.
3. Agree upon a password or passphrase for encryption and enter the password.
4. Start sending messages.