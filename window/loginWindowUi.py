# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginWindowUi.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_loginWindow(object):
    def setupUi(self, loginWindow):
        loginWindow.setObjectName("loginWindow")
        loginWindow.resize(400, 300)
        self.registerBut = QtWidgets.QPushButton(loginWindow)
        self.registerBut.setGeometry(QtCore.QRect(230, 240, 93, 28))
        self.registerBut.setObjectName("registerBut")
        self.loginBut = QtWidgets.QPushButton(loginWindow)
        self.loginBut.setGeometry(QtCore.QRect(90, 240, 93, 28))
        self.loginBut.setObjectName("loginBut")
        self.accountInput = QtWidgets.QLineEdit(loginWindow)
        self.accountInput.setGeometry(QtCore.QRect(180, 90, 113, 21))
        self.accountInput.setObjectName("accountInput")
        self.passwordInput = QtWidgets.QLineEdit(loginWindow)
        self.passwordInput.setGeometry(QtCore.QRect(180, 140, 113, 21))
        self.passwordInput.setObjectName("passwordInput")
        self.label = QtWidgets.QLabel(loginWindow)
        self.label.setGeometry(QtCore.QRect(110, 90, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(loginWindow)
        self.label_2.setGeometry(QtCore.QRect(110, 150, 72, 15))
        self.label_2.setObjectName("label_2")
        self.showLab = QtWidgets.QLabel(loginWindow)
        self.showLab.setGeometry(QtCore.QRect(110, 180, 171, 16))
        self.showLab.setText("")
        self.showLab.setObjectName("showLab")
        self.showLab_2 = QtWidgets.QLabel(loginWindow)
        self.showLab_2.setGeometry(QtCore.QRect(110, 190, 171, 20))
        self.showLab_2.setText("")
        self.showLab_2.setObjectName("showLab_2")

        self.retranslateUi(loginWindow)
        QtCore.QMetaObject.connectSlotsByName(loginWindow)

    def retranslateUi(self, loginWindow):
        _translate = QtCore.QCoreApplication.translate
        loginWindow.setWindowTitle(_translate("loginWindow", "登录"))
        self.registerBut.setText(_translate("loginWindow", "注册"))
        self.loginBut.setText(_translate("loginWindow", "登录"))
        self.label.setText(_translate("loginWindow", "账号"))
        self.label_2.setText(_translate("loginWindow", "密码"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loginWindow = QtWidgets.QDialog()
    ui = Ui_loginWindow()
    ui.setupUi(loginWindow)
    loginWindow.show()
    sys.exit(app.exec_())
