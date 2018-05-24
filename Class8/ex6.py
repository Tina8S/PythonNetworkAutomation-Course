#! /usr/bin/env python

from datetime import datetime
import threading
import django
django.setup()
from net_system.models import NetworkDevice, Credentials
from netmiko import ConnectHandler

def show_version(device):

    creds = device.credentials
    rconn = ConnectHandler(device_type=device.device_type, ip=device.ip_address, username=creds.username, password=creds.password, port=device.port, secret='')

    print()
    print("*" * 80)
    print(device)
    print("*" * 80)
    print(rconn.send_command('show version'))
    print("*" * 80)
    print()
    rconn.disconnect()

def main():
    my_devices = NetworkDevice.objects.all()
    start_time = datetime.now()
    for device in my_devices:
        my_thread = threading.Thread(target=show_version, args = (device,))
        my_thread.start()

    main_thread = threading.currentThread()

    for th in threading.enumerate():
        if th != main_thread:
            print(th)
            th.join()    
 
    print("Elapsed time: {}".format(datetime.now()-start_time))




if __name__ == "__main__":
    main()
