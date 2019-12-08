# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registerWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_registerWindow(object):
    def setupUi(self, registerWindow):
        registerWindow.setObjectName("registerWindow")
        registerWindow.resize(652, 510)
        registerWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.accountInput = QtWidgets.QLineEdit(registerWindow)
        self.accountInput.setGeometry(QtCore.QRect(190, 90, 261, 41))
        self.accountInput.setObjectName("accountInput")
        self.nickInput = QtWidgets.QLineEdit(registerWindow)
        self.nickInput.setGeometry(QtCore.QRect(192, 160, 261, 41))
        self.nickInput.setObjectName("nickInput")
        self.passwordInput = QtWidgets.QLineEdit(registerWindow)
        self.passwordInput.setGeometry(QtCore.QRect(192, 230, 261, 41))
        self.passwordInput.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordInput.setReadOnly(False)
        self.passwordInput.setObjectName("passwordInput")
        self.rePasswordInput = QtWidgets.QLineEdit(registerWindow)
        self.rePasswordInput.setGeometry(QtCore.QRect(190, 300, 261, 41))
        self.rePasswordInput.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.rePasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.rePasswordInput.setReadOnly(False)
        self.rePasswordInput.setObjectName("rePasswordInput")
        self.label = QtWidgets.QLabel(registerWindow)
        self.label.setGeometry(QtCore.QRect(70, 100, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(registerWindow)
        self.label_2.setGeometry(QtCore.QRect(70, 170, 72, 15))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(registerWindow)
        self.label_3.setGeometry(QtCore.QRect(70, 240, 72, 15))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(registerWindow)
        self.label_4.setGeometry(QtCore.QRect(70, 310, 101, 16))
        self.label_4.setObjectName("label_4")
        self.registerBut = QtWidgets.QPushButton(registerWindow)
        self.registerBut.setGeometry(QtCore.QRect(370, 400, 241, 51))
        self.registerBut.setObjectName("registerBut")

        self.retranslateUi(registerWindow)
        QtCore.QMetaObject.connectSlotsByName(registerWindow)

    def retranslateUi(self, registerWindow):
        _translate = QtCore.QCoreApplication.translate
        registerWindow.setWindowTitle(_translate("registerWindow", "Dialog"))
        self.label.setText(_translate("registerWindow", "学号"))
        self.label_2.setText(_translate("registerWindow", "昵称"))
        self.label_3.setText(_translate("registerWindow", "密码"))
        self.label_4.setText(_translate("registerWindow", "再次输入密码"))
        self.registerBut.setText(_translate("registerWindow", "注册"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    registerWindow = QtWidgets.QDialog()
    ui = Ui_registerWindow()
    ui.setupUi(registerWindow)
    registerWindow.show()
    sys.exit(app.exec_())
