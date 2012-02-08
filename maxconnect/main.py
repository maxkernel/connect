
import sys
from PyQt4 import QtGui

import tasks


class MaxWizard(QtGui.QWizard):
	
	def __init__(self):
		super(MaxWizard, self).__init__()

	

def gui_deploy():
	app = QtGui.QApplication(sys.argv)
	
	w = MaxWizard()
	w.resize(700, 500)
	w.move(50, 50)
	w.setWindowTitle('MaxConnect Deploy Wizard')
	
	w.show()
	sys.exit(app.exec_())


if __name__ == '__main__':
	gui_deploy()
