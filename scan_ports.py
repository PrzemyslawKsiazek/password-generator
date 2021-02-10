#Software for scanning open ports in the network
import socket
import ipaddress

def is_port_open(ip: str, port: int) -> bool:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    result = sock.connect_ex((ip, port))
    sock.close()
    return result == 0

ports = [
    53,
    67,
    68,
    80,
    443
]

for ip in ipaddress.ip_network('10.0.0.0/24'):
    print(f"I'm checking address ip {ip}")

    for port in ports:
        if is_port_open(str(ip), port):
            print(f"The address IP: {ip} has an open port: {port}")