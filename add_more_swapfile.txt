sudo swapoff -a
sudo fallocate -l 16G /swapfile
#sudo dd if=/dev/zero of=/swapfile bs=16000 count=1048576
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
sudo nano /etc/fstab
	/swapfile swap swap defaults 0 0
sudo swapon --show

