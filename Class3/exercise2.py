#!/usr/bin/env python

import importlib.util
snmp_spec = importlib.util.spec_from_file_location("snmp_helper", "/home/tstrauf/python-libs/snmp_helper.py")
snmp_helper = importlib.util.module_from_spec(snmp_spec)
snmp_spec.loader.exec_module(snmp_helper)
#import snmp_helper
from datetime import datetime, timedelta
import pickle
import pygal
import math


class IntData:

    def __init__(self, device, user):
        self.dev = device
        self.snmp_user = user
        self.timestamp = datetime.now()
        self.octets = self.get_octets()
        self.packets = self.get_packets()


    def get_octets(self):

        data = snmp_helper.snmp_get_oid_v3(self.dev, self.snmp_user, oid='1.3.6.1.2.1.2.2.1.10.5')
        try:
            in_octets = int(snmp_helper.snmp_extract(data))
        except ValueError as e:
            in_octets = 0
            print(e)

        data = snmp_helper.snmp_get_oid_v3(self.dev, self.snmp_user, oid='1.3.6.1.2.1.2.2.1.16.5')
        try:
            out_octets = int(snmp_helper.snmp_extract(data))
        except ValueError as e:
            out_octets = 0
            print(e)

        return in_octets, out_octets


    def get_packets(self):

        data = snmp_helper.snmp_get_oid_v3(self.dev, self.snmp_user, oid='1.3.6.1.2.1.2.2.1.11.5')
        try:
            in_packets = int(snmp_helper.snmp_extract(data))
        except ValueError as e:
            in_packets = 0
            print(e)

        data = snmp_helper.snmp_get_oid_v3(self.dev, self.snmp_user, oid='1.3.6.1.2.1.2.2.1.17.5')
        try:
            out_packets = int(snmp_helper.snmp_extract(data))
        except ValueError as e:
            out_packets = 0
            print(e)

        return in_packets, out_packets


def calc_diff(values1, values2):

    return math.fabs(values2[0]-values1[0]),math.fabs(values2[1]-values1[1])


def get_prev_data_from_file(file):

    data_objects = []

    try:
        prev_datasets = open(file, 'rb')
    except:
        return data_objects
    next = True
    # assume that at least one object is in the file
    prev_dataset = pickle.load(prev_datasets)
    data_objects.append(prev_dataset)
    while next:
        try:
            next_dataset = pickle.load(prev_datasets)
        except EOFError:
            next = False
        if 'next_dataset' in locals():
            data_objects.append(next_dataset)
    prev_datasets.close()
    return data_objects


def dump_dataset(dataset, file):
    
    try:
        datasets = open(file, 'ab')
        pickle.dump(dataset, datasets)
        datasets.close()
    except e:
        print("Problem opening file to write")
        print(e)


def gen_delta_octets(data_objects):

    deltas = []

    for i, int_data in enumerate(data_objects[:-1]):
        deltas.append(calc_diff(data_objects[i+1].octets, int_data.octets))

    return deltas

    
def gen_delta_packets(data_objects):

    deltas = []

    for i, int_data in enumerate(data_objects[:-1]):
        deltas.append(calc_diff(data_objects[i+1].packets, int_data.packets))

    return deltas


def gen_delta_timestamps(data_objects):

    deltas = []

    zero_value = data_objects[0].timestamp

    for i, int_data in enumerate(data_objects[:-1]):
        deltas.append(int_data.timestamp - zero_value)

    return deltas


def gen_svg(title, labels, dataset_in, dataset_out):

    chart = pygal.Line()
    chart.title = title
    chart.x_lables = labels
    chart.add("in", dataset_in)
    chart.add("out", dataset_out)
    chart.render_to_file(title +".svg")


def main():

    router1_ip = '184.105.247.70'
    router1_port = 161
    router1 = (router1_ip, router1_port)
    rtr1_file = 'rtr1.pkl'

    router2_ip = '184.105.247.71'
    router2_port = 161
    router2 = (router2_ip, router2_port)
    rtr2_file = 'rtr2.pkl'

    user = 'pysnmp'
    auth_key = 'galileo1'
    encrypt_key = 'galileo1'
    snmp_user = (user, auth_key, encrypt_key)

    datasets1 = get_prev_data_from_file(rtr1_file)
    datasets2 = get_prev_data_from_file(rtr2_file)

    new_data_rtr1 = IntData(router1, snmp_user)
    new_data_rtr2 = IntData(router2, snmp_user)

    dump_dataset(new_data_rtr1, rtr1_file)
    dump_dataset(new_data_rtr2, rtr2_file)

    datasets1.append(new_data_rtr1)
    datasets2.append(new_data_rtr2)

    if len(datasets1) > 1:
        octets1 = gen_delta_octets(datasets1)
        octets2 = gen_delta_octets(datasets2)
        packets1 = gen_delta_packets(datasets1)
        packets2 = gen_delta_packets(datasets2)
        labels1 = gen_delta_timestamps(datasets1)
        labels2 = gen_delta_timestamps(datasets2)
        zipoctets1 = list(zip(*octets1))
        zippackets1 = list(zip(*packets1))
        zipoctets2 = list(zip(*octets2))
        zippackets2 = list(zip(*packets2))
        gen_svg("Octets_Router1", labels1, list(zipoctets1[0]), list(zipoctets1[1]))
        gen_svg("Packets_Router2", labels2, list(zippackets2[0]), list(zippackets2[1]))  
    

if __name__ == "__main__":
    main()
