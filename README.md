# Network-and-Port-Scanning-with-Alerts
This project demonstrates how to perform network and port scanning and set up alerts for open ports using Python. The script discovers devices on a network, scans for open ports on these devices, and can trigger alerts if certain conditions are met.

Features
Network Scanning: Discovers devices on a specified IP range.
Port Scanning: Checks which ports are open on each discovered device.
Alerts: (Optional) Setup to notify or log when certain ports are detected as open.

Prerequisites
Before running the script, ensure you have the following:

Python: This script is compatible with Python 3.x.
Libraries: scapy for network scanning and socket for port scanning.
Install the required Python library:

Copy code
sudo pip install scapy

1. Network Scanning
Function: scan_network(ip_range)

Description: Scans the specified IP range using ARP requests to discover devices.
Parameters:
ip_range: The IP range to scan (e.g., '192.168.122.1/24').
Returns: A list of devices with their IP and MAC addresses.
2. Port Scanning
Function: scan_ports(ip, ports)

Description: Scans the specified ports on a given IP address to check if they are open.
Parameters:
ip: The IP address to scan.
ports: A list of ports to scan.
Returns: A list of open ports.
3. Print Results
Function: print_results(devices)

Description: Prints out the IP addresses, MAC addresses, and open ports of the discovered devices.
Parameters:
devices: A list of dictionaries with ip and mac keys.
Alerts
(Optional) You can integrate alerts by adding functionality to notify when specific ports are detected. For example:

Email Alerts: Use an email library to send notifications.
Logging: Write alerts to a log file.
System Notifications: Use system-specific methods to show notifications.
