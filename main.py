import sys
import scapy.all as scapy
from scapy.layers.inet import IP, TCP
from scapy.sendrecv import send


def main():
    args = sys.argv
    spoofed_ip = args[1]  # fake src ip
    dst_ip = args[2]  # victim
    src_port = args[3]
    dst_port = args[4]
    payload = "sorry"

    spoofed_packet = IP(src=spoofed_ip, dst=dst_ip) / TCP(sport=src_port, dport=dst_port) / payload
    send(spoofed_packet)


if __name__ == '__main__':
    main()
