# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui_mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(652, 582)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/icons/applogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setObjectName("mainLayout")
        self.groupBox_1 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_1.sizePolicy().hasHeightForWidth())
        self.groupBox_1.setSizePolicy(sizePolicy)
        self.groupBox_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox_1.setObjectName("groupBox_1")
        self.hLayout_M_g1 = QtWidgets.QHBoxLayout(self.groupBox_1)
        self.hLayout_M_g1.setObjectName("hLayout_M_g1")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_1 = QtWidgets.QLabel(self.groupBox_1)
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_1)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineEdit_1 = QtWidgets.QLineEdit(self.groupBox_1)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.gridLayout.addWidget(self.lineEdit_1, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_1)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_1)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 2, 1, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.groupBox_1)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout.addWidget(self.lineEdit_10, 4, 4, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_1)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 1, 1, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_1)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 3, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_1)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_1)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 0, 4, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_1)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 2, 4, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_1)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_1)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_1)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 4, 3, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_1)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 1, 4, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox_1)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout.addWidget(self.lineEdit_8, 3, 4, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_1)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox_1)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout.addWidget(self.lineEdit_9, 4, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_1)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_1)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.groupBox_1)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.gridLayout.addWidget(self.lineEdit_14, 6, 4, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox_1)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 6, 3, 1, 1)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.groupBox_1)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.gridLayout.addWidget(self.lineEdit_13, 6, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox_1)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 6, 0, 1, 1)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.groupBox_1)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout.addWidget(self.lineEdit_12, 5, 4, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_1)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 7, 4, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.groupBox_1)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 7, 3, 1, 1)
        self.comboBox_1 = QtWidgets.QComboBox(self.groupBox_1)
        self.comboBox_1.setObjectName("comboBox_1")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.gridLayout.addWidget(self.comboBox_1, 7, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.groupBox_1)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 7, 0, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.groupBox_1)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout.addWidget(self.lineEdit_11, 5, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_1)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 5, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_1)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 5, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(50, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.hLayout_M_g1.addLayout(self.gridLayout)
        self.mainLayout.addWidget(self.groupBox_1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.hLayout_M_g2 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.hLayout_M_g2.setContentsMargins(0, 0, 0, 0)
        self.hLayout_M_g2.setSpacing(0)
        self.hLayout_M_g2.setObjectName("hLayout_M_g2")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser.setEnabled(True)
        self.textBrowser.setMaximumSize(QtCore.QSize(10000, 10000))
        self.textBrowser.setObjectName("textBrowser")
        self.hLayout_M_g2.addWidget(self.textBrowser)
        self.mainLayout.addWidget(self.groupBox_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_2.addWidget(self.label_17)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_2.addWidget(self.progressBar)
        self.mainLayout.addLayout(self.horizontalLayout_2)
        self.mainLayout.setStretch(0, 12)
        self.mainLayout.setStretch(1, 8)
        self.mainLayout.setStretch(2, 1)
        self.verticalLayout_6.addLayout(self.mainLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar_1 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_1.setIconSize(QtCore.QSize(24, 24))
        self.toolBar_1.setObjectName("toolBar_1")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_1)
        self.toolBar_2 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_2.setObjectName("toolBar_2")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        self.toolBar_3 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_3.setObjectName("toolBar_3")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_3)
        self.toolBar_4 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_4.setObjectName("toolBar_4")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_4)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/toolbar/icons/folder_open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon1)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/toolbar/icons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon2)
        self.actionSave.setObjectName("actionSave")
        self.actionStart = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/toolbar/icons/control_play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStart.setIcon(icon3)
        self.actionStart.setObjectName("actionStart")
        self.actionStop = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/toolbar/icons/control_stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStop.setIcon(icon4)
        self.actionStop.setObjectName("actionStop")
        self.actionClear = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/toolbar/icons/broom.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClear.setIcon(icon5)
        self.actionClear.setObjectName("actionClear")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/toolbar/icons/question.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHelp.setIcon(icon6)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/toolbar/icons/information.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon7)
        self.actionAbout.setObjectName("actionAbout")
        self.actionPlot = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/toolbar/icons/map.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPlot.setIcon(icon8)
        self.actionPlot.setObjectName("actionPlot")
        self.actionAnimation = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/toolbar/icons/video.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAnimation.setIcon(icon9)
        self.actionAnimation.setObjectName("actionAnimation")
        self.actionTracer = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/toolbar/icons/videodisplay.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTracer.setIcon(icon10)
        self.actionTracer.setObjectName("actionTracer")
        self.toolBar_1.addAction(self.actionOpen)
        self.toolBar_1.addAction(self.actionSave)
        self.toolBar_1.addAction(self.actionClear)
        self.toolBar_2.addAction(self.actionStart)
        self.toolBar_2.addAction(self.actionStop)
        self.toolBar_2.addAction(self.actionTracer)
        self.toolBar_3.addAction(self.actionPlot)
        self.toolBar_3.addAction(self.actionAnimation)
        self.toolBar_4.addAction(self.actionHelp)
        self.toolBar_4.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LakeM"))
        self.groupBox_1.setTitle(_translate("MainWindow", "Model Setup"))
        self.label_1.setText(_translate("MainWindow", "Grid Number(x)"))
        self.label_3.setText(_translate("MainWindow", "Grid Number(y)"))
        self.label_5.setText(_translate("MainWindow", "No. of Time Step"))
        self.label_7.setText(_translate("MainWindow", "Wind Stress(x)"))
        self.label_8.setText(_translate("MainWindow", "Wind Stress(y)"))
        self.label_4.setText(_translate("MainWindow", "Grid Space(y)"))
        self.label_10.setText(_translate("MainWindow", "Flooding Depth"))
        self.label_9.setText(_translate("MainWindow", "Latitude"))
        self.label_6.setText(_translate("MainWindow", "Time Step(s)"))
        self.label_2.setText(_translate("MainWindow", "Grid Space(x)"))
        self.label_14.setText(_translate("MainWindow", "Output Interval"))
        self.label_13.setText(_translate("MainWindow", "Eddy Viscosity"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "0-Full-Slip"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "1-Semi-Slip"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "2-No-Slip"))
        self.label_16.setText(_translate("MainWindow", "Slip Boundary Condition"))
        self.comboBox_1.setItemText(0, _translate("MainWindow", "1-Upwind"))
        self.comboBox_1.setItemText(1, _translate("MainWindow", "2-Lax-Wendroff"))
        self.comboBox_1.setItemText(2, _translate("MainWindow", "3-Superbee"))
        self.label_15.setText(_translate("MainWindow", "Difference Scheme"))
        self.label_11.setText(_translate("MainWindow", "Water Density"))
        self.label_12.setText(_translate("MainWindow", "Bottom Roughness"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Details"))
        self.label_17.setText(_translate("MainWindow", "Progress:"))
        self.toolBar_1.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2"))
        self.toolBar_3.setWindowTitle(_translate("MainWindow", "toolBar_4"))
        self.toolBar_4.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setToolTip(_translate("MainWindow", "打开水深文件"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setToolTip(_translate("MainWindow", "保存输出文件"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionStart.setText(_translate("MainWindow", "Start"))
        self.actionStart.setToolTip(_translate("MainWindow", "开始运行模型"))
        self.actionStop.setText(_translate("MainWindow", "Stop"))
        self.actionStop.setToolTip(_translate("MainWindow", "停止运行模型"))
        self.actionClear.setText(_translate("MainWindow", "Clear"))
        self.actionClear.setToolTip(_translate("MainWindow", "清空参数设置"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionHelp.setToolTip(_translate("MainWindow", "帮助"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionAbout.setToolTip(_translate("MainWindow", "关于"))
        self.actionPlot.setText(_translate("MainWindow", "Plot"))
        self.actionPlot.setToolTip(_translate("MainWindow", "作图"))
        self.actionAnimation.setText(_translate("MainWindow", "Animation"))
        self.actionAnimation.setToolTip(_translate("MainWindow", "动画"))
        self.actionTracer.setText(_translate("MainWindow", "Tracer"))
        self.actionTracer.setToolTip(_translate("MainWindow", "示踪物模块"))

import res
