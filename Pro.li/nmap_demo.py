import nmap

# 创建nmap扫描器对象
nm = nmap.PortScanner()

# 执行主机扫描并获取结果
nm.scan(hosts='192.168.0.0/24', arguments='-sn')
hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]

# 显示结果
print("Available devices in the network:")
for host, status in hosts_list:
    print(f'{host} ({status})')