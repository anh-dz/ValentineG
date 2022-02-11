#Lưu ý: File nit.jpeg phải để cùng thư mục chạy file main.py

from PyQt6 import QtCore, QtGui, QtWidgets

#Chỉnh sửa nội dung tại đây
FORMNAME = "Hê hê"
TITLE = "Valentine năm nay mình quay lại nhé"
SMALLTITLE = "Tắt đi là đồng ý nha 😘 "
NOO = "Đéo"
YESS = "Ô kê anh yêu"

NIT = "Có cái nịt nhá em"
NITPICTURE = "nit.jpeg" #Xoá đi là không mở được ảnh

#Main Code - Không chỉnh sửa
class AnotherWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.resize(400, 300)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(80, 100, 241, 81))
        self.label.setStyleSheet("font-size: 30pt; font: bold;")
        self.label.setObjectName("label")
        self.label.setText(NIT)
        self.setWindowFlags(QtCore.Qt.WindowType.WindowStaysOnTopHint)

class MainApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.check_place = 1
        self.setObjectName('Mink')
        self.resize(717, 399)
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(270, 120, 320, 51))
        self.label_2.setStyleSheet("font-size: 20pt;\n"
"font: italic;")
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 200, 281, 131))
        self.pushButton_2.setStyleSheet("font-size: 30pt;\n"
"font: bold;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(50, 200, 281, 131))
        self.pushButton.setStyleSheet("font-size: 30pt;\n"
"font: bold;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.happy)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(100, 70, 600, 51))
        self.label.setStyleSheet("font-size: 30pt;\n"
"font: bold;")
        self.label.setObjectName("label")

        self.pushButton_2.setAttribute(QtCore.Qt.WidgetAttribute.WA_Hover)
        self.pushButton_2.installEventFilter(self)

        self.setWindowTitle(FORMNAME)
        self.label.setText(TITLE)
        self.label_2.setText(SMALLTITLE)
        self.pushButton_2.setText(NOO)
        self.pushButton.setText(YESS)
    
    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.Type.HoverEnter:
            if self.check_place == 1:
                self.pushButton_2.setGeometry(QtCore.QRect(50, 200, 281, 131))
                self.pushButton.setGeometry(QtCore.QRect(400, 200, 281, 131))
                self.check_place = 0
            else:
                self.pushButton_2.setGeometry(QtCore.QRect(400, 200, 281, 131))
                self.pushButton.setGeometry(QtCore.QRect(50, 200, 281, 131))
                self.check_place = 1
        return super().eventFilter(obj, event)
    
    def happy(self):
        if os.name=='posix':
            os.system(f'open {os.path.dirname(__file__)}/{NITPICTURE}')
        else:
            os.system(f'start {os.path.dirname(__file__)}/{NITPICTURE}')
        kk = AnotherWindow()
        kk.show()
        kk.exec()

if __name__ == "__main__":
    import sys, os, time
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())