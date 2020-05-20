# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/spock/PycharmProjects/KiberKrolik/copulation.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import datetime


class Ui_Copulation_window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 255)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_mother = QtWidgets.QLabel(self.centralwidget)
        self.label_mother.setObjectName("label_mother")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_mother)
        self.comboBox_mother = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_mother.setObjectName("comboBox_mother")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox_mother)
        self.label_father = QtWidgets.QLabel(self.centralwidget)
        self.label_father.setObjectName("label_father")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_father)
        self.comboBox_2_father = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2_father.setObjectName("comboBox_2_father")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBox_2_father)
        self.label_date_copulation = QtWidgets.QLabel(self.centralwidget)
        self.label_date_copulation.setObjectName("label_date_copulation")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_date_copulation)
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(datetime.datetime.today())
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.dateEdit)
        self.label_prepare_nest = QtWidgets.QLabel(self.centralwidget)
        self.label_prepare_nest.setObjectName("label_prepare_nest")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_prepare_nest)
        self.label_setDate_prepare_nest = QtWidgets.QLabel(self.centralwidget)
        self.label_setDate_prepare_nest.setObjectName("label_setDate_prepare_nest")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.label_setDate_prepare_nest)
        self.pushButton_copulation_save = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_copulation_save.setObjectName("pushButton_copulation_save")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.pushButton_copulation_save)
        self.label_plannet_date = QtWidgets.QLabel(self.centralwidget)
        self.label_plannet_date.setObjectName("label_plannet_date")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_plannet_date)
        self.label_setDate_plannet = QtWidgets.QLabel(self.centralwidget)
        self.label_setDate_plannet.setObjectName("label_setDate_plannet")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.label_setDate_plannet)
        self.label_check_fertilization = QtWidgets.QLabel(self.centralwidget)
        self.label_check_fertilization.setObjectName("label_check_fertilization")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_check_fertilization)
        self.label_setDate_check_fer = QtWidgets.QLabel(self.centralwidget)
        self.label_setDate_check_fer.setObjectName("label_setDate_check_fer")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_setDate_check_fer)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(6, QtWidgets.QFormLayout.LabelRole, spacerItem)
        self.verticalLayout.addLayout(self.formLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_mother.setText(_translate("MainWindow", "Крольчиха: "))
        self.label_father.setText(_translate("MainWindow", "Крол:"))
        self.label_date_copulation.setText(_translate("MainWindow", "Дата случки:"))
        self.label_prepare_nest.setText(_translate("MainWindow", "Подготовить маточник к:"))
        self.label_setDate_prepare_nest.setText(_translate("MainWindow", "число установки мат"))
        self.pushButton_copulation_save.setText(_translate("MainWindow", "Сохранить"))
        self.label_plannet_date.setText(_translate("MainWindow", "Планируемая дата окрола: "))
        self.label_setDate_plannet.setText(_translate("MainWindow", "вывести дату окрола"))
        self.label_check_fertilization.setText(_translate("MainWindow", "Проверить оплодотворение:"))
        self.label_setDate_check_fer.setText(_translate("MainWindow", "дата проверки опл"))
