# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui_tracerdialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_tracerDialog(object):
    def setupUi(self, tracerDialog):
        tracerDialog.setObjectName("tracerDialog")
        tracerDialog.resize(530, 370)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/icons/applogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        tracerDialog.setWindowIcon(icon)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(tracerDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout1.setObjectName("horizontalLayout1")
        self.label_1 = QtWidgets.QLabel(tracerDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_1.sizePolicy().hasHeightForWidth())
        self.label_1.setSizePolicy(sizePolicy)
        self.label_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_1.setObjectName("label_1")
        self.horizontalLayout1.addWidget(self.label_1)
        self.lineEdit_1 = QtWidgets.QLineEdit(tracerDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_1.setSizePolicy(sizePolicy)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.horizontalLayout1.addWidget(self.lineEdit_1)
        self.pushButton_1 = QtWidgets.QPushButton(tracerDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_1.sizePolicy().hasHeightForWidth())
        self.pushButton_1.setSizePolicy(sizePolicy)
        self.pushButton_1.setObjectName("pushButton_1")
        self.horizontalLayout1.addWidget(self.pushButton_1)
        self.horizontalLayout1.setStretch(0, 20)
        self.horizontalLayout1.setStretch(1, 75)
        self.horizontalLayout1.setStretch(2, 5)
        self.verticalLayout.addLayout(self.horizontalLayout1)
        self.horizontalLayout2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout2.setObjectName("horizontalLayout2")
        self.label_2 = QtWidgets.QLabel(tracerDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(tracerDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout2.addWidget(self.lineEdit_2)
        self.pushButton_2 = QtWidgets.QPushButton(tracerDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout2.addWidget(self.pushButton_2)
        self.horizontalLayout2.setStretch(0, 20)
        self.horizontalLayout2.setStretch(1, 75)
        self.horizontalLayout2.setStretch(2, 5)
        self.verticalLayout.addLayout(self.horizontalLayout2)
        self.gridLayout2 = QtWidgets.QGridLayout()
        self.gridLayout2.setObjectName("gridLayout2")
        self.label_3 = QtWidgets.QLabel(tracerDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout2.addWidget(self.label_3, 0, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(tracerDialog)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout2.addWidget(self.lineEdit_3, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(tracerDialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout2.addWidget(self.label_4, 0, 2, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(tracerDialog)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout2.addWidget(self.lineEdit_4, 0, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(tracerDialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout2.addWidget(self.label_5, 1, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(tracerDialog)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout2.addWidget(self.lineEdit_5, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(tracerDialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout2.addWidget(self.label_6, 1, 2, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(tracerDialog)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout2.addWidget(self.lineEdit_6, 1, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(tracerDialog)
        self.label_7.setObjectName("label_7")
        self.gridLayout2.addWidget(self.label_7, 2, 0, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(tracerDialog)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout2.addWidget(self.lineEdit_7, 2, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(tracerDialog)
        self.label_8.setObjectName("label_8")
        self.gridLayout2.addWidget(self.label_8, 2, 2, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(tracerDialog)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout2.addWidget(self.lineEdit_8, 2, 3, 1, 1)
        self.label_9 = QtWidgets.QLabel(tracerDialog)
        self.label_9.setObjectName("label_9")
        self.gridLayout2.addWidget(self.label_9, 3, 0, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(tracerDialog)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout2.addWidget(self.lineEdit_9, 3, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(tracerDialog)
        self.label_10.setObjectName("label_10")
        self.gridLayout2.addWidget(self.label_10, 3, 2, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(tracerDialog)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout2.addWidget(self.lineEdit_10, 3, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.pushButton_3 = QtWidgets.QPushButton(tracerDialog)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(tracerDialog)
        QtCore.QMetaObject.connectSlotsByName(tracerDialog)

    def retranslateUi(self, tracerDialog):
        _translate = QtCore.QCoreApplication.translate
        tracerDialog.setWindowTitle(_translate("tracerDialog", "Tracer tracking"))
        self.label_1.setText(_translate("tracerDialog", "hydrodynamic files"))
        self.pushButton_1.setText(_translate("tracerDialog", "..."))
        self.label_2.setText(_translate("tracerDialog", "tracer initial file"))
        self.pushButton_2.setText(_translate("tracerDialog", "..."))
        self.label_3.setText(_translate("tracerDialog", "Grid Number(x)"))
        self.label_4.setText(_translate("tracerDialog", "Grid Space(x)"))
        self.label_5.setText(_translate("tracerDialog", "Grid Number(y)"))
        self.label_6.setText(_translate("tracerDialog", "Grid Space(y)"))
        self.label_7.setText(_translate("tracerDialog", "No. of Time Step"))
        self.label_8.setText(_translate("tracerDialog", "Time Step(s)"))
        self.label_9.setText(_translate("tracerDialog", "Eddy Diffusivity"))
        self.label_10.setText(_translate("tracerDialog", "Output Interval"))
        self.pushButton_3.setText(_translate("tracerDialog", "Run"))

import res