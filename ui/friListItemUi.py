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
        friListItem.resize(333, 110)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(friListItem.sizePolicy().hasHeightForWidth())
        friListItem.setSizePolicy(sizePolicy)
        self.avatar = QtWidgets.QGraphicsView(friListItem)
        self.avatar.setGeometry(QtCore.QRect(20, 20, 71, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.avatar.sizePolicy().hasHeightForWidth())
        self.avatar.setSizePolicy(sizePolicy)
        self.avatar.setObjectName("avatar")
        self.nick = QtWidgets.QLabel(friListItem)
        self.nick.setGeometry(QtCore.QRect(110, 30, 91, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nick.sizePolicy().hasHeightForWidth())
        self.nick.setSizePolicy(sizePolicy)
        self.nick.setObjectName("nick")
        self.status = QtWidgets.QLabel(friListItem)
        self.status.setGeometry(QtCore.QRect(250, 60, 72, 15))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.status.sizePolicy().hasHeightForWidth())
        self.status.setSizePolicy(sizePolicy)
        self.status.setObjectName("status")
        self.message = QtWidgets.QLabel(friListItem)
        self.message.setGeometry(QtCore.QRect(110, 60, 91, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.message.sizePolicy().hasHeightForWidth())
        self.message.setSizePolicy(sizePolicy)
        self.message.setObjectName("message")
        self.account = QtWidgets.QLabel(friListItem)
        self.account.setGeometry(QtCore.QRect(200, 30, 72, 15))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.account.sizePolicy().hasHeightForWidth())
        self.account.setSizePolicy(sizePolicy)
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
