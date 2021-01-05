import math
from PyQt5 import QtCore, QtGui, QtWidgets
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

dizi = []
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(406, 493)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 331, 91))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(120, 20, 121, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 50, 121, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 20, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setObjectName("label_2")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 130, 331, 161))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 50, 241, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 251, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 80, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(20, 120, 241, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.groupBox_4 = QtWidgets.QGroupBox(Form)
        self.groupBox_4.setGeometry(QtCore.QRect(30, 290, 331, 141))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setGeometry(QtCore.QRect(20, 20, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setGeometry(QtCore.QRect(20, 60, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setTextFormat(QtCore.Qt.AutoText)
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setGeometry(QtCore.QRect(20, 95, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setTextFormat(QtCore.Qt.AutoText)
        self.label_7.setObjectName("label_7")

        self.spinBox = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBox.setGeometry(QtCore.QRect(270, 20, 51, 22))
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setMaximum(5)
        self.spinBox_2 = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBox_2.setGeometry(QtCore.QRect(230, 65, 81, 22))
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_2.setMaximum(500)
        self.spinBox_3 = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBox_3.setGeometry(QtCore.QRect(230, 100, 81, 22))
        self.spinBox_3.setObjectName("spinBox_3")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(260, 440, 81, 31))
        self.pushButton.clicked.connect(self.baslat)

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "İnstagram Çekiliş Botu v1.0 by12NumaraVolkan"))
        self.groupBox.setTitle(_translate("Form", "İnstagram"))
        self.label.setText(_translate("Form", "Kullanıcı Adı :"))
        self.label_2.setText(_translate("Form", "Şifre               :"))
        self.groupBox_2.setTitle(_translate("Form", "Linkler"))
        self.label_3.setText(_translate("Form", "Kullanıcı çekilecek gönderi linki :"))
        self.label_4.setText(_translate("Form", "Çekiliş linki :"))
        self.groupBox_4.setTitle(_translate("Form", "Kişiler"))
        self.label_5.setText(_translate("Form", "Yoruma etiketlenecek kişi sayısı :"))
        self.label_6.setText(_translate("Form", "Yapılacak yorum sayısı :"))
        self.label_7.setText(_translate("Form", "Yorumlar arası süre (dakika) :"))
        self.pushButton.setText(_translate("Form", "Başlat"))

    def baslat (self, Form):
        PATH = "C:\Program Files (x86)\chromedriver.exe"
        driver = webdriver.Chrome(PATH)
        driver.get("https://instagram.com")
        sleep(1)
        driver.find_element_by_xpath("//input[@name='username']") \
            .send_keys(self.lineEdit.text())
        driver.find_element_by_xpath("//input[@name='password']") \
            .send_keys(self.lineEdit_2.text())
        driver.find_element_by_xpath("//button[@type='submit']") \
            .click()
        sleep(3)
        driver.find_element_by_xpath("//button[@type='button']") \
            .click()
        sleep(2)
        driver.get(self.lineEdit_3.text())
        sleep(1)
        driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[2]/div/div/button") \
            .click()
        sleep(2)

        kisi = self.spinBox.text()
        yorum = self.spinBox_2.text()
        p = int(kisi)*int(yorum)
        z = math.ceil(int(p) / 10)
        for i in range(z):
            for j in range(12):
                k1 = driver.find_element_by_xpath(f"/html/body/div[5]/div/div/div[2]/div/div/div[{j+1}]/div[2]/div[1]/div/span/a").text
                dizi.append(k1)
                k11 = ActionChains(driver)
                k11.send_keys(Keys.TAB * 13)
                k11.perform()

        sleep(1)
        driver.get(self.lineEdit_4.text())
        sleep(2)


        t = int(kisi)

        a = 0
        b = 0
        c = 0
        d = 0
        n = int((self.spinBox_3.text()))*60
        for i in range(z*10):
            if t == 1:
                commentArea = driver.find_element_by_class_name('Ypffh')
                commentArea.click()
                sleep(1)
                commentArea = driver.find_element_by_class_name('Ypffh')
                commentArea.click()
                commentArea.send_keys("@"+dizi[i])
                sleep(1)
                driver.find_element_by_xpath("//button[@type='submit']") \
                    .click()
                sleep(int(n))
            elif t == 2:
                a = a + 2
                commentArea = driver.find_element_by_class_name('Ypffh')
                commentArea.click()
                sleep(1)
                commentArea = driver.find_element_by_class_name('Ypffh')
                commentArea.click()
                commentArea.send_keys("@"+dizi[a]," @"+dizi[a+1])
                sleep(1)
                driver.find_element_by_xpath("//button[@type='submit']") \
                    .click()
                sleep(int(n))
            elif t == 3:
                b = b + 3
                commentArea = driver.find_element_by_class_name('Ypffh')
                commentArea.click()
                sleep(1)
                commentArea = driver.find_element_by_class_name('Ypffh')
                commentArea.click()
                commentArea.send_keys("@"+dizi[b]," @"+dizi[b+1]," @"+dizi[b+2])
                sleep(1)
                driver.find_element_by_xpath("//button[@type='submit']") \
                    .click()
                sleep(int(n))
            elif t == 4:
                c = c + 4
                commentArea = driver.find_element_by_class_name('Ypffh')
                commentArea.click()
                sleep(1)
                commentArea = driver.find_element_by_class_name('Ypffh')
                commentArea.click()
                commentArea.send_keys("@"+dizi[c]," @"+dizi[c+1]," @"+dizi[c+2]," @"+dizi[c+3])
                sleep(1)
                driver.find_element_by_xpath("//button[@type='submit']") \
                    .click()
                sleep(int(n))
            elif t == 5:
                d = d +5
                commentArea = driver.find_element_by_class_name('Ypffh')
                commentArea.click()
                sleep(1)
                commentArea = driver.find_element_by_class_name('Ypffh')
                commentArea.click()
                commentArea.send_keys("@"+dizi[d]," @"+dizi[d+1]," @"+dizi[d+2]," @"+dizi[d+3]," @"+dizi[d+4])
                sleep(1)
                driver.find_element_by_xpath("//button[@type='submit']") \
                    .click()
                sleep(int(n))
        driver.quit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())