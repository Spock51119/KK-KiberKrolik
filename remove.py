# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/spock/PycharmProjects/KiberKrolik/remove.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_remove_animal(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(460, 200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 2, 1, 1, 1)
        self.btn_save_rabbit = QtWidgets.QPushButton(self.tab)
        self.btn_save_rabbit.setObjectName("btn_save_rabbit")
        self.gridLayout_2.addWidget(self.btn_save_rabbit, 3, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 3, 0, 1, 1)
        self.comboBox_rabbit = QtWidgets.QComboBox(self.tab)
        self.comboBox_rabbit.setObjectName("comboBox_rabbit")
        self.gridLayout_2.addWidget(self.comboBox_rabbit, 1, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 3, 0, 1, 1)
        self.btn_save_nest = QtWidgets.QPushButton(self.tab_2)
        self.btn_save_nest.setObjectName("btn_save_nest")
        self.gridLayout_3.addWidget(self.btn_save_nest, 3, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem3, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.comboBox_nest = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_nest.setObjectName("comboBox_nest")
        self.gridLayout_3.addWidget(self.comboBox_nest, 1, 0, 1, 2)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_save_rabbit.setText(_translate("MainWindow", "Списать"))
        self.label.setText(_translate("MainWindow", "Кролик:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Кролика"))
        self.btn_save_nest.setText(_translate("MainWindow", "Списать"))
        self.label_2.setText(_translate("MainWindow", "Гнездо:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Гнездо"))
