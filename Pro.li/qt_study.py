from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
app = QApplication([])
window = QWidget()
window.setGeometry(100, 100, 200, 200)
window.setWindowTitle("My Window")
label = QLabel(window)
label.setText("Hello, World!")
label.move(60, 50)

button = QPushButton(window)
button.setText("Click Me!")
button.move(70, 80)
window.show()
app.exec_()
