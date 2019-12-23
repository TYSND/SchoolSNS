from PyQt5 import QtCore, QtGui, QtWidgets
from util import *

class loginFuncs:
    #store funcions used when login
    #exception info to show
    wrongText=""
    father=""
    ctrlDict=[(QtWidgets.QPushButton,'loginBut'),(QtWidgets.QPushButton,'registerBut'),
              (QtWidgets.QLineEdit,'accountInput'),(QtWidgets.QLineEdit,'passwordInput')]

    def __init__(self,father):
        self.father=father
    
    def isAccValid(self,account):
        'is account valid or not'
        return True
        if len(account)<=0:
            self.wrongText="账户不能为空"
            return False
        else:
            self.wrongText=""
            return True

    def isPwValid(self,pw):
        'is password valid or not'
        return True
        if len(pw)<=0:
            self.wrongText="密码不能为空"
            return False
        else:
            self.wrongText=""
            return True

    def disableWindow(self):
        log('ctrlDict:',self.ctrlDict)
        for ctrlInfo in self.ctrlDict:
            try:
                self.father.findChild(ctrlInfo[0],ctrlInfo[1]).setEnabled(False)
            except:
                log('set disable for ',ctrlInfo,' fail')

    def enableWindow(self):
        for ctrlInfo in self.ctrlDict:
            father._Dialog.findChild(ctrlInfo[0],ctrlInfo[1]).setEnabled(True)


if __name__ == "__main__":
    tmp=loginFuncs('s')
    tmp.disableWindow()
