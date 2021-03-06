# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chaxun1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
import pandas as pd
from sqlalchemy import  create_engine
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 700)
        MainWindow.setMinimumSize(QtCore.QSize(850, 700))
        MainWindow.setMaximumSize(QtCore.QSize(850, 700))
        MainWindow.setStyleSheet("background-image: url(微信图片_20220527085047.png);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 111, 31))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 150, 141, 31))
        self.lineEdit.setStyleSheet("border-radius: 10px;  border: 2px groove gray;\n"
"border-style: outset;\n"
"border-top:0px solid #e8f3f9;background:  transparent; ")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 150, 93, 31))
        self.pushButton.setStyleSheet("border-radius: 10px;  border: 2px groove gray;\n"
"border-style: outset;"
                                      )
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(480, 150, 93, 31))
        self.pushButton_2.setStyleSheet("border-radius: 10px;  border: 2px groove gray;\n"
                        "border-style: outset;"

                                        )
        self.pushButton_2.setObjectName("pushButton_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 280, 591, 241))
        self.tableWidget.setStyleSheet("border-top:0px solid #e8f3f9;background:  transparent; "
                                       "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  # 按下时的样式
        )
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
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
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(30, 150, 71, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 850, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        # 将tablewidget的表头变透明
        self.tableWidget.horizontalHeader().setStyleSheet("QHeaderView::section{background-color:rgb(255, 0,0, 0);"
                                                          "font:11pt '宋体';color: black;};")
        self.tableWidget.verticalHeader().setStyleSheet("QHeaderView::section{background-color:rgb(255, 0,0, 0);"
                                                        "font:11pt '宋体';color: black;};")
        self.comboBox.setStyleSheet("border-radius: 13px;  border: 2px groove gray;\n"
                                    "border-style: outset;\n")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.update)
        self.pushButton_2.clicked.connect(self.bujige)
    def update(self):
        conn = pymysql.connect(host="localhost",user="root",password="987433",database="keshe01",charset="utf8")# 连接数据库
        cursor = conn.cursor()  # 得到一个可执行的游标对象
        name = self.lineEdit.text()
        xuanxiang = self.comboBox.currentText()
        if xuanxiang == '姓名':
            if name != '':
                sql = "select student.sno,student.sname,course.cname,choose.score from student left JOIN choose on " \
                      "choose.sno = student.sno LEFT JOIN course on course.cno=choose.cno where student.sname ='%s'" % \
                      (name)
                cursor.execute(sql)
                data = cursor.fetchall()
                row_num = len(data)
                self.tableWidget.setRowCount(row_num)
                for row in range(row_num):
                    self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(data[row][0])))
                    self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(data[row][1]))
                    self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(data[row][2])))
                    self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(data[row][3])))
        else:
            if name != '':
                sql = "select student.sno,student.sname,course.cname,choose.score from student left JOIN choose on " \
                      "choose.sno = student.sno LEFT JOIN course on course.cno=choose.cno where student.sno ='%s'" \
                      % (name)
                cursor.execute(sql)
                data = cursor.fetchall()
                row_num = len(data)
                self.tableWidget.setRowCount(row_num)
                for row in range(row_num):
                    self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(data[row][0])))
                    self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(data[row][1]))
                    self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(data[row][2])))
                    self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(data[row][3])))
    def bujige(self):
        conn = pymysql.connect(host="localhost", user="root", password="987433",database="keshe01",charset="utf8")
        cursor = conn.cursor()  # 得到一个可执行的游标对象
        sql=("select student.sno,student.sname,course.cname,choose.score from student left JOIN "
             "choose on choose.sno = student.sno LEFT JOIN course on course.cno=choose.cno where choose.score<'60' ")
        cursor.execute(sql) # 执行sql语句
        data = cursor.fetchall() # 获取数据库查询得到的信息
        row_num = len(data)
        self.tableWidget.setRowCount(row_num)
        for row in range(row_num):# for循环将数据插入表格
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(data[row][0])))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(data[row][1]))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(data[row][2])))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(data[row][3])))


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">成绩查询</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "查询"))
        self.pushButton_2.setText(_translate("MainWindow", "查询不及格"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "学号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "姓名"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "课程名称"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "成绩"))
        self.comboBox.setItemText(0, _translate("MainWindow", "学号"))
        self.comboBox.setItemText(1, _translate("MainWindow", "姓名"))
