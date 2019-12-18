# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'friWindowUi.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_friWindow(object):
    def setupUi(self, friWindow):
        friWindow.setObjectName("friWindow")
        friWindow.resize(400, 705)
        self.avatar = QtWidgets.QGraphicsView(friWindow)
        self.avatar.setGeometry(QtCore.QRect(20, 20, 80, 80))
        self.avatar.setObjectName("avatar")
        self.nick = QtWidgets.QLabel(friWindow)
        self.nick.setGeometry(QtCore.QRect(110, 30, 111, 16))
        self.nick.setObjectName("nick")
        self.account = QtWidgets.QLabel(friWindow)
        self.account.setGeometry(QtCore.QRect(110, 70, 72, 15))
        self.account.setObjectName("account")
        self.friendInvite = QtWidgets.QPushButton(friWindow)
        self.friendInvite.setGeometry(QtCore.QRect(240, 20, 141, 31))
        self.friendInvite.setObjectName("friendInvite")
        self.addFriend = QtWidgets.QPushButton(friWindow)
        self.addFriend.setGeometry(QtCore.QRect(240, 60, 141, 31))
        self.addFriend.setObjectName("addFriend")
        self.setting = QtWidgets.QPushButton(friWindow)
        self.setting.setGeometry(QtCore.QRect(290, 660, 93, 31))
        self.setting.setObjectName("setting")
        self.scrollArea = QtWidgets.QScrollArea(friWindow)
        self.scrollArea.setGeometry(QtCore.QRect(20, 120, 361, 531))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 338, 529))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 321, 511))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.friList = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.friList.setContentsMargins(0, 0, 0, 0)
        self.friList.setObjectName("friList")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(friWindow)
        QtCore.QMetaObject.connectSlotsByName(friWindow)

    def retranslateUi(self, friWindow):
        _translate = QtCore.QCoreApplication.translate
        friWindow.setWindowTitle(_translate("friWindow", "Dialog"))
        self.nick.setText(_translate("friWindow", "nick"))
        self.account.setText(_translate("friWindow", "account"))
        self.friendInvite.setText(_translate("friWindow", "好友邀请"))
        self.addFriend.setText(_translate("friWindow", "添加好友"))
        self.setting.setText(_translate("friWindow", "账户设置"))
