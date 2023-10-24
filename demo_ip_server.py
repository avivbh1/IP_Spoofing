from scapy.layers.inet import TCP, IP
from scapy.sendrecv import send, sniff
from datetime import datetime


def handle_syn(packet):
    print(f"[{datetime.now()}] Received a SYN packet from {packet[IP].src}:{packet[TCP].sport}")

    # Create and send a SYN-ACK response
    syn_ack_segment = TCP(sport=12345, dport=packet[TCP].sport, flags="SA", seq=1, ack=packet[TCP].seq + 1)
    response = IP(src=packet[IP].dst, dst=packet[IP].src) / syn_ack_segment
    send(response)
    print(f"[{datetime.now()}] Sent a SYN-ACK response to {packet[IP].src}:{packet[TCP].sport}")


def handle_ack(packet):
    if packet.haslayer(TCP) and packet[TCP].flags:
        print(f"Received an ACK packet from {packet[IP].src}:{packet[TCP].sport}")


def handle_three_way_handshake(packet):
    if packet[TCP].flags.S == 1:
        handle_syn(packet)
    if packet[TCP].flags.A == 1:
        handle_ack(packet)


def run_demo_server(port):
    sniff(filter=f"tcp and port {port}", prn=handle_three_way_handshake)
    print(f"demo server runs on PORT f{port}")
