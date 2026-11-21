"""port_check.py - checks whether TCP ports are open on a host.

Usage:  python port_check.py [host] [port1 port2 ...]
Example: python port_check.py 127.0.0.1 22 80 443

Only scan machines you own or have permission to test.
"""
import socket
import sys


def is_open(host, port, timeout=1.0):
    """Return True if a TCP connection to host:port succeeds."""
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except (OSError, socket.timeout):
        return False


def main():
    host = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
    ports = [int(p) for p in sys.argv[2:]] or [21, 22, 80, 443, 3306, 8080]
    print(f"Checking {host} ...")
    for port in ports:
        state = "OPEN" if is_open(host, port) else "closed"
        print(f"  port {port:<5} {state}")


if __name__ == "__main__":
    main()
