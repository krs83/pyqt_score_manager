import datetime
import math as m
from random import shuffle

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog

from Modules.messages import *
from UI.Modals.UIshuffle_list_notification import UIShuffleNotification


def logging(msg, is_start=False):
    date = datetime.datetime.now()
    with open('logs.txt', 'a') as file_log:
        if is_start:
            print(f'{msg}', file=file_log)
        else:
            print(f'{date.today().replace(microsecond=0)}: {msg}', file=file_log)


def filling_cells(table, end, s_list, member_len, sheet, file, is_odd=False, start=start_init):
    shuffle_notif = ShuffleNotification()

    shuffle_notif.setWindowTitle(table.title)
    shuffle_notif.show()
    answer = shuffle_notif.exec_()

    start_cell = 8
    inc = 0

    # запрос на смешивание списка
    # берет начальный список из excel файла
    if answer == QDialog.Accepted:
        logging('Да')
        shuffle(s_list)
        # replace with shuffled list and fill start cells
        for count, j in enumerate(range(start, end)):
            table[f'B{j}'] = s_list[count]
        save_file(sheet, file)
    else:
        logging('Нет')

    # fill the fight cells with shuffled list if accepted

    res = m.ceil((member_len - start_cell) / 3)
    for count, j in enumerate(range(start_cell, member_len, 3)):
        if res - 1 != count:
            table[f'B{j}'] = s_list[count + inc]
            table[f'B{j + 1}'] = s_list[count + inc + 1]
        else:
            if is_odd:
                table[f'B{j}'] = s_list[count + inc]
            else:
                table[f'B{j}'] = s_list[count + inc]
                table[f'B{j + 1}'] = s_list[count + inc + 1]
        inc += 1
    save_file(sheet, file)


class ShuffleNotification(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.shuffle_notif = UIShuffleNotification()
        self.shuffle_notif.setupUi(self)
        logging(self.shuffle_notif.label.text())


def counter_reset(counter, key, num):
    counter[key][f'l_losers_{num}'].clear()
    counter[key][f'count{num}'] = -1
    counter[key][f'inc_{num}'] = 0
    counter[key][f'inc1_{num}'] = 0


def counter_inc(counter, key, num):
    counter[key][f'inc_{num}'] += 2
    counter[key][f'inc1_{num}'] += 0.5


def close_file_msg():
    msg = QMessageBox()
    logging('Пожалуйста, закройте excel файл')
    msg.setIcon(QMessageBox.Warning)
    msg.setText('ФАЙЛ НЕ СОХРАНЕН!!!\nПожалуйста, закройте excel файл')
    msg.setWindowTitle('ФАЙЛ НЕ СОХРАНЕН!!!')
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()


def save_file(sheet, file):
    try:
        sheet.save(filename=file)
    except PermissionError:
        close_file_msg()
