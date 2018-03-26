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


def connect(ip_addr, TELNET_PORT, TELNET_TIMEOUT):
    try:
        return telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    except socket.timeout:
        print("Probleme beim Herstellen der Verbindung")
        sys.exit(1)


def login(conn, user, passw):
    conn.read_until("sername:".encode('utf-8'), TELNET_TIMEOUT)
    sleep(1)
    my_user = (user + "\n").encode('utf-8')
    conn.write(my_user)
    conn.read_until("assword:".encode('utf-8'), TELNET_TIMEOUT)
    sleep(1)
    my_pass = (passw + "\n").encode('utf-8')
    conn.write(my_pass)
    output = conn.read_until("pynet-rtr#".encode('utf-8'), TELNET_TIMEOUT)
    print(output.decode('utf-8'))


def send_command(conn, command):
    my_cmd = (command.rstrip() + "\n").encode('utf8')
    conn.write(my_cmd)
    sleep(1)
    try:
        return conn.read_very_eager()
    except EOFError:
        print("Something went wrong during execution of this command")
        return ""


def set_terminal_length(conn, length):
    my_cmd = "set terminal length " + str(length)
    send_command(conn, my_cmd)


def main():
    my_conn = connect(IP_ADDR, TELNET_PORT, TELNET_TIMEOUT)
    login(my_conn, USER, PASS)
    set_terminal_length(my_conn, 0)
    sleep(1)
    print(send_command(my_conn, "show ip int brief").decode('utf-8'))


if __name__ == "__main__":
    main()
