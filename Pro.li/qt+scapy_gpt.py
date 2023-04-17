from PyQt5.QtWidgets import QApplication, QMainWindow, QPlainTextEdit, QAction
from scapy.all import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Create the main widget
        self.central_widget = QPlainTextEdit()
        self.setCentralWidget(self.central_widget)
        
        # Add a menu bar with a "Capture Packets" action
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')
        capture_action = QAction('Capture Packets', self)
        capture_action.triggered.connect(self.capture_packets)
        file_menu.addAction(capture_action)
        
        # Start the event loop
        self.show()

    def capture_packets(self):
        # Use Scapy to capture packets
        packets = sniff(count=10)

        # Display packet information in the main widget
        for packet in packets:
            self.central_widget.appendPlainText(repr(packet))

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec_()