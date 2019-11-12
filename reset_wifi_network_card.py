import os

# ifconfig wlan0 down
# ifconfig wlan0 hw ether 00:11:22:33:44:55
# ifconfig wlan0 up

list_interface = os.listdir('/sys/class/net/')

print("List interface network:")
for i in range(0, len(list_interface)):
	print("   {}. {}".format(str(i+1), str(list_interface[i])))
option = int(input("Choice: "))
print("[] Reseting network {}".format(list_interface[option-1]))
os.system("sudo ifconfig {} down".format(str(list_interface[option-1])))
os.system("sudo ifconfig {} up".format(str(list_interface[option-1])))
print("[*] Reseted network")
