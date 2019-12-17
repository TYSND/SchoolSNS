from PyQt5 import QtCore, QtGui, QtWidgets
from util import *

class Ui_chatListItem(object):
    def setupUi(self, chatListItem):
        chatListItem.setObjectName("chatListItem")
        chatListItem.resize(529, 80)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(chatListItem.sizePolicy().hasHeightForWidth())
        chatListItem.setSizePolicy(sizePolicy)
        self.nick = QtWidgets.QLabel(chatListItem)
        self.nick.setGeometry(QtCore.QRect(30, 5, 81, 15))
        self.nick.setObjectName("nick")
        self.date = QtWidgets.QLabel(chatListItem)
        self.date.setGeometry(QtCore.QRect(100, 5, 155, 15))
        self.date.setObjectName("date")
        self.text = QtWidgets.QTextBrowser(chatListItem)
        self.text.setGeometry(QtCore.QRect(30, 35, 471, 40))
        self.text.setObjectName("text")

        self.retranslateUi(chatListItem)
        QtCore.QMetaObject.connectSlotsByName(chatListItem)

    def retranslateUi(self, chatListItem):
        _translate = QtCore.QCoreApplication.translate
        chatListItem.setWindowTitle(_translate("chatListItem", "Form"))
        self.nick.setText(_translate("chatListItem", "nick"))
        self.date.setText(_translate("chatListItem", "send date"))



class Ui_chatListItemR(object):
    def setupUi(self, chatListItem):
        chatListItem.setObjectName("chatListItem")
        chatListItem.resize(529, 80)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(chatListItem.sizePolicy().hasHeightForWidth())
        chatListItem.setSizePolicy(sizePolicy)
        self.nick = QtWidgets.QLabel(chatListItem)
        self.nick.setGeometry(QtCore.QRect(330, 5, 81, 15))
        self.nick.setObjectName("nick")
        self.date = QtWidgets.QLabel(chatListItem)
        self.date.setGeometry(QtCore.QRect(400, 5, 155, 15))
        self.date.setObjectName("date")
        self.text = QtWidgets.QTextBrowser(chatListItem)
        self.text.setGeometry(QtCore.QRect(330, 35, 471, 40))
        self.text.setObjectName("text")

        self.retranslateUi(chatListItem)
        QtCore.QMetaObject.connectSlotsByName(chatListItem)

    def retranslateUi(self, chatListItem):
        _translate = QtCore.QCoreApplication.translate
        chatListItem.setWindowTitle(_translate("chatListItem", "Form"))
        self.nick.setText(_translate("chatListItem", "nick"))
        self.date.setText(_translate("chatListItem", "send date"))


class Ui_friListItem(object):
    'list item show friend info in friend window'
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
