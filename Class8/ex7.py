#! /usr/bin/env python

from datetime import datetime
from multiprocessing import Process
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

    my_procs = []
    for device in my_devices:
        my_proc = Process(target=show_version, args = (device,))
        my_proc.start()
        my_procs.append(my_proc)


    for p in my_procs:
        print(p)
        p.join()    
 
    print("Elapsed time: {}".format(datetime.now()-start_time))




if __name__ == "__main__":
    main()
