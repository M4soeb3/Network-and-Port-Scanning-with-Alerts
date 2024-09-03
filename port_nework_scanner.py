import socket
from scapy.all import ARP, Ether, srp

def scan_network(ip_range):
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp
    result = srp(packet, timeout=3, verbose=0)[0]

    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})
    
    return devices

def scan_ports(ip, ports):
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

def print_results(devices):
    print("IP Address\t\tMAC Address\t\tOpen Ports")
    print("-----------------------------------------")
    for device in devices:
        open_ports = scan_ports(device['ip'], range(1, 1025))  # Scanning ports 1-1024
        ports = ', '.join(map(str, open_ports)) if open_ports else 'None'
        print(f"{device['ip']}\t\t{device['mac']}\t\t{ports}")

# Define IP range
ip_range = '192.168.122.1/24'
devices = scan_network(ip_range)
print_results(devices)

