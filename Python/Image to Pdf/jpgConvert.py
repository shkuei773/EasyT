import sys
import os.path
from PyQt5.QtWidgets import *
from PIL import Image

class BTP(QWidget):
    imageList = list()
    #numbering = 0
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
        try:
            openFileBtn = QPushButton("Select Image File", self)
            clearFileBtn = QPushButton("Image List Clear", self)
            selDelBtn = QPushButton("Select ListItem Delete", self)
            conFileBtn = QPushButton("Image To PDF",self)
            self.textList = QListWidget(self)
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
            form.addWidget(selDelBtn)

            openFileBtn.clicked.connect(self.DefFileOpen)
            clearFileBtn.clicked.connect(self.FunClearBtn)
            conFileBtn.clicked.connect(self.FunConImg)
            selDelBtn.clicked.connect(self.FunSelDel)

            self.setLayout(form) 
        except:
            QMessageBox.question(self, 'Error', 'Error', QMessageBox.Yes)

    def DefFileOpen(self):
        try:
            #self, 파일 타이틀, 기본 디렉토리위치, 필터 종류들(;;로 구분), 디폴트 필터종류
            fO = QFileDialog.getOpenFileNames(self,"Open", './',"Images (*.png *.jpg *bmp *jpeg)","Images (*.png *.jpg *bmp *jpeg)")
            # qm = QMessageBox.question(self, 'Test', fO[0], QMessageBox.Yes|QMessageBox.No)
            for i in fO[0]:
                # print(i.split('/')[-1]) #주소에서 맨뒤만 이미지이름으로 가져옴.
                self.ImageConvert(i)
            # print(self.imageList)  
            #this?
            self.textList.setText(self.imageList) 
            #or this?
            for i in self.imageList:                               
                self.textList.addItem(i)#insertItem(self.numbering, i) #.lstrip('[]')특정 문자열 삭제    
                #If using addItem, not need
                #self.numbering += 1 
        except:
            QMessageBox.question(self, 'Error', 'Error', QMessageBox.Yes)            

    def ImageConvert(self, img):
        imgs = Image.open(img)
        imgsC = imgs.convert('RGB')
        self.imageList.append(imgsC)

    def FunClearBtn(self):      
        try:
            resetM = QMessageBox.question(self, 'Do', 'Do you want reset ImageList?',QMessageBox.Yes|QMessageBox.No)
            if resetM == QMessageBox.Yes:
                self.imageList.clear()
                self.textList.clear()
                #self.numbering = 0
                QMessageBox.question(self, 'Success', 'Success Image List Clear', QMessageBox.Yes)
            else:
                self.MessageCancel()       
        except:
            QMessageBox.question(self, 'Error', 'Error', QMessageBox.Yes)

    def FunConImg(self):
        naming = './'+self.textEdt.toPlainText()+'.pdf'
        messNY
        if os.path.exists(naming):
            messNY = QMessageBox.question(self, 'Want?', 'The same file exists, Do you want to cover it up?',QMessageBox.Yes|QMessageBox.No) 
        if messNY == QMessageBox.No:
            self.MessageCancel()  
        else:                   
            self.imageList[0].save(naming, save_all=True, append_images=self.imageList[1:])
            QMessageBox.question(self, 'Success', 'Success Image To PDF', QMessageBox.Yes)
            
    def FunSelDel(self):
        if self.textList.currentItem() is None:
            QMessageBox.question(self, 'Empty', 'Not Selected', QMessageBox.Yes)
        else:
            delList = self.textList.currentItem()
            try:
                selDelMsg = QMessageBox.question(self, 'Want?', delList.text() + ", Do you want to Delete?", QMessageBox.Yes|QMessageBox.No)
                if selDelMsg = QMessageBox.Yes:#del
                    self.textList.takeItem( self.textList.currentRow() )
                else:
                    self.MessageCancel()
            except:            
                QMessageBox.question(self, 'Error', 'Error', QMessageBox.Yes)
        
        
    def MessageCancel(self):
        QMessageBox.question(self, 'RollBack', 'This Cancelled', QMessageBox.Yes)


app = QApplication(sys.argv)
ex = BTP()
sys.exit(app.exec_())
