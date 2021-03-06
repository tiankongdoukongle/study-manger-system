# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shanchu.ui'
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
        MainWindow.setStyleSheet("background-image: url(微信图片_20220430232135.png);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 171, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 100, 71, 31))
        self.label_2.setStyleSheet("border-radius: 10px;  border: 2px groove gray;\n"
"border-style: outset;\n"
"")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 100, 121, 31))
        self.lineEdit.setStyleSheet("border-radius: 10px;  border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 100, 71, 31))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton.setStyleSheet("border-radius: 10px;  border: 2px groove gray;\n"
"border-style: outset;\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 100, 71, 31))
        self.pushButton_2.setStyleSheet("border-radius: 10px;  border: 2px groove gray;\n"
"border-style: outset;\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(60, 210, 648, 181))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 0, 0, 0);")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
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
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.horizontalHeader().setStyleSheet("QHeaderView::section{background-color:rgb(255, 0,0, 0);"
                                                          "font:11pt '宋体';color: black;};")
        self.tableWidget.verticalHeader().setStyleSheet("QHeaderView::section{background-color:rgb(255, 0,0, 0);"
                                                        "font:11pt '宋体';color: black;};")
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.chaxun)
        self.pushButton_2.clicked.connect(self.shanchu)


    def chaxun(self):
        cno1 = self.lineEdit.text()
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="987433",
            database="keshe01",
            charset="utf8"
        )
        sql1 = ("select * from `course` where course.cno = '%s'") % (cno1)
        cursor1 = conn.cursor()  # 得到一个可执行的游标对象
        cursor1.execute(sql1)
        data1 = cursor1.fetchall()
        if  cno1 != '':
            try:
                self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(str(data1[0][0])))
                self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(data1[0][1]))
                self.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem(str(data1[0][2])))
                self.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem(str(data1[0][3])))
                self.tableWidget.setItem(0, 4, QtWidgets.QTableWidgetItem(str(data1[0][4])))
            except:
                QtWidgets.QMessageBox.information(self, '失败', '不存在此课程', QtWidgets.QMessageBox.Yes |
                                                  QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes)
        cursor1.close()
        conn.close()

    def shanchu(self):
        cno1 = self.lineEdit.text()
        conn = pymysql.connect(host="localhost", user="root", password="987433", database="keshe01", charset="utf8")
        sql1 = ("delete  from `course` where course.cno = '%s'") % (cno1)
        cursor1 = conn.cursor()  # 得到一个可执行的游标对象
        if cno1 != '':
            sql2=("set foreign_key_checks = 0")
            sql3=("set foreign_key_checks = 1")
            cursor1.execute(sql2)
            try:
                reply = QtWidgets.QMessageBox.question(self, '提示', '确定删除吗', QtWidgets.QMessageBox.Yes |
                                                       QtWidgets.QMessageBox.No)
                if (reply == QtWidgets.QMessageBox.Yes):
                    cursor1.execute(sql1)
                    conn.commit()
                    cursor1.execute(sql3)
                    cursor1.close()
                    conn.close()
                    QtWidgets.QMessageBox.information(self, '成功', '删除成功', QtWidgets.QMessageBox.Yes |
                                                      QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes)
                elif (reply == QtWidgets.QMessageBox.No):
                    cursor1.execute(sql3)
                    cursor1.close()
                    conn.close()


            except:
                QtWidgets.QMessageBox.information(self, '失败', '删除失败', QtWidgets.QMessageBox.Yes |
                                                  QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">课程信息删除</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">课程号</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "查询"))
        self.pushButton_2.setText(_translate("MainWindow", "删除"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "课程号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "课程名称"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "学时"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "学分"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "先修课程号"))

