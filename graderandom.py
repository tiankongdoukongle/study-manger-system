# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graderandom.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 700)
        MainWindow.setMinimumSize(QtCore.QSize(850, 700))
        MainWindow.setMaximumSize(QtCore.QSize(850, 700))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                 "background-image: url(微信图片_20220501225953.png);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(150, 70, 141, 30))
        self.comboBox.setStyleSheet("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 70, 141, 30))
        self.pushButton.setStyleSheet("border-radius: 10px;  border: 2px groove gray;\n"
                                        "border-style: outset;")
        self.pushButton.setObjectName("pushButton")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 130, 421, 471))
        self.tableWidget.setStyleSheet("border-top:0px solid #e8f3f9;background:  transparent; ")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 111, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 101, 31))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 850, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.tableWidget.horizontalHeader().setStyleSheet("QHeaderView::section{background-color:rgb(255, 0,0, 0);"
                                                          "font:11pt '宋体';color: black;};")
        self.tableWidget.verticalHeader().setStyleSheet("QHeaderView::section{background-color:rgb(255, 0,0, 0);"
                                                        "font:11pt '宋体';color: black;};")
        self.comboBox.setStyleSheet("border-radius: 13px;  border: 2px groove gray;\n"
                                    "border-style: outset;\n"
                                    )
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.updatetable)
    def updatetable(self):
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="987433",
            database="keshe01",
            charset="utf8"
        )
        cursor = conn.cursor()  # 得到一个可执行的游标对象
        xuanxiang = self.comboBox.currentText()
        if xuanxiang == '个人总成绩':
            sql1=("select student.sno,student.sname,sum(score) from student,choose "
                  "where choose.sno=student.sno GROUP BY student.sno order by sum(score) desc ")
            cursor.execute(sql1)

            data1 = cursor.fetchall()
            row_num = len(data1)
            self.tableWidget.setRowCount(row_num)
            for row in range(row_num):
                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(data1[row][0])))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(data1[row][1]))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(data1[row][2])))
        elif(xuanxiang=='个人平均成绩'):
            sql1 = ("select student.sno,student.sname,avg(score) from student,choose "
                    "where choose.sno=student.sno GROUP BY student.sno order by sum(score) desc ")
            cursor.execute(sql1)
            data1 = cursor.fetchall()
            row_num = len(data1)
            self.tableWidget.setRowCount(row_num)
            for row in range(row_num):
                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(data1[row][0])))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(data1[row][1]))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(data1[row][2])))
        elif(xuanxiang=='数据结构成绩'):
            sql1 = ("select student.sno,student.sname,choose.score from student,choose "
                    "where choose.sno=student.sno and choose.cno='100' GROUP BY student.sno order by score desc ")
            cursor.execute(sql1)
            data1 = cursor.fetchall()
            row_num = len(data1)
            self.tableWidget.setRowCount(row_num)
            for row in range(row_num):
                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(data1[row][0])))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(data1[row][1]))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(data1[row][2])))
        elif (xuanxiang == '计算机网络成绩'):
            sql1 = ("select student.sno,student.sname,choose.score from student,choose "
                    "where choose.sno=student.sno and choose.cno='101' GROUP BY student.sno order by score desc ")
            cursor.execute(sql1)
            data1 = cursor.fetchall()
            row_num = len(data1)
            self.tableWidget.setRowCount(row_num)
            for row in range(row_num):
                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(data1[row][0])))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(data1[row][1]))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(data1[row][2])))
        elif (xuanxiang == '大学物理成绩'):
            sql1 = ("select student.sno,student.sname,choose.score from student,choose "
                    "where choose.sno=student.sno and choose.cno='102' GROUP BY student.sno order by score desc ")
            cursor.execute(sql1)
            data1 = cursor.fetchall()
            row_num = len(data1)
            self.tableWidget.setRowCount(row_num)
            for row in range(row_num):
                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(data1[row][0])))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(data1[row][1]))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(data1[row][2])))

        elif (xuanxiang == '大学英语成绩'):
            sql1 = ("select student.sno,student.sname,choose.score from student,choose "
                    "where choose.sno=student.sno and choose.cno='103' GROUP BY student.sno order by score desc ")
            cursor.execute(sql1)
            data1 = cursor.fetchall()
            row_num = len(data1)
            self.tableWidget.setRowCount(row_num)
            for row in range(row_num):
                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(data1[row][0])))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(data1[row][1]))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(data1[row][2])))
        elif (xuanxiang == '大学体育成绩'):
            sql1 = ("select student.sno,student.sname,choose.score from student,choose "
                    "where choose.sno=student.sno and choose.cno='104' GROUP BY student.sno order by score desc ")
            cursor.execute(sql1)
            data1 = cursor.fetchall()
            row_num = len(data1)
            self.tableWidget.setRowCount(row_num)
            for row in range(row_num):
                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(data1[row][0])))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(data1[row][1]))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(data1[row][2])))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "个人总成绩"))
        self.comboBox.setItemText(1, _translate("MainWindow", "个人平均成绩"))
        self.comboBox.setItemText(2, _translate("MainWindow", "数据结构成绩"))
        self.comboBox.setItemText(3, _translate("MainWindow", "计算机网络成绩"))
        self.comboBox.setItemText(4, _translate("MainWindow", "大学物理成绩"))
        self.comboBox.setItemText(5, _translate("MainWindow", "大学英语成绩"))
        self.comboBox.setItemText(6, _translate("MainWindow", "大学体育成绩"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "学号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "姓名"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "成绩"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" "
                                                    "font-size:16pt; font-weight:600;\">成绩排名</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">排名方式</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "查询"))