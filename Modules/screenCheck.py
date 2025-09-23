from PyQt5 import QtCore, QtGui

# screen_width = [800, 1024, 1152, 1280, 1360, 1400, 1600, 1680, 1792, 1856, 1920, 2048, 2560]
# screen_height = [600, 768, 800, 900, 1024, 1080, 1152, 1200, 1344, 1440, 1536, 1600]


def set_height(blue, red, bottom, b_scoreNum, r_scoreNum):
    h = QtGui.QGuiApplication.primaryScreen().size().height()
    block_height = h * 0.70
    bottom_height = h * 0.20
    scores_height = h * 0.3
    blue.setMinimumSize(QtCore.QSize(0, block_height))
    red.setMinimumSize(QtCore.QSize(0, block_height))
    bottom.setMinimumSize(QtCore.QSize(0, bottom_height))
    b_scoreNum.setMinimumSize(QtCore.QSize(0, scores_height))
    r_scoreNum.setMinimumSize(QtCore.QSize(0, scores_height))


def set_bottom_width(lcd_timer, right_bottom, left_bottom, tabWidget):
    w = QtGui.QGuiApplication.primaryScreen().size().width()
    halves = w * 0.4
    rest = w * 0.2
    lcd_timer.setMinimumSize(QtCore.QSize(rest, 0))
    left_bottom.setMinimumSize(QtCore.QSize(halves, 0))
    right_bottom.setMinimumSize(QtCore.QSize(halves, 0))
    tabWidget.setMaximumSize(QtCore.QSize(halves, 16777215))



