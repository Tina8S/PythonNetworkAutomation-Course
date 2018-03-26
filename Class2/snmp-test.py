#!/usr/bin/env python

# Create a script that connects to both routers (pynet-rtr1
# and pynet-rtr2) and prints out both the MIB2 sysName and
# sysDescr.

import snmp_helper

def main():
    COMMUNITY_STRING = "galileo"
    RTR1 = '184.105.247.70'
    RTR2 = '184.105.247.71'
    SNMP_PORT = 161

    device1 = (RTR1, COMMUNITY_STRING, SNMP_PORT)
    device2 = (RTR2, COMMUNITY_STRING, SNMP_PORT)

    sysName_oid = '1.3.6.1.2.1.1.5.0'
    sysDescr_oid = '1.3.6.1.2.1.1.1.0'

    sysName_rtr1 = snmp_helper.snmp_get_oid(device1, oid=sysName_oid)
    sysDescr_rtr1 = snmp_helper.snmp_get_oid(device1, oid=sysDescr_oid)

    print(snmp_helper.snmp_extract(sysName_rtr1))
    print(snmp_helper.snmp_extract(sysDescr_rtr1))

    sysName_rtr2 = snmp_helper.snmp_get_oid(device2, oid=sysName_oid)
    sysDescr_rtr2 = snmp_helper.snmp_get_oid(device2, oid=sysDescr_oid)

    print(snmp_helper.snmp_extract(sysName_rtr2))
    print(snmp_helper.snmp_extract(sysDescr_rtr2))


if __name__ == "__main__":
    main()
