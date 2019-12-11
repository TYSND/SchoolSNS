# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'friListItem.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_friListItem(object):
    def setupUi(self, friListItem):
        friListItem.setObjectName("friListItem")
        friListItem.resize(400, 110)
        self.avatar = QtWidgets.QGraphicsView(friListItem)
        self.avatar.setGeometry(QtCore.QRect(20, 20, 71, 71))
        self.avatar.setObjectName("avatar")
        self.nick = QtWidgets.QLabel(friListItem)
        self.nick.setGeometry(QtCore.QRect(110, 30, 91, 16))
        self.nick.setObjectName("nick")
        self.status = QtWidgets.QLabel(friListItem)
        self.status.setGeometry(QtCore.QRect(290, 60, 72, 15))
        self.status.setObjectName("status")
        self.message = QtWidgets.QLabel(friListItem)
        self.message.setGeometry(QtCore.QRect(110, 60, 91, 21))
        self.message.setObjectName("message")
        self.account = QtWidgets.QLabel(friListItem)
        self.account.setGeometry(QtCore.QRect(200, 30, 72, 15))
        self.account.setObjectName("account")

        self.retranslateUi(friListItem)
        QtCore.QMetaObject.connectSlotsByName(friListItem)

    def retranslateUi(self, friListItem):
        _translate = QtCore.QCoreApplication.translate
        friListItem.setWindowTitle(_translate("friListItem", "Form"))
        self.nick.setText(_translate("friListItem", "friendnick"))
        self.status.setText(_translate("friListItem", "offline"))
        self.message.setText(_translate("friListItem", "3条新消息"))
        self.account.setText(_translate("friListItem", "(account)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    friListItem = QtWidgets.QWidget()
    ui = Ui_friListItem()
    ui.setupUi(friListItem)
    friListItem.show()
    sys.exit(app.exec_())
