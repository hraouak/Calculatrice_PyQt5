from PyQt5 import QtCore, QtGui, QtWidgets
from menu import Ui_Dialog
from math import *
import sys

def boutton(i):
	screen=str(ui.lineEdit.text())
	ui.lineEdit.setText(screen+str(i))

def boutton_effacer():
	ui.lineEdit.clear()

def boutton_entrer():
	screen=str(ui.lineEdit.text())
	ui.lineEdit.clear()
	ui.lineEdit.setText(str(eval(screen)))

app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()

ui.un.clicked.connect(lambda:boutton(1))
ui.deux.clicked.connect(lambda:boutton(2))
ui.trois.clicked.connect(lambda:boutton(3))
ui.quatre.clicked.connect(lambda:boutton(4))
ui.cinq.clicked.connect(lambda:boutton(5))
ui.six.clicked.connect(lambda:boutton(6))
ui.sept.clicked.connect(lambda:boutton(7))
ui.huit.clicked.connect(lambda:boutton(8))
ui.neuf.clicked.connect(lambda:boutton(9))
ui.zero.clicked.connect(lambda:boutton(0))

ui.effacer.clicked.connect(boutton_effacer)
ui.entrer.clicked.connect(boutton_entrer)

ui.division.clicked.connect(lambda:boutton('/'))
ui.multiplication.clicked.connect(lambda:boutton('*'))
ui.soustraction.clicked.connect(lambda:boutton('-'))
ui.addition.clicked.connect(lambda:boutton('+'))

sys.exit(app.exec_())
