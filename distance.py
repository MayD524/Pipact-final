#!/usr/bin/python3

"""

    Author: Ryan Draskovics
    Date: 6/22/2020

"""

import json
import datetime
import os



with open('host.txt', 'r') as f:
    temp_MAC = f.read()
    temp_MAC = temp_MAC.rsplit()
    host_MAC = temp_MAC[0]

## JSON files
main_list = "bk.json"
logs = "logs.json"
udict = "usr_dict.json"

## Set local var
users = []
needed_data = {'safe':True,"rssi": 0, "host":" ", "mac2":" "}
safe = True



def make_log(host_MAC):
    log_time = datetime.datetime.now()
    
    with open(main_list, 'r') as f:
        data = json.load(f)
    data[str(log_time)] = needed_data

    with open(main_list, 'w') as f:
        json.dump(data, f, indent = 4)

class estimate_distance_samsung: ## For samsung s10e

    def __init__(self,rssi, mac):
        self.rssi = rssi
        self.mac = mac
        self.safe = True

    def is_safe(self):## checking if dev 2 is safe enough
        if self.safe:
            return True
        else:
            return False

    def get_distance(self):
        is_between = self.rssi <= 85
        if is_between:
            print(f'{self.mac} is too close')
            self.safe = False
        else:
            print('safe')

        SAFE = self.is_safe() 
        return SAFE
    
class estimate_distance_raspberrypi:

    def __init__(self,rssi, mac):
        self.rssi = rssi
        self.mac = mac
        self.safe = True
    
    def is_safe(self): ## checking if dev 2 is safe enough
        if self.safe:
            return True    
        else:
            return False

    def get_distance(self):
        is_between = self.rssi <= 85
        if is_between:
            print(f'{self.mac} is too close')
            self.safe = False
        else:
            print('safe')

        SAFE = self.is_safe() 
        return SAFE


def get_rssi(filename, mac):
    with open(logs, 'r') as f:
        data = json.load(f)
    rssi = int(data.get(mac)) * -1

    return rssi

def set_class_raspberrypi(rssi, mac):
    rpi_estd = estimate_distance_raspberrypi(rssi, mac)
    safe = rpi_estd.get_distance()
    return safe

def set_class_samsung(rssi, mac):
    sam_estd = estimate_distance_samsung(rssi, mac)
    safe = sam_estd.get_distance()
    return safe

def get_host(HOST):
    pass

if __name__ == "__main__":
    with open ("usr_dict.json", 'r') as f:
        data = json.load(f)
    with open("logs.json", 'r') as f:
        local_users = json.load(f)

    for user in local_users:
        mac = user
        rssi = get_rssi(logs, mac)
        if user in data['samsung']:
       	    is_safe = set_class_samsung(rssi, mac)

        elif user in data['raspberry pi']:
            is_safe = set_class_raspberrypi(rssi, mac)

        if not is_safe:
            needed_data['safe'] = False
            needed_data["host"] = host_MAC
            needed_data["mac2"] = mac
            needed_data['rssi'] = rssi
            make_log(host_MAC)

