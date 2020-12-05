import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *




class TaxBill(QWidget):
    def __init__(self):
        super().__init__()
        self.TaxBill()

    def TaxBill(self):
        #메인틀
        self.setWindowTitle('세금계산서')
        self.setStyleSheet('background:#0f0f0f')
        self.resize(550,600)
        self.center()
        form = QFormLayout()
        self.setLayout(form)
        #제목
        label = QLabel("세금계산서",self)
        label.setAlignment(Qt.AlignCenter)
        label.setFixedHeight(50)
        label.setStyleSheet('color:white;font-size:40px; font-weight: bold')
        label.setAlignment(Qt.AlignCenter)
        form.addWidget(QLabel())
        form.addRow(label)
        form.addWidget(QLabel())
        # 종료버튼
        button_exit = QPushButton("    종료    ", self)
        button_exit.setStyleSheet('color:white; background:black;font-size:20px; font-weight: bold;border-color:white;')
        button_exit.setFixedHeight(80)
        button_exit.clicked.connect(self.this_Close)
        # Run버튼
        button_run = QPushButton("    실행    ", self)
        button_run.setStyleSheet('color:white; background:black;font-size:20px; font-weight: bold;border-color:white;')
        button_run.setFixedHeight(80)
        button_run.clicked.connect(self.run_Btn)

        #세금계산서 회사명, 월, 금액
        #_(주)스프링클라우드_621,190_8월분담금
        self.form_name()

        form.addWidget(QLabel())
        form.addRow(self.form_name,self.form_name_edit)
        form.addWidget(QLabel())
        form.addRow(self.form_name1,self.form_name_edit1)
        form.addWidget(QLabel())
        form.addRow(self.form_name2,self.form_name_edit2)
        form.addWidget(QLabel())
        form.addRow(self.form_result)
        form.addWidget(QLabel())

        form.addRow(button_run)
        form.addRow(button_exit)




    #Window 센터지정
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    #form에 사용할 이름들
    def form_name(self):
        self.form_name = QLabel('회사명', self)
        self.form_name_edit = QLineEdit(self)
        self.form_name.setFixedHeight(50)
        self.form_name.setStyleSheet('color:white;font-size:40px; font-weight: bold')
        self.form_name_edit.setFixedHeight(50)
        self.form_name_edit.setStyleSheet('color:white;font-size:40px; font-weight: bold')

        self.form_name1 = QLabel('월', self)
        self.form_name_edit1 = QLineEdit(self)
        self.form_name1.setFixedHeight(50)
        self.form_name1.setStyleSheet('color:white;font-size:40px; font-weight: bold')
        self.form_name_edit1.setFixedHeight(50)
        self.form_name_edit1.setStyleSheet('color:white;font-size:40px; font-weight: bold')

        self.form_name2 = QLabel('금액', self)
        self.form_name_edit2 = QLineEdit(self)
        self.form_name2.setFixedHeight(50)
        self.form_name2.setStyleSheet('color:white;font-size:40px; font-weight: bold')
        self.form_name_edit2.setFixedHeight(50)
        self.form_name_edit2.setStyleSheet('color:white;font-size:40px; font-weight: bold')

        self.form_result = QLineEdit(self)
        self.form_result.setFixedHeight(50)
        self.form_result.setStyleSheet('color:white;font-size:20px; font-weight: bold')
        self.form_result.setText("값이 나오면 복붙하면 됨")
    #Run 버튼 사용
    def run_Btn(self):
        a = self.form_name_edit1.text().replace(" ", "")
        b = self.form_name_edit2.text().replace(" ", "")
        c = self.form_name_edit.text().replace(" ", "")
        run_result = "_{}_{}_{}월분담금".format(c,b,a)
        self.form_result.setText(run_result)

    def this_Close(self):
        self.close()


if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = TaxBill()
    ex.show()
    sys.exit(app.exec_())