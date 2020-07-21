#!/usr/bin/python3
import json
import random
import os

"""

    Author: Ryan Draskovics
    Date: 6/22/2020

"""


## declairing user files
usr_file = "users.json"
legend = "usr_dict.json"
usr_list = []



class add_usr:

    def __init__(self, usr, mac, dev):
        self.usr = usr
        self.mac = mac
        self.dev = dev

    def generate_usernumber(self):
        with open(usr_file, 'r') as f:
            dicto = json.load(f)

        while True:
            self.user_number = random.randint(0, 100000000000) ## generating a unique user number

            if self.user_number not in dicto.keys():
                break

    def make_user(self):
        with open(usr_file, 'r') as f: ## Makes a user log with a random number
            jsdata = json.load(f)
        with open(legend, 'r') as f: ## makes log with id and mac
            data = json.load(f)

    
        usr_list.append(self.usr)
        usr_list.append(self.mac)
        usr_list.append(self.dev)

        jsdata[self.user_number] = usr_list
        if self.dev in data.keys() and self.mac not in data[self.dev]:
            data[self.dev].append(self.mac)
        
        with open(usr_file, 'w') as f:
            json.dump(jsdata, f)
        with open(legend, 'w') as f:
            json.dump(data,f)



    def check_MAC(self):

        if len(self.mac) == 17:
            return True ## checking for a MAC address

        else:
            print('Incorrect mac address')
            return False
        
        





def get_usr():
    ## getting basic user details
    usr = input("Username: ")
    mac = os.system("hcitool dev | cut -sf3")
    dev = input("Divice name: ")

    ## Starting the check steps
    nu = add_usr(usr, mac, dev)
    nu.generate_usernumber()

    ## Making the user 
    if nu.check_MAC():
        nu.make_user()


## File starts here
if __name__ == "__main__":
    get_usr()
