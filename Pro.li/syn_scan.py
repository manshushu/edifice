import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
from scapy.layers.inet import IP,TCP

def syn_scan(target_ip, ports, timeout):
    print("Starting Syn Scan...")
    open_ports = []

    # Send SYN packets to each port and wait for response
    for port in ports:
        src_port = RandShort()
        dst_port = int(port)
        syn_packet = IP(dst=target_ip) / TCP(sport=src_port, dport=dst_port, flags="S")
        response = sr1(syn_packet, timeout=timeout, verbose=0)

        # Check if a SYN/ACK packet was received
        if response is not None and response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
            print(f"Port {port} is open.")
            open_ports.append(port)

            # Send a RST packet to close the connection
            rst_packet = IP(dst=target_ip) / TCP(sport=src_port, dport=dst_port, flags="R")
            send(rst_packet, verbose=0)

        # Otherwise, check if a RST packet was received
        elif response is not None and response.haslayer(TCP) and response.getlayer(TCP).flags == 0x14:
            print(f"Port {port} is closed.")

    print("Syn Scan complete.")
    return open_ports


# Example usage:
target_ip = "192.168.0.8"
ports = [22, 80, 443, 3389]
timeout = 0.5

open_ports = syn_scan(target_ip, ports, timeout)
print("Open ports:", open_ports)

# 在这个例子中，我们使用Scapy库来构造和发送IP和TCP数据包，并侦听响应。 对于每个指定的端口，我们发送一个标志为“S”的TCP数据包（即SYN包），然后等待响应。 如果收到的响应是一个标志为“SA”的TCP数据包（即SYN/ACK包），则说明该端口是打开状态；如果收到的响应是一个标志为“RA”的TCP数据包（即RST/ACK包），则说明该端口是关闭状态。 在任何情况下，我们都会通过发送带有RST标志的TCP数据包来关闭连接。 最后，我们将所有打开的端口返回给调用者。