from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QMenu, QFileDialog, QSpinBox, QLineEdit, \
    QPushButton
from PyQt5.QtWidgets import QWidget, QToolButton, QApplication, QLabel, QMessageBox, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt, QSize, QVersionNumber, QT_VERSION_STR
from PyQt5.QtGui import QIcon, QFont, QPalette, QColor, QBrush, QPixmap, QImage
import sys
import os
import pandas as pd

import drawer


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.file_open = os.getcwd()
        self.run = QPushButton("运行", self)
        self.input_1 = QLineEdit(self)
        self.input_1.setText('100')
        self.sp3 = QLineEdit(self)
        self.sp2 = QSpinBox(self)
        self.sp1 = QSpinBox(self)
        self.Show = QLabel(self)
        self.Show2 = QLabel(self)
        self.Show1 = QLabel(self)
        self.ShowY = QLabel(self)
        self.ShowX = QLabel(self)
        self.title_iter = QLabel('迭代次数', self)
        self.title_rho = QLabel('信息素挥发', self)
        self.title_beta = QLabel('客观因子影响', self)
        self.title_alpha = QLabel('优化系数', self)
        self.title_para = QLabel('调参处', self)
        self.title_dev = QLabel('发达系数', self)
        self.title_x = QLabel('X坐标', self)
        self.title_y = QLabel('Y坐标', self)
        self.title_stop = QLabel('停滞量', self)
        self.InitUI()
        self.Function()
        self.setWindowIcon(QIcon('simulator.ico'))

    def InitUI(self):
        self.setGeometry(300, 80, 700, 630)
        self.setWindowTitle('基于混合群智能算法的物流分配系统')
        exitAct = QAction(QIcon('exit.jpg'), '退出(&E)', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('退出程序')
        exitAct.triggered.connect(qApp.quit)

        openAct = QAction(QIcon('new.jpg'), '打开(&N)', self)
        openAct.setShortcut('Ctrl+N')
        openAct.setStatusTip('新建文件')
        openAct.triggered.connect(self.open_file)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('文件(&F)')
        fileMenu.addAction(openAct)
        fileMenu.addSeparator()
        fileMenu.addAction(exitAct)

        openHelp = QAction('关于', self)
        openHelp.setShortcut('Ctrl+H')
        openHelp.setStatusTip('打开帮助')
        openHelp.triggered.connect(self.open_help)

        openTeam = QAction('制作团队', self)
        openTeam.setShortcut('F11')
        openTeam.setStatusTip('星火团队')
        openTeam.triggered.connect(self.open_team)

        aboutMenu = menubar.addMenu('关于(&A)')
        aboutMenu.addAction(openHelp)
        aboutMenu.addAction(openTeam)

        toolbar = self.addToolBar('工具栏')
        toolbar.addAction(openAct)
        toolbar.addAction(exitAct)
        # self.show()

    def Function(self):
        self.title_x.setFont(QFont("Times_New_Romance", 13))
        # self.title.resize(100, 50)
        self.title_x.setAlignment(Qt.AlignCenter)
        self.title_x.move(20, 70)

        self.title_y.setFont(QFont("Times_New_Romance", 13))
        # self.title.resize(100, 50)
        self.title_y.setAlignment(Qt.AlignCenter)
        self.title_y.move(100, 70)

        self.title_stop.setFont(QFont("Times_New_Romance", 13))
        # self.title.resize(100, 50)
        self.title_stop.setAlignment(Qt.AlignCenter)
        self.title_stop.move(190, 70)

        self.title_dev.setFont(QFont("Times_New_Romance", 13))
        # self.title.resize(100, 50)
        # self.title2.setAlignment(Qt.AlignCenter)
        self.title_dev.move(290, 70)

        self.title_para.setFont(QFont("Times_New_Romance", 13))
        # self.title.resize(100, 50)
        # self.title2.setAlignment(Qt.AlignCenter)
        self.title_para.move(500, 70)

        self.title_alpha.setFont(QFont("Times_New_Romance", 13))
        # self.title.resize(100, 50)
        # self.title2.setAlignment(Qt.AlignCenter)
        self.title_alpha.move(400, 130)

        self.title_beta.setFont(QFont("Times_New_Romance", 12))
        # self.title.resize(100, 50)
        # self.title2.setAlignment(Qt.AlignCenter)
        self.title_beta.move(400, 230)

        self.title_rho.setFont(QFont("Times_New_Romance", 10))
        self.title_rho.move(400, 330)

        self.title_iter.setFont(QFont("Times_New_Romance", 13))
        self.title_iter.move(400, 430)

        self.ShowX.setFont(QFont("Times_New_Romance", 13))
        self.ShowX.resize(80, 500)
        self.ShowX.move(20, 100)
        self.ShowX.setStyleSheet("border: 2px solid break;border-radius:25px")
        self.ShowX.setAlignment(Qt.AlignCenter)
        self.ShowX.setWordWrap(True)

        self.ShowY.setFont(QFont("Times_New_Romance", 13))
        self.ShowY.resize(80, 500)
        self.ShowY.move(110, 100)
        self.ShowY.setAlignment(Qt.AlignCenter)
        self.ShowY.setWordWrap(True)
        self.ShowY.setStyleSheet("border: 2px solid break;border-radius:25px")

        self.Show1.setFont(QFont("Times_New_Romance", 13))
        self.Show1.resize(80, 500)
        self.Show1.move(200, 100)
        self.Show1.setAlignment(Qt.AlignCenter)
        self.Show1.setWordWrap(True)
        self.Show1.setStyleSheet("border: 2px solid break;border-radius:25px")

        self.Show2.setFont(QFont("Times_New_Romance", 13))
        self.Show2.resize(80, 500)
        self.Show2.move(290, 100)
        self.Show2.setAlignment(Qt.AlignCenter)
        self.Show2.setWordWrap(True)
        self.Show2.setStyleSheet("border: 2px solid break;border-radius:25px")

        self.Show.setFont(QFont("Times_New_Romance", 20))
        self.Show.resize(280, 350)
        self.Show.move(400, 100)
        # self.Show.setStyleSheet("border: 2px solid red;border-radius:25px")

        self.sp1.setRange(0, 10)
        self.sp1.setSingleStep(20)
        self.sp1.setWrapping(True)
        self.sp1.setValue(3)
        self.sp1.move(500, 130)
        self.sp1.resize(150, 40)

        self.sp2.setRange(0, 10)
        self.sp2.setSingleStep(20)
        self.sp2.setWrapping(True)
        self.sp2.setValue(5)
        self.sp2.move(500, 230)
        self.sp2.resize(150, 40)

        self.sp3.move(500, 330)
        self.sp3.resize(150, 40)
        self.sp3.setText('0.2')
        self.sp3.setFont(QFont("Times_New_Romance", 13))

        self.input_1.move(500, 430)
        self.input_1.resize(150, 40)
        self.input_1.setFont(QFont("Times_New_Romance", 13))

        self.run.move(440, 500)
        self.run.setFont(QFont("Times_New_Romance", 40))
        self.run.resize(200, 100)
        self.run.clicked.connect(self.Next_start)
        self.show()

    def open_file(self):
        try:
            self.file_name = QFileDialog.getOpenFileName(self, "打开文件", self.file_open)
            print(self.file_name[0])
            data = pd.read_excel(self.file_name[0], header=None)
            x = list(data[1][2:12])
            y = list(data[2][2:12])
            r = list(data[3][2:12])
            c = list(data[4][2:12])
            x = str(x)[1:-1].replace(',', '\n\n')
            y = str(y)[1:-1].replace(',', '\n\n')
            r = str(r)[1:-1].replace(',', '\n\n')
            c = str(c)[1:-1].replace(',', '\n\n')
            self.ShowX.setText(str(x))
            self.ShowY.setText(str(y))
            self.Show1.setText(r)
            self.Show2.setText(c)
        except:
            pass

    def open_help(self):
        QMessageBox.information(self, '使用帮助', '打开文件选择excel文档，运行开始模拟')

    def open_team(self):
        QMessageBox.information(self, '制作团队', '指导老师：朱晓庆\n 项目成员：陈宇卿，陈研，陈冰，卓一康')

    def Next_start(self):
        self.close()
        drawer.run()
        self.ex = Example()


if __name__ == '__main__':
    v_compare = QVersionNumber(5, 6, 0)
    v_current, _ = QVersionNumber.fromString(QT_VERSION_STR)  # 获取当前Qt版本
    if QVersionNumber.compare(v_current, v_compare) >= 0:
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)  # Qt从5.6.0开始，支持High-DPI
        app = QApplication(sys.argv)
    else:
        app = QApplication(sys.argv)
        font = QFont("宋体")
        pointsize = font.pointSize()
        font.setPixelSize(pointsize * 90 / 72)
        app.setFont(font)
    ex = Example()
    sys.exit(app.exec_())
