import sys
import test002
import test0001
from PyQt5.QtWidgets import QApplication,QMainWindow,QDialog
from PyQt5 import QtCore,QtWidgets
class Mainwindow(test002.Ui_MainWindow,QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
class Loginwindow(test0001.Ui_MainWindow,QMainWindow):
    def __init__(self):
        super(Loginwindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_pushButton_enter_clicked)
    def on_pushButton_enter_clicked(self):
        # 账号判断
        account_dict = {}
        f = open("1.txt", 'r+')
        for line in f:
            (keys, value) = line.strip().split()
            account_dict[keys] = value
        account1 = self.lineEdit.text()
        password1 = self.lineEdit_2.text()
        account_keys = list(account_dict.keys())
        if account1 != "" and password1 != "":
            if account1 not in account_keys:
                QtWidgets.QMessageBox.information(self, '登录出错', '用户不存在',
                                                           QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                 QtWidgets.QMessageBox.Yes)

            elif password1 == account_dict[account1]:
                # 通过验证，关闭对话框并返回1
                self.close()
                mainwindow.show()
            else:
                QtWidgets.QMessageBox.information(self, '登录出错', '密码错误', QtWidgets.QMessageBox.Yes |
                                                  QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes)
        else:
            QtWidgets.QMessageBox.information(self, '错误', '输入不能为空！', QtWidgets.QMessageBox.Yes
                                    | QtWidgets.QMessageBox.No,QtWidgets.QMessageBox.Yes)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = Mainwindow()
    loginwindow = Loginwindow()
    loginwindow.show()
    # 进入程序的主循环、并通过exit函数确保主循环安全结束
    sys.exit(app.exec())
