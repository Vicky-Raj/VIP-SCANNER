import socket
import ipaddress

def get_input():
    start_ip = ipaddress.IPv4Address(input("Enter start IP: "))
    end_ip = ipaddress.IPv4Address(input("Enter end IP: "))
    if(start_ip > end_ip):
        raise Exception("Enter Valid IP Range")
    return(str(start_ip),str(end_ip))

def get_ports():
    ports = str(input("Enter ports(eg: 22,80 ): ")).split(',')
    ports = list(map(int, ports))
    return ports

def start_scan(start_ip, end_ip, ports):
    start_ip = ipaddress.IPv4Address(start_ip)
    end_ip = ipaddress.IPv4Address(end_ip)
    opened_ports = []
    while start_ip <= end_ip:
        for port in ports:
            sock = socket.socket()
            sock.settimeout(1)
            error = sock.connect_ex((str(start_ip),port))
            if error == 0:
                opened_ports.append(port)
        print(f'{str(start_ip)} - {opened_ports}')
        opened_ports.clear()
        start_ip = start_ip + 1

if __name__ == "__main__":
    start_ip,end_ip = get_input()
    ports = get_ports()
    start_scan(start_ip, end_ip, ports)   