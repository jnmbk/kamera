#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under GPL v2
# Copyright 2008, Ugur Cetin
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.
#

def gspcaList():
    devices = []
    for line in open("drivers/gspca.txt").readlines()[1:]:
        devices.append(
                (
                    2, # driver_id
                    "%s:%s" % ( # device_id
                        line[line.find('0x') + 2:][:4],
                        line[line.find('0x', line.find('0x') + 1) + 2:][:4]
                        ),
                    line[line.rfind("/*") + 3:line.rfind("*/") - 1] # description
                    )
                )
    return devices

def ov511List():
    devices = []
    for line in open("drivers/ov511.txt").readlines()[1:]:
        if "VEND" in line:
            vendor = (line[line.rfind("0x") + 2:][:4], line[line.find('_') + 1:line.rfind('\t')])
        if "PROD" in line:
            devices.append((
                    8, # driver_id
                    "%s:%s" % ( # device_id
                        vendor[0],
                        line[line.rfind("0x") + 2:][:4]
                        ),
                    "%s %s" % ( # description
                        vendor[1],
                        line[line.find('_') + 1:line.rfind('\t')]
                        )
                    ))
    return devices

def linux_uvcList():
    devices = []
    info = [7, "0000:0000", "Generic camera"] # template
    for line in open("drivers/linux-uvc.txt").readlines()[1:]:
        if "/*" in line:
            info[2] = line[line.find("/*") + 3:line.rfind("*/") - 1] # description
        elif "Vendor" in line:
            info[1] = line[line.rfind("0x") + 2:][:4]
        elif "Product" in line:
            info[1] += ":%s" % line[line.rfind("0x") + 2:][:4]
        elif "driver_info" in line:
            devices.append(tuple(info))
    return devices

def pwcList():
    devices = []
    for line in open("drivers/pwc.txt").readlines()[1:]:
        if not '*' in line:
            line += " /* Generic Philips Webcam */"
        devices.append(
                (
                    1, # driver_id
                    "%s:%s" % ( # device_id
                        line[line.find('0x') + 2:][:4],
                        line[line.find('0x', line.find('0x') + 1) + 2:][:4]
                        ),
                    line[line.rfind("/*") + 3:line.rfind("*/") - 1] # description
                    )
                )
    return devices

def r5u870List():
    devices = []
    for line in open("drivers/r5u870.txt").readlines()[1:]:
        devices.append(
                (
                    5, # driver_id
                    line[:9], # device_id
                    line[10:-1] # description
                    )
                )
    return devices

def sn9c1xxList():
    devices = []
    for line in open("drivers/sn9c1xx.txt").readlines()[1:]:
        devices.append(
                (
                    4, # driver_id
                    "%s:%s" % ( # device_id
                        line[line.find('0x') + 2:][:4],
                        line[line.find('0x', line.find('0x') + 1) + 2:][:4]
                        ),
                    line[line.rfind('_') + 1:line.rfind(')')] # description
                    )
                )
    return devices

def syntekdriverList():
    devices = []
    vendors = []
    counter = -1
    for line in open("drivers/syntekdriver.txt").readlines()[1:]:
        if "VENDOR" in line:
            vendors.append(line[line.find("0x") + 2:][:4])
        elif "PRODUCT" in line:
            devices.append(
                    (
                        6, # driver_id
                        "%s:%s" % ( # device_id
                            vendors[counter],
                            line[line.find("0x") + 2:][:4],
                            ),
                        line[line.rfind("camera") + 7:line.rfind('*') - 1] # description
                        )
                    )
        else:
            counter += 1
    return devices

def zr364xxList():
    devices = []
    for line in open("drivers/zr364xx.txt").readlines()[1:]:
        devices.append(
                (
                    3, # driver_id
                    "%s:%s" % ( # device_id
                        line[line.find('0x') + 2:][:4],
                        line[line.find('0x', line.find('0x') + 1) + 2:][:4]
                        ),
                    line[line.rfind(" \"") + 2:line.rfind('"')] # description
                    )
                )
    return devices

drivers = []
for line in open("drivers.txt").readlines():
    drivers.append(tuple(line[line.find('|')+1:-1].split('|')))

devices = []
devices.extend(gspcaList())
devices.extend(linux_uvcList())
devices.extend(ov511List())
devices.extend(pwcList())
devices.extend(r5u870List())
devices.extend(sn9c1xxList())
devices.extend(syntekdriverList())
devices.extend(zr364xxList())

def filldb():
    from pysqlite2 import dbapi2 as sqlite
    import os
    os.unlink("webcams.db")
    con = sqlite.connect("webcams.db")
    cur = con.cursor()
    cur.execute("create table drivers(package_name, version, date, homepage)")
    cur.execute("create table devices(driver_id, usb_id, description)")
    cur.executemany("insert into drivers(package_name, version, date, homepage) values(?,?,?,?)", drivers)
    cur.executemany("insert into devices(driver_id, usb_id, description) values(?,?,?)", devices)
    con.commit()
    con.close()

if __name__ == "__main__":
    filldb()
