# using scapy and qt to build a tool for understanding the 
# network traffic
# 
#

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from scapy.all import *
from PyQt5.QtWidgets import QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Network Traffic Analyzer")

        self.show()
        def __init__(self):
            super().__init__()
    
            self.setWindowTitle("Network Traffic Analyzer")
    
            self.setCentralWidget(QWidget())
            self.show()
            #self.show()
        


app = QApplication(sys.argv)

window = MainWindow()

app.exec_()

sys.exit(0)

#
