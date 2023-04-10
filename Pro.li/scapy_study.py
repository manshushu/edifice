# from scapy.all import * 
from scapy.all import * 
packet = IP(dst="www.google.com")/ICMP()
response = sr1(packet, timeout=2)
response.show()
