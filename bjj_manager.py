import sys
import datetime

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QIcon


from Modules.messages import *

# enter point main function
from Modules.mainWindow import MainWindow


def main():
    date = datetime.datetime.now()
    # first preparations
    app = QtWidgets.QApplication(sys.argv)  # QApplication's object
    logging(app.primaryScreen().size())
    print(app.primaryScreen().size())
    try:
        check_folder()
    except FileNotFoundError:
        logging('Каталог или установочный файл отсутствуют')
    try:
        check_tables()
        window = MainWindow()
        window.setWindowTitle(f'BJJ SCORE MANAGER ©Все права принадлежат'
                              f' ОО "Федерация Айкидо и Джиу-Джитсу" {date.year} год')
        window.setWindowIcon(QIcon(r'.\Images\logo.jpg'))
        # window.showMaximized()
        # window.showFullScreen()
        window.show()
        app.exec_()
        logging('Закрытие программы')
    except NoAgeFilesError:
        pass


if __name__ == '__main__':
    logging('', is_start=True)
    logging('Открытие программы')
    main()
