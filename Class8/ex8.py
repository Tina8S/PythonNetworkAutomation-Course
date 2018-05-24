#! /usr/bin/env python

from datetime import datetime
from multiprocessing import Process, Queue
import django
django.setup()
from net_system.models import NetworkDevice, Credentials
from netmiko import ConnectHandler

def show_version(device, qu):

    output_dict = {}
    creds = device.credentials
    rconn = ConnectHandler(device_type=device.device_type, ip=device.ip_address, username=creds.username, password=creds.password, port=device.port, secret='')

    output = "\n"
    output += "*" * 80 + "\n"
    output += device.device_name + "\n"
    output += "*" * 80 + "\n"
    output += rconn.send_command('show version') + "\n"
    output += "*" * 80 + "\n"
    output += "\n"
    rconn.disconnect()
    output_dict[device.device_name] = output
    qu.put(output_dict)

def main():
    my_devices = NetworkDevice.objects.all()
    start_time = datetime.now()
    
    my_queue = Queue(maxsize=20)
    my_procs = []
    for device in my_devices:
        my_proc = Process(target=show_version, args = (device, my_queue))
        my_proc.start()
        my_procs.append(my_proc)


    for p in my_procs:
        print(p)
        p.join()

    while not my_queue.empty():
        my_dict = my_queue.get()
        for k, v in my_dict.items():
            print(v)
 
    print("Elapsed time: {}".format(datetime.now()-start_time))




if __name__ == "__main__":
    main()
