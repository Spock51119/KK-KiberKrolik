# -*- coding: utf-8 -*-

import sys
import datetime
import sqlite3

from PyQt5 import QtWidgets, QtCore
from main_window import Ui_Main_Window
from add_rabbit import Ui_Add_rabbit
from copulation import Ui_Copulation_window
from mass import Ui_weigh_window
from settingsKK import Ui_settings_window
from vaccination import Ui_vaccination
from remove import Ui_remove_animal
from transplanted import Ui_transplanted
from status import Ui_status_window
from kill_rabbit import Ui_kill_window
from settings_finance import Ui_settings_finanse


conn = sqlite3.connect('rabbitDB.db')
cursor = conn.cursor()
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS rabbit (
    id_rabbit integer primary key,
    cell_number integer,
    gender text,
    arrive text,
    line text, st integer
    )
    """
)
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS ancestors (
    id_rabbit integer,
    mother_id text,
    father_id text,
    where_from text,
    date_record text)
    """
)
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS the_note (
    id_rabbit integer,
    note text
    )
    """
)
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS more_data (
    id_rabbit integer,
    mass_rabbit real,
    status_rabbit text
    )
    """
)
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS settings (
    status text,
    gestation integer,
    check_gestation integer,
    installation_nest integer,
    growing integer,
    vaccinations integer,
    weigh integer
    )
    """
)
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS vaccinations (
    id_rabbit integer,
    id_nest integer,
    date_vac text,
    date_next text,
    name_vac text
    )
    """
)
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS rabbit_litter (
    id_rabbit_litter integer primary key,
    id_mother integer,
    id_father integer,
    cell integer,
    date_copulation text,
    date_arrive text,
    rabbits_litter integer,
    count_rabbits integer,
    kukovanie integer,
    rabbits_nest integer,
    living_rabbits integer,
    the_note text,
    status integer
    )
    """
)
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS weigh (
    id_nest integer,
    weigh_nest real,
    srWeigh_nest real,
    date_weigh text
    )
    """
)
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS weigh_meat (
    id_rabbit integer,
    id_nest integer,
    weigh_all real,
    weigh_one real,
    date_kill text
    )
    """
)
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS finance (
    form integer,
    number real,
    categories text,
    note text,
    date text
    )
    """
)
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS settings_finance (
    categories text,
    period integer
    )
    """
)
conn.commit()

check_birth_list = []
check_pre_birth = []
growing_list = []
installation_nest_list = []
vaccinations_list = []
weigh_list = []
count = 1


def get_id():
    """Получение Id и № клетки кролика."""
    id_rabbit_in_cell = {}
    cursor.execute("""SELECT id_rabbit, cell_number FROM rabbit""")
    row = cursor.fetchone()
    while row is not None:
        id_rabbit_in_cell.update([(row[0], row[1])])
        row = cursor.fetchone()
    return id_rabbit_in_cell


def average_gain(id_nest):
    """Высчитывание среднего привеса для гнезда."""
    if isinstance(id_nest, int):
        cursor.execute(f"""SELECT * FROM weigh WHERE id_nest={id_nest}""")
        row = cursor.fetchone()
        if row is not None:
            list_date = []
            mass = {}
            while row is not None:
                mass.update([(str(datetime.datetime.strptime(row[3], '%Y-%m-%d').date()), row[2])])
                list_date.append(datetime.datetime.strptime(row[3], '%Y-%m-%d').date())
                row = cursor.fetchone()
            if max(list_date) != min(list_date):
                delta_days = int(str(datetime.datetime.strptime(str(max(list_date)), '%Y-%m-%d') -
                                     datetime.datetime.strptime(str(min(list_date)), '%Y-%m-%d')).split(' ')[0])
                sr_mass = round(((mass[str(max(list_date))] - mass[str(min(list_date))]) / delta_days) * 30, 2)
                return sr_mass
            return 'н/д'
        return 'н/д'
    else:
        return 'н/д'


def default_settings():
    """Задает стандартные настройки и создает базу данных."""
    cursor.execute("""SELECT * FROM settings""")
    if cursor.fetchone() is None:
        x = ('Не задан,Ремонт,Откорм,Карантин,Болеет', 30, 14, 25, 45, 180, 30)
        cursor.execute("""INSERT INTO settings (status, gestation, check_gestation, installation_nest, growing,
             vaccinations, weigh) VALUES (?,?,?,?,?,?,?)""", x)
        conn.commit()

    cursor.execute("""SELECT * FROM settings_finance""")
    if cursor.fetchone() is None:
        data = ('Без категории,Общее,Мясо,Кролик,Комбикорм,Лекарства', 30)
        cursor.execute("""INSERT INTO settings_finance VALUES(?, ?)""", data)
        conn.commit()


class GuiSettingsFinance(QtWidgets.QMainWindow, Ui_settings_finanse):
    """Окно настроек вкладки 'Финансы' ."""

    def __init__(self):
        super(GuiSettingsFinance, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Настройки')
        self.record_categories()
        self.record_period()

        self.btn_save_status.clicked.connect(self.save_categories)
        self.btn_save_periodicity.clicked.connect(self.save_period)

    def record_categories(self):
        """Заполняет поля из БД во вкладке 'Категории' ."""
        cursor.execute("""SELECT categories FROM settings_finance""")
        items = str(cursor.fetchone()).strip('(),\'').split(',')
        stat = (self.lineEdit_status1, self.lineEdit_status2, self.lineEdit_status3, self.lineEdit_status4,
                self.lineEdit_status5, self.lineEdit_status6, self.lineEdit_status7, self.lineEdit_status8,
                self.lineEdit_status9, self.lineEdit_status10)
        for i in range(len(items)):
            stat[i].setText(items[i])

    def save_categories(self):
        """Сохраняет в БД вкладку 'Категории' ."""
        items = []
        stat = (self.lineEdit_status1, self.lineEdit_status2, self.lineEdit_status3, self.lineEdit_status4,
                self.lineEdit_status5, self.lineEdit_status6, self.lineEdit_status7, self.lineEdit_status8,
                self.lineEdit_status9, self.lineEdit_status10)

        for i in stat:  # проверяет заполненность поля и сохраняет категории в список
            if len(i.text()) > 0:
                items.append(i.text())
        cursor.execute(f"""UPDATE settings_finance SET categories='{','.join(items)}'""")
        conn.commit()
        self.close()

    def record_period(self):
        self.spinBox_period.setMaximum(365)
        cursor.execute("""SELECT period FROM settings_finance""")
        period = cursor.fetchone()[0]
        self.spinBox_period.setValue(period)

    def save_period(self):
        period = (self.spinBox_period.value())
        cursor.execute(f"""UPDATE settings_finance SET period={period}""")
        conn.commit()
        self.close()


class GuiKill(QtWidgets.QMainWindow, Ui_kill_window):

    def __init__(self):
        super(GuiKill, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Забой кроликов')
        self.label_sr_kg.setText('н/д')
        self.label_o_kg.setText('н/д')
        self.record_rabbit()
        self.record_nest()
        self.check_count()

        self.btn_save_rabbit.clicked.connect(self.save_rabbit)
        self.btn_save_rabbit.clicked.connect(self.close)
        self.btn_save_nest.clicked.connect(self.save_nest)
        self.btn_save_nest.clicked.connect(self.close)

    def record_rabbit(self):
        cursor.execute(
            """
            SELECT rabbit.id_rabbit,
            rabbit.cell_number,
            rabbit.gender,
            rabbit.arrive,
            more_data.status_rabbit FROM
             rabbit,
             more_data WHERE 
             rabbit.id_rabbit=more_data.id_rabbit AND 
             rabbit.st=1""")
        row = cursor.fetchone()
        while row is not None:
            age = str(datetime.datetime.today() - datetime.datetime.strptime(row[3], '%Y, %m, %d')).split(' ')[0]
            self.comboBox_rabbit.addItem(f'Id-{row[0]}, клетка №{row[1]}, {row[2]}, статус- "{row[4]}",'
                                         f' возвраст-{age} д.')
            row = cursor.fetchone()

    def save_rabbit(self):
        if len(self.comboBox_rabbit.currentText()) > 0:
            rabbit = int(self.comboBox_rabbit.currentText().split(',')[0][3:])
            date = str(datetime.datetime.today()).split(' ')[0]
            mass = round(self.doubleSpinBox_rabbit.value(), 2)
            cursor.execute("""INSERT INTO weigh_meat (id_rabbit, weigh_one, date_kill) VALUES (?, ?, ?)""",
                           (rabbit, mass, date))
            cursor.execute(f"""UPDATE rabbit SET st=0 WHERE id_rabbit={rabbit}""")
            cursor.execute(f"""UPDATE more_data SET status_rabbit='Забит на мясо' WHERE id_rabbit={rabbit} """)
            conn.commit()

    def record_nest(self):
        cursor.execute("""SELECT * FROM rabbit_litter WHERE rabbits_nest>0 AND status=1""")
        row = cursor.fetchone()
        while row is not None:
            date = str(datetime.datetime.today() - datetime.datetime.strptime(row[5], '%d.%m.%Y')).split(' ')[0]
            self.comboBox_nest.addItem(f'Id-{row[0]}, {row[9]}- кроликов, возвраст {date}-д. клетка №{row[3]}')
            row = cursor.fetchone()

    def count_kills(self):
        count_kill = 0
        list_box = (self.doubleSpinBox1, self.doubleSpinBox2, self.doubleSpinBox3, self.doubleSpinBox4,
                    self.doubleSpinBox5, self.doubleSpinBox6, self.doubleSpinBox7, self.doubleSpinBox8,
                    self.doubleSpinBox9, self.doubleSpinBox10)
        for item in list_box:
            if item.value() > 0:
                count_kill += 1

        mass = 0
        for box in list_box:
            mass = mass + box.value()

        sr_mass = 0
        if count_kill > 0:
            sr_mass = round((mass / count_kill), 2)
        return count_kill, round(mass, 2), sr_mass

    def record_label(self):
        data = self.count_kills()
        self.label_o_kg.setText(str(data[1]))
        self.label_sr_kg.setText(str(data[2]))

    def check_count(self):
        self.doubleSpinBox1.valueChanged.connect(self.record_label)
        self.doubleSpinBox2.valueChanged.connect(self.record_label)
        self.doubleSpinBox3.valueChanged.connect(self.record_label)
        self.doubleSpinBox4.valueChanged.connect(self.record_label)
        self.doubleSpinBox5.valueChanged.connect(self.record_label)
        self.doubleSpinBox6.valueChanged.connect(self.record_label)
        self.doubleSpinBox7.valueChanged.connect(self.record_label)
        self.doubleSpinBox8.valueChanged.connect(self.record_label)
        self.doubleSpinBox9.valueChanged.connect(self.record_label)
        self.doubleSpinBox10.valueChanged.connect(self.record_label)

    def save_nest(self):
        if len(self.comboBox_nest.currentText()) > 0:
            nest = int(self.comboBox_nest.currentText().split(',')[0][3:])
            count_nest = int(self.comboBox_nest.currentText().split(',')[1][:-10])
            count_kill = self.count_kills()  # Количество, общий вес, средний вес
            date = str(datetime.datetime.today()).split(' ')[0]
            cursor.execute("""INSERT INTO weigh_meat (id_nest, weigh_all, weigh_one, date_kill) VALUES (?, ?, ?, ?)
            """, (nest, count_kill[1], count_kill[2], date))
            if count_nest > count_kill[0]:
                x = count_nest-count_kill[0]
                cursor.execute(f"""UPDATE rabbit_litter SET rabbits_nest={x} WHERE id_rabbit_litter={nest}""")
            else:
                cursor.execute(f"""UPDATE rabbit_litter SET status=0 WHERE id_rabbit_litter={nest} """)
            conn.commit()


class GuiStatus(QtWidgets.QMainWindow, Ui_status_window):
    """Окно смены статуса."""

    def __init__(self):
        super(GuiStatus, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Сменить статус')
        self.record()

        self.btn_save.clicked.connect(self.save)
        self.btn_save.clicked.connect(self.close)

    def record(self):
        """Заполняет comboBox статусами из БД."""
        cursor.execute(
            """
            SELECT rabbit.id_rabbit,
            rabbit.cell_number,
            rabbit.gender,
            more_data.status_rabbit FROM rabbit,
            more_data WHERE
            rabbit.id_rabbit=more_data.id_rabbit AND
            rabbit.st=1
            """
        )
        row = cursor.fetchone()
        while row is not None:
            self.comboBox_rabbit.addItem(f'Id-{row[0]}, клетка №{row[1]}, {row[2]}, статус- "{row[3]}" ')
            row = cursor.fetchone()

        cursor.execute("""SELECT status FROM settings""")
        status = cursor.fetchone()[0].split(',')
        self.comboBox_next_status.addItems(status)

    def save(self):
        """Обновляет статус кролика в БД."""
        if len(self.comboBox_rabbit.currentText()) > 0:
            rabbit = int(self.comboBox_rabbit.currentText().split(',')[0][3:])
            status = self.comboBox_next_status.currentText()
            cursor.execute(f"""UPDATE more_data SET status_rabbit='{status}' WHERE id_rabbit={rabbit}""")
            conn.commit()


class GuiTransplanted(QtWidgets.QMainWindow, Ui_transplanted):
    """Окно пересадки кролика/гнезда."""
    def __init__(self):
        super(GuiTransplanted, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Переместить')
        self.record_rabbit()
        self.record_nest()

        self.btn_save_rabit.clicked.connect(self.save_rabbit)
        self.btn_save_rabit.clicked.connect(self.close)
        self.btn_save_nest.clicked.connect(self.save_nest)
        self.btn_save_nest.clicked.connect(self.close)

    def record_rabbit(self):
        """Заполнение comboBox кролика."""
        cursor.execute("""SELECT * FROM rabbit WHERE st='1' """)
        row = cursor.fetchone()
        while row is not None:
            self.comboBox_rabbit.addItem(
                f'Id-{row[0]}, клетка №{row[1]}, {row[2]}, ({row[3]})- рождения, {row[4]}-линия.')
            row = cursor.fetchone()

    def record_nest(self):
        """Заполнение comboBox кролика."""
        cursor.execute("""SELECT * FROM rabbit_litter WHERE status='1' """)
        row = cursor.fetchone()
        while row is not None:
            if row[5] is not None:
                self.comboBox_nest.addItem(f'Id-{row[0]}, в клетке №{row[3]}, {row[6]} кроликов, ({row[5]})-рождения')
            else:
                self.comboBox_nest.addItem(f'Id-{row[0]}, самка id-{row[1]} клетка №{row[3]}, ({row[4]})- покрыта')
            row = cursor.fetchone()

    def save_rabbit(self):
        if len(self.comboBox_rabbit.currentText()) > 0:
            rabbit = int(self.comboBox_rabbit.currentText().split(',')[0][3:])
            cell = self.spinBox_rabbit.value()
            cursor.execute(f"""UPDATE rabbit SET cell_number={cell} WHERE id_rabbit={rabbit} """)
            conn.commit()

    def save_nest(self):
        if len(self.comboBox_nest.currentText()) > 0:
            rabbit_litter = int(self.comboBox_nest.currentText().split(',')[0][3:])
            cell = self.spinBox_nest.value()
            cursor.execute(f"""UPDATE rabbit_litter SET cell={cell} WHERE id_rabbit_litter={rabbit_litter}""")
            conn.commit()


class GuiRemoveAnimal(QtWidgets.QMainWindow, Ui_remove_animal):
    """Вкладка 'Списать' ."""
    def __init__(self):
        super(GuiRemoveAnimal, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Списать')
        self.record_rabbit()
        self.record_nest()

        self.btn_save_rabbit.clicked.connect(self.save_rabbit)
        self.btn_save_rabbit.clicked.connect(self.close)
        self.btn_save_nest.clicked.connect(self.save_nest)
        self.btn_save_nest.clicked.connect(self.close)

    def record_rabbit(self):
        cursor.execute("""SELECT * FROM rabbit WHERE st='1' """)
        row = cursor.fetchone()
        while row is not None:
            self.comboBox_rabbit.addItem(
                f'Id-{row[0]}, клетка №{row[1]}, {row[2]}, ({row[3]})- рождения, {row[4]}-линия.')
            row = cursor.fetchone()

    def record_nest(self):
        cursor.execute("""SELECT * FROM rabbit_litter WHERE status='1' """)
        row = cursor.fetchone()
        while row is not None:
            if row[5] is not None:
                self.comboBox_nest.addItem(f'Id-{row[0]}, в клетке №{row[3]}, {row[6]} кроликов, ({row[5]})-рождения')
            else:
                self.comboBox_nest.addItem(f'Id-{row[0]}, самка id-{row[1]} клетка №{row[3]}, ({row[4]})- покрыта')
            row = cursor.fetchone()

    def save_rabbit(self):
        if len(self.comboBox_rabbit.currentText()) > 0:
            rabbit = int(self.comboBox_rabbit.currentText().split(',')[0][3:])
            cursor.execute(f"""UPDATE rabbit SET st=0 WHERE id_rabbit={rabbit}""")
            conn.commit()

    def save_nest(self):
        if len(self.comboBox_nest.currentText()) > 0:
            nest = int(self.comboBox_nest.currentText().split(',')[0][3:])
            mother = (self.comboBox_nest.currentText().split(' ')[2][3:])
            if mother.isalpha():
                cursor.execute(f"""UPDATE rabbit_litter SET status=0 WHERE id_rabbit_litter={nest}""")
            else:
                mother = int(mother)
                cursor.execute(f"""UPDATE more_data SET status_rabbit='Не задан' WHERE id_rabbit={mother} """)
                cursor.execute(f"""UPDATE rabbit_litter SET status=0 WHERE id_rabbit_litter={nest}""")
            conn.commit()


class GuiVaccination(QtWidgets.QMainWindow, Ui_vaccination):
    """Вкладка 'Вакцинация' ."""
    def __init__(self):
        super(GuiVaccination, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Вакцинация')
        self.dateEdit_rabbit.setDate(datetime.datetime.today())
        self.dateEdit_rabbit.setCalendarPopup(True)
        self.dateEdit_nest.setDate(datetime.datetime.today())
        self.dateEdit_nest.setCalendarPopup(True)
        self.record_rabbit()
        self.record_nest()

        self.btn_save_rabbit.clicked.connect(self.save_rabbit)
        self.btn_save_rabbit.clicked.connect(self.close)
        self.btn_save_nest.clicked.connect(self.save_nest)
        self.btn_save_nest.clicked.connect(self.close)

    def record_rabbit(self):
        """Заполняет окна датами и комбобокс 'Кролик' ."""
        cursor.execute("""SELECT vaccinations FROM settings""")
        x = cursor.fetchone()[0]
        next_vaccina = datetime.datetime.today()+datetime.timedelta(days=x)
        self.dateEdit_next_vaccine.setDate(next_vaccina)
        self.dateEdit_next_vaccine.setCalendarPopup(True)
        self.dateEdit_nest_next.setDate(next_vaccina)
        self.dateEdit_nest_next.setCalendarPopup(True)

        cursor.execute(
            """
            SELECT rabbit.id_rabbit,
            rabbit.cell_number,
            rabbit.gender,
            more_data.status_rabbit FROM rabbit,
            more_data WHERE
             rabbit.id_rabbit=more_data.id_rabbit 
            """
        )
        row = cursor.fetchone()
        while row is not None:
            self.comboBox_rabbit.addItem(f'Id-{row[0]}, в клетке №{row[1]}, статус- {row[3]}, {row[2]}')
            row = cursor.fetchone()

    def record_nest(self):
        """ Заполняет comboBox 'Гнездо' """
        cursor.execute("""SELECT * FROM rabbit_litter WHERE date_arrive!='None' """)
        row = cursor.fetchone()
        while row is not None:
            days = str(datetime.datetime.today() - datetime.datetime.strptime(row[5], '%d.%m.%Y')).split(' ')[0]
            self.comboBox_nest.addItem(f'Id-{row[0]}, в клетке №{row[3]}, возраст-{days} дней')
            row = cursor.fetchone()

    def save_rabbit(self):
        x = (int(self.comboBox_rabbit.currentText().split(',')[0][3:]), self.dateEdit_rabbit.date().toPyDate(),
             self.dateEdit_next_vaccine.date().toPyDate(), self.lineEdit_vaccine.text())
        cursor.execute("""INSERT INTO vaccinations (id_rabbit, date_vac, date_next, name_vac) VALUES (?, ?, ?, ?)""", x)
        conn.commit()

    def save_nest(self):
        x = (int(self.comboBox_nest.currentText().split(',')[0][3:]), self.dateEdit_nest.date().toPyDate(),
             self.dateEdit_nest_next.date().toPyDate(), self.lineEdit_nest.text())
        cursor.execute("""INSERT INTO vaccinations (id_nest, date_vac, date_next, name_vac) VALUES (?, ?, ?, ?)""", x)
        conn.commit()


class GuiSettingsRabbit(QtWidgets.QMainWindow, Ui_settings_window):
    """Окно настроек вкладки 'Ферма' ."""
    def __init__(self):
        super(GuiSettingsRabbit, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Настройки')
        self.spinBox_vaccinations.setMaximum(999)  # Ограничение программы количеством клеток.
        self.record_periodicity()
        self.record_status()

        self.btn_save_periodicity.clicked.connect(self.save_periodicity)
        self.btn_save_periodicity.clicked.connect(self.close)
        self.btn_save_status.clicked.connect(self.save_status)
        self.btn_save_status.clicked.connect(self.close)

    def record_periodicity(self):
        """Заполняет окно периодичностей по умолчанию и из БД"""
        cursor.execute("""SELECT * FROM settings""")
        if cursor.fetchone() is None:
            default_settings()
        cursor.execute("""SELECT * FROM settings""")
        row = cursor.fetchone()

        self.spinBox_gestation.setValue(row[1])
        self.spinBox_check_gestation.setValue(row[2])
        self.spinBox_installation_nest.setValue(row[3])
        self.spinBox_growing.setValue(row[4])
        self.spinBox_vaccinations.setValue(row[5])
        self.spinBox_weigh.setValue(row[6])

    def save_periodicity(self):
        """ Сохраняет изменения в окне переодичностей"""
        cursor.execute(
            f"""UPDATE settings SET 
            gestation={self.spinBox_gestation.value()},
            check_gestation={self.spinBox_check_gestation.value()},
            installation_nest={self.spinBox_installation_nest.value()},
            growing={self.spinBox_growing.value()},
            vaccinations={self.spinBox_vaccinations.value()},
            weigh={self.spinBox_weigh.value()}"""
        )
        conn.commit()

    def record_status(self):
        """Заполняет поля из БД во вкладке 'Статус' ."""
        cursor.execute("""SELECT status FROM settings""")
        items = str(cursor.fetchone()).strip('(),\'').split(',')
        stat = (self.lineEdit_status1, self.lineEdit_status2, self.lineEdit_status3, self.lineEdit_status4,
                self.lineEdit_status5, self.lineEdit_status6, self.lineEdit_status7, self.lineEdit_status8,
                self.lineEdit_status9, self.lineEdit_status10)
        for i in range(len(items)):
            stat[i].setText(items[i])

    def save_status(self):
        """Сохраняет вкладку 'Статус' """
        items = []
        stat = (self.lineEdit_status1, self.lineEdit_status2, self.lineEdit_status3, self.lineEdit_status4,
                self.lineEdit_status5, self.lineEdit_status6, self.lineEdit_status7, self.lineEdit_status8,
                self.lineEdit_status9, self.lineEdit_status10)

        for i in stat:
            if len(i.text()) > 0:
                items.append(i.text())
        cursor.execute(f"""UPDATE settings SET status='{','.join(items)}'""")
        conn.commit()


class GuiWeigh(QtWidgets.QMainWindow, Ui_weigh_window):
    """Вкладка 'Взвесить кролика' ."""
    def __init__(self):
        super(GuiWeigh, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Взвесить кролика')
        self.spinBox_count_nest.setMinimum(1)
        self.spinBox_nest1_count.setMinimum(1)
        self.one_weigh()
        self.nest_weigh()
        self.nest_weigh_combox_nest()
        self.nest1_mother()
        self.check_count()
        self.label_nest1_srm.setText('н/д')
        self.label_all_mass.setText("н/д")

        self.btn_mass1_save.clicked.connect(self.one_weigh_save)  # сохраняет в БД окно "Одного"
        self.btn_mass1_save.clicked.connect(self.close)
        self.comboBox_nest_mother.currentTextChanged.connect(self.nest_weigh_combox_nest)  # команда зополняющая комБок
        self.comboBox_nest_nest.currentTextChanged.connect(self.nest_nest_count)  # Обновляет комбобокс гнезда
        self.doubleSpinBox_mass_nest.valueChanged.connect(self.sr_weigh_rabbit_litter)
        self.spinBox_count_nest.valueChanged.connect(self.sr_weigh_rabbit_litter)
        self.btn_nest_save.clicked.connect(self.save_rabbit_litter)  # Сохраняет в БД окно "помет"
        self.btn_nest_save.clicked.connect(self.close)
        self.comboBox_nest1_mother.currentTextChanged.connect(self.nest1_nest)  # обновляет КмБ при изменении самки
        self.btn_nest1_save.clicked.connect(self.save_nest1)
        self.btn_nest1_save.clicked.connect(self.close)

    def one_weigh(self):
        """Заполняет вкладку 'Одного' ."""
        cursor.execute("""SELECT id_rabbit, cell_number FROM rabbit""")
        row = cursor.fetchone()
        if row is not None:
            while row is not None:
                self.comboBox_3.addItem('Клетка №{c}, Id-{i}'.format(i=row[0], c=row[1]))
                row = cursor.fetchone()

    def one_weigh_save(self):
        """ Сохраняет вкладку 'Одного'. """
        cursor.execute(
            """
            UPDATE more_data SET
             mass_rabbit={m} WHERE
              id_rabbit={i}""".format(
                m=round(self.doubleSpinBox_mass1.value(), 2),
                i=int(self.comboBox_3.currentText().split(' ')[2][3:])))
        conn.commit()

    def nest_weigh(self):
        """ Заполняет комбобокс 'Самка' во вкладке 'Гнездо'. """
        cursor.execute(
            """
            SELECT rabbit_litter.id_mother,
            rabbit.id_rabbit,
            rabbit.cell_number,
            rabbit.line FROM rabbit,
            rabbit_litter
            WHERE rabbit_litter.id_mother=rabbit.id_rabbit AND rabbit_litter.status=1 AND
             rabbit_litter.rabbits_nest>0
             """
        )
        row = cursor.fetchone()  # id самкиб №клетки, линия
        if row is not None:
            while row is not None:
                self.comboBox_nest_mother.addItem('Id-{i}, клетка №{n}, линия-{l}'.format(i=row[1], n=row[2], l=row[3]))
                row = cursor.fetchone()
            self.nest_weigh_combox_nest()

    def nest_weigh_combox_nest(self):
        self.comboBox_nest_nest.clear()
        if len(self.comboBox_nest_mother.currentText()) > 0 and self.comboBox_nest_mother.currentText() is not None:
            id_mother = int(self.comboBox_nest_mother.currentText().split(',')[0][3:])
            cursor.execute("""SELECT * FROM rabbit_litter WHERE id_mother='{im}' """.format(im=id_mother))
            row = cursor.fetchone()
            while row is not None:
                if row[9] is not None:
                    count_rabbits = row[9]
                else:
                    count_rabbits = -1
                if row[12] == 1 and count_rabbits > 0:
                    self.comboBox_nest_nest.addItem('Id-{i}, родились- {da},"{n}" кроликов в гнезде'.format(
                        i=row[0], da=row[4], n=row[9]))
                row = cursor.fetchone()
            self.nest_nest_count()

    def nest_nest_count(self):
        """ Заполняет spinBox в окне 'Помёт' количеством кроликов."""
        if len(self.comboBox_nest_nest.currentText()) > 0:
            x = int((self.comboBox_nest_nest.currentText().split(',')[2]).split(' ')[0][1:-1])
            self.spinBox_count_nest.setValue(x)
            self.sr_weigh_rabbit_litter()

    def sr_weigh_rabbit_litter(self):
        """ Заполняет средний вес в окне 'Помет'. """
        self.label_nest_srm.setText(
            str(round((self.doubleSpinBox_mass_nest.value()/self.spinBox_count_nest.value()), 2)))

    def save_rabbit_litter(self):
        """ Сохраняет данные из окна 'Гнездо' в базу данных. """
        id_nest = int(self.comboBox_nest_nest.currentText().split(',')[0][3:])
        mass = round(self.doubleSpinBox_mass_nest.value(), 2)
        sr_mass = round((self.doubleSpinBox_mass_nest.value()/self.spinBox_count_nest.value()), 2)
        date_w = str(datetime.datetime.today().date())
        cursor.execute("""
        INSERT INTO weigh (id_nest, weigh_nest, srWeigh_nest, date_weigh) VALUES (?, ?, ?, ?)""", (
            id_nest, mass, sr_mass, date_w))
        conn.commit()

    def nest1_mother(self):
        """Заполняет комбоббокс 'Самка' в окне 'Гнездо по одному'. """
        cursor.execute(
            """
            SELECT id_rabbit,
            cell_number,
            line,
            id_mother 
            FROM rabbit,
            rabbit_litter 
            WHERE id_rabbit=id_mother and status=1""")
        row = cursor.fetchone()
        while row is not None:
            self.comboBox_nest1_mother.addItem('Id-{i}, клетка №{n}, линия-{l}'.format(i=row[0], n=row[1], l=row[2]))
            row = cursor.fetchone()
        self.nest1_nest()

    def nest1_nest(self):
        """ Заполняет комбобокс 'Гнездо' в окне 'Гнездо по одному'. """
        self.comboBox_nest1_nest.clear()
        if len(self.comboBox_nest1_mother.currentText()) > 0 and self.comboBox_nest1_mother.currentText() is not None:
            id_mother = int(self.comboBox_nest1_mother.currentText().split(',')[0][3:])
            cursor.execute("""SELECT * FROM rabbit_litter WHERE id_mother='{im}' """.format(im=id_mother))
            row = cursor.fetchone()
            while row is not None:
                if row[9] is not None:
                    count_rabbits = row[9]
                else:
                    count_rabbits = -1
                if row[12] == 1 and count_rabbits > 0:
                    self.comboBox_nest1_nest.addItem(
                        'Id-{i}, родились- {da},"{n}" кроликов в гнезде'.format(i=row[0], da=row[4], n=row[9]))
                row = cursor.fetchone()
            self.nest_nest_count()

    def count_kills(self):
        count_kill = 0
        list_box = (self.doubleSpinBox1, self.doubleSpinBox2, self.doubleSpinBox3, self.doubleSpinBox4,
                    self.doubleSpinBox5, self.doubleSpinBox6, self.doubleSpinBox7, self.doubleSpinBox8,
                    self.doubleSpinBox9, self.doubleSpinBox10)
        for item in list_box:
            if item.value() > 0:
                count_kill += 1

        mass = 0
        for box in list_box:
            mass = mass + box.value()

        sr_mass = 0
        if count_kill > 0:
            sr_mass = round((mass/count_kill), 2)
        return count_kill, round(mass, 2), sr_mass

    def check_count(self):
        self.doubleSpinBox1.valueChanged.connect(self.record_label)
        self.doubleSpinBox2.valueChanged.connect(self.record_label)
        self.doubleSpinBox3.valueChanged.connect(self.record_label)
        self.doubleSpinBox4.valueChanged.connect(self.record_label)
        self.doubleSpinBox5.valueChanged.connect(self.record_label)
        self.doubleSpinBox6.valueChanged.connect(self.record_label)
        self.doubleSpinBox7.valueChanged.connect(self.record_label)
        self.doubleSpinBox8.valueChanged.connect(self.record_label)
        self.doubleSpinBox9.valueChanged.connect(self.record_label)
        self.doubleSpinBox10.valueChanged.connect(self.record_label)

    def record_label(self):
        mass = self.count_kills()
        self.label_nest1_srm.setText(str(mass[2]))
        self.label_all_mass.setText(str(mass[1]))
        self.spinBox_nest1_count.setValue(mass[0])

    def save_nest1(self):
        if len(self.comboBox_nest1_nest.currentText()) > 0:
            nest = int(self.comboBox_nest1_nest.currentText().split(',')[0][3:])
            mass_count = self.count_kills()
            mass = mass_count[1]
            sr_mass = mass_count[2]
            date = str(datetime.datetime.today()).split(' ')[0]
            cursor.execute("""INSERT INTO weigh VALUES (?, ?, ?, ?)""", (nest, mass, sr_mass, date))
            conn.commit()


class GuiCopulationWindow(QtWidgets.QMainWindow, Ui_Copulation_window):
    """Окно случки"""
    def __init__(self):
        super(GuiCopulationWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Случка')
        self.recodr_data()
        self.record_mother()

        self.pushButton_copulation_save.clicked.connect(self.record_to_db)
        self.pushButton_copulation_save.clicked.connect(self.close)
        self.dateEdit.dateChanged.connect(self.recodr_data)
        self.comboBox_mother.currentIndexChanged.connect(self.record_mother)

    def recodr_data(self):
        cursor.execute("""SELECT * FROM settings""")
        dates = cursor.fetchone()
        if dates is None:
            default_settings()
            cursor.execute("""SELECT * FROM settings""")
            dates = cursor.fetchone()

        date_check_fer = dates[2]
        date_prepare_nest = dates[3]
        planned_date = dates[1]

        check_fertilization = str((self.dateEdit.date()).toPyDate() + datetime.timedelta(days=date_check_fer))
        prepare_nest = str((self.dateEdit.date()).toPyDate() + datetime.timedelta(days=date_prepare_nest))
        planned_date_okrol = str((self.dateEdit.date()).toPyDate() + datetime.timedelta(days=planned_date))

        self.label_setDate_check_fer.setText(check_fertilization)
        self.label_setDate_prepare_nest.setText(prepare_nest)
        self.label_setDate_plannet.setText(planned_date_okrol)

        rabbit_status = {}
        cursor.execute("""SELECT * FROM more_data""")
        row = cursor.fetchone()
        if row is not None:
            while row is not None:
                rabbit_status.update([(row[0], row[2])])
                row = cursor.fetchone()

    def record_mother(self):
        cursor.execute(
            """
            SELECT rabbit.id_rabbit,
            more_data.status_rabbit,
            rabbit.line,
            rabbit.cell_number FROM rabbit,
            more_data WHERE rabbit.id_rabbit=more_data.id_rabbit and 
            rabbit.st=1 and rabbit.gender='Самка' and 
            more_data.status_rabbit!='Покрыта' """)
        row = cursor.fetchone()

        while row is not None:
            self.comboBox_mother.addItem(
                'id {i}, статус "{c}", Линия {l}, в клетке №{n}'.format(i=row[0], c=row[1], l=row[2], n=row[3]))
            row = cursor.fetchone()
        self.record_father()

    def record_father(self):
        self.comboBox_2_father.clear()
        cursor.execute(
            """
            SELECT rabbit.id_rabbit,
            more_data.status_rabbit,
            rabbit.line,
            rabbit.cell_number FROM rabbit,
            more_data WHERE
             rabbit.id_rabbit=more_data.id_rabbit and
              rabbit.st=1 and
               rabbit.gender='Самец' 
               """
        )
        row = cursor.fetchone()
        while row is not None:
            if len(self.comboBox_mother.currentText()) > 0:
                if row[2] == (self.comboBox_mother.currentText()).split(',')[2][7:]:
                    self.comboBox_2_father.addItem('id {i}, статус "{s}", в клетке №{c}'.format(
                        i=row[0], s=row[1], c=row[3]))
            row = cursor.fetchone()

    def record_to_db(self):
        id_mother = int(self.comboBox_mother.currentText().split(',')[0][3:])
        id_father = self.comboBox_2_father.currentText().split(',')[0].split(' ')[1]
        cell_pom = get_id()[id_mother]
        date_copulation = self.dateEdit.text()
        cursor.execute(
            """
            INSERT INTO rabbit_litter (
            id_mother,
            id_father,
            cell,
            date_copulation,
            status)
            VALUES (?, ?, ?, ?, ?)""",
            (
                id_mother,
                id_father,
                cell_pom,
                date_copulation,
                1
            )
        )
        cursor.execute("""UPDATE more_data SET status_rabbit='Покрыта' WHERE id_rabbit={i}""".format(i=id_mother))
        conn.commit()


class GUIAddRabbit(QtWidgets.QMainWindow, Ui_Add_rabbit):
    """ Окно добавления кролика """
    def __init__(self):
        super(GUIAddRabbit, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Добавить кролика')
        self.rabbit_litter_record()
        self.from_rabbit_litter_mother()
        self.from_rabbit_litter_record_label()
        self.combox_status()

        """Изменения и дополнения"""
        self.dateEdit_rabbit_litter_arrive.setDate(datetime.datetime.today())
        self.label_9.setText("{d}".format(d=str(datetime.datetime.today()).split(' ')[0]))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(datetime.datetime.today())
        self.comboBox_gender_1.addItems(('Самка', 'Самец'))
        self.comboBox_gender_2.addItems(('Самка', 'Самец'))
        self.lineEdit.setText('Неизвестен')
        self.lineEdit_2.setText('Неизвестена')
        self.label_16.setText("Среднемесячный привес:")
        self.set_living()

        """Нажатия кнопок"""
        self.btn_save_3.clicked.connect(self.record_to_db)  # Обрабатывает сохранение в первой вкладке
        self.btn_save_3.clicked.connect(self.close)  # Закрывает окно добавления)
        self.spinBox_kukovanie.valueChanged.connect(self.count_rabbit_in_nest)
        self.spinBox_count_rabbits_rabbit_litter.valueChanged.connect(self.set_living)
        self.comboBox_mother.currentTextChanged.connect(self.from_rabbit_litter_okrol)
        self.pushButton.clicked.connect(self.rabbit_litter_record_db)
        self.pushButton.clicked.connect(self.close)
        self.comboBox_okrol.currentTextChanged.connect(self.from_rabbit_litter_record_label)
        self.spinBox_living_rabbit_litter.valueChanged.connect(self.count_rabbit_in_nest)
        self.btn_save_2.clicked.connect(self.save_from_pom)

    def combox_status(self):
        cursor.execute("""SELECT status FROM settings""")
        status = cursor.fetchone()
        if status is not None:
            status = str(status[0]).split(',')
            self.comboBox_status.addItems(status)
            self.comboBox_status2.addItems(status)

    def record_to_db(self):   # Первая форма добавления
        date_record = self.label_9.text()  # Дата внесения в базу
        date_arrive = str(self.dateEdit.date())[19:-1]  # дата рождения/появления
        gender = self.comboBox_gender_1.currentText()  # Выбор пола кролика
        father = self.lineEdit.text()  # Отец кролика
        mother = self.lineEdit_2.text()  # Мать кролика
        line_rabbit = self.lineEdit_3.text()  # Линия кролика
        where_from = self.lineEdit_4.text()  # Источник появления кролика
        mass_rabbit = str(round(self.doubleSpinBox.value(), 2))  # Вес кролика
        cell = self.spinBox.value()  # Номер клетки в которую помещен кролик
        status_rabbit = self.comboBox_status.currentText()  # Задает статус кролика
        the_note = self.plainTextEdit.toPlainText()  # Заметка о кролике

        """Заполнение базы данных"""
        cursor.execute("""INSERT INTO rabbit (cell_number, gender, arrive, line, st) VALUES(?, ?, ?, ?, ?)""",
                       (cell, gender, date_arrive, line_rabbit, 1))
        conn.commit()
        cursor.execute("""SELECT id_rabbit FROM rabbit""")
        max_id = (max(cursor.fetchall())[0])
        cursor.execute(
            """
            INSERT INTO ancestors (
            id_rabbit,
            mother_id,
            father_id,
            where_from,
            date_record) 
            VALUES(?, ?, ?, ?, ?)""", (
                max_id,
                mother,
                father,
                where_from,
                date_record
            )
        )
        cursor.execute("""INSERT INTO the_note VALUES(?, ?)""", (max_id, the_note))
        cursor.execute("""INSERT INTO more_data VALUES(?, ?, ?)""", (max_id, mass_rabbit, status_rabbit))
        conn.commit()

    def rabbit_litter_record(self):
        cursor.execute("""SELECT * FROM rabbit_litter WHERE status=1 """)
        row = cursor.fetchone()
        if row is not None:
            while row is not None:
                if row[5] is None:
                    self.comboBox_mother_rabbit_litter.addItem('Id-{i}, в клетке №{n}, {d} покрыта, id помета-{ip}'.
                                                               format(i=row[1], n=get_id()[row[1]], d=row[4], ip=row[0]))
                row = cursor.fetchone()

        self.count_rabbit_in_nest()

    def count_rabbit_in_nest(self):
        """ обновляет число кроликов которых можно откуковать в кладке 'Помёт'. """
        self.spinBox_kukovanie.setMinimum(-(self.spinBox_living_rabbit_litter.value()))
        self.label_28.setText(str(self.spinBox_living_rabbit_litter.value() + self.spinBox_kukovanie.value()))

    def set_living(self):
        count_living = self.spinBox_count_rabbits_rabbit_litter.value()
        self.spinBox_living_rabbit_litter.setMaximum(count_living)
        self.spinBox_living_rabbit_litter.setValue(count_living)
        self.count_rabbit_in_nest()

    def from_rabbit_litter_mother(self):
        """Заполняет комбобокс 'Мать' из вкладки 'Из помета' """
        cell = get_id()
        cursor.execute("""SELECT id_mother FROM rabbit_litter WHERE date_arrive!='None' and status=1 """)
        row = cursor.fetchone()
        if row is not None:
            while row is not None:
                self.comboBox_mother.addItem(f'Id-{row[0]}, клетка №{cell[row[0]]}')
                row = cursor.fetchone()

            self.from_rabbit_litter_okrol()

    def from_rabbit_litter_okrol(self):
        """Заполняет комбобокс 'окрол' из вкладки 'Из помёта'. """
        self.comboBox_okrol.clear()
        cursor.execute(
            """SELECT * FROM rabbit_litter WHERE id_mother={m}""".format(
                m=int(self.comboBox_mother.currentText().split(',')[0][3:])))
        row = cursor.fetchone()
        if row is not None:
            while row is not None:
                self.comboBox_okrol.addItem('id-{i}, {d}-рождения'.format(i=row[0], d=row[5]))
                row = cursor.fetchone()

    def from_rabbit_litter_record_label(self):
        if len(self.comboBox_okrol.currentText()) > 0:
            id_nest = int(self.comboBox_okrol.currentText().split(',')[0][3:])
            cursor.execute(f"""SELECT date_arrive FROM rabbit_litter WHERE id_rabbit_litter='{id_nest}' """)
            items = cursor.fetchone()
            self.label_14.setText(items[0])
            self.label_23.setText(
                str((datetime.datetime.today()-datetime.datetime.strptime(items[0], '%d.%m.%Y')).days))
            cursor.execute(f"""SELECT srWeigh_nest FROM weigh WHERE id_nest='{id_nest}'""")
            mass = cursor.fetchone()
            if mass is None:
                self.label_19.setText('н/д')
                self.label_21.setText('н/д')
            else:
                self.label_19.setText(str(average_gain(int(self.comboBox_okrol.currentText().split(',')[0][3]))))
                self.label_21.setText(str(mass[0]))

            id_mother = self.comboBox_mother.currentText().split(',')[0][3:]
            cursor.execute(f"""SELECT line FROM rabbit WHERE id_rabbit={id_mother}""")
            self.lineEdit_from_rabbit_litter_line.setText(str(cursor.fetchone()[0]) + '+')

    def rabbit_litter_record_db(self):
        """Сохраняет в БД вкладку 'Помёт' """
        id_rabbit_litter = int(self.comboBox_mother_rabbit_litter.currentText().split(',')[3][11:])
        id_mother = self.comboBox_mother_rabbit_litter.currentText().split(',')[0][3:]
        date_arrive = self.dateEdit_rabbit_litter_arrive.text()
        count_rabbits_litter = self.spinBox_count_rabbits_rabbit_litter.value()
        living_rabbits = self.spinBox_living_rabbit_litter.value()
        kukkov = self.spinBox_kukovanie.value()
        count_rabbits_nest = int(self.label_28.text())
        the_note = str(self.plainTextEdit_3.toPlainText())
        cursor.execute(
            """
            UPDATE rabbit_litter SET date_arrive='{d}',
            rabbits_litter={rp},
            count_rabbits={cr},
            kukovanie={ku},
            rabbits_nest={rn},
            living_rabbits={lr},
            the_note='{th}',
            status=1 
            WHERE id_rabbit_litter={ip}
            """.format(
                d=date_arrive,
                rp=count_rabbits_litter,
                cr=count_rabbits_nest,
                ku=kukkov,
                rn=count_rabbits_nest,
                lr=living_rabbits,
                th=the_note,
                ip=id_rabbit_litter
            )
        )
        cursor.execute(
            """
            UPDATE more_data SET
             status_rabbit='Не задан' WHERE
              id_rabbit={id_m}
            """.format(
                id_m=id_mother
            )
        )

        conn.commit()

    def save_from_pom(self):
        """Сохранение вкладки 'Из помета'. """
        cell = self.spinBox_2.value()
        gender = self.comboBox_gender_2.currentText()
        line = self.lineEdit_from_rabbit_litter_line.text()
        mass = self.label_21.text()
        status = self.comboBox_status2.currentText()
        arrive = str(self.comboBox_okrol.currentText().split(' ')[1][:-9]).split('.')
        arrive_r = f'{arrive[2]}, {arrive[1]}, {arrive[0]}'
        date_record = str(datetime.datetime.today()).split(' ')[0]
        where_from = int(self.comboBox_okrol.currentText().split(',')[0][3:])
        cursor.execute(f"""SELECT id_mother, id_father FROM rabbit_litter WHERE id_rabbit_litter={where_from}""")
        parents = cursor.fetchone()  # Родители 0-мать, 1-отец
        cursor.execute("""INSERT INTO rabbit (cell_number,gender, arrive, line, st) VALUES(?,?,?,?,?)""", (
            cell, gender, arrive_r, line, 1))
        conn.commit()
        id_rabbit = 9999  # костыль для получения ид кролика
        cursor.execute("""SELECT id_rabbit FROM rabbit""")
        row = cursor.fetchone()
        while row is not None:
            id_rabbit = row[0]
            row = cursor.fetchone()

        cursor.execute("""INSERT INTO ancestors VALUES(?,?,?,?,?)""", (
            id_rabbit, parents[0], parents[1], where_from, date_record))
        cursor.execute("""INSERT INTO more_data VALUES(?,?,?)""", (id_rabbit, mass, status))
        cursor.execute("""INSERT INTO the_note VALUES(?,?)""", (id_rabbit, self.plainTextEdit_2.toPlainText()))
        conn.commit()

        cursor.execute(f"""SELECT rabbits_nest FROM rabbit_litter WHERE id_rabbit_litter={where_from}""")
        count_rabbits = int(cursor.fetchone()[0])-1
        cursor.execute(f"""UPDATE rabbit_litter SET rabbits_nest={count_rabbits}""")
        conn.commit()


class MainWindow(QtWidgets.QMainWindow, Ui_Main_Window):
    """ Главное окно приложения"""
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('КК- Кибер Кролики')
        self.table_selection.addItems(('Кролики', 'Гнёзда'))
        self.dateEdit.setDate(datetime.datetime.today())
        self.dateEdit.setCalendarPopup(True)
        default_settings()
        self.record_to_main_table()
        self.pre_birth()
        self.gestation()
        self.installation_nest()
        self.growing()
        self.vaccinations()
        self.weigh()
        self.label.deleteLater()
        self.records_finance()
        self.check_finance_combox()
        self.saldo_table()

        """Нажатие кнопок"""
        self.btn_add_rabbit.clicked.connect(self.show_add_rabbit)
        self.btn_copulation.clicked.connect(self.show_copulation_window)
        self.btn_weigh.clicked.connect(self.show_weigh_window)
        self.btn_setting.clicked.connect(self.show_settings_window)
        self.btn_graft.clicked.connect(self.show_vaccination_window)
        self.btn_write_off.clicked.connect(self.show_remove_window)
        self.btn_transplanted.clicked.connect(self.show_transplanted_window)
        self.pushButton_2.clicked.connect(self.show_status_window)
        self.btn_killing.clicked.connect(self.show_kill_window)
        self.table_selection.currentTextChanged.connect(self.check_table)
        self.dateEdit.dateChanged.connect(self.remove_checkbox)
        self.btn_hide_done.clicked.connect(self.remove_checkbox)
        self.btn_save_finance.clicked.connect(self.save_finance)
        self.comboBox_diagram.currentTextChanged.connect(self.check_finance_combox)
        self.toolButton.clicked.connect(self.show_settings_fin_window)

    """ Вызов окон, еще не разобрался как вызывать окна в '__init__' """
    def show_settings_fin_window(self):
        self.gui_settingsF_window = GuiSettingsFinance()
        self.gui_settingsF_window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.gui_settingsF_window.show()

    def show_kill_window(self):
        self.gui_kill_window = GuiKill()
        self.gui_kill_window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.gui_kill_window.show()

    def show_status_window(self):
        self.gui_status_window = GuiStatus()
        self.gui_status_window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.gui_status_window.show()

    def show_transplanted_window(self):
        self.gui_transplanted_window = GuiTransplanted()
        self.gui_transplanted_window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.gui_transplanted_window.show()

    def show_remove_window(self):
        self.gui_remove_window = GuiRemoveAnimal()
        self.gui_remove_window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.gui_remove_window.show()

    def show_vaccination_window(self):
        self.gui_vaccination_window = GuiVaccination()
        self.gui_vaccination_window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.gui_vaccination_window.show()

    def show_settings_window(self):
        self.gui_settings_window = GuiSettingsRabbit()
        self.gui_settings_window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.gui_settings_window.show()

    def show_weigh_window(self):
        self.gui_weigh_window = GuiWeigh()
        self.gui_weigh_window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.gui_weigh_window.show()

    def show_add_rabbit(self):
        self.gui_add_rabbit = GUIAddRabbit()
        self.gui_add_rabbit.setWindowModality(QtCore.Qt.ApplicationModal)
        self.gui_add_rabbit.show()

    def show_copulation_window(self):
        self.gui_copulation_window = GuiCopulationWindow()
        self.gui_copulation_window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.gui_copulation_window.show()

    """Таблицы"""
    def check_table(self):
        if self.table_selection.currentText() == 'Кролики':
            self.tableWidget.clear()
            self.record_to_main_table()
        elif self.table_selection.currentText() == 'Гнёзда':
            self.tableWidget.clear()
            self.rabbit_litter_table()

    def record_to_main_table(self):
        count_row_in_record = 1
        self.tableWidget.setColumnCount(8)  # Задает количество колонок в таблице
        self.tableWidget.setRowCount(count_row_in_record)  # Задает количество рядов в таблице
        self.tableWidget.setHorizontalHeaderLabels(
            ('Id Кролика', 'Пол', '№ Клетки', 'Статус', 'Возвраст', 'Линия', 'Вес', 'Родился'))
        cursor.execute(
            """
            SELECT rabbit.id_rabbit,
            rabbit.gender,
            rabbit.cell_number,
            more_data.status_rabbit,
            rabbit.arrive,
            rabbit.line,
            more_data.mass_rabbit FROM rabbit,
            more_data WHERE rabbit.id_rabbit=more_data.id_rabbit AND rabbit.st=1
            """
        )
        row = cursor.fetchone()
        while row is not None:
            self.tableWidget.setRowCount(count_row_in_record)  # Добавляет новую строку в таблицу
            rabbit_id = str(row[0])
            gender = row[1]
            rabbit_in_cell = str(row[2])
            status = row[3]
            arrive = row[4]
            line = row[5]
            mass = str(row[6])
            age = str(datetime.datetime.today() - datetime.datetime.strptime(arrive, '%Y, %m, %d')).split(' ')[0]
            x = (rabbit_id, gender, rabbit_in_cell, status, age, line, mass, arrive)

            for i in range(8):
                cellinfo = QtWidgets.QTableWidgetItem(x[i])
                self.tableWidget.setItem(count_row_in_record-1, i, cellinfo)
            count_row_in_record += 1
            row = cursor.fetchone()

    def rabbit_litter_table(self):
        count_row_in_record = 1
        self.tableWidget.setColumnCount(6)  # Задает количество колонок в таблице
        self.tableWidget.setRowCount(count_row_in_record)
        self.tableWidget.setHorizontalHeaderLabels(('Id-гнезда', "Возвраст", "Кроликов", "Клетка №", "Мать", "Отец"))
        cursor.execute("""SELECT * FROM rabbit_litter WHERE date_arrive!='None' AND status=1 """)
        row = cursor.fetchone()
        while row is not None:
            self.tableWidget.setRowCount(count_row_in_record)
            age = str(datetime.datetime.today()-datetime.datetime.strptime(row[5], '%d.%m.%Y'))
            if len(age) > 15:
                age = age.split(' ')[0]
            else:
                age = '1'
            items = [str(row[0]), age, str(row[9]), str(row[3]), str(row[1]), str(row[2])]
            for i in range(6):
                cellinfo = QtWidgets.QTableWidgetItem(items[i])
                self.tableWidget.setItem(count_row_in_record-1, i, cellinfo)
            count_row_in_record += 1
            row = cursor.fetchone()

    def check_finance_combox(self):
        """ Таблицы финансов"""
        if self.comboBox_diagram.currentText() == 'Все финансы':
            self.tableWidget_money.clear()
            self.all_finance()
        if self.comboBox_diagram.currentText() == 'Расходы':
            self.tableWidget_money.clear()
            self.costs_table()
        if self.comboBox_diagram.currentText() == 'Доходы':
            self.tableWidget_money.clear()
            self.income_table()

    def all_finance(self):
        count_row_in_record = 1
        self.tableWidget_money.setColumnCount(5)  # Задает количество колонок в таблице
        self.tableWidget_money.setRowCount(count_row_in_record)
        self.tableWidget_money.setHorizontalHeaderLabels(("Статья", "Число", "Категория", "Дата", "Заметка"))
        cursor.execute("""SELECT * FROM finance""")
        row = cursor.fetchone()
        while row is not None:
            self.tableWidget_money.setRowCount(count_row_in_record)
            if row[0] == 1:
                form = 'Доход'
            else:
                form = 'Расход'
            items = (form, str(row[1]), row[2], row[4], row[3])
            for i in range(5):
                cellinfo = QtWidgets.QTableWidgetItem(items[i])
                self.tableWidget_money.setItem(count_row_in_record-1, i, cellinfo)
            count_row_in_record += 1
            row = cursor.fetchone()

    def costs_table(self):
        count_row_in_record = 1
        self.tableWidget_money.setColumnCount(5)  # Задает количество колонок в таблице
        self.tableWidget_money.setRowCount(count_row_in_record)
        self.tableWidget_money.setHorizontalHeaderLabels(("Статья", "Число", "Категория", "Дата", "Заметка"))
        cursor.execute("""SELECT * FROM finance WHERE form=0""")
        row = cursor.fetchone()
        while row is not None:
            self.tableWidget_money.setRowCount(count_row_in_record)
            if row[0] == 1:
                form = 'Доход'
            else:
                form = 'Расход'
            items = (form, str(row[1]), row[2], row[4], row[3])
            for i in range(5):
                cellinfo = QtWidgets.QTableWidgetItem(items[i])
                self.tableWidget_money.setItem(count_row_in_record - 1, i, cellinfo)
            count_row_in_record += 1
            row = cursor.fetchone()

    def income_table(self):
        count_row_in_record = 1
        self.tableWidget_money.setColumnCount(5)  # Задает количество колонок в таблице
        self.tableWidget_money.setRowCount(count_row_in_record)
        self.tableWidget_money.setHorizontalHeaderLabels(("Статья", "Число", "Категория", "Дата", "Заметка"))
        cursor.execute("""SELECT * FROM finance WHERE form=1""")
        row = cursor.fetchone()
        while row is not None:
            self.tableWidget_money.setRowCount(count_row_in_record)
            if row[0] == 1:
                form = 'Доход'
            else:
                form = 'Расход'
            items = (form, str(row[1]), row[2], row[4], row[3])
            for i in range(5):
                cellinfo = QtWidgets.QTableWidgetItem(items[i])
                self.tableWidget_money.setItem(count_row_in_record - 1, i, cellinfo)
            count_row_in_record += 1
            row = cursor.fetchone()

    def saldo_table(self):
        costs = 0
        income = 0

        cursor.execute("""SELECT period FROM settings_finance""")
        days = cursor.fetchone()[0]

        cursor.execute("""SELECT number, date FROM finance WHERE form=1""")
        row = cursor.fetchone()
        while row is not None:
            date = datetime.datetime.today() - datetime.timedelta(days=days)
            if date < datetime.datetime.strptime(row[1], '%Y-%m-%d'):
                income = round(income+row[0])
            else:
                row = None
            row = cursor.fetchone()

        cursor.execute("""SELECT number, date FROM finance Where form=0""")
        row = cursor.fetchone()
        while row is not None:
            date = datetime.datetime.today()-datetime.timedelta(days=days)
            if date < datetime.datetime.strptime(row[1], '%Y-%m-%d'):
                costs = round(costs+row[0])
            else:
                row = None
            row = cursor.fetchone()

        saldo = income + costs

        """Заполнение таблицы сальдо"""
        self.tableWidget_saldo.setColumnCount(1)  # Задает количество колонок в таблице
        self.tableWidget_saldo.setRowCount(3)
        self.tableWidget_saldo.setVerticalHeaderLabels(('Баланс', f'Доход за {days}д.', f'Расход за {days}д.'))
        items = [str(saldo), str(income), str(costs)]
        for i in range(3):
            cellinfo = QtWidgets.QTableWidgetItem(items[i])
            self.tableWidget_saldo.setItem(i-1, 1, cellinfo)

    """Оповещения"""
    def pre_birth(self):
        global check_pre_birth
        global count
        cursor.execute("""SELECT check_gestation FROM settings""")
        days = cursor.fetchone()
        if days is None:
            default_settings()
            cursor.execute("""SELECT check_gestation FROM settings""")
            days = cursor.fetchone()[0]
        else:
            days = days[0]
        date = datetime.datetime.strptime(str(self.dateEdit.date().toPyDate()), '%Y-%m-%d')
        cursor.execute("""SELECT * FROM rabbit_litter WHERE status=1""")
        row = cursor.fetchone()
        while row is not None:
            if row[5] is None:
                date_cap = datetime.datetime.strptime(row[4], '%d.%m.%Y')
                check_date = date_cap + datetime.timedelta(days=days)
                if date == check_date:
                    exec('self.label{x} = QtWidgets.QLabel(self.scrollAreaWidgetContents)'.format(x=count))
                    exec('self.label{x}.setObjectName("label{x}")'.format(x=count))
                    exec('self.gridLayout.addWidget(self.label{x}, {x}, 0, 1, 2)'.format(x=count))
                    exec('self.label{x}.setText("Проверить покрытие самки Id-{i} в клетке №{x2}")'.
                         format(x=count, x2=row[3], i=row[1]))
                    check_box = f'self.label{count}'
                    check_pre_birth.append(check_box)
                    count += 1
            row = cursor.fetchone()

    def gestation(self):
        global check_birth_list
        global count
        cursor.execute("""SELECT gestation FROM settings""")
        days = cursor.fetchone()[0]
        date = datetime.datetime.strptime(str(self.dateEdit.date().toPyDate()), '%Y-%m-%d')
        cursor.execute("""SELECT * FROM rabbit_litter WHERE status=1""")
        row = cursor.fetchone()
        while row is not None:
            if row[5] is None:
                date_cap = datetime.datetime.strptime(row[4], '%d.%m.%Y')
                check_date = date_cap + datetime.timedelta(days=days)
                if date == check_date:
                    exec('self.label{x} = QtWidgets.QLabel(self.scrollAreaWidgetContents)'.format(x=count))
                    exec('self.label{x}.setObjectName("label{x}")'.format(x=count))
                    exec('self.gridLayout.addWidget(self.label{x}, {x}, 0, 1, 2)'.format(x=count))
                    exec('self.label{x}.setText("Проверить окрол самки Id-{i} в клетке №{x2}")'.format(
                        x=count, x2=row[3], i=row[1]))
                    check_box = f'self.label{count}'
                    check_birth_list.append(check_box)
                    count += 1
            row = cursor.fetchone()

    def installation_nest(self):
        global installation_nest_list
        global count
        cursor.execute("""SELECT installation_nest FROM settings""")
        days = cursor.fetchone()[0]
        date = datetime.datetime.strptime(str(self.dateEdit.date().toPyDate()), '%Y-%m-%d')
        cursor.execute("""SELECT * FROM rabbit_litter WHERE status=1""")
        row = cursor.fetchone()
        while row is not None:
            if row[5] is None:
                date_cap = datetime.datetime.strptime(row[4], '%d.%m.%Y')
                check_date = date_cap + datetime.timedelta(days=days)
                if date == check_date:
                    exec('self.label{x} = QtWidgets.QLabel(self.scrollAreaWidgetContents)'.format(x=count))
                    exec('self.label{x}.setObjectName("label{x}")'.format(x=count))
                    exec('self.gridLayout.addWidget(self.label{x}, {x}, 0, 1, 2)'.format(x=count))
                    exec('self.label{x}.setText("Установить маточник самке Id-{i} в клетке №{x2}")'.format(
                        x=count, x2=row[3], i=row[1]))
                    check_box = f'self.label{count}'
                    installation_nest_list.append(check_box)
                    count += 1
            row = cursor.fetchone()

    def growing(self):
        global growing_list
        global count
        cursor.execute("""SELECT growing FROM settings""")
        days = cursor.fetchone()[0]
        date = datetime.datetime.strptime(str(self.dateEdit.date().toPyDate()), '%Y-%m-%d')
        cursor.execute("""SELECT * FROM rabbit_litter WHERE rabbits_nest>0 and status=1 """)
        row = cursor.fetchone()
        while row is not None:
            if row[5] is not None:
                date_cap = datetime.datetime.strptime(row[5], '%d.%m.%Y')
                check_date = date_cap + datetime.timedelta(days=days)
                if date == check_date:
                    exec('self.label{x} = QtWidgets.QLabel(self.scrollAreaWidgetContents)'.format(x=count))
                    exec('self.label{x}.setObjectName("label{x}")'.format(x=count))
                    exec('self.gridLayout.addWidget(self.label{x}, {x}, 0, 1, 2)'.format(x=count))
                    exec('self.label{x}.setText("Отсадить молодняк самки Id-{i} в клетке №{x2}")'.
                         format(x=count, x2=row[3], i=row[1]))
                    check_box = f'self.label{count}'
                    growing_list.append(check_box)
                    count += 1
            row = cursor.fetchone()

    def vaccinations(self):
        global vaccinations_list
        global count
        cursor.execute("""SELECT vaccinations.date_next, vaccinations.id_rabbit, rabbit.cell_number FROM vaccinations,
         rabbit WHERE vaccinations.id_rabbit=rabbit.id_rabbit and rabbit.st=1""")
        row = cursor.fetchone()
        while row is not None:
            date_next = datetime.datetime.strptime(row[0], '%Y-%m-%d')
            date = datetime.datetime.strptime(str(self.dateEdit.date().toPyDate()), '%Y-%m-%d')
            if date == date_next:
                exec('self.label{x} = QtWidgets.QLabel(self.scrollAreaWidgetContents)'.format(x=count))
                exec('self.label{x}.setObjectName("label{x}")'.format(x=count))
                exec('self.gridLayout.addWidget(self.label{x}, {x}, 0, 1, 2)'.format(x=count))
                exec('self.label{x}.setText("Привить кролика Id-{i} в клетке №{x2}")'.format(
                    x=count, x2=row[2], i=row[1]))
                check_box = f'self.label{count}'
                vaccinations_list.append(check_box)
                count += 1
            row = cursor.fetchone()

    def weigh(self):
        global weigh_list
        global count
        cursor.execute("""SELECT weigh FROM settings""")
        days = cursor.fetchone()[0]
        cursor.execute(
            """
            SELECT weigh.date_weigh,
            weigh.id_nest,
            rabbit_litter.cell FROM weigh,
            rabbit_litter 
            WHERE weigh.id_nest=rabbit_litter.id_rabbit_litter and status=1""")
        row = cursor.fetchone()
        while row is not None:
            date_past = datetime.datetime.strptime(row[0], '%Y-%m-%d')+datetime.timedelta(days=days)
            date = datetime.datetime.strptime(str(self.dateEdit.date().toPyDate()), '%Y-%m-%d')
            if date == date_past:
                exec('self.label{x} = QtWidgets.QLabel(self.scrollAreaWidgetContents)'.format(x=count))
                exec('self.label{x}.setObjectName("label{x}")'.format(x=count))
                exec('self.gridLayout.addWidget(self.label{x}, {x}, 0, 1, 2)'.format(x=count))
                exec('self.label{x}.setText("Взвесить гнездо Id-{i} в клетке №{x2}")'.
                     format(x=count, x2=row[2], i=row[1]))
                check_box = f'self.label{count}'
                weigh_list.append(check_box)
                count += 1
            row = cursor.fetchone()

    def remove_checkbox(self):
        global check_birth_list
        global growing_list
        global installation_nest_list
        global vaccinations_list
        global weigh_list
        global count
        count = 1
        if len(check_birth_list) > 0:
            for i in check_birth_list:
                exec(i+'.deleteLater()')
                lab = 'self.gridLayout.removeWidget('+i+')'
                exec(lab)
            check_birth_list.clear()

        if len(check_pre_birth) > 0:
            for i in check_pre_birth:
                exec(i+'.deleteLater()')
                lab1 = 'self.gridLayout.removeWidget('+i+')'
                exec(lab1)
            check_pre_birth.clear()

        if len(growing_list) > 0:
            for i in growing_list:
                exec(i+'.deleteLater()')
                lab2 = 'self.gridLayout.removeWidget('+i+')'
                exec(lab2)
            growing_list.clear()

        if len(installation_nest_list) > 0:
            for i in installation_nest_list:
                exec(i+'.deleteLater()')
                lab3 = 'self.gridLayout.removeWidget('+i+')'
                exec(lab3)
            installation_nest_list.clear()

        if len(vaccinations_list) > 0:
            for i in vaccinations_list:
                exec(i + '.deleteLater()')
                lab3 = 'self.gridLayout.removeWidget(' + i + ')'
                exec(lab3)
            vaccinations_list.clear()

        if len(weigh_list) > 0:
            for i in weigh_list:
                exec(i + '.deleteLater()')
                lab3 = 'self.gridLayout.removeWidget(' + i + ')'
                exec(lab3)
            weigh_list.clear()

        self.pre_birth()
        self.gestation()
        self.installation_nest()
        self.growing()
        self.vaccinations()
        self.weigh()

    def records_finance(self):
        """ Вкладка финансы."""
        cursor.execute("""SELECT categories FROM settings_finance""")
        self.comboBox_categories.addItems(str(cursor.fetchone()[0]).split(','))
        self.lineEdit_TheNote.setText('Без заметки')
        self.comboBox_diagram.addItems(("Все финансы", "Расходы", "Доходы"))

    def save_finance(self):
        """Сохраняет финансы."""
        date = str(datetime.datetime.today()).split(' ')[0]
        if self.doubleSpinBox_money.value() > 0:
            form = 1
        else:
            form = 0
        categories = self.comboBox_categories.currentText()
        note = self.lineEdit_TheNote.text()
        money = round(self.doubleSpinBox_money.value(), 2)

        cursor.execute("""INSERT INTO finance VALUES(?,?,?,?,?)""", (form, money, categories, note, date))
        conn.commit()
        self.check_finance_combox()
        self.saldo_table()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    application = MainWindow()
    application.show()

    sys.exit(app.exec_())
