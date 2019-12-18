# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'friListItemUi.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_friListItem(object):
    def setupUi(self, friListItem):
        friListItem.setObjectName("friListItem")
        friListItem.resize(302, 84)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(friListItem.sizePolicy().hasHeightForWidth())
        friListItem.setSizePolicy(sizePolicy)
        self.avatar = QtWidgets.QGraphicsView(friListItem)
        self.avatar.setGeometry(QtCore.QRect(10, 10, 61, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.avatar.sizePolicy().hasHeightForWidth())
        self.avatar.setSizePolicy(sizePolicy)
        self.avatar.setObjectName("avatar")
        self.nick = QtWidgets.QLabel(friListItem)
        self.nick.setGeometry(QtCore.QRect(80, 10, 91, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nick.sizePolicy().hasHeightForWidth())
        self.nick.setSizePolicy(sizePolicy)
        self.nick.setObjectName("nick")
        self.status = QtWidgets.QLabel(friListItem)
        self.status.setGeometry(QtCore.QRect(200, 50, 72, 15))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.status.sizePolicy().hasHeightForWidth())
        self.status.setSizePolicy(sizePolicy)
        self.status.setObjectName("status")
        self.account = QtWidgets.QLabel(friListItem)
        self.account.setGeometry(QtCore.QRect(200, 10, 72, 15))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.account.sizePolicy().hasHeightForWidth())
        self.account.setSizePolicy(sizePolicy)
        self.account.setObjectName("account")
        self.message = QtWidgets.QPushButton(friListItem)
        self.message.setGeometry(QtCore.QRect(90, 40, 93, 28))
        self.message.setObjectName("message")

        self.retranslateUi(friListItem)
        QtCore.QMetaObject.connectSlotsByName(friListItem)

    def retranslateUi(self, friListItem):
        _translate = QtCore.QCoreApplication.translate
        friListItem.setWindowTitle(_translate("friListItem", "Form"))
        self.nick.setText(_translate("friListItem", "friendnick"))
        self.status.setText(_translate("friListItem", "offline"))
        self.account.setText(_translate("friListItem", "(account)"))
        self.message.setText(_translate("friListItem", "3条新消息"))
