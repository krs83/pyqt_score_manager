from PyQt5 import QtCore

from Modules.mainWindow import *
from UI.counter_screen import Ui_MainWindow


class Scores(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.flags = Flags()

        self.r_scores = 0
        self.r_adv = 0
        self.r_pen = 0
        self.b_scores = 0
        self.b_adv = 0
        self.b_pen = 0

        self.r_old_scores = 0
        self.b_old_scores = 0

    def reset(self):
        self.r_scores = 0
        self.b_scores = 0
        self.r_adv = 0
        self.b_adv = 0
        self.r_pen = 0
        self.b_pen = 0
        self.ui.b_scoreNum.display(self.b_scores)
        self.ui.r_scoreNum.display(self.r_scores)
        self.ui.b_advNum.display(self.b_adv)
        self.ui.r_advNum.display(self.r_adv)
        self.ui.r_penNum.display(self.r_pen)
        self.ui.b_penNum.display(self.b_pen)
        self.ui.b_fin.setDisabled(False)
        self.ui.r_fin.setDisabled(False)
        self.ui.b_fin_cancel.setDisabled(True)
        self.ui.r_fin_cancel.setDisabled(True)
        self.stop_timer()

    def r_finalization(self):
        self.r_scores += 100
        self.scores_check()
        self.ui.r_scoreNum.display(self.r_scores)
        self.ui.r_fin_cancel.setDisabled(False)
        self.ui.r_fin.setDisabled(True)

    def b_finalization(self):
        self.b_scores += 100
        self.scores_check()
        self.ui.b_scoreNum.display(self.b_scores)
        self.ui.b_fin_cancel.setDisabled(False)
        self.ui.b_fin.setDisabled(True)

    def r_finalization_cancel(self, scores):
        self.r_scores = scores-100
        self.ui.r_scoreNum.display(self.r_scores)
        self.ui.r_fin_cancel.setDisabled(True)
        self.ui.r_fin.setDisabled(False)

    def b_finalization_cancel(self, scores):
        self.b_scores = scores-100
        self.ui.b_scoreNum.display(self.b_scores)
        self.ui.b_fin_cancel.setDisabled(True)
        self.ui.b_fin.setDisabled(False)

    def scores_check(self):
        self.b_old_scores = self.b_scores
        self.r_old_scores = self.r_scores
        if self.b_scores < 0:
            self.b_scores = 0
        elif self.b_adv < 0:
            self.b_adv = 0
        elif self.b_pen < 0:
            self.b_pen = 0
        elif self.r_scores < 0:
            self.r_scores = 0
        elif self.r_adv < 0:
            self.r_adv = 0
        elif self.r_pen < 0:
            self.r_pen = 0
        elif self.b_scores > 99:
            self.b_scores = 99
        elif self.b_adv > 99:
            self.b_adv = 99
        elif self.b_pen > 99:
            self.b_pen = 99
        elif self.r_scores > 99:
            self.r_scores = 99
        elif self.r_adv > 99:
            self.r_adv = 99
        elif self.r_pen > 99:
            self.r_pen = 99

    def red_scores_add(self):
        self.r_scores += 1
        self.scores_check()
        self.ui.r_scoreNum.display(self.r_scores)

    def red_scores_sub(self):
        self.r_scores -= 1
        self.scores_check()
        self.ui.r_scoreNum.display(self.r_scores)

    def red_adv_add(self):
        self.r_adv += 1
        self.scores_check()
        self.ui.r_advNum.display(self.r_adv)

    def red_adv_sub(self):
        self.r_adv -= 1
        self.scores_check()
        self.ui.r_advNum.display(self.r_adv)

    def red_pen_add(self):
        self.r_pen += 1
        self.scores_check()
        self.ui.r_penNum.display(self.r_pen)

    def red_pen_sub(self):
        self.r_pen -= 1
        self.scores_check()
        self.ui.r_penNum.display(self.r_pen)

    def blue_scores_add(self):
        self.b_scores += 1
        self.scores_check()
        self.ui.b_scoreNum.display(self.b_scores)

    def blue_scores_sub(self):
        self.b_scores -= 1
        self.scores_check()
        self.ui.b_scoreNum.display(self.b_scores)

    def blue_adv_add(self):
        self.b_adv += 1
        self.scores_check()
        self.ui.b_advNum.display(self.b_adv)

    def blue_adv_sub(self):
        self.b_adv -= 1
        self.scores_check()
        self.ui.b_advNum.display(self.b_adv)

    def blue_pen_add(self):
        self.b_pen += 1
        self.scores_check()
        self.ui.b_penNum.display(self.b_pen)

    def blue_pen_sub(self):
        self.b_pen -= 1
        self.scores_check()
        self.ui.b_penNum.display(self.b_pen)

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Space:
            self.switcher()

        if e.key() == QtCore.Qt.Key_Escape:
            QtCore.QCoreApplication.quit()
        elif e.key() == QtCore.Qt.Key_Backspace:
            self.backward()

        elif e.key() == QtCore.Qt.Key_F12:
            self.reset()

        elif e.key() == QtCore.Qt.Key_BracketLeft:
            self.red_scores_add()
        elif e.key() == QtCore.Qt.Key_BracketRight:
            self.red_scores_sub()
        elif e.key() == QtCore.Qt.Key_Apostrophe:
            self.red_adv_add()
        elif e.key() == QtCore.Qt.Key_Backslash:
            self.red_adv_sub()
        elif e.key() == QtCore.Qt.Key_Period:
            self.red_pen_add()
        elif e.key() == QtCore.Qt.Key_Slash:
            self.red_pen_sub()

        elif e.key() == QtCore.Qt.Key_Q:
            self.blue_scores_add()
        if e.key() == QtCore.Qt.Key_W:
            self.blue_scores_sub()
        if e.key() == QtCore.Qt.Key_A:
            self.blue_adv_add()
        if e.key() == QtCore.Qt.Key_S:
            self.blue_adv_sub()
        if e.key() == QtCore.Qt.Key_Z:
            self.blue_pen_add()
        if e.key() == QtCore.Qt.Key_X:
            self.blue_pen_sub()

        elif e.key() == QtCore.Qt.Key_F12:
            self.reset()

        elif e.key() == QtCore.Qt.Key_F5:
            self.b_finalization()

        elif e.key() == QtCore.Qt.Key_F6:
            self.r_finalization()

        elif e.key() == QtCore.Qt.Key_Minus and not self.is_on:
            self.stop_timer()
        if self.ui.btn_timer_start.isEnabled():
            if e.key() == QtCore.Qt.Key_Plus:
                self.start_timer()

        if not self.is_on and not self.is_paused:
            if e.key() == QtCore.Qt.Key_2:
                self.set_2min()
            elif e.key() == QtCore.Qt.Key_3:
                self.set_3min()
            elif e.key() == QtCore.Qt.Key_4:
                self.set_4min()
            elif e.key() == QtCore.Qt.Key_5:
                self.set_5min()
