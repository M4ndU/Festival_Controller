import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MyWindow(QMainWindow):

    front_wid = None

    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)

        # MAIN WINDOW size
        self.setFixedSize(500,500)

        # CENTRAL WIDGET
        self.central_wid = QWidget()
        self.layout_for_wids = QStackedLayout()

        # BUTTON TO SWITCH BETWEEN WIDGETS
        self.btn_switch = QPushButton("Switch")
        self.btn_switch.clicked.connect(self.switch_wids)
        self.btn_switch.setFixedSize(70,50)
        self.btn_switch

        # BUTTON TO SWITCH BETWEEN WIDGETS
        self.btn_switch2 = QPushButton("Switch2")
        self.btn_switch2.clicked.connect(self.switch_wids)
        self.btn_switch2.setFixedSize(70,50)
        self.btn_switch2

        # BUTTON TO SWITCH BETWEEN WIDGETS
        self.btn2 = QPushButton("btn2")
        self.btn2.clicked.connect(self.pr)
        self.btn2.setFixedSize(70,50)
        self.btn2.move(0,50)

        # 2 WIDGETS
        self.wid1 = QWidget()
        self.wid1.setStyleSheet("""background: blue;""")
        self.wid1.setFixedSize(200,200)
        self.wid1.move(100, 100)
        self.wid2 = QWidget()
        self.wid2.setStyleSheet("""background: green;""")
        self.wid2.setFixedSize(200, 200)
        self.wid2.move(100, 100)
        self.wid1.show()

        # LAYOUT CONTAINER FOR WIDGETS AND BUTTON
        self.layout_for_wids.addWidget(self.btn_switch)
        self.layout_for_wids.addWidget(self.btn_switch2)
        self.layout_for_wids.addWidget(self.btn2)
        self.layout_for_wids.addWidget(self.wid1)
        self.layout_for_wids.addWidget(self.wid2)

        # ENTERING LAYOUT
        self.central_wid.setLayout(self.layout_for_wids)

        # CHOOSE YOUR CENTRAL WIDGET
        self.setCentralWidget(self.central_wid)

        # WHICH WIDGET IS ON THE FRONT
        self.front_wid = 1
        self.wid2.show()
        self.btn2.show()
    def switch_wids(self):

        # LOGIC TO SWITCH
        if self.front_wid == 1:
            self.setCentralWidget(self.central_wid).hide()
            self.front_wid = 2
        else:
            self.wid1.show()
            self.btn_switch.show()
            self.wid2.hide()
            self.btn_switch2.hide()
            self.front_wid = 1

    def pr(self):
            print("hi")



if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    app.setApplicationName('MyWindow')

    main = MyWindow()
    main.resize(222, 222)
    main.show()

    sys.exit(app.exec_())
