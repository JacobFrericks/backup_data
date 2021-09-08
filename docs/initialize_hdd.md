## Initializing the larger HDD in EC2
On the instance, run the following

```
sudo mkfs -t xfs /dev/XXX
sudo mkdir /data
sudo mount /dev/XXX /data
cd /data
```