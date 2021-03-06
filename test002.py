# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test002.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

# 主窗口，显示主界面的功能
from PyQt5 import QtCore, QtGui, QtWidgets
import chaxun
import zengjia01
import shanchu3
import xiugai
import classzengjia
import classxiugai1
import classshanchu
import graderandom
import classrandom1
import jiangxuejin
import baobiao
import history
class test1(chaxun.Ui_MainWindow,QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.update()
        self.bujige()
class test2(shanchu3.Ui_MainWindow,QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.chaxun()
        self.delete()
class test3(xiugai.Ui_MainWindow,QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.chaxun()

class test4(zengjia01.Ui_MainWindow,QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.add()
class test5(classrandom1.Ui_MainWindow,QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.chaxun()

class test6(graderandom.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.updatetable()


class test7(classshanchu.Ui_MainWindow,QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.shanchu()
class test8(classxiugai1.Ui_MainWindow,QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.xiugai()
        self.chaxun()
class test9(classzengjia.Ui_MainWindow,QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.add()
class test10(jiangxuejin.Ui_MainWindow,QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class test11(baobiao.Ui_MainWindow,QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
class test12(history.Ui_MainWindow,QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.infomation()

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.setFixedSize(960, 700)
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局
        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.left_widget.setLayout(self.left_layout)  # 设置左侧部件布局为网格
        self.left_widget.setStyleSheet("background-image: url(微信图片_20220430232135.png);")
        self.right_widget = QtWidgets.QStackedWidget() # 创建堆栈窗口
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为网格
        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2)  # 左侧窗口大小
        self.main_layout.addWidget(self.right_widget, 0, 2, 12, 10)  # 右侧窗口大小
        self.setCentralWidget(self.main_widget)  # 设置窗口主部件
        self.left_close = QtWidgets.QPushButton("")  # 关闭按钮
        self.left_close.clicked.connect(self.close)  # 关闭窗口
        self.left_mini = QtWidgets.QPushButton("")  # 最小化按钮
        self.left_mini.clicked.connect(self.showMinimized)  # 最小化窗口



        self.left_widget.setStyleSheet('''
                   QPushButton{border:none;color:white;}
                   
                   QPushButton#left_label{
                       border:none;
                       border-bottom:1px solid SteelBlue;
                       font-size:18px;
                       font-weight:700;
                       font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
                    
                   }
                   QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}

                   QWidget#left_widget{
                       background:SteelBlue;
                       background-image: url(微信图片_20220430232135.png);
                       border-top:1px solid white;
                       border-bottom:1px solid white;
                       border-left:1px solid white;
                       border-top-left-radius:10px;
                       border-bottom-left-radius:10px;
                   }
               ''')
        # 右边栏美化
        # 右边框整体风格美化
        self.right_widget.setStyleSheet('''
          QWidget#right_widget{
            color:#232C51;
            background:white;
            border-top:1px solid darkGray;
            border-bottom:1px solid darkGray;
            border-right:1px solid darkGray;
            border-top-right-radius:10px;
            border-bottom-right-radius:10px;
          }
          QLabel#right_lable{
            border:none;
            font-size:16px;
            font-weight:700;
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
          }
        ''')

        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明

        self.main_widget.setStyleSheet('''
        QWidget#left_widget{
        background:gray;
        border-top:1px solid white;
        border-bottom:1px solid white;
        border-left:1px solid white;
        border-top-left-radius:10px;
        border-bottom-left-radius:10px;
        }
        ''')
        self.main_layout.setSpacing(0)
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框

        self.list = QtWidgets.QListWidget()
        self.list.setMaximumWidth(100)
        self.list.setStyleSheet("background-image: url(微信图片_20220430232135.png);")
        # 设置列表内容（stack的索引）
        self.list.insertItem(0, '成绩查询')
        self.list.insertItem(1, '学生信息删除')
        self.list.insertItem(2, '学生信息修改')
        self.list.insertItem(3, '学生信息增加')
        self.list.insertItem(4, '班级排名')
        self.list.insertItem(5, '成绩排名')
        self.list.insertItem(6, '课程信息删除')
        self.list.insertItem(7, '课程信息修改')
        self.list.insertItem(8, '课程信息增加')
        self.list.insertItem(9, '奖学金统计')
        self.list.insertItem(10,'报表输出及维护')
        self.list.insertItem(11,'历史学生')

        self.left_layout.addWidget(self.list)
        self.stack1 = test1()
        self.stack2 = test2()
        self.stack3 = test3()
        self.stack4 = test4()
        self.stack5 = test5()
        self.stack6 = test6()
        self.stack7 = test7()
        self.stack8 = test8()
        self.stack9 = test9()
        self.stack10=test10()
        self.stack11=test11()
        self.stack12=test12()

        self.right_widget.addWidget(self.stack1)
        self.right_widget.addWidget(self.stack2)
        self.right_widget.addWidget(self.stack3)
        self.right_widget.addWidget(self.stack4)
        self.right_widget.addWidget(self.stack5)
        self.right_widget.addWidget(self.stack6)
        self.right_widget.addWidget(self.stack7)
        self.right_widget.addWidget(self.stack8)
        self.right_widget.addWidget(self.stack9)
        self.right_widget.addWidget(self.stack10)
        self.right_widget.addWidget(self.stack11)
        self.right_widget.addWidget(self.stack12)
        self.list.currentRowChanged.connect(self.stackSwitch)

    def stackSwitch(self, index):
        self.right_widget.setCurrentIndex(index)
