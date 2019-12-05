from PyQt5 import QtCore, QtGui, QtWidgets
serverIp=""
serverPort=0

def initWin(uiClass):
    'initial window and set ui,then return window'
    Dialog = QtWidgets.QDialog()
    ui = uiClass()
    ui.setupUi(Dialog)
    return Dialog


def jsonGene(action,dataDict):
##      standard method to generate json to send,simply add
##      'action' key to dataDict.
        dataDict.action=action
        return dataDict


def XHR(payload,port=serverPort,ip=serverIp):
    """
    like XmlHttpRequest,send one payload to server and
    wait for one reply then return
    """
    #to be done
    return {status:'true'}
    
