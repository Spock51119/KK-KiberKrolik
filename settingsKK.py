# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/spock/PycharmProjects/KiberKrolik/settingsKK.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_settings_window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(359, 313)
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
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 1)
        self.spinBox_check_gestation = QtWidgets.QSpinBox(self.tab)
        self.spinBox_check_gestation.setObjectName("spinBox_check_gestation")
        self.gridLayout_2.addWidget(self.spinBox_check_gestation, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 8, 0, 1, 1)
        self.spinBox_growing = QtWidgets.QSpinBox(self.tab)
        self.spinBox_growing.setObjectName("spinBox_growing")
        self.gridLayout_2.addWidget(self.spinBox_growing, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.spinBox_gestation = QtWidgets.QSpinBox(self.tab)
        self.spinBox_gestation.setObjectName("spinBox_gestation")
        self.gridLayout_2.addWidget(self.spinBox_gestation, 0, 1, 1, 1)
        self.spinBox_weigh = QtWidgets.QSpinBox(self.tab)
        self.spinBox_weigh.setObjectName("spinBox_weigh")
        self.gridLayout_2.addWidget(self.spinBox_weigh, 5, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 5, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.spinBox_vaccinations = QtWidgets.QSpinBox(self.tab)
        self.spinBox_vaccinations.setObjectName("spinBox_vaccinations")
        self.gridLayout_2.addWidget(self.spinBox_vaccinations, 4, 1, 1, 1)
        self.spinBox_installation_nest = QtWidgets.QSpinBox(self.tab)
        self.spinBox_installation_nest.setObjectName("spinBox_installation_nest")
        self.gridLayout_2.addWidget(self.spinBox_installation_nest, 2, 1, 1, 1)
        self.btn_save_periodicity = QtWidgets.QPushButton(self.tab)
        self.btn_save_periodicity.setObjectName("btn_save_periodicity")
        self.gridLayout_2.addWidget(self.btn_save_periodicity, 8, 1, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEdit_status8 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_status8.setObjectName("lineEdit_status8")
        self.gridLayout_3.addWidget(self.lineEdit_status8, 3, 1, 1, 1)
        self.lineEdit_status6 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_status6.setObjectName("lineEdit_status6")
        self.gridLayout_3.addWidget(self.lineEdit_status6, 1, 1, 1, 1)
        self.lineEdit_status2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_status2.setObjectName("lineEdit_status2")
        self.gridLayout_3.addWidget(self.lineEdit_status2, 2, 0, 1, 1)
        self.lineEdit_status1 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_status1.setObjectName("lineEdit_status1")
        self.gridLayout_3.addWidget(self.lineEdit_status1, 1, 0, 1, 1)
        self.lineEdit_status4 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_status4.setObjectName("lineEdit_status4")
        self.gridLayout_3.addWidget(self.lineEdit_status4, 4, 0, 1, 1)
        self.lineEdit_status7 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_status7.setObjectName("lineEdit_status7")
        self.gridLayout_3.addWidget(self.lineEdit_status7, 2, 1, 1, 1)
        self.lineEdit_status10 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_status10.setObjectName("lineEdit_status10")
        self.gridLayout_3.addWidget(self.lineEdit_status10, 5, 1, 1, 1)
        self.lineEdit_status9 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_status9.setObjectName("lineEdit_status9")
        self.gridLayout_3.addWidget(self.lineEdit_status9, 4, 1, 1, 1)
        self.lineEdit_status5 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_status5.setObjectName("lineEdit_status5")
        self.gridLayout_3.addWidget(self.lineEdit_status5, 5, 0, 1, 1)
        self.lineEdit_status3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_status3.setObjectName("lineEdit_status3")
        self.gridLayout_3.addWidget(self.lineEdit_status3, 3, 0, 1, 1)
        self.btn_save_status = QtWidgets.QPushButton(self.tab_2)
        self.btn_save_status.setObjectName("btn_save_status")
        self.gridLayout_3.addWidget(self.btn_save_status, 6, 1, 1, 1)
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
        self.label_6.setText(_translate("MainWindow", "Отсадка молодняка:"))
        self.label_4.setText(_translate("MainWindow", "Установка/открытие маточника:"))
        self.label.setText(_translate("MainWindow", "Беременность:"))
        self.label_5.setText(_translate("MainWindow", "Периодичность прививок:"))
        self.label_7.setText(_translate("MainWindow", "Периодичность взвешиваний:"))
        self.label_3.setText(_translate("MainWindow", "Проверка оплодотворения:"))
        self.btn_save_periodicity.setText(_translate("MainWindow", "Сохранить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Периодичность"))
        self.btn_save_status.setText(_translate("MainWindow", "Сохранить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Статусы"))