# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/spock/PycharmProjects/KiberKrolik/settings_finance.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_settings_finanse(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(359, 313)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_categories = QtWidgets.QWidget()
        self.tab_categories.setObjectName("tab_categories")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_categories)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEdit_status8 = QtWidgets.QLineEdit(self.tab_categories)
        self.lineEdit_status8.setObjectName("lineEdit_status8")
        self.gridLayout_3.addWidget(self.lineEdit_status8, 3, 1, 1, 1)
        self.lineEdit_status6 = QtWidgets.QLineEdit(self.tab_categories)
        self.lineEdit_status6.setObjectName("lineEdit_status6")
        self.gridLayout_3.addWidget(self.lineEdit_status6, 1, 1, 1, 1)
        self.lineEdit_status2 = QtWidgets.QLineEdit(self.tab_categories)
        self.lineEdit_status2.setObjectName("lineEdit_status2")
        self.gridLayout_3.addWidget(self.lineEdit_status2, 2, 0, 1, 1)
        self.lineEdit_status1 = QtWidgets.QLineEdit(self.tab_categories)
        self.lineEdit_status1.setObjectName("lineEdit_status1")
        self.gridLayout_3.addWidget(self.lineEdit_status1, 1, 0, 1, 1)
        self.lineEdit_status4 = QtWidgets.QLineEdit(self.tab_categories)
        self.lineEdit_status4.setObjectName("lineEdit_status4")
        self.gridLayout_3.addWidget(self.lineEdit_status4, 4, 0, 1, 1)
        self.lineEdit_status7 = QtWidgets.QLineEdit(self.tab_categories)
        self.lineEdit_status7.setObjectName("lineEdit_status7")
        self.gridLayout_3.addWidget(self.lineEdit_status7, 2, 1, 1, 1)
        self.lineEdit_status10 = QtWidgets.QLineEdit(self.tab_categories)
        self.lineEdit_status10.setObjectName("lineEdit_status10")
        self.gridLayout_3.addWidget(self.lineEdit_status10, 5, 1, 1, 1)
        self.lineEdit_status9 = QtWidgets.QLineEdit(self.tab_categories)
        self.lineEdit_status9.setObjectName("lineEdit_status9")
        self.gridLayout_3.addWidget(self.lineEdit_status9, 4, 1, 1, 1)
        self.lineEdit_status5 = QtWidgets.QLineEdit(self.tab_categories)
        self.lineEdit_status5.setObjectName("lineEdit_status5")
        self.gridLayout_3.addWidget(self.lineEdit_status5, 5, 0, 1, 1)
        self.lineEdit_status3 = QtWidgets.QLineEdit(self.tab_categories)
        self.lineEdit_status3.setObjectName("lineEdit_status3")
        self.gridLayout_3.addWidget(self.lineEdit_status3, 3, 0, 1, 1)
        self.btn_save_status = QtWidgets.QPushButton(self.tab_categories)
        self.btn_save_status.setObjectName("btn_save_status")
        self.gridLayout_3.addWidget(self.btn_save_status, 6, 1, 1, 1)
        self.tabWidget.addTab(self.tab_categories, "")
        self.tab_period = QtWidgets.QWidget()
        self.tab_period.setObjectName("tab_period")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_period)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.spinBox_period = QtWidgets.QSpinBox(self.tab_period)
        self.spinBox_period.setObjectName("spinBox_period")
        self.gridLayout_2.addWidget(self.spinBox_period, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab_period)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 1)
        self.btn_save_periodicity = QtWidgets.QPushButton(self.tab_period)
        self.btn_save_periodicity.setObjectName("btn_save_periodicity")
        self.gridLayout_2.addWidget(self.btn_save_periodicity, 3, 1, 1, 1)
        self.label_period = QtWidgets.QLabel(self.tab_period)
        self.label_period.setObjectName("label_period")
        self.gridLayout_2.addWidget(self.label_period, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_period, "")
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
        self.btn_save_status.setText(_translate("MainWindow", "Сохранить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_categories), _translate("MainWindow", "Категории"))
        self.btn_save_periodicity.setText(_translate("MainWindow", "Сохранить"))
        self.label_period.setText(_translate("MainWindow", "Данные за период(дней)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_period), _translate("MainWindow", "Период "))
