import nmap

# 创建端口扫描器对象
nm = nmap.PortScanner()

# 扫描内网IP地址
nm.scan(hosts='172.20.10.0/24', arguments='-F')

# 遍历所有主机
for host in nm.all_hosts():
    print('----------------------------------------------------')
    print(f'Host : {host} ({nm[host].hostname()})')
    print(f'State : {nm[host].state()}')
    
    # 遍历主机上所有开放端口和服务
    for protocol in nm[host].all_protocols():
        print('----------')
        print(f'Protocol : {protocol}')
        
        lport = list(nm[host][protocol].keys())
        lport.sort()
        for port in lport:
            service = nm[host][protocol][port]['name']
            product = nm[host][protocol][port]['product']
            version = nm[host][protocol][port]['version']
            extrainfo = nm[host][protocol][port]['extrainfo']
            print(f'port : {port}\tservice : {service}\tproduct: {product}\tversion : {version}\textrainfo : {extrainfo}')