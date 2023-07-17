# 0x13. Firewall
---

This project will deal with configuring ufw to your web server. (UFW is Uncomplicated Fire Wall)

### Some handy commands to use

```
To see a working portal - telnet IP Port (press ctrl + c to exit)
sudo ufw allow [port] - w
sudo ufw enable 

We are going to set a few rules for our server using UFW.
- Block all the incoming trafffic
- Enable all the outgoing traffic
- Enable the following ports:
* 22 (SSH)
* 443 (HTTPS SSL)
* 80 (HTTP)

****Enjoy****
