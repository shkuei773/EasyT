import sys
from PyQt5.QtWidgets import *
from PIL import Image

class BTP(QWidget):
    imageList = list()
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('To PDF')
        self.selectImages()
        #self.resize(500, 100)
        self.centerWnd()
        self.show()

    def centerWnd(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def selectImages(self):
        openFileBtn = QPushButton("Select Image File", self)
        clearFileBtn = QPushButton("Image List Clear", self)
        conFileBtn = QPushButton("Image To PDF",self)
        self.textList = QTextEdit(self)
        self.textEdt = QLineEdit(self)

        form = QFormLayout()
        form.addWidget(openFileBtn)
        form.addWidget(QLabel()) #<br>
        form.addWidget(QLabel("Save PDF File Name"))
        form.addWidget(self.textEdt)
        form.addWidget(QLabel()) #<br>
        form.addWidget(QLabel("Image List"))
        form.addWidget(self.textList)        
        form.addWidget(QLabel()) #<br>
        form.addWidget(conFileBtn)
        form.addWidget(clearFileBtn)

        openFileBtn.clicked.connect(self.DefFileOpen)
        clearFileBtn.clicked.connect(self.FunClearBtn)
        conFileBtn.clicked.connect(self.FunConImg)

        self.setLayout(form)

    def DefFileOpen(self):
        #self, 파일 타이틀, 기본 디렉토리위치, 필터 종류들(;;로 구분), 디폴트 필터종류
        fO = QFileDialog.getOpenFileNames(self,"Open", './',"Images (*.png *.jpg *bmp *jpeg)","Images (*.png *.jpg *bmp *jpeg)")
        # qm = QMessageBox.question(self, 'Test', fO[0], QMessageBox.Yes|QMessageBox.No)
        for i in fO[0]:
            # print(i.split('/')[-1]) #주소에서 맨뒤만 이미지이름으로 가져옴.
            self.ImageConvert(i)
        # print(self.imageList)

    def ImageConvert(self, img):
        imgs = Image.open(img)
        imgsC = imgs.convert('RGB')
        self.imageList.append(imgsC)

    def FunClearBtn(self):        
        resetM = QMessageBox.question(self, 'Do', 'Do you want reset ImageList?',QMessageBox.Yes|QMessageBox.No)
        if resetM == QMessageBox.Yes:
            self.imageList.clear()
            QMessageBox.question(self, 'Success', 'Success Image List Clear', QMessageBox.Yes)
        else:
            QMessageBox.question(self, 'RollBack', 'This Cancelled', QMessageBox.Yes)        

    def FunConImg(self):
        naming = './'+self.textEdt.toPlainText()+'.pdf'
        self.imageList[0].save(naming, save_all=True, append_images=self.imageList[1:])
        QMessageBox.question(self, 'Success', 'Success Image To PDF', QMessageBox.Yes)


app = QApplication(sys.argv)
ex = BTP()
sys.exit(app.exec_())
