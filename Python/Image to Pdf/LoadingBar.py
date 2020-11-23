import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class LoadingState(QDialog):
  def __init__(self):
    super().__init__()
    self.LoadingLayout()
    
  def LoadingLayout(self):
    self.setGeometry(1100, 200, 300, 100)
    self.setWindowTitle("Loading Bar")
    layout = QGridLayout()
    layout.addWidget(QLabel("In Progress"),0,0)
    self.setLayout(layout)
    
