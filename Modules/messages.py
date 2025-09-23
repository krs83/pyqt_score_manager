import os

from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore

from Errors.noagefileserror import NoAgeFilesError
from Modules.const import *
from Modules.utilities import logging

age_list = []
age_list_unuse = []


# QMessageBoxes
# no Categories folder or sample file
def no_folder_msg():
    msg = QMessageBox()
    logging('Пожалуйста, добавьте файлы в проект')
    msg.setIcon(QMessageBox.Warning)
    msg.setText(f'Пожалуйста, добавьте {sample} в каталог Categories в проект')
    msg.setWindowTitle('Установочный каталог или файл не существуют!!!')
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()


def no_table_files_msg():
    msg = QMessageBox()
    logging('Пожалуйста, добавьте файлы с возрастными категориями в проект')
    msg.setIcon(QMessageBox.Warning)
    msg.setText(f'Пожалуйста, добавьте файлы с возрастными категориями в проект')
    msg.setWindowTitle('Файлы с возрастными категориями не обнаружены')
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()


def table_files_msg():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText(f'Обнаружены следующие файлы с возрастными категориями\n{file_name}\n{age_list}')
    logging(age_list)
    msg.setWindowTitle('Файлы с возрастными категориями')
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()


def no_key_msg():
    msg = QMessageBox()
    logging('Пожалуйста, сначала выберите возрастную категорию')
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Пожалуйста, сначала выберите возрастную категорию')
    msg.setWindowTitle('Возрастная категория не выбрана!!!')
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()


def empty_cells_msg():
    msg = QMessageBox()
    logging('Одна или более ячеек на данный момент пустые!')
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Одна или более ячеек на данный момент пустые!')
    msg.setWindowTitle('Ошибка данных в ячейках!!!')
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()


# check if sample file or Category folder exists
def check_folder():
    if not os.path.isfile(f'{file_name}\\{sample}'):
        no_folder_msg()
        QtCore.QCoreApplication.quit()
    else:
        logging('Sample файл устанавливает начальные значения...')
        return


def check_tables():
    c = 0
    for age in ages_file:
        if os.path.isfile(f'{file_name}\\{age}'):
            c += 1
            if c == 1:
                logging('Обнаружены следующие файлы с возрастными категориями')
            age_list.append(age)
    table_files_msg()
    if c == 0:
        logging('Ошибка! Файлы с возрастными категориями не обнаружены')
        no_table_files_msg()
        raise NoAgeFilesError


def tab_index_search():
    for c, i in enumerate(ages_file):
        if i not in age_list:
            age_list_unuse.append(c)
