# Ezoic Intern Summer 2022 Project 

## Assumptions
 - Simple local, networking protocol communication through sockets 
 - Don't need webpage (i.e HTML, CSS, JS) or UI

## Approach
 - Setup server first so clients to connect by listening
 - Connect clients to server to allow socket communication
 - Implement multi-threading to handle multiple clients after 1 on 1 communication works
 - Add small details 

## Libraries used
 - `import socket` to handle communication between sockerts
 - `import threading` to handle multi-threading to allow clients executing independently
 - `import colorama` to color username text
 - `import sys` 

## Decisions and tradeoffs 
 - OOP vs Procedural Programming
   - For this project, I took on a more procedural path since the server and client code didn't need to be reused or shared for other programs

## Features 
 - Chatroom that allows multiple clients to communicate to everyone in the chat
 - Implemented a help menu, a quit system, and a way to get current users in the chat
 - Usernames have colors

## Improvements
 - If it were a bigger project
   - Display on webpage, style it, and make it look nice 
   - Use a framework like React instead of Python's socket implementation
 
 - If I had more time
   - Fix current bug issues:
     - Disconnection message isn't shown properly on exit on exception
     - Client1 has to enter their username first before Client2 can do anything
   - Implement /kick function
     - Tried but there's a few bugs so didn't end up pushing
    - Implement possibly a /ban
    - Implement unique usernames
    - Figure out why timestamps were inaccurate using multiple sockets.
     - Client2 ends up exceeding Client1's timestamp even though Client1 started first