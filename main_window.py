# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/spock/PycharmProjects/KiberKrolik/main_window2.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main_Window(object):
    def setupUi(self, Main_Window):
        Main_Window.setObjectName("Main_Window")
        Main_Window.resize(660, 480)
        self.centralwidget = QtWidgets.QWidget(Main_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabble_widget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabble_widget.setObjectName("tabble_widget")
        self.farm = QtWidgets.QWidget()
        self.farm.setObjectName("farm")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.farm)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.scrollArea = QtWidgets.QScrollArea(self.farm)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 328, 116))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_hide_done = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btn_hide_done.setObjectName("btn_hide_done")
        self.gridLayout.addWidget(self.btn_hide_done, 0, 0, 1, 1, QtCore.Qt.AlignTop)
        self.dateEdit = QtWidgets.QDateEdit(self.scrollAreaWidgetContents)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 0, 1, 1, 1, QtCore.Qt.AlignTop)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_5.addWidget(self.scrollArea, 0, 0, 5, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.farm)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_5.addWidget(self.tableWidget, 5, 0, 1, 5)
        self.btn_add_rabbit = QtWidgets.QPushButton(self.farm)
        self.btn_add_rabbit.setObjectName("btn_add_rabbit")
        self.gridLayout_5.addWidget(self.btn_add_rabbit, 0, 1, 1, 1)
        self.btn_write_off = QtWidgets.QPushButton(self.farm)
        self.btn_write_off.setObjectName("btn_write_off")
        self.gridLayout_5.addWidget(self.btn_write_off, 0, 2, 1, 1)
        self.btn_transplanted = QtWidgets.QPushButton(self.farm)
        self.btn_transplanted.setObjectName("btn_transplanted")
        self.gridLayout_5.addWidget(self.btn_transplanted, 0, 3, 1, 1)
        self.btn_killing = QtWidgets.QPushButton(self.farm)
        self.btn_killing.setObjectName("btn_killing")
        self.gridLayout_5.addWidget(self.btn_killing, 3, 2, 1, 1)
        self.btn_copulation = QtWidgets.QPushButton(self.farm)
        self.btn_copulation.setObjectName("btn_copulation")
        self.gridLayout_5.addWidget(self.btn_copulation, 2, 1, 1, 1)
        self.table_selection = QtWidgets.QComboBox(self.farm)
        self.table_selection.setObjectName("table_selection")
        self.gridLayout_5.addWidget(self.table_selection, 4, 1, 1, 3)
        self.btn_graft = QtWidgets.QPushButton(self.farm)
        self.btn_graft.setObjectName("btn_graft")
        self.gridLayout_5.addWidget(self.btn_graft, 3, 1, 1, 1)
        self.btn_setting = QtWidgets.QPushButton(self.farm)
        self.btn_setting.setObjectName("btn_setting")
        self.gridLayout_5.addWidget(self.btn_setting, 3, 3, 1, 1)
        self.btn_weigh = QtWidgets.QPushButton(self.farm)
        self.btn_weigh.setObjectName("btn_weigh")
        self.gridLayout_5.addWidget(self.btn_weigh, 2, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.farm)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_5.addWidget(self.pushButton_2, 2, 3, 1, 1)
        self.tabble_widget.addTab(self.farm, "")
        self.finance = QtWidgets.QWidget()
        self.finance.setObjectName("finance")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.finance)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.comboBox_categories = QtWidgets.QComboBox(self.finance)
        self.comboBox_categories.setObjectName("comboBox_categories")
        self.gridLayout_2.addWidget(self.comboBox_categories, 2, 1, 1, 1)
        self.doubleSpinBox_money = QtWidgets.QDoubleSpinBox(self.finance)
        self.doubleSpinBox_money.setMinimum(-99999.99)
        self.doubleSpinBox_money.setMaximum(99999.99)
        self.doubleSpinBox_money.setSingleStep(100.0)
        self.doubleSpinBox_money.setObjectName("doubleSpinBox_money")
        self.gridLayout_2.addWidget(self.doubleSpinBox_money, 1, 1, 1, 1)
        self.toolButton = QtWidgets.QToolButton(self.finance)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout_2.addWidget(self.toolButton, 6, 2, 1, 1, QtCore.Qt.AlignRight)
        self.lineEdit_TheNote = QtWidgets.QLineEdit(self.finance)
        self.lineEdit_TheNote.setObjectName("lineEdit_TheNote")
        self.gridLayout_2.addWidget(self.lineEdit_TheNote, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.finance)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.finance)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.tableWidget_money = QtWidgets.QTableWidget(self.finance)
        self.tableWidget_money.setObjectName("tableWidget_money")
        self.tableWidget_money.setColumnCount(0)
        self.tableWidget_money.setRowCount(0)
        self.gridLayout_2.addWidget(self.tableWidget_money, 7, 0, 1, 3)
        self.label_5 = QtWidgets.QLabel(self.finance)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 6, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.finance)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.btn_save_finance = QtWidgets.QPushButton(self.finance)
        self.btn_save_finance.setObjectName("btn_save_finance")
        self.gridLayout_2.addWidget(self.btn_save_finance, 4, 1, 1, 1)
        self.comboBox_diagram = QtWidgets.QComboBox(self.finance)
        self.comboBox_diagram.setObjectName("comboBox_diagram")
        self.gridLayout_2.addWidget(self.comboBox_diagram, 6, 1, 1, 1)
        self.tableWidget_saldo = QtWidgets.QTableWidget(self.finance)
        self.tableWidget_saldo.setObjectName("tableWidget_saldo")
        self.tableWidget_saldo.setColumnCount(0)
        self.tableWidget_saldo.setRowCount(0)
        self.gridLayout_2.addWidget(self.tableWidget_saldo, 1, 2, 4, 1)
        self.tabble_widget.addTab(self.finance, "")
        self.gridLayout_3.addWidget(self.tabble_widget, 0, 1, 1, 1)
        Main_Window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Main_Window)
        self.statusbar.setObjectName("statusbar")
        Main_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Main_Window)
        self.tabble_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Main_Window)

    def retranslateUi(self, Main_Window):
        _translate = QtCore.QCoreApplication.translate
        Main_Window.setWindowTitle(_translate("Main_Window", "MainWindow"))
        self.btn_hide_done.setText(_translate("Main_Window", "Обновить"))
        self.label.setText(_translate("Main_Window", "TextLabel"))
        self.btn_add_rabbit.setText(_translate("Main_Window", "Добавить"))
        self.btn_write_off.setText(_translate("Main_Window", "Списать"))
        self.btn_transplanted.setText(_translate("Main_Window", "Пересадил"))
        self.btn_killing.setText(_translate("Main_Window", "Забой"))
        self.btn_copulation.setText(_translate("Main_Window", "Случил"))
        self.btn_graft.setText(_translate("Main_Window", "Прививки"))
        self.btn_setting.setText(_translate("Main_Window", "Настройка"))
        self.btn_weigh.setText(_translate("Main_Window", "Взвесил"))
        self.pushButton_2.setText(_translate("Main_Window", "Статусы"))
        self.tabble_widget.setTabText(self.tabble_widget.indexOf(self.farm), _translate("Main_Window", "Ферма"))
        self.toolButton.setText(_translate("Main_Window", "..."))
        self.label_2.setText(_translate("Main_Window", "Сумма:"))
        self.label_4.setText(_translate("Main_Window", "Заметка:"))
        self.label_5.setText(_translate("Main_Window", "Таблица:"))
        self.label_3.setText(_translate("Main_Window", "Категория:"))
        self.btn_save_finance.setText(_translate("Main_Window", "Сохранить"))
        self.tabble_widget.setTabText(self.tabble_widget.indexOf(self.finance), _translate("Main_Window", "Финансы"))
