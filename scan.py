"""
scan.py

this handles the scaning of the network.
"""


import netifaces as net
import socket


RANGES = {"172": ((172, 16, 0, 0), (172, 31, 255, 255)),
          "192": ((192, 168, 0, 0), (192, 168, 255, 255))}


def get_ip():
    """
    acuiers the hosts IP address (not starting with '127.etc').
    """
    for interface in net.interfaces():
        addresses = net.ifaddresses(interface)
        for key in addresses.keys():
            info = addresses.get(key)[0]
            try:
                if int(info.get('addr')[0:3]) != 127:
                    return info
            except ValueError:
                pass
    return "ERROR"


def get_str_ip(list_ip):
    """
    turns a list of 4 integers into IP address format.
    """
    return ".".join([str(_) for _ in list_ip])


def reverse_dns(ip):
    """
    gets the host name of the machine at ip.
    """
    try:
        reversed_dns = socket.gethostbyaddr(ip)
        hostname = reversed_dns[0]
    except socket.herror:
        hostname = None
    return hostname


def scan(ip, database):
    """
    scans the network for hosts
    """
    lower, upper = RANGES.get(ip[0:3])
    # print(lower)
    # print(upper)
    net_1 = ip[0:3]
    up_machines = []
    last_host_1 = 0
    for net_2 in range(lower[1], upper[1] + 1):
        for host_1 in range(lower[2], upper[2] + 1):
            # print(host_1)
            for host_2 in range(lower[3], upper[3]):
                target_ip = f"{net_1}.{net_2}.{host_1}.{host_2}"
                if target_ip not in [get_str_ip(lower), get_str_ip(upper)]:
                    host_name = reverse_dns(target_ip)
                    machine = {"ip": target_ip, "name": host_name}
                    # if host_name:
                    #     print(f">   {host_name} - {target_ip}")
                    if (host_name is not None) and (machine not in database):
                        up_machines.append(machine)
                        last_host_1 = host_1
            if host_1 - last_host_1 > 3:
                break
    return up_machines


def get_hosts(database=()):
    """
    returns a list of all responding hosts not already in the database.
    """
    network_info = get_ip()
    ip = network_info.get("addr")
    # netmask = network_info.get("netmask")
    # broadcast = network_info.get("boardcast")
    hosts = scan(ip, database)
    return hosts


if __name__ == "__main__":
    get_hosts()
