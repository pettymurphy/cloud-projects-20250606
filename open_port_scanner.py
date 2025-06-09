import socket
import threading

# List of IP addresses across subnets to scan
target_ips = [
    '10.0.1.10',
    '10.0.2.20',
    '10.0.3.30'
]

# List of common ports to scan
common_ports = [22, 80, 443, 3389]

# This function checks if a port is open
def scan_port(ip, port):
    try:
        # Create a new socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set timeout so it doesn't hang forever
        sock.settimeout(1)
        # Try to connect to the given IP and port
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"[+] {ip}:{port} is OPEN")
        sock.close()
    except Exception as e:
        print(f"[!] Error scanning {ip}:{port} - {str(e)}")

# Loop through each IP and port and start a scan
for ip in target_ips:
    for port in common_ports:
        # Use threading to scan ports in parallel
        thread = threading.Thread(target=scan_port, args=(ip, port))
        thread.start()
