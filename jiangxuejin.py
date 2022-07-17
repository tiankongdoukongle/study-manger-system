from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 700)
        MainWindow.setMinimumSize(QtCore.QSize(850, 700))
        MainWindow.setMaximumSize(QtCore.QSize(850, 700))
        MainWindow.setStyleSheet("background-image: url(微信图片_20220430232135.png);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(500, 30, 100, 30))
        self.pushButton1.setStyleSheet("border-radius: 22px;  border: 2px groove gray;\n")
        self.pushButton1.setObjectName("pushButton")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 120, 671, 391))
        self.tableWidget.setStyleSheet("border-top:0px solid #e8f3f9;background:  transparent; ")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(2, item)
        # item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 30, 141, 31))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 850, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.tableWidget.horizontalHeader().setStyleSheet("QHeaderView::section{background-color:rgb(255, 0,0, 0);"
                                                          "font:11pt '宋体';color: black;};")
        self.tableWidget.verticalHeader().setStyleSheet("QHeaderView::section{background-color:rgb(255, 0,0, 0);"
                                                        "font:11pt '宋体';color: black;};")

        self.pushButton1.clicked.connect(self.charu)
    def charu(self):
        conn = pymysql.connect(host="localhost", user="root", password="987433", database="keshe01", charset="utf8")
        cursor = conn.cursor()
        sql1 = ("select student.sno,student.sname from student,choose where student.sno=choose.sno "
                "GROUP BY student.sno ORDER BY sum(choose.score) desc ")
        cursor.execute(sql1)
        data1 = cursor.fetchall()
        self.tableWidget.setRowCount(20)
        # 插入国家奖学金
        self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(str(data1[0][0])))
        self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(str(data1[0][1])))
        self.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem(str('国家奖学金')))
        self.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem(str('2000')))
        for i in range(1,5):
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(data1[i][0])))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(data1[i][1])))
            self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str('一等奖学金')))
            self.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str('1000')))
        for i in range(5,10):
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(data1[i][0])))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(data1[i][1])))
            self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str('二等奖学金')))
            self.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str('600')))
        for i in range(10,20):
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(data1[i][0])))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(data1[i][1])))
            self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str('三等奖学金')))
            self.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str('300')))
        cursor.close()
        conn.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton1.setText(_translate("MainWindow", "查询"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "学号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "姓名"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "奖学金等级"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "奖学金数目"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">奖学金统计</span></p></body></html>"))

