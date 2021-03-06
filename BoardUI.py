# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BoardUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget, QMessageBox

playFlag =0
playerX = 0
playerO = 0

class Ui_Form(object):

    def resetBoard(self):


        #enable again

        self.pB1.setEnabled(True)
        self.pB2.setEnabled(True)
        self.pB3.setEnabled(True)
        self.pB4.setEnabled(True)
        self.pB5.setEnabled(True)
        self.pB6.setEnabled(True)
        self.pB7.setEnabled(True)
        self.pB8.setEnabled(True)
        self.pB9.setEnabled(True)
        
        #reset Text

        self.pB1.setText('')
        self.pB2.setText('')
        self.pB3.setText('')
        self.pB4.setText('')
        self.pB5.setText('')
        self.pB6.setText('')
        self.pB7.setText('')
        self.pB8.setText('')
        self.pB9.setText('')


    def btnClk(self, pos):
        global playFlag
        mark =''

        if (playFlag%2==0):
            mark = 'X'
        else:
            mark = 'O'
        
        if pos == 1:
            self.pB1.setText(mark)
            self.pB1.setEnabled(False)
        if pos == 2:
            self.pB2.setText(mark)
            self.pB2.setEnabled(False)
        if pos == 3:
            self.pB3.setText(mark)
            self.pB3.setEnabled(False)
        if pos == 4:
            self.pB4.setText(mark)
            self.pB4.setEnabled(False)
        if pos == 5:
            self.pB5.setText(mark)
            self.pB5.setEnabled(False)
        if pos == 6:
            self.pB6.setText(mark)
            self.pB6.setEnabled(False)
        if pos == 7:
            self.pB7.setText(mark)
            self.pB7.setEnabled(False)
        if pos == 8:
            self.pB8.setText(mark)
            self.pB8.setEnabled(False)
        if pos == 9:
            self.pB9.setText(mark)
            self.pB9.setEnabled(False)
        playFlag+=1
        self.chkWin()

    
    def chkWin(self):
        global playerX, playerO
        winner = ''
        if self.pB1.text() == self.pB2.text() and self.pB2.text() == self.pB3.text():
            winner = self.pB1.text()
        elif self.pB4.text() == self.pB5.text() and self.pB5.text() == self.pB6.text():
            winner = self.pB4.text()
        elif self.pB7.text() == self.pB8.text() and self.pB8.text() == self.pB9.text():
            winner = self.pB7.text()
        elif self.pB1.text() == self.pB4.text() and self.pB4.text() == self.pB7.text():
            winner = self.pB1.text()
        elif self.pB2.text() == self.pB5.text() and self.pB5.text() == self.pB8.text():
            winner = self.pB2.text()
        elif self.pB3.text() == self.pB6.text() and self.pB6.text() == self.pB9.text():
            winner = self.pB3.text()
        elif self.pB1.text() == self.pB5.text() and self.pB5.text() == self.pB9.text():
            winner = self.pB1.text()
        elif self.pB3.text() == self.pB5.text() and self.pB5.text() == self.pB7.text():
            winner = self.pB3.text()
        
        if winner == 'X':
            playerX+=1
            self.xScore.setText('Player X : '+str(playerX))
            msg = QMessageBox()
            msg.setWindowTitle("Status")
            msg.setText("X is the winner in Board.")
            msg.setGeometry(QtCore.QRect(130, 130, 100, 200))
            msg.setIcon(QMessageBox.Information)
            msg.exec_()
            self.resetBoard()
        elif winner == 'O':
            playerO+=1
            self.oScore.setText('Player O : '+str(playerO))
            msg = QMessageBox()
            msg.setWindowTitle("Status")
            msg.setText("O is the winner in Board.")
            msg.setGeometry(QtCore.QRect(130, 130, 100, 200))
            msg.setIcon(QMessageBox.Information)
            msg.exec_()
            self.resetBoard()
        

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(350, 400)
        Form.setMinimumSize(QtCore.QSize(350, 400))
        Form.setMaximumSize(QtCore.QSize(350, 400))
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 331, 293))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName("gridLayout")

        #Button 3
        
        self.pB3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pB3.setMinimumSize(QtCore.QSize(100, 93))
        self.pB3.setMaximumSize(QtCore.QSize(100, 93))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Light")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.pB3.setFont(font)
        self.pB3.setText("")
        self.pB3.setObjectName("pB3")
        self.pB3.clicked.connect(lambda: self.btnClk(3))
        self.gridLayout.addWidget(self.pB3, 0, 2, 1, 1)

        #Button 4

        self.pB4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pB4.setMinimumSize(QtCore.QSize(100, 93))
        self.pB4.setMaximumSize(QtCore.QSize(100, 93))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Light")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.pB4.setFont(font)
        self.pB4.setText("")
        self.pB4.setObjectName("pB4")
        self.pB4.clicked.connect(lambda: self.btnClk(4))
        self.gridLayout.addWidget(self.pB4, 3, 0, 1, 1)

        #Button 9

        self.pB9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pB9.setMinimumSize(QtCore.QSize(100, 93))
        self.pB9.setMaximumSize(QtCore.QSize(100, 93))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Light")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.pB9.setFont(font)
        self.pB9.setText("")
        self.pB9.setObjectName("pB9")
        self.pB9.clicked.connect(lambda: self.btnClk(9))
        self.gridLayout.addWidget(self.pB9, 4, 2, 1, 1)
        
        #Button 6

        self.pB6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pB6.setMinimumSize(QtCore.QSize(100, 93))
        self.pB6.setMaximumSize(QtCore.QSize(100, 93))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Light")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.pB6.setFont(font)
        self.pB6.setText("")
        self.pB6.setObjectName("pB6")
        self.pB6.clicked.connect(lambda: self.btnClk(6))
        self.gridLayout.addWidget(self.pB6, 3, 2, 1, 1)
        
        #Button 7

        self.pB7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pB7.setMinimumSize(QtCore.QSize(100, 93))
        self.pB7.setMaximumSize(QtCore.QSize(100, 93))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Light")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.pB7.setFont(font)
        self.pB7.setText("")
        self.pB7.setObjectName("pB7")
        self.pB7.clicked.connect(lambda: self.btnClk(7))
        self.gridLayout.addWidget(self.pB7, 4, 0, 1, 1)
        
        #Button 1

        self.pB1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pB1.setMinimumSize(QtCore.QSize(100, 93))
        self.pB1.setMaximumSize(QtCore.QSize(100, 93))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Light")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.pB1.setFont(font)
        self.pB1.setText("")
        self.pB1.setObjectName("pB1")
        self.pB1.clicked.connect(lambda: self.btnClk(1))
        self.gridLayout.addWidget(self.pB1, 0, 0, 1, 1)
        
        #Button 2

        self.pB2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pB2.setMinimumSize(QtCore.QSize(100, 93))
        self.pB2.setMaximumSize(QtCore.QSize(100, 93))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Light")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.pB2.setFont(font)
        self.pB2.setText("")
        self.pB2.setObjectName("pB2")
        self.pB2.clicked.connect(lambda: self.btnClk(2))
        self.gridLayout.addWidget(self.pB2, 0, 1, 1, 1)
        
        #Button 5

        self.pB5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pB5.setMinimumSize(QtCore.QSize(100, 93))
        self.pB5.setMaximumSize(QtCore.QSize(100, 93))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Light")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.pB5.setFont(font)
        self.pB5.setText("")
        self.pB5.setObjectName("pB5")
        self.pB5.clicked.connect(lambda: self.btnClk(5))
        self.gridLayout.addWidget(self.pB5, 3, 1, 1, 1)
        
        #Button 8

        self.pB8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pB8.setMinimumSize(QtCore.QSize(100, 93))
        self.pB8.setMaximumSize(QtCore.QSize(100, 93))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Light")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.pB8.setFont(font)
        self.pB8.setText("")
        self.pB8.setObjectName("pB8")
        self.pB8.clicked.connect(lambda: self.btnClk(8))
        self.gridLayout.addWidget(self.pB8, 4, 1, 1, 1)
        
        #xScore

        self.xScore = QtWidgets.QLabel(Form)
        self.xScore.setGeometry(QtCore.QRect(20, 320, 91, 71))
        self.xScore.setMinimumSize(QtCore.QSize(91, 71))
        self.xScore.setMaximumSize(QtCore.QSize(91, 71))
        self.xScore.setObjectName("xScore")
        
        #oScore

        self.oScore = QtWidgets.QLabel(Form)
        self.oScore.setGeometry(QtCore.QRect(240, 320, 91, 71))
        self.oScore.setMinimumSize(QtCore.QSize(91, 71))
        self.oScore.setMaximumSize(QtCore.QSize(91, 71))
        self.oScore.setObjectName("oScore")
        
        #reset

        self.res = QtWidgets.QPushButton(Form)
        self.res.setGeometry(QtCore.QRect(130, 340, 89, 25))
        self.res.setObjectName("res")
        self.res.clicked.connect(self.resetBoard)
        

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Board"))
        self.xScore.setText(_translate("Form", "Player X : 0"))
        self.oScore.setText(_translate("Form", "Player O : 0"))
        self.res.setText(_translate("Form", "Reset"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
