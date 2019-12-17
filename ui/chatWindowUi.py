# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chatWindowUi.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_chatWindow(object):
    def setupUi(self, chatWindow):
        chatWindow.setObjectName("chatWindow")
        chatWindow.resize(908, 759)
        self.scrollArea = QtWidgets.QScrollArea(chatWindow)
        self.scrollArea.setGeometry(QtCore.QRect(20, 20, 871, 471))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 848, 469))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 871, 471))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.messageList = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.messageList.setContentsMargins(0, 0, 0, 0)
        self.messageList.setObjectName("messageList")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.textarea = QtWidgets.QTextEdit(chatWindow)
        self.textarea.setGeometry(QtCore.QRect(20, 510, 871, 181))
        self.textarea.setObjectName("textarea")
        self.sendBut = QtWidgets.QPushButton(chatWindow)
        self.sendBut.setGeometry(QtCore.QRect(650, 700, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.sendBut.setFont(font)
        self.sendBut.setObjectName("sendBut")

        self.retranslateUi(chatWindow)
        QtCore.QMetaObject.connectSlotsByName(chatWindow)

    def retranslateUi(self, chatWindow):
        _translate = QtCore.QCoreApplication.translate
        chatWindow.setWindowTitle(_translate("chatWindow", "与 某某用户 交谈中"))
        self.sendBut.setText(_translate("chatWindow", "发送"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    chatWindow = QtWidgets.QDialog()
    ui = Ui_chatWindow()
    ui.setupUi(chatWindow)
    chatWindow.show()
    sys.exit(app.exec_())
