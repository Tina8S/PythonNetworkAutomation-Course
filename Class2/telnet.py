#!/usr/bin/env python

# Write a script that connects using telnet to pynet-rtrq.
# Execute the "show ip int brief" command on the router and return 
# the output

import telnetlib
import sys
from time import sleep

TELNET_PORT = 23
TELNET_TIMEOUT = 7
IP_ADDR = "184.105.247.70"
USER = "pyclass"
PASS = "88newclass"


if __name__ == "__main__":
    main()


def connect(ip_addr, TELNET_PORT, TELNET_TIMEOUT):
    try:
        return telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    except socket.timeout:
        print("Probleme beim Herstellen der Verbindung")
        sys.exit(1)


def login(conn, user, pass):
    conn.read_until("sername:", TELNET_TIMEOUT)
    sleep(1)
    comm.write(USER + "\n")
    conn.read_until("assword:", TELNET_TIMEOUT)
    sleep(1)
    conn.write(PASS + "\n")
    output = conn.read_until("pynet-rtr#", TELNET_TIMEOUT)
    print(output)


def main():
    my_conn = connect(IP_ADDR, TELNET_PORT, TELNET_TIEMOUT)
    login(my_conn, USER, PASS)
