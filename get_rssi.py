#!/usr/bin/python3
import json


"""

    Author: Ryan Draskovics
    Date: 6/22/2020

"""


save = {} ## All usr mac adress will be here

json_file = "logs.json" ## Output file
white = "white_list.json" ## Active usrs

def save_to_json(log):
    ## Write to json file
    with open(json_file, 'w') as f:
        json.dump(log, f, indent = 4)


def get_BT_DATA(line):
    with open(white, 'r') as f:
        wlist = json.load(f)
    if len(line) > 5:
        mac = line[2]
        try:
            rssi = int(line[7])
        except:
            rssi = int(line[6])
        if mac not in wlist['usr']:
            return
        else:
            print(f"{mac} - {rssi}")
            save[mac] = rssi
    else:
        return

def read_file(filename):
    get_file = open(filename, 'r')
    lines = get_file.readlines()
    for line in lines:
        line = line.split(' ')
        #print(line)
        get_BT_DATA(line)



if __name__ == "__main__":
	log_file = "rssi_log.txt"
	read_file(log_file)
	save_to_json(save)
