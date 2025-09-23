import os

from PyQt5.QtCore import QTimer
from PyQt5 import QtWidgets, QtMultimedia
from datetime import datetime, timedelta

from Modules.utilities import logging
from UI.counter_screen import Ui_MainWindow


class ScoreTimer(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.time = None
        self.ui = Ui_MainWindow()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.show_time)
        self.set_time = '03:00'
        self.time = datetime.strptime(self.set_time, "%H:%M")
        self.is_on = False
        self.is_paused = False
        self.CURRENT_DIR = os.path.join(os.path.dirname(__file__))
        self.filename = os.path.join(self.CURRENT_DIR, r"..\Music\gong.wav")

    def setting_time(self):
        self.time = datetime.strptime(self.set_time, "%H:%M")
        self.ui.lcd_timer.display(self.set_time)

    def set_2min(self):
        self.set_time = '02:00'
        self.setting_time()

    def set_3min(self):
        self.set_time = '03:00'
        self.setting_time()

    def set_4min(self):
        self.set_time = '04:00'
        self.setting_time()

    def set_5min(self):
        self.set_time = '05:00'
        self.setting_time()

    def stop_timer(self):
        logging('Остановка времени')
        self.ui.lcd_timer.setStyleSheet("background-color: rgb(26, 255, 141)")
        self.timer.stop()
        self.time = datetime.strptime(self.set_time, "%H:%M")
        self.ui.lcd_timer.display(self.set_time)
        self.is_on = False
        self.is_paused = False
        self.ui.time_box.setDisabled(False)
        self.ui.btn_timer_start.setText('Старт')
        self.ui.btn_timer_start.setDisabled(False)

    def show_time(self):
        if self.is_on:
            self.ui.btn_timer_reset.setDisabled(True)
        self.time = self.time - timedelta(seconds=60)
        self.ui.lcd_timer.display(str(self.time).split()[1])
        if self.time == datetime.strptime('00:00', "%H:%M"):
            self.ui.lcd_timer.setStyleSheet('background-color: rgb(255, 40, 0)')
            self.timer.stop()
            self.ui.btn_timer_start.setDisabled(True)
            QtMultimedia.QSound.play(self.filename)
            self.ui.btn_timer_reset.setDisabled(False)
            self.ui.time_box.setDisabled(False)
            self.is_on = False

    def pause_timer(self):
        self.timer.stop()
        self.is_on = False
        self.is_paused = True
        self.ui.btn_timer_reset.setDisabled(False)
        self.ui.btn_timer_start.setText('Старт')
        self.ui.lcd_timer.setStyleSheet('background-color: rgb(255, 255, 0)')

    def start_timer(self):
        self.ui.lcd_timer.setStyleSheet("background-color: rgb(26, 255, 141)")
        if not self.is_on:
            self.is_on = True
            self.is_paused = False
            self.ui.btn_timer_reset.setDisabled(True)
            self.ui.time_box.setDisabled(True)
            self.ui.btn_timer_start.setText('Пауза')
            self.timer.start(1000)
        else:
            self.pause_timer()
