#!/usr/bin/env python3
# coding=utf-8

import sys
from random import randint

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('uis/main.ui', self)  # загрузка формы в py-скрипт

        self.setWindowTitle('GMB05_lab4_1')
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))

        self.btn_random_number.clicked.connect(self.fill_random_numbers)
        self.btn_solve.clicked.connect(self.solve)

    def fill_random_numbers(self):
        """
        заполняем таблицу случайными числами
        :return:
        """
        row = 0
        col = 0

        # заполняем таблицу случайными числами

        while row < self.tableWidget.rowCount():
            while col < self.tableWidget.columnCount():
                random_num = randint(0, 101)
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(random_num)))
                item = self.tableWidget.item(row, col).text()
                col += 1
            row += 1
            col = 0

        # находим максимальное число и его координаты
        # [0] - максимальное число, [1] - строка максимума, [2] - столбец максимума
        list_information_max_num = find_max(self.tableWidget)

        if not list_information_max_num:
            self.label_error.setText('Введены неправильные данные!')
        else:
            # выводим на экран информацию о расположении максимального числа
            self.label_max_el.setText(
                'Максимальный элемент: ' + str(list_information_max_num[0]) + ' [' +
                str(list_information_max_num[1]) + ';' + str(list_information_max_num[2]) + ']')
            self.label_min_el.setText(
                'Минимальный элемент: ' + str(list_information_max_num[3]) + ' [' +
                str(list_information_max_num[4]) + ';' + str(list_information_max_num[5]) + ']')

        # list_information_min_num = find_min(self.tableWidget)

        # if not list_information_min_num:
        #     self.label_error.setText('Введены неправильные данные!')
        # else:
        # #     # выводим на кэран информацию о расположении максимального числа
        #     self.label_min_el.setText(
        #         'Минимальный элемент: ' + str(list_information_min_num[0]) + ' [' +
        #         str(list_information_min_num[1]) + ';' + str(list_information_min_num[2]) + ']')

        self.label_error.setText('')

    def solve(self):
        list_information_max_num = find_max(self.tableWidget)
        # list_information_min_num = find_min(self.tableWidget)

        if not list_information_max_num:
            self.label_error.setText('Введены некорректные данные!')
        else:
            self.label_max_el.setText(
                'Максимальный элемент: ' + str(list_information_max_num[0]) + ' [' +
                str(list_information_max_num[1]) + ';' + str(list_information_max_num[2]) + ']')
            self.label_min_el.setText(
                'Минимальный элемент: ' + str(list_information_max_num[3]) + ' [' +
                str(list_information_max_num[4]) + ';' + str(list_information_max_num[5]) + ']')

            # if not list_information_min_num:
        #     self.label_error.setText('Введены некорректные данные!')
        # else:
        #     self.label_min_el.setText(
        #         'Минимальный элемент: ' + str(list_information_max_num[3]) + ' [' +
        #         str(list_information_max_num[4]) + ';' + str(list_information_max_num[5]) + ']')

            # -*- решение задания -*-
        row = 0
        col = 0
        num_zero = 0
        num_one = 1

        pol_min = list_information_max_num[4] * self.tableWidget.rowCount() + list_information_max_num[5] + 1
        pol_max = list_information_max_num[1] * self.tableWidget.rowCount() + list_information_max_num[2] + 1

        if (pol_max > pol_min):
            while row < self.tableWidget.rowCount():
                while col < self.tableWidget.columnCount():
                    number = [float(self.tableWidget.item(row, col).text()), row, col]
                    if number != list_information_max_num:
                        self.tableWidget.setItem(row, col, QTableWidgetItem(str(num_zero)))
                        self.tableWidget.setItem(list_information_max_num[1], list_information_max_num[2], QTableWidgetItem(str(num_one)))
                        self.tableWidget.setItem(list_information_max_num[4], list_information_max_num[5], QTableWidgetItem(str(num_one)))
                    col += 1
                row += 1
                col = 0
        else:
            self.label_error.setText('Условия не выполнены!')


def find_max(table_widget):
    """
    находим максимальное число из таблицы и его координаты
    :param table_widget: таблица
    :return: [max_num, row_max_number, col_max_number], если выкинуто исключение,
            то None
    """
    row_min_number = 0  # номер строки, в котором находится максимальне число
    col_min_number = 0
    row_max_number = 0  # номер строки, в котором находится максимальне число
    col_max_number = 0  # номер столбца, в котором находится максимальне число
    max_num = float(table_widget.item(row_max_number, col_max_number).text())  # Максимальное значение
    min_num = max_num

    row = 0
    col = 0

    try:
        while row < table_widget.rowCount():
            while col < table_widget.columnCount():
                number = float(table_widget.item(row, col).text())
                if number >= max_num:
                    max_num = number
                    row_max_number = row
                    col_max_number = col
                if number <= min_num:
                    min_num = number
                    row_min_number = row
                    col_min_number = col
                col += 1
            row += 1
            col = 0
        return [max_num, row_max_number, col_max_number, min_num, row_min_number, col_min_number]
    except Exception:
        return None

# def find_min(table_widget):
#     """
#     находим максимальное число из таблицы и его координаты
#     :param table_widget: таблица
#     :return: [max_num, row_max_number, col_max_number], если выкинуто исключение,
#             то None
#     """
#
#     row_min_number = 0  # номер строки, в котором находится максимальне число
#     col_min_number = 0  # номер столбца, в котором находится максимальне число
#     min_num = float(table_widget.item(row_min_number, col_min_number).text())  # Максимальное значение
#
#     row = 0
#     col = 0
#
#     try:
#         while row < table_widget.rowCount():
#             while col < table_widget.columnCount():
#                 number = float(table_widget.item(row, col).text())
#                 if number <= min_num:
#                     min_num = number
#                     row_min_number = row
#                     col_min_number = col
#                 col += 1
#             row += 1
#             col = 0
#         return [min_num, row_min_number, col_min_number]
#     except Exception:
#         return None
#

def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
