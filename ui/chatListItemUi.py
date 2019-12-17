# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chatListItemUi.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_chatListItem(object):
    def setupUi(self, chatListItem):
        chatListItem.setObjectName("chatListItem")
        chatListItem.resize(529, 100)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(chatListItem.sizePolicy().hasHeightForWidth())
        chatListItem.setSizePolicy(sizePolicy)
        self.nick = QtWidgets.QLabel(chatListItem)
        self.nick.setGeometry(QtCore.QRect(30, 20, 81, 16))
        self.nick.setObjectName("nick")
        self.date = QtWidgets.QLabel(chatListItem)
        self.date.setGeometry(QtCore.QRect(100, 20, 141, 16))
        self.date.setObjectName("date")
        self.text = QtWidgets.QTextBrowser(chatListItem)
        self.text.setGeometry(QtCore.QRect(30, 40, 471, 51))
        self.text.setObjectName("text")

        self.retranslateUi(chatListItem)
        QtCore.QMetaObject.connectSlotsByName(chatListItem)

    def retranslateUi(self, chatListItem):
        _translate = QtCore.QCoreApplication.translate
        chatListItem.setWindowTitle(_translate("chatListItem", "Form"))
        self.nick.setText(_translate("chatListItem", "nick"))
        self.date.setText(_translate("chatListItem", "send date"))
