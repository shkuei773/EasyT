import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import D_One,D_Two,D_Three

class MainView(QWidget):
    def __init__(self):
        super().__init__()
        self.ChungBukUI()

    def ChungBukUI(self):
        #메인틀
        self.setWindowTitle('충북대학교 융합기술원')
        self.setStyleSheet('background:#0f0f0f')
        self.resize(550,600)
        self.center()
        #제목
        label = QLabel("충북대학교 융합기술원",self)
        label.setAlignment(Qt.AlignCenter)
        label.setFixedHeight(50)
        label.setStyleSheet('color:white;font-size:40px; font-weight: bold;')
        #메인 뷰의 클릭버튼(1~4)
        button_1 = QPushButton("분담금 세금계산서",self)
        button_1.setStyleSheet('color:white; background:black;font-size:20px; font-weight: bold;border-color:white;')
        button_1.setFixedHeight(80)
        button_1.clicked.connect(self.oness)
        button_2 = QPushButton("입금등록(운영비) 전체",self)
        button_2.setStyleSheet('color:white; background:black;font-size:20px; font-weight: bold;border-color:white;')
        button_2.setFixedHeight(80)
        button_2.clicked.connect(self.twoss)
        button_3 = QPushButton("월분담금청구서(X월분)",self)
        button_3.setStyleSheet('color:white; background:black;font-size:20px; font-weight: bold;border-color:white;')
        button_3.setFixedHeight(80)
        button_3.clicked.connect(self.threess)
        #종료버튼
        button_exit=QPushButton("    종료    ",self)
        button_exit.setStyleSheet('color:white; background:black;font-size:20px; font-weight: bold;border-color:white;')
        button_exit.setFixedHeight(80)
        button_exit.clicked.connect(QCoreApplication.instance().quit)
        #종료버튼 위치 조정
        hboxExit = QHBoxLayout()
        hboxExit.addStretch(1)
        hboxExit.addWidget(button_exit)
        #1~4버튼 위치조정
        vboxBtn = QVBoxLayout()
        vboxBtn.addStretch(1)
        vboxBtn.addWidget(button_1)
        vboxBtn.addWidget(button_2)
        vboxBtn.addWidget(button_3)
        vboxBtn.addStretch(1)
        #전체 위치조정
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(label)
        vbox.addStretch(1)
        vbox.addLayout(vboxBtn)
        vbox.addStretch(1)
        vbox.addLayout(hboxExit)
        #위치조정한 박스 레이아웃에 적용
        self.setLayout(vbox)

    #Window 센터지정
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    #taxbill
    def oness(self):
        self.news =  D_One.TaxBill()
        self.news.show()
    #Deposit
    def twoss(self):
        self.news=D_Two.Deposit()
        self.news.show()
    #bill
    def threess(self):
        self.news=D_Three.MonthBill()
        self.news.show()


if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = MainView()
    ex.show()
    sys.exit(app.exec_())