import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # create vertical layout for button containers
        vbox = QVBoxLayout()

        # create horizontal layout for each row of buttons
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()

        # create buttons and add them to horizontal layouts
        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")
        button3 = QPushButton("Button 3")
        button4 = QPushButton("Button 4")
        button5 = QPushButton("Button 5")

        hbox1.addWidget(button1)
        hbox1.addWidget(button2)
        hbox1.addWidget(button3)

        hbox2.addWidget(button4)
        hbox2.addWidget(button5)

        # add the horizontal layouts to the vertical layout
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)

        # set the layout of the main window
        self.setLayout(vbox)

        # set window properties
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('My Window')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())