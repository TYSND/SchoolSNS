from PyQt5 import QtCore, QtGui, QtWidgets
from util import *
from customWidgetsUi import *

class customWidget(QtWidgets.QWidget):
    """parent class for all custom widgets,
       every child must set uiClass attribute
    """
    def __init__(self):
        'every custom widget must call QWidget __init__ first'
        super(customWidget,self).__init__()
        try:
            ui=self.uiClass()
            ui.setupUi(self)
        except:
            print('wrong ui')
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    h=friListItem()
    h.show()
    sys.exit(app.exec_())

