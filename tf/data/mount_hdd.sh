hdd=$(lsblk | grep 125G | awk '{print $1;}')
sudo mkfs -t xfs /dev/$hdd
sudo mkdir /data
sudo mount /dev/nvme1n1 /data
