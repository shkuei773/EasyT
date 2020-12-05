import sys
from PyQt5.QtWidgets import *
import D_View, D_One

app = QApplication(sys.argv)
ex = D_View.MainView()
ex.show()
sys.exit(app.exec_())