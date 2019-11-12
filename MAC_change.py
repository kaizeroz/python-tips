#!usr/bin/env python
    
 import subprocess
 import optparse
 import re

# ifconfig wlan0 down
# ifconfig wlan0 hw ether 00:11:22:33:44:55
# ifconfig wlan0 up

interface = ''
new_mac = ''

def get_current_mac(interface):
	ifconfig_result = subprocess.check_output(["ifconfig", interface])
	regex_mac_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
	if regex_mac_search_result:
	    return regex_mac_search_result.group(0)
	else:
	    print("[-] Error: could not read MAC address.")

current_mac = get_current_mac(interface)
print("The current MAC Address = " + str(current_mac))

change_mac(interface, new_mac)

current_mac = get_current_mac(.interface)
if current_mac == new_mac:
    print("[+] The MAC address successfully changed to " + current_mac)
else:
    print("[-] Error: the MAC address did not get changed. Contact tech support for help.")