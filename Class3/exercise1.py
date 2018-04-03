#! /usr/bin/env python

import snmp_helper
import pickle
import email_helper

def get_save_dates(device, user):


    runLastChanged = '1.3.6.1.4.1.9.9.43.1.1.1.0'
    runLastSaved = '1.3.6.1.4.1.9.9.43.1.1.2.0'
    startLastChanged = '1.3.6.1.4.1.9.9.43.1.1.3.0'

    snmp_data = snmp_helper.snmp_get_oid_v3(device, user, runLastChanged)
    rlc_value = snmp_helper.snmp_extract(snmp_data)

    snmp_data = snmp_helper.snmp_get_oid_v3(device, user, runLastSaved)
    rls_value = snmp_helper.snmp_extract(snmp_data)

    snmp_data = snmp_helper.snmp_get_oid_v3(device, user, startLastChanged)
    slc_value = snmp_helper.snmp_extract(snmp_data)

    return rlc_value, rls_value, slc_value

def get_prev_date_from_file(file):

    try:
        prev_dates = open(file, 'rb')
    except:
        return None
    next = True
    # assume that at least one date is in file
    prev_date = pickle.load(prev_dates)
    while next:
        try:
            next_date = pickle.load(prev_dates)
        except EOFError:
                next = False
    if 'next_date' in locals():
        prev_date = next_date
    prev_dates.close()
    return prev_date


def compare_dates(date_new, date_old):

    delta_rlc = int(date_new[0]) - int(date_old[0])
    delta_rls = int(date_new[1]) - int(date_old[1])
    delta_slc = int(date_new[2]) - int(date_old[2])

    return delta_rlc, delta_rls, delta_slc


def write_date(date, file):

    try:
        dates = open(file, 'wb')
        pickle.dump(date, dates)
    except e:
        print("Problem opening file to write")
        print(e)


def write_email(device_name, changes):
    recpt = 'tina.strauf@tu-braunschweig.de'
    sender = 'tstrauf@tu-braunschweig.de'
    subject = 'Changes to router ' + device_name

    message_body = 'There were changes made to ' + device_name + '.\n\n'

    if changes[0]:
        message_body += 'The running configuration was changed.\n'

    if changes[1]:
        message_body += 'The running configurtion was saved.\n'

    if changes[2]:
        message_body += 'The startup configuration was changed.\n'

    email_helper.send_mail(recpt, subject, message_body, sender)


def main():

# 1. Get Data from Device

    router1_ip = '184.105.247.70'
    router1_port = 161
    router1 = (router1_ip, router1_port)

    router2_ip = '184.105.247.71'
    router2_port = 161
    router2 = (router2_ip, router2_port)

    user = 'pysnmp'
    auth_key = 'galileo1'
    encrypt_key = 'galileo1'
    snmp_user = (user, auth_key, encrypt_key)

    dates_router1 = get_save_dates(router1, snmp_user)
    dates_router2 = get_save_dates(router2, snmp_user)
    

# 2. See if there was a change and/or store data for future comparison

    prev_date_rtr1 = get_prev_date_from_file('dates_rtr1.pkl')
    prev_date_rtr2 = get_prev_date_from_file('dates_rtr2.pkl')

    change_rtr1 = False
    change_rtr2 = False

    if prev_date_rtr1:
        change_rtr1 = compare_dates(dates_router1, prev_date_rtr1)
    write_date(dates_router1, 'dates_rtr1.pkl')

    if prev_date_rtr2:
        change_rtr2 = compare_dates(dates_router2, prev_date_rtr2) 
    write_date(dates_router2, 'dates_rtr2.pkl')

# 3. Potentially wirte e-mail
    
    if change_rtr1:
        if change_rtr1[0] or change_rtr1[2]:
            print("Writing an e-mail for router 1...")
            write_email("Changes on router 1", change_rtr1)

    if change_rtr2:
        if change_rtr2[0] or change_rtr2[2]:
            print("Writing an e-mail for router 2...")
            write_email("Changes on router 2", change_rtr2)


if __name__ == "__main__":
    main()
