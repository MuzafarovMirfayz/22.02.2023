from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QHBoxLayout, QVBoxLayout, QMessageBox
import random
class window(QWidget):
    def tekshir(self):
        if self.btn1.text()=="1" and self.btn2.text()=="2"and self.btn3.text()=="3" and self.btn4.text()=="4" and self.btn5.text()=="5":
            if self.btn6.text()=="6" and self.btn7.text()=="7" and self.btn8.text()=="8" and self.btn9.text()=="9" and self.btn10.text()=="10":
                if self.btn11.text()=="11" and self.btn12.text()=="12" and self.btn13.text()=="13" and self.btn14.text()=="14" and self.btn15.text()=="15" and self.btn16.text()=="":
                            self.msg.setIcon(self.msg.Information)
                            self.msg.setText("Siz g'alaba qozondingiz")
                            self.msg.buttonClicked.connect(self.reset1)
                            self.msg.exec_()
    def start1(self):
        self.Reset.show()
        self.b = ["1", '2', '3', '4','5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', ""]
        for i in range(len(self.lst)):
            self.a = random.choice(self.b)
            self.b.pop(self.b.index(self.a))
            self.lst[i].setText(self.a)
        for i in self.lst:
            i.setEnabled(True)
        self.exit.hide()
        self.Start.hide()
    def reset1(self):
        self.btn1.setText('1')
        self.btn2.setText('2')
        self.btn3.setText('3')
        self.btn4.setText('4')
        self.btn5.setText('5')
        self.btn6.setText('6')
        self.btn7.setText('7')
        self.btn8.setText('8')
        self.btn9.setText('9')
        self.btn10.setText('10')
        self.btn11.setText('11')
        self.btn12.setText('12')
        self.btn13.setText('13')
        self.btn14.setText('14')
        self.btn15.setText('15')
        self.btn16.setText('')
        for i in self.lst:
            i.setEnabled(False)
        self.Start.show()
        self.Reset.hide()
        self.exit.show()
    def fun1(self):
        if self.btn1.text() != "":
            if self.btn2.text() == "":
                self.btn2.setText(self.btn1.text())
                self.btn1.setText("")
            elif self.btn5.text() == "":
                self.btn5.setText(self.btn1.text())
                self.btn1.setText("")
            self.tekshir()
    def fun2(self):
        if self.btn2.text() != "":
            if self.btn3.text() == "":
                self.btn3.setText(self.btn2.text())
                self.btn2.setText("")
            elif self.btn6.text() == "":
                self.btn6.setText(self.btn2.text())
                self.btn2.setText("")
            elif self.btn1.text()=="":
                self.btn1.setText(self.btn2.text())
                self.btn2.setText("") 
            self.tekshir()
    def fun3(self):
        if self.btn3.text() != "":
            if self.btn2.text() == "":
                self.btn2.setText(self.btn3.text())
                self.btn3.setText("")
            elif self.btn4.text() == "":
                self.btn4.setText(self.btn3.text())
                self.btn3.setText("")
            elif self.btn7.text()=="":
                self.btn7.setText(self.btn3.text())
                self.btn3.setText("")
            self.tekshir()
    def fun4(self):
        if self.btn4.text() != "":
            if self.btn3.text() == "":
                self.btn3.setText(self.btn4.text())
                self.btn4.setText("")
            elif self.btn8.text() == "":
                self.btn8.setText(self.btn4.text())
                self.btn4.setText("")
            self.tekshir()
    def fun5(self):
        if self.btn5.text() != "":
            if self.btn1.text() == "":
                self.btn1.setText(self.btn5.text())
                self.btn5.setText("")
            elif self.btn6.text() == "":
                self.btn6.setText(self.btn5.text())
                self.btn5.setText("")
            elif self.btn9.text()=="":
                self.btn9.setText(self.btn5.text())
                self.btn5.setText("")
            self.tekshir()
    def fun6(self):
        if self.btn6.text() != "":
            if self.btn2.text() == "":
                self.btn2.setText(self.btn6.text())
                self.btn6.setText("")
            elif self.btn5.text() == "":
                self.btn5.setText(self.btn6.text())
                self.btn6.setText("")
            elif self.btn10.text()=="":
                self.btn10.setText(self.btn6.text())
                self.btn6.setText("")
            elif self.btn7.text() =="":
                self.btn7.setText(self.btn6.text())
                self.btn6.setText("")
            self.tekshir()
    def fun7(self):
        if self.btn7.text() != "":
            if self.btn3.text() == "":
                self.btn3.setText(self.btn7.text())
                self.btn7.setText("")
            elif self.btn6.text() == "":
                self.btn6.setText(self.btn7.text())
                self.btn7.setText("")
            elif self.btn11.text()=="":
                self.btn11.setText(self.btn7.text())
                self.btn7.setText("")
            elif self.btn8.text() =="":
                self.btn8.setText(self.btn7.text())
                self.btn7.setText("")
            self.tekshir()
    def fun8(self):
        if self.btn8.text() != "":
            if self.btn4.text() == "":
                self.btn4.setText(self.btn8.text())
                self.btn8.setText("")
            elif self.btn7.text() == "":
                self.btn7.setText(self.btn8.text())
                self.btn8.setText("")
            elif self.btn12.text()=="":
                self.btn12.setText(self.btn8.text())
                self.btn8.setText("")
            self.tekshir()
    def fun9(self):
        if self.btn9.text() != "":
            if self.btn5.text() == "":
                self.btn5.setText(self.btn9.text())
                self.btn9.setText("")
            elif self.btn10.text() == "":
                self.btn10.setText(self.btn9.text())
                self.btn9.setText("")
            elif self.btn13.text()=="":
                self.btn13.setText(self.btn9.text())
                self.btn9.setText("")
            self.tekshir()
    def fun10(self):
        if self.btn10.text() != "":
            if self.btn6.text() == "":
                self.btn6.setText(self.btn10.text())
                self.btn10.setText("")
            elif self.btn9.text() == "":
                self.btn9.setText(self.btn10.text())
                self.btn10.setText("")
            elif self.btn14.text()=="":
                self.btn14.setText(self.btn10.text())
                self.btn10.setText("")
            elif self.btn11.text() =="":
                self.btn11.setText(self.btn10.text())
                self.btn10.setText("")
            self.tekshir()
    def fun11(self):
        if self.btn11.text() != "":
            if self.btn7.text() == "":
                self.btn7.setText(self.btn11.text())
                self.btn11.setText("")
            elif self.btn10.text() == "":
                self.btn10.setText(self.btn11.text())
                self.btn11.setText("")
            elif self.btn15.text()=="":
                self.btn15.setText(self.btn11.text())
                self.btn11.setText("")
            elif self.btn12.text() =="":
                self.btn12.setText(self.btn11.text())
                self.btn11.setText("")
            self.tekshir()
    def fun12(self):
        if self.btn12.text() != "":
            if self.btn8.text() == "":
                self.btn8.setText(self.btn12.text())
                self.btn12.setText("")
            elif self.btn11.text() == "":
                self.btn11.setText(self.btn12.text())
                self.btn12.setText("")
            elif self.btn16.text()=="":
                self.btn16.setText(self.btn12.text())
                self.btn12.setText("")
            self.tekshir()
    def fun13(self):
        if self.btn13.text() != "":
            if self.btn9.text() == "":
                self.btn9.setText(self.btn13.text())
                self.btn13.setText("")
            elif self.btn14.text() == "":
                self.btn14.setText(self.btn13.text())
                self.btn13.setText("")
            self.tekshir()
    def fun14(self):
        if self.btn14.text() != "":
            if self.btn10.text() == "":
                self.btn10.setText(self.btn14.text())
                self.btn14.setText("")
            elif self.btn13.text() == "":
                self.btn13.setText(self.btn14.text())
                self.btn14.setText("")
            elif self.btn15.text()=="":
                self.btn15.setText(self.btn14.text())
                self.btn14.setText("")
            self.tekshir()
    def fun15(self):
        if self.btn15.text() != "":
            if self.btn11.text() == "":
                self.btn11.setText(self.btn15.text())
                self.btn15.setText("")
            elif self.btn14.text() == "":
                self.btn14.setText(self.btn15.text())
                self.btn15.setText("")
            elif self.btn16.text()=="":
                self.btn16.setText(self.btn15.text())
                self.btn15.setText("")
            self.tekshir()
    def fun16(self):
        if self.btn16.text() != "":
            if self.btn12.text() == "":
                self.btn12.setText(self.btn16.text())
                self.btn16.setText("")
            elif self.btn15.text() == "":
                self.btn15.setText(self.btn16.text())
                self.btn16.setText("")
            self.tekshir()
    def __init__(self):
        super().__init__()
        self.glay = QGridLayout()
        self.hlay = QHBoxLayout()
        self.vmain = QVBoxLayout()
        self.msg =QMessageBox()

        self.btn1 = QPushButton('1')
        self.btn1.clicked.connect(self.fun1)
        self.btn2 = QPushButton('2')
        self.btn2.clicked.connect(self.fun2)
        self.btn3 = QPushButton('3')
        self.btn3.clicked.connect(self.fun3)
        self.btn4 = QPushButton('4')
        self.btn4.clicked.connect(self.fun4)
        self.btn5 = QPushButton('5')
        self.btn5.clicked.connect(self.fun5)
        self.btn6 = QPushButton('6')
        self.btn6.clicked.connect(self.fun6)
        self.btn7 = QPushButton('7')
        self.btn7.clicked.connect(self.fun7)
        self.btn8 = QPushButton('8')
        self.btn8.clicked.connect(self.fun8)
        self.btn9 = QPushButton('9')
        self.btn9.clicked.connect(self.fun9)
        self.btn10 = QPushButton('10')
        self.btn10.clicked.connect(self.fun10)
        self.btn11 = QPushButton('11')
        self.btn11.clicked.connect(self.fun11)
        self.btn12 = QPushButton('12')
        self.btn12.clicked.connect(self.fun12)
        self.btn13= QPushButton('13')
        self.btn13.clicked.connect(self.fun13)
        self.btn14 = QPushButton('14')
        self.btn14.clicked.connect(self.fun14)
        self.btn15 = QPushButton('15')
        self.btn15.clicked.connect(self.fun15)
        self.btn16 = QPushButton('')
        self.btn16.clicked.connect(self.fun16)



        self.Start = QPushButton('START')
        self.Start.clicked.connect(self.start1)
        self.Reset = QPushButton('RESET')
        self.Reset.clicked.connect(self.reset1)
        self.exit = QPushButton("EXIT")
        self.exit.clicked.connect(self.close)

        self.str_style = """QPushButton {
            color:red;
            background-color:solidyellow;
            border:1px solid black;
            border-radius:50%;
            font: bold 12pt;
            height:70px;
            width:100px;
        }"""

        self.lst = [self.btn1, self.btn2, self.btn3, self.btn4, self.btn5, self.btn6, self.btn7, self.btn8, self.btn9, self.btn10, self.btn11, self.btn12,self.btn13, self.btn14, self.btn15, self.btn16]
        index = 0
        for i in range(4):
            for j in range(4):
                self.glay.addWidget(self.lst[index], i, j)
                self.lst[index].setStyleSheet(self.str_style)
                index+=1
        for i in self.lst:
            i.setEnabled(False)
        self.hlay.addWidget(self.Start)
        self.hlay.addWidget(self.Reset)
        self.hlay.addWidget(self.exit)
        self.Reset.hide()
        self.vmain.addLayout(self.glay)
        self.vmain.addLayout(self.hlay)
        self.setLayout(self.vmain)
if __name__ == "__main__":
    app = QApplication([])
    oyna = window()
    oyna.show()
    app.exec_()