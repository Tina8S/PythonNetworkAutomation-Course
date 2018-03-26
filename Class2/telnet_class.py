#!/usr/bin/env python

# Write a script that connects using telnet to pynet-rtrq.
# Execute the "show ip int brief" command on the router and return 
# the output

import telnetlib
import sys
import socket
from time import sleep

class TelTest:

    USER = "pyclass"
    PASS = "88newclass"
    
    def __init__(self, ip_addr = "184.105.247.70", port = 23, timeout = 7):
        self.TELNET_TIMEOUT = timeout
        try:
            self.conn = telnetlib.Telnet(ip_addr, port, timeout)
        except socket.timeout:
            print("Probleme beim Herstellen der Verbindung")
            sys.exit("timout")


    def login(self, user = USER, passw = PASS):
        self.conn.read_until("sername:".encode('utf-8'), self.TELNET_TIMEOUT)
        sleep(1)
        my_user = (user + "\n").encode('utf-8')
        self.conn.write(my_user)
        self.conn.read_until("assword:".encode('utf-8'), self.TELNET_TIMEOUT)
        sleep(1)
        my_pass = (passw + "\n").encode('utf-8')
        self.conn.write(my_pass)
        output = self.conn.read_until("pynet-rtr#".encode('utf-8'), self.TELNET_TIMEOUT)
        print(output.decode('utf-8'))


    def send_command(self, command):
        my_cmd = (command.rstrip() + "\n").encode('utf8')
        self.conn.write(my_cmd)
        sleep(1)
        try:
            return self.conn.read_very_eager()
        except EOFError:
            print("Something went wrong during execution of this command")
            return ""


    def set_terminal_length(self, length):
        my_cmd = "set terminal length " + str(length)
        self.send_command(my_cmd)


def main():

    my_tt = TelTest()
    my_tt.login()
    my_tt.set_terminal_length(0)
    sleep(1)
    print(my_tt.send_command("show ip int brief").decode('utf-8'))


if __name__ == "__main__":
    main()
