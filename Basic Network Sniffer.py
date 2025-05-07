import socket

def sniff_packets():
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    s.bind(("localhost", 0))
    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    print("Sniffing packets...")
    while True:
        packet = s.recvfrom(65565)
        print(packet)

sniff_packets()
