import sys
from PyQt5.QtCore import QTimer, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction
from scapy.all import *

class PacketSniffer(QThread):
    packetReceived = pyqtSignal(object)

    def __init__(self):
        super().__init__()
        self.stopRequested = False

    def run(self):
        while not self.stopRequested:
            sniff(prn=lambda x: self.packetReceived.emit(str(x)), count=1)

    def stop(self):
        self.stopRequested = True

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建文本编辑器
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        # 添加菜单栏
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')

        # 添加“退出”菜单项
        exitAct = QAction('Exit', self)
        exitAct.triggered.connect(self.close)
        fileMenu.addAction(exitAct)

        # 创建数据包嗅探器并启动线程
        self.sniffer = PacketSniffer()
        self.sniffer.packetReceived.connect(lambda x: textEdit.append(x))
        self.sniffer.start()

        # 设置窗口属性
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Packet Sniffer')
        self.show()

    def closeEvent(self, event):
        self.sniffer.stop()
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())
