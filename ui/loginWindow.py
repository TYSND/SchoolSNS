# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import loginWindowAction
from loginWindowAction import *

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.registerBut = QtWidgets.QPushButton(Dialog)
        self.registerBut.setGeometry(QtCore.QRect(230, 240, 93, 28))
        self.registerBut.setObjectName("registerBut")
        self.loginBut = QtWidgets.QPushButton(Dialog)
        self.loginBut.setGeometry(QtCore.QRect(90, 240, 93, 28))
        self.loginBut.setObjectName("loginBut")
        self.accountInput = QtWidgets.QLineEdit(Dialog)
        self.accountInput.setGeometry(QtCore.QRect(180, 90, 113, 21))
        self.accountInput.setObjectName("accountInput")
        self.passwordInput = QtWidgets.QLineEdit(Dialog)
        self.passwordInput.setGeometry(QtCore.QRect(180, 140, 113, 21))
        self.passwordInput.setObjectName("passwordInput")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(110, 90, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(110, 150, 72, 15))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "登录"))
        self.registerBut.setText(_translate("Dialog", "注册"))
        self.loginBut.setText(_translate("Dialog", "登录"))
        self.label.setText(_translate("Dialog", "账号"))
        self.label_2.setText(_translate("Dialog", "密码"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    alert()
    sys.exit(app.exec_())
