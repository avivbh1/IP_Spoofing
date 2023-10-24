from scapy.layers.inet import TCP, IP
from scapy.sendrecv import send


def handle_syn(packet):
    if packet.haslayer(TCP) and (packet[TCP].flags.S == 1 and packet[TCP].flags.A == 0):
        print(f"Received an SYN packet from {packet[IP].src}:{packet[TCP].sport}")

        syn_ack_segment = TCP(sport=packet[TCP].dport, dport=packet[TCP].sport, flags="SA", seq=1, ack=packet[TCP].seq + 1)
        response = IP(src=packet[IP].dst, dst=packet[IP].src) / syn_ack_segment
        send(response)


def handle_syn_ack(packet):
    if packet.haslayer(TCP) and (packet[TCP].flags.S == 0 and packet[TCP].flags.A == 1):
        print(f"Received a SYN_ACK packet from {packet[IP].src}:{packet[TCP].sport}")

        ack_segment = TCP(sport=packet[TCP].dport, dport=packet[TCP].sport, flags="A", ack=packet[TCP].seq + 1)
        response = IP(src=packet[IP].dst, dst=packet[IP].src) / ack_segment
        send(response)


def handle_ack(packet):
    if packet.haslayer(TCP) and (packet[TCP].flags.S == 0 and packet[TCP].flags.A == 1):
        print(f"Received an ACK packet from {packet[IP].src}:{packet[TCP].sport}")
