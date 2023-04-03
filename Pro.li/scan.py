import socket
import nmap
import ipaddress
import ping3

# 扫描目标主机列表
target_hosts = ["192.168.0.1", "192.168.0.2", "192.168.0.3"]

# 定义扫描函数
def scan_host(host):
    # 创建socket对象，设置超时时间
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    try:
        # 尝试连接指定端口
        result = sock.connect_ex((host, 135))
        if result == 0:
            print(f"[+] {host}:135/tcp open")
    except:
        pass
    sock.close()

# 端口扫描
print("[*] 开始端口扫描")
for host in target_hosts:
    scan_host(host)

# 服务探测
print("\n[*] 开始服务探测")
nm = nmap.PortScanner()
for host in target_hosts:
    nm.scan(hosts=host, arguments="-A -Pn")
    for hostname in nm.all_hosts():
        print(f"[*] {hostname}({nm[hostname].hostname()})")
        for proto in nm[hostname].all_protocols():
            print(f"协议：{proto}")
            lport = nm[hostname][proto].keys()
            for port in lport:
                print(f"端口：{port}； 服务：{nm[hostname][proto][port]['name']}")

# IP地址处理
print("\n[*] IP地址处理")
net = ipaddress.ip_network("192.168.0.0/24")
for ip in net.hosts():
    if ping3.ping(str(ip), timeout=1) is not None:
        print(f"{ip} is alive")