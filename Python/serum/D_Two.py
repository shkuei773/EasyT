import sys, xlrd
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Deposit(QWidget):
    def __init__(self):
        super().__init__()
        self.TaxBill()

    def TaxBill(self):
        ####
        #틀잡기
        #파일오픈 버튼 *1
        #wants = int(input("A열에서 시작하길 원하는 번호: ")) 에디트박스*1
        #실행버튼=>누를때마다 값나오게
        #번호:
        #년도:
        #금액:
        #운영비:
        #회사명:
        #붙여넣을값:
        self.num=0##여기에 넣을 메시지박스를 가져와야할듯
        self.i = 0
        #메인틀
        self.setWindowTitle('입금등록(운영비)')
        self.setStyleSheet('background:#0f0f0f')
        self.resize(550,600)
        self.center()
        form = QFormLayout()
        self.setLayout(form)
        #제목
        label = QLabel("입금등록(운영비)",self)
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

        #FileOpen 버튼
        button_oepn = QPushButton("열기", self)
        button_oepn.setStyleSheet('color:white; background:black;font-size:20px; font-weight: bold;border-color:white;')
        button_oepn.setFixedHeight(40)
        button_oepn.clicked.connect(self.open_Btn)

        #세금계산서 회사명, 월, 금액
        #_(주)스프링클라우드_621,190_8월분담금
        self.form_name()
        form.addWidget(QLabel())
        form.addRow(button_oepn)
        form.addWidget(QLabel())
        form.addRow(self.form_namea, self.form_name_edita)
        form.addWidget(QLabel())
        form.addRow(self.form_name,self.form_name_edit)
        form.addWidget(QLabel())
        form.addRow(self.form_name1,self.form_name_edit1)
        form.addWidget(QLabel())
        form.addRow(self.form_name2,self.form_name_edit2)
        form.addWidget(QLabel())
        form.addRow(self.form_name3,self.form_name_edit3)
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
        # wants = int(input("A열에서 시작하길 원하는 번호: ")) 에디트박스*1

        self.form_namea = QLabel('A열 번호 입력', self)
        self.form_name_edita = QLineEdit(self)
        self.form_namea.setFixedHeight(30)
        self.form_namea.setStyleSheet('color:white;font-size:20px; font-weight: bold')
        self.form_name_edita.setFixedHeight(30)
        self.form_name_edita.setStyleSheet('color:white;font-size:20px; font-weight: bold')
        self.form_name_edita.setText(str(self.num))

        self.form_name = QLabel('금액', self)
        self.form_name_edit = QLineEdit(self)
        self.form_name.setFixedHeight(30)
        self.form_name.setStyleSheet('color:white;font-size:20px; font-weight: bold')
        self.form_name_edit.setFixedHeight(30)
        self.form_name_edit.setStyleSheet('color:white;font-size:20px; font-weight: bold')

        self.form_name1 = QLabel('년도', self)
        self.form_name_edit1 = QLineEdit(self)
        self.form_name1.setFixedHeight(30)
        self.form_name1.setStyleSheet('color:white;font-size:20px; font-weight: bold')
        self.form_name_edit1.setFixedHeight(30)
        self.form_name_edit1.setStyleSheet('color:white;font-size:20px; font-weight: bold')

        self.form_name2 = QLabel('운영비', self)
        self.form_name_edit2 = QLineEdit(self)
        self.form_name2.setFixedHeight(30)
        self.form_name2.setStyleSheet('color:white;font-size:20px; font-weight: bold')
        self.form_name_edit2.setFixedHeight(30)
        self.form_name_edit2.setStyleSheet('color:white;font-size:20px; font-weight: bold')

        self.form_name3 = QLabel('회사명', self)
        self.form_name_edit3= QLineEdit(self)
        self.form_name3.setFixedHeight(30)
        self.form_name3.setStyleSheet('color:white;font-size:20px; font-weight: bold')
        self.form_name_edit3.setFixedHeight(30)
        self.form_name_edit3.setStyleSheet('color:white;font-size:20px; font-weight: bold')

        self.form_result = QLineEdit(self)
        self.form_result.setFixedHeight(50)
        self.form_result.setStyleSheet('color:white;font-size:20px; font-weight: bold')
        self.form_result.setText("값이 나오면 복붙하면 됨")
    #Run 버튼 사용
    def run_Btn(self):
        self.num=int(self.form_name_edita.text())
        a = self.form_name_edit1.text().replace(" ", "")
        b = self.form_name_edit2.text().replace(" ", "")
        c = self.form_name_edit.text().replace(" ", "")
        run_result = "_{}_{}_{}".format(c,b,a)
        self.form_result.setText(run_result)
        self.num=self.num+1
        self.form_name_edita.setText(str(self.num))

        excel_name = self.fna
        wants = self.num
        while True:
            wb = xlrd.open_workbook(excel_name)
            sheet = wb.sheet_by_index(0)
            str_key = ""

            if int(sheet.cell(self.i, 0).value) < wants:
                self.i = self.i + 1
                continue
            for j in range(0, 6):
                keyword = sheet.cell(self.i, j).value
                if j == 0:
                    str_key = str_key + "_" + str(int(keyword))
                    self.form_name_edit.setText(str(int(keyword)))
                elif j == 1:
                    str_key = str_key + "_" + str(keyword[4:])
                    self.form_name_edit1.setText(str(keyword[4:]))
                elif j ==2:
                    self.form_name_edit.setText(str(int(keyword)))
                elif j == 5:
                    a = keyword.split('/')
                    if len(a)<=1:
                        self.form_name_edit3.setText(a[0])
                    else:
                        self.form_name_edit3.setText(a[1])
                    self.form_name_edit2.setText(keyword)
                print(keyword, end='\t')
                if j == 5:
                    self.form_result.setText(str_key)
            self.i = self.i+1
            break



    # Open버튼 사용
    def open_Btn(self):
        fname = QFileDialog.getOpenFileName(self, 'Open', './')
        self.fna = fname[0]
        print(self.fna)

    #이창만 닫기
    def this_Close(self):
        self.close()


if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = Deposit()
    ex.show()
    sys.exit(app.exec_())