# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/spock/PycharmProjects/KiberKrolik/status.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_status_window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(339, 173)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.comboBox_next_status = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_next_status.setObjectName("comboBox_next_status")
        self.gridLayout.addWidget(self.comboBox_next_status, 2, 1, 1, 1)
        self.comboBox_rabbit = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_rabbit.setObjectName("comboBox_rabbit")
        self.gridLayout.addWidget(self.comboBox_rabbit, 1, 0, 1, 2)
        self.btn_save = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save.setObjectName("btn_save")
        self.gridLayout.addWidget(self.btn_save, 4, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Новый статус:"))
        self.btn_save.setText(_translate("MainWindow", "Сохранить"))
        self.label.setText(_translate("MainWindow", "Кролик:"))
