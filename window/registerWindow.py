from PyQt5 import QtCore, QtGui, QtWidgets
from windowUi import *
from util import *


class registerWindow(publicWindow):
    _uiClass = Ui_registerWindow
    ctrlInfo = {'regBut': (QtWidgets.QPushButton, 'registerBut'),
                'accIn': (QtWidgets.QLineEdit, 'accountInput'),
                'nickIn': (QtWidgets.QLineEdit, 'nickInput'),
                'pwIn': (QtWidgets.QLineEdit, 'passwordInput'),
                'rePwIn': (QtWidgets.QLineEdit, 'rePasswordInput'),
                'showInfo': (QtWidgets.QLabel, 'showInfo'),
                'avatar': (QtWidgets.QLabel, 'avatar'),
                'selectAvatar': (QtWidgets.QPushButton, 'selectAvatar')
                }
    # store handle for qt controls
    ctrl = {}
    avatar = 0

    def __init__(self):
        super(registerWindow, self).__init__()
        for id, info in self.ctrlInfo.items():
            self.ctrl[id] = self._Dialog.findChild(info[0], info[1])
        self.ctrl['regBut'].clicked.connect(self.register)

    #        self.ctrl['selectAvatar'].clicked.connect(lambda:selectAvatar(self.avatar))

    def register(self):
        if not self.validAcc() or not self.validNick() or not self.validPw():
            self.showInfo('输入信息不规范')
            return
        log('register info valid')
        jstr = {'ope':opeDict('register'),
                'id':self.ctrl['accIn'].text(),
                'pw':self.ctrl['pwIn'].text(),
                'avatar':self.avatar,
                'nick':self.ctrl['nickIn'].text()
                }
        log(jstr)
        jstr=XHR(jstr)


    def validAcc(self):
        """valid user account"""
        return True
        return len(self.ctrl['accIn'].text()) > 0

    def validNick(self):
        """valid user nickname"""
        return True
        return len(self.ctrl['nickIn'].text()) > 0

    def validPw(self):
        """valid Password"""
        return True
        return len(self.ctrl['pwIn'].text()) > 0 \
               and self.ctrl['pwIn'].text() == self.ctrl['rePwIn'].text()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    h = registerWindow()
    h.show()
    sys.exit(app.exec_())
