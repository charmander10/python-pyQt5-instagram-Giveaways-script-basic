from PyQt5 import QtCore, QtGui, QtWidgets
import time
from instapy import InstaPy
from instapy import smart_run
import resources


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(493, 685)
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        Form.setFont(font)
        Form.setFocusPolicy(QtCore.Qt.NoFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/ii.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("*{\n"
"    font-family:century gothic;\n"
"    font-size:24px;\n"
"}\n"
"\n"
"QFrame\n"
"{\n"
"    background:#242323;\n"
"    border-radius:15px;\n"
"}\n"
"\n"
"#Form\n"
"{\n"
"\n"
"    background:url(:/newPrefix/Blur.jpg);\n"
"}\n"
"\n"
"#pushButton\n"
"{\n"
"background:red;\n"
"border-radius:15px;\n"
"color:white;\n"
"}\n"
"\n"
"#toolButton\n"
"{\n"
"background:red;\n"
"border-radius:45px;\n"
"}\n"
"\n"
"#toolButton_2\n"
"{\n"
"background:white;\n"
"border-radius:25px;\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"    color:white;\n"
"    background:transparent;\n"
"}\n"
"\n"
"#pushButton:hover\n"
"{\n"
"color:red;\n"
"border-radius:15px;\n"
"background:#49ebff;\n"
"}\n"
"\n"
"#lineEdit\n"
"{\n"
"background:transparent;\n"
"border:none;\n"
"color:#717072;\n"
"border-bottom:1px solid #717072;\n"
"}\n"
"\n"
"#lineEdit_2\n"
"{\n"
"background:transparent;\n"
"border:none;\n"
"color:#717072;\n"
"border-bottom:1px solid #717072;\n"
"}\n"
"\n"
"#lineEdit_3\n"
"{\n"
"background:transparent;\n"
"border:none;\n"
"color:#717072;\n"
"border-bottom:1px solid #717072;\n"
"}\n"
"\n"
"\n"
"#lineEdit_6\n"
"{\n"
"background:transparent;\n"
"border:none;\n"
"color:#717072;\n"
"border-bottom:1px solid #717072;\n"
"}\n"
"\n"
"#lineEdit_7\n"
"{\n"
"background:transparent;\n"
"border:none;\n"
"color:#717072;\n"
"border-bottom:1px solid #717072;\n"
"}\n"
"#lineEdit_11\n"
"{\n"
"background:transparent;\n"
"border:none;\n"
"color:#717072;\n"
"border-bottom:1px solid #717072;\n"
"}")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(30, 70, 421, 601))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(70, 530, 291, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.Baslat)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(150, 20, 131, 41))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(30, 60, 371, 121))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(20, 20, 331, 31))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 70, 331, 31))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setCursorPosition(0)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(100, 180, 251, 41))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 220, 371, 181))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 20, 341, 31))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(10, 70, 341, 31))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_7.setGeometry(QtCore.QRect(10, 120, 341, 31))
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(110, 400, 251, 41))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_3.setGeometry(QtCore.QRect(30, 440, 371, 80))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_11.setGeometry(QtCore.QRect(10, 20, 341, 31))
        self.lineEdit_11.setText("")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.toolButton = QtWidgets.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(80, 30, 91, 91))
        self.toolButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/Daco_67009.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon1)
        self.toolButton.setIconSize(QtCore.QSize(128, 128))
        self.toolButton.setObjectName("toolButton")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(250, 20, 231, 31))
        self.label_4.setObjectName("label_4")
        self.toolButton_2 = QtWidgets.QToolButton(Form)
        self.toolButton_2.setGeometry(QtCore.QRect(200, 10, 51, 51))
        self.toolButton_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/tt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon2)
        self.toolButton_2.setIconSize(QtCore.QSize(128, 128))
        self.toolButton_2.setObjectName("toolButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "İnstagram Çekiliş Botu v2.0 by12NumaraVolkan"))
        self.pushButton.setText(_translate("Form", "BAŞLAT"))
        self.label.setText(_translate("Form", " GİRİŞ YAP"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Kullanıcı Adı"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Şifre"))
        self.label_2.setText(_translate("Form", "YORUM AYARLARI"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "Kullanıcı çekilecek hesap"))
        self.lineEdit_6.setPlaceholderText(_translate("Form", "Etiketlencek kullanıcı sayısı"))
        self.lineEdit_7.setPlaceholderText(_translate("Form", "Yapılacak yorum sayısı"))
        self.label_3.setText(_translate("Form", "ÇEKİLİŞ AYARLARI"))
        self.lineEdit_11.setPlaceholderText(_translate("Form", "Çekiliş linki"))
        self.label_4.setText(_translate("Form", "@12NumaraVolkan"))

    def Baslat(self, Form):

        accounts = [self.lineEdit_11.text()]
        kisi = self.lineEdit_6.text()
        yorum = self.lineEdit_7.text()
        n = int(kisi) * int(yorum)
        cekusername = self.lineEdit_3.text()
        session = InstaPy(username=self.lineEdit.text(), password=self.lineEdit_2.text())

        a = 0
        b = 0
        c = 0
        d = 0
        e = 0
        f = 0

        with smart_run(session):
            followers = session.grab_followers(username=cekusername, amount=n+10, live_match=True, store_locally=True)
            for i in range(int(yorum)):
                if int(kisi) == 1:
                    commenttext = ["@" + followers[i]]
                elif int(kisi) == 2:
                    a = a + 2
                    commenttext = ["@" + followers[b]+" "+"@"+followers[b+1]]
                elif int(kisi) == 3:
                    b = b + 3
                    commenttext = ["@" + followers[b]+" "+"@"+followers[b+1]+" "+"@"+followers[b+3]]
                elif int(kisi) == 4:
                    c = c + 4
                    commenttext = ["@" + followers[c]+" "+"@"+followers[c+1]+" "+"@"+followers[c+2]+" "+"@"+followers[c+3]]
                elif int(kisi) == 5:
                    d = d + 5
                    commenttext = ["@" + followers[d]+" "+"@"+followers[d+1]+" "+"@"+followers[d+2]+" "+"@"+followers[d+3]+" "+"@"+followers[d+4]]
                elif int(kisi) == 6:
                    e = e + 6
                    commenttext = ["@" + followers[e]+" "+"@"+followers[e+1]+" "+"@"+followers[e+2]+" "+"@"+followers[e+3]+" "+"@"+followers[e+4]+" "+"@"+followers[e+5]]
                elif int(kisi) == 7:
                    f = f + 7
                    commenttext = ["@" + followers[f]+" "+"@"+followers[f+1]+" "+"@"+followers[f+2]+" "+"@"+followers[f+3]+" "+"@"+followers[f+4]+" "+"@"+followers[f+5]+" "+"@"+followers[f+6]]
                else:
                    print("Lütfen etiketlenecek kişi sayısına 1 ve 7 arasında rakam giriniz")

                session.set_comments(commenttext, media='Photo')
                session.set_do_comment(enabled=True, percentage=100)
                session.interact_by_URL(urls=accounts, randomize=False, interact=True)
                time.sleep(270)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())