import sys
from scapy.all import *
from scapy.layers.inet import IP, ICMP
from scapy.sendrecv import sr1
from scapy.utils import wrpcap
from fpdf import FPDF

def send_ping():
    # 构造ping数据包
    packet = IP(dst='www.baidu.com')/ICMP()

    # 发送数据包并等待回复
    reply_packet = sr1(packet, timeout=2)

    # 输出回复信息
    if reply_packet:
        print(reply_packet.summary())
        
        # 保存流量数据包
        wrpcap('ping.pcap', packet / reply_packet)

        # 生成PDF报告
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(40, 10, 'Ping Report')
        pdf.ln()
        pdf.set_font('Arial', '', 12)
        pdf.multi_cell(0, 10, packet.show(dump=True))
        pdf.multi_cell(0, 10, reply_packet.show(dump=True))
        pdf.output('ping_report.pdf')
    else:
        print("No response received")

if __name__ == '__main__':
    send_ping()