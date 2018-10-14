#!/usr/bin/env python

import subprocess
import optparse
import re           # importing Regex ( Regular Expression )


# Function to get user options and arguements

def get_arguements():
    parser=optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change Mac Address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New Mac Address")
    (options, arguements) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an Interface, use --help for more info")
    elif not options.new_mac:
        parser.error("[-] Please specify a New Mac Address using -m, use --help for more info")
    return options


# Function to change Mac Address

def change_mac(interface, new_mac):
    print("[+] Changing Mac Address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


# Function to get current Mac Address

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read Mac Address.")




options = get_arguements()


# Fetching Original Mac Address

current_mac = get_current_mac(options.interface)
print("Current Mac = " + str(current_mac))


#  Call to change Mac Address

change_mac(options.interface, options.new_mac)


# Fetching Changed Mac Address and Validating with User input

current_mac=get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] Mac Address was successfully changed to " + current_mac)
else:
    print("[-] Mac address did not get changed.")


# Program End

