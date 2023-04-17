from scapy.all import ARP, Ether, srp
# import nmap
# 定义要扫描的IP地址段
target_ip = "192.168.0.0/24"

# 创建ARP数据包
arp = ARP(pdst=target_ip)

# 创建以太网数据包
ether = Ether(dst="ff:ff:ff:ff:ff:ff")

# 合并ARP和以太网数据包
packet = ether / arp

# 发送数据包并获取响应
result = srp(packet, timeout=3, verbose=0)[0]

# 处理响应数据
clients = []
for sent, received in result:
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})

# 显示结果
print("Available devices in the network:")
print("IP" + " "*18+"MAC")
for client in clients:
    print("{:16}    {}".format(client['ip'], client['mac']))