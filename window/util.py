from PyQt5 import QtCore, QtGui, QtWidgets
serverIp=""
serverPort=0


class publicWindow:
    _Dialog=""
    def __init__(self):
        print('init')
        self._Dialog=initWin(self._uiClass)

    def show(self):
        self._Dialog.show()


def initWin(uiClass):
    'initial window and set ui,then return window'
    Dialog = QtWidgets.QDialog()
    try:
        ui = uiClass()
        ui.setupUi(Dialog)
    except:
        print('wrong ui class')
    return Dialog


def initWidget(uiClass):
    Widget = QtWidgets.QWidget()
    try:
        ui = uiClass()
        ui.setupUi(Widget)
    except:
        print('wrong ui class')
    return Widget


def jsonGene(action,dataDict):
##      standard method to generate json to send,simply add
##      'action' key to dataDict.
    dataDict['action']=action
    return dataDict


def XHR(payload,port=serverPort,ip=serverIp):
    """
    like XmlHttpRequest,send one payload to server and
    wait for one reply then return
    """
    #to be done
    return {'status':'true'}
    
