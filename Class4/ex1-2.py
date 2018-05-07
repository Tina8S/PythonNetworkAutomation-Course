#!/usr/bin/env python

import paramiko


def main():
    ip = "184.105.247.71"
    username = "pyclass"
    password = "88newclass"

    remote_conn = paramiko.SSHClient()
    remote_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    remote_conn.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False)

    remote_conn = remote_conn.invoke_shell()

    remote_conn.exec_command("terminal length 0\n")

    remote_conn.exec_command("show version\n")

    output = remote_conn.recv(10000)
    print(output)

if __name__ == "__main__":
    main()
