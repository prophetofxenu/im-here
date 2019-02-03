# im-here: Simple way to keep track of servers with dynamic IPs

This project is essentially a TCP echo client and server pair. However, the server program records the message transmitted during a connection along with the IP it came from. It is meant to be as simple to use as possible.

I have a VPS at home that I need to connect to, but my home internet connection gets assigned a dynamic IP. I also have a rental VPS that has a static IP. My home VPS runs the client program and my rental VPS runs the server. Every five minutes or so, the client program is run and the record on my rental VPS is updated. When I need to connect to my home VPS, I update my SSH config with the most recent IP that was exchanged. A single server instance can be run with theoretically unlimited clients.

## Requirements
* Python 3
* At least two computers
    * One of these computers must have a static IP

## Setup Instructions
1. Set the server address in client.py (line 4) and change the port if needed (line 5)
2. Change the localhost address of the server and the port if needed in server.py (lines 6-7)
3. Set the location where client connections are logged (line 5). Make sure you have permission to write in this location. The server program will make the last folder if it doesn't exist; it doesn't need to exist before running.
4. Run the server program. The server runs indefinitely. You may want to either run it as a service or for a simpler but less efficient solution, leave it running in tmux or screen.
5. Schedule the client program to be run periodically. This can be done through cron or another scheduling program.