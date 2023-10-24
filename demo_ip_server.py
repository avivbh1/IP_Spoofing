from scapy.layers.inet import TCP, IP
from scapy.sendrecv import sniff
from datetime import datetime
from ddos_manipulation.three_way_handshake_handlers import handle_syn, handle_ack


def handle_three_way_handshake_server(packet):
    if packet[TCP].flags.S == 1 and packet[TCP].flags.A == 0:
        print(f"[{datetime.now()}] RECEIVED a SYN packet from {packet[IP].src}:{packet[TCP].sport}")
        handle_syn(packet)
        print(f"[{datetime.now()}] SENT a SYN-ACK response to {packet[IP].src}:{packet[TCP].sport}")

    if packet[TCP].flags.S == 0 and packet[TCP].flags.A == 1:
        print(f"[{datetime.now()}] RECEIVED an ACK packet from {packet[IP].src}:{packet[TCP].sport}")
        handle_ack(packet)


def run_demo_server(port):
    sniff(filter=f"tcp and port {port}", prn=handle_three_way_handshake_server)
    print(f"demo server runs on PORT f{port}")
