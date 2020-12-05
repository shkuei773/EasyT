import sys, xlrd, openpyxl, os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *



class MonthBill(QWidget):
    def __init__(self):
        super().__init__()
        self.Bill()

    def Bill(self):
        #메인틀
        self.setWindowTitle('월분담금청구서(X월분)')
        self.setStyleSheet('background:#0f0f0f')
        self.center()
        form = QFormLayout()
        self.setLayout(form)
        #제목
        label = QLabel("월분담금청구서(X월분)",self)
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
        # 파일 열기
        # 엑셀 월분담청구서 수정(월만입력) :
        # 엑셀 시트 이름(20년 9월) :
        # 년도입력(4자리)
        # 월입력
        # 기간넣기(09.01 - 09.30)
        self.form_name()
        form.addWidget(QLabel())
        form.addRow(button_oepn)
        form.addWidget(QLabel())
        form.addRow(self.form_name,self.form_name_edit)
        form.addWidget(QLabel())
        form.addRow(self.form_name1,self.form_name_edit1)
        form.addWidget(QLabel())
        form.addRow(self.form_name2,self.form_name_edit2)
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
        # 년도입력(4자리)
        # 월입력
        # 기간넣기(09.01 - 09.30)
        self.form_name = QLabel('년도 입력(4자리)', self)
        self.form_name_edit = QLineEdit(self)
        self.form_name.setFixedHeight(30)
        self.form_name.setStyleSheet('color:white;font-size:20px; font-weight: bold')
        self.form_name_edit.setFixedHeight(30)
        self.form_name_edit.setStyleSheet('color:white;font-size:30px; font-weight: bold')

        self.form_name1 = QLabel('월 입력', self)
        self.form_name_edit1 = QLineEdit(self)
        self.form_name1.setFixedHeight(30)
        self.form_name1.setStyleSheet('color:white;font-size:20px; font-weight: bold')
        self.form_name_edit1.setFixedHeight(30)
        self.form_name_edit1.setStyleSheet('color:white;font-size:30px; font-weight: bold')

        self.form_name2 = QLabel('기간입력(09.01 - 09.30)', self)
        self.form_name_edit2 = QLineEdit(self)
        self.form_name2.setFixedHeight(30)
        self.form_name2.setStyleSheet('color:white;font-size:20px; font-weight: bold')
        self.form_name_edit2.setFixedHeight(30)
        self.form_name_edit2.setStyleSheet('color:white;font-size:30px; font-weight: bold')

    #Run 버튼 사용
    def run_Btn(self):
        chk = 0
        want_sheet_name = "{}년 {}월".format(self.form_name_edit.text()[2:],self.form_name_edit1.text())

        for name in self.fna:
            # 엑셀이름
            excel_name = name
            if os.path.exists(excel_name):
                wb = openpyxl.load_workbook(excel_name)
                # sheetAc = wb.index(wb.active)
                # 시트이름 (0번째)
                sheet_list = wb.sheetnames

                for kas in sheet_list:
                    if kas == want_sheet_name:
                        chk = 1
                if chk == 1:
                    chk = 0
                    continue
                curSheet = wb.get_sheet_by_name(sheet_list[0])
                # copy
                copysit = wb.copy_worksheet(curSheet)
                copysit.title = want_sheet_name
                # 리스트 재설정
                sheet_list = wb.sheetnames
                # 맨앞으로 이동(-로해야 맨앞으로감)
                wb.move_sheet(sheet_list[-1], -(len(wb.sheetnames) - 1))
                ###여기서부터 값변경시작###
                sheet_list = wb.sheetnames
                curSheet = wb.get_sheet_by_name(sheet_list[0])

                curSheet.cell(row=1, column=5, value="{}년도 충북대학교 융합기술원 입주기관 {}월분담금 내역서".format(self.form_name_edit.text(), self.form_name_edit1.text()))
                curSheet.cell(row=6, column=6, value="{}".format(self.form_name_edit2.text()))

                wb.save(filename=excel_name)
                wb.close()


        for name in self.fna:
            src = name
            split_name = src.split('/')
            file_path = '/'.join(split_name[:-1])
            excelname = split_name[-1]
            chname = excelname.split('-')
            a = "월분담금청구서({}월분)".format(self.form_name_edit1.text()) + '-' + chname[1]
            rename = os.path.join(file_path, a)
            os.rename(src, rename)

    # Open버튼 사용
    def open_Btn(self):
        fname = QFileDialog.getOpenFileNames(self, 'Open', './')
        self.fna = fname[0]

    #이창만 닫기
    def this_Close(self):
        self.close()


if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = MonthBill()
    ex.show()
    sys.exit(app.exec_())