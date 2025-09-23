from random import randint

from PyQt5.QtWidgets import QWidget

from Modules.flags import Flags
from Modules.utilities import *
from Modules.messages import *

from UI.counter_screen import Ui_MainWindow


class ExcelFunc(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.flags = Flags()
        self.equal_scores = self.isOpenedFile = False

        self.r_scores = 0
        self.b_scores = 0
        self.r_adv = 0
        self.b_adv = 0
        self.r_pen = 0
        self.b_pen = 0

    def init_sportsmen_list(self, table, end, s_list, s_dict, start=start_init):
        for j in range(start, end):
            s_list.append(table[f'B{j}'].value)
        for keys in s_list:
            s_dict[keys] = {'Wins': 0, 'Loses': 0}

    def no_losers_msg(self):
        msg = QMessageBox()
        logging(t_lose_msg)
        msg.setIcon(QMessageBox.Warning)
        msg.setText(lose_msg)
        msg.setWindowTitle(t_lose_msg)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def draw_by_lot(self, table, cell, s_losers, num):
        try:
            table[cell] = s_losers[randint(0, num)]
            logging('по жеребьевке: ' + s_losers[randint(0, num)])
        except IndexError:
            self.no_losers_msg()

    def draw_for_round_laps(self, table, s_list, sheet, file, cell='B', members=members_6_lap):
        start_cell = 8
        if members == members_6_lap:
            # laps for three
            for c, i in enumerate(range(start_cell, members_6_show, 3), start=-2):
                table[f'{cell}{i}'] = s_list[c]
                table[f'{cell}{i + 1}'] = s_list[c + 1]
        else:
            # laps for two
            for c, i in enumerate(range(start_cell, members_6_show, 3), start=-1):
                table[f'{cell}{i}'] = s_list[c]
                table[f'{cell}{i + 1}'] = s_list[c - 1]
        save_file(sheet, file) # save the file to see names defined

    def set_inactive_tables(self, btn):
        self.ui.btn_all_tables.setDisabled(True)
        btn.setStyleSheet(active_btn)
        self.ui.btn_send_results.setDisabled(False)

    # TODO: V2 PermissionError - не учитывать шаг при открытом файле - все count and incs минусовать
    def set_active_tables(self, btn, sheet, file):
        self.ui.btn_send_results.setDisabled(True)
        self.ui.btn_all_tables.setDisabled(False)
        btn.setStyleSheet(non_active_btn)
        try:
            sheet.save(filename=file)
        except PermissionError:
            self.equal_scores = True
            close_file_msg()

    def define_places(self, table, btn, num, is_places2=False):
        btn.setText(f'({num})ЗАВЕРШЕНО')

        place1 = table[place_1].value
        place2 = table[place_2].value
        place3 = table[place_3].value
        cell1 = table['E23'].value
        cell2 = table['E24'].value
        cell3 = table['E25'].value

        try:
            if not is_places2:
                self.ui.first_place_label.setText(cell1 + ': ' + place1)
                self.ui.second_place_label.setText(cell2 + ': ' + place2)
                self.ui.third_place_label.setText(cell3 + ': ' + place3)
                logging(cell1 + ': ' + place1)
                logging(cell2 + ': ' + place2)
                logging(cell3 + ': ' + place3)
            else:
                self.ui.first_place_label.setText(cell1 + ': ' + place1)
                self.ui.second_place_label.setText(cell2 + ': ' + place2)
                logging(cell1 + ': ' + place1)
                logging(cell2 + ': ' + place2)
        except TypeError:
            empty_cells_msg()

    def late_loser_add(self, table, as_losers_cell, end, s_losers):
        # эта проверка отвечает за нечетные круги слева и распределяет поигравших
        # responsible for left odd laps and place losers to proper cells from the right
        inc = 0
        start_cell = 8
        is_10_members = False

        members10 = '10_'
        members9 = '9_'
        members6 = '6_'
        members5 = '5_'

        if table.title.__contains__(members10):
            start_cell = 12
            is_10_members = True
        elif table.title.__contains__(members9) and (end == members_6_lap or end == members_4_lap):
            start_cell = 11
        elif table.title.__contains__(members6) and end == members_4_lap:
            start_cell = 11
        elif table.title.__contains__(members5) and end == members_4_lap:
            start_cell = 9

        s_losers.remove(self.ui.b_sportsman_name.text())
        s_len = len(s_losers)
        for i in range(s_len):
            table[f'{as_losers_cell}{i + start_cell + m.floor(inc)}'] = s_losers[i]
            if is_10_members:
                inc += 1
            else:
                inc += 0.5

    def lap_for_finals(self, table, score_cell, s_losers, s_list, s_dict, win_cell='F',
                       lose_cell=default_cell, is_final=False):
        self.count_results(table=table, winner=f'{win_cell}23',
                           loser=f'{lose_cell}24',
                           s_list=s_list, s_dict=s_dict,
                           red_scores=f'{score_cell}8',
                           blue_scores=f'{score_cell}9',
                           s_losers=s_losers) if is_final \
            else self.count_results(table=table,
                                    winner=f'{win_cell}{25}',
                                    s_list=s_list, s_dict=s_dict,
                                    red_scores=f'{score_cell}8',
                                    blue_scores=f'{score_cell}9',
                                    s_losers=s_losers)

    def round_lap(self,
                  table,
                  score_cell,
                  end,
                  count,
                  s_losers,
                  s_list,
                  s_dict):
        start_lose_cell = 8
        for c, j in enumerate(range(start_lose_cell, end, 3)):
            if c == count < end:
                self.count_results(table=table, s_list=s_list, s_dict=s_dict,
                                   red_scores=f'{score_cell}{j}',
                                   blue_scores=f'{score_cell}{j + 1}',
                                   s_losers=s_losers)

    def lap(self,
            table,
            win_cell,
            score_cell,
            end,
            count,
            s_losers,
            s_list,
            s_dict,
            inc, inc1,
            start_lose_cell=8,
            lose_cell=default_cell,
            is_loser=False):
        if not self.equal_scores:
            for c, j in enumerate(range(0, end)):
                if c == count < end:
                    if is_loser:
                        self.count_results(table=table, winner=f'{win_cell}{j + 8 + m.floor(inc1)}',
                                           loser=f'{lose_cell}{j + start_lose_cell + m.floor(inc1)}',
                                           s_list=s_list, s_dict=s_dict,
                                           red_scores=f'{score_cell}{j + 8 + inc}',
                                           blue_scores=f'{score_cell}{j + 9 + inc}',
                                           s_losers=s_losers)
                    else:
                        self.count_results(table=table, winner=f'{win_cell}{j + 8 + m.floor(inc1)}',
                                           red_scores=f'{score_cell}{j + 8 + inc}',
                                           s_list=s_list, s_dict=s_dict,
                                           blue_scores=f'{score_cell}{j + 9 + inc}',
                                           s_losers=s_losers)

    def lap_with_late_loser_add(self,
                                table,
                                win_cell,
                                score_cell,
                                end,
                                count,
                                s_losers,
                                s_list,
                                s_dict,
                                inc, inc1):
        for c, j in enumerate(range(0, end)):

            if c == count < end - 1:
                self.count_results(table=table, winner=f'{win_cell}{j + 8 + m.floor(inc1)}',
                                   s_list=s_list, s_dict=s_dict,
                                   red_scores=f'{score_cell}{j + 8 + inc}',
                                   blue_scores=f'{score_cell}{j + 9 + inc}',
                                   s_losers=s_losers)

    def last_round(self,
                   table,
                   win_cell,
                   score_cell,
                   end,
                   end_show_lap,
                   s_losers,
                   s_list,
                   s_dict,
                   as_losers_cell):
        if end_show_lap % end == 0:
            inc = False + 1
        else:
            inc = True + 1
        cell_value = (end_show_lap - end) - int(inc)

        self.count_results(table=table, winner=f'{win_cell}{cell_value}',
                           s_list=s_list, s_dict=s_dict,
                           red_scores=f'{score_cell}{end_show_lap - 1}',
                           blue_scores=f'{score_cell}{end_show_lap}',
                           s_losers=s_losers)
        self.late_loser_add(table, as_losers_cell, end, s_losers)

    def lap_show(self, table, cell, end, count, s_losers, is_draw_by_lot=True, lot_cell=default_cell, rand_num=0):
        if end > members_4_show:
            limit = m.floor(end / 4)
        else:
            limit = m.floor(end / 5)
        for c, j in enumerate(range(0, end, 3)):
            if c == count and count < limit + 1:
                if is_draw_by_lot and count == limit - 1:
                    self.draw_by_lot(table, lot_cell, s_losers, rand_num)  # жеребьевка
                self.ui.r_sportsman_name.setText(table['{0}{1}'.format(cell, j + 8)].value)
                self.ui.b_sportsman_name.setText(table['{0}{1}'.format(cell, j + 9)].value)
                logging('красный: ' + str(table['{0}{1}'.format(cell, j + 8)].value))
                logging('синий: ' + str(table['{0}{1}'.format(cell, j + 9)].value))

    def red_wins_counter(self, table, s_list, s_dict):
        try:
            if self.ui.r_sportsman_name.text() in s_dict:
                s_dict[self.ui.r_sportsman_name.text()]['Wins'] += 1
                s_dict[self.ui.b_sportsman_name.text()]['Loses'] += 1

                table['C{0}'.format(s_list.index(self.ui.r_sportsman_name.text()) + 23)] = \
                    '{0}/{1}'.format(s_dict[self.ui.r_sportsman_name.text()]['Wins'],
                                     s_dict[self.ui.r_sportsman_name.text()]['Loses'])
                table['C{0}'.format(s_list.index(self.ui.b_sportsman_name.text()) + 23)] = \
                    '{0}/{1}'.format(s_dict[self.ui.b_sportsman_name.text()]['Wins'],
                                     s_dict[self.ui.b_sportsman_name.text()]['Loses'])
        except KeyError:
            empty_cells_msg()

    def blue_wins_counter(self, table, s_list, s_dict):
        try:
            if self.ui.b_sportsman_name.text() in s_dict:
                s_dict[self.ui.b_sportsman_name.text()]['Wins'] += 1
                s_dict[self.ui.r_sportsman_name.text()]['Loses'] += 1
                table['C{0}'.format(s_list.index(self.ui.b_sportsman_name.text()) + 23)] = \
                    '{0}/{1}'.format(s_dict[self.ui.b_sportsman_name.text()]['Wins'],
                                     s_dict[self.ui.b_sportsman_name.text()]['Loses'])
                table['C{0}'.format(s_list.index(self.ui.r_sportsman_name.text()) + 23)] = \
                    '{0}/{1}'.format(s_dict[self.ui.r_sportsman_name.text()]['Wins'],
                                     s_dict[self.ui.r_sportsman_name.text()]['Loses'])
        except KeyError:
            empty_cells_msg()

    def red_won(self, table, winner, loser, s_losers, s_list, s_dict):
        table[winner] = self.ui.r_sportsman_name.text()
        table[loser] = self.ui.b_sportsman_name.text()
        self.red_wins_counter(table, s_list, s_dict)
        s_losers.append(self.ui.b_sportsman_name.text())

    def blue_won(self, table, winner, loser, s_losers, s_list, s_dict):
        table[winner] = self.ui.b_sportsman_name.text()
        table[loser] = self.ui.r_sportsman_name.text()
        self.blue_wins_counter(table, s_list, s_dict)
        s_losers.append(self.ui.r_sportsman_name.text())

    def scores_equal_msg(self):
        msg = QMessageBox()
        logging(score_equal_msg)
        msg.setIcon(QMessageBox.Warning)
        msg.setText(score_equal_msg)
        msg.setWindowTitle(t_score_equal_msg)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def count_results(self, table, red_scores, blue_scores, s_losers, s_list, s_dict,
                      winner=default_cell, loser=default_cell):
        if self.r_scores == self.b_scores:
            if self.r_adv == self.b_adv:
                if self.r_pen == self.b_pen:
                    self.equal_scores = True
                    self.scores_equal_msg()
                else:
                    self.blue_won(table, winner, loser, s_losers, s_list, s_dict) if self.r_pen > self.b_pen else \
                        self.red_won(table, winner, loser, s_losers, s_list, s_dict)
            else:
                self.red_won(table, winner, loser, s_losers, s_list, s_dict) if self.r_adv > self.b_adv else \
                    self.blue_won(table, winner, loser, s_losers, s_list, s_dict)
        else:
            self.red_won(table, winner, loser, s_losers, s_list, s_dict) if self.r_scores > self.b_scores else \
                self.blue_won(table, winner, loser, s_losers, s_list, s_dict)
        table[red_scores] = f'{self.r_scores}-{self.r_adv}-{self.r_pen}'
        table[blue_scores] = f'{self.b_scores}-{self.b_adv}-{self.b_pen}'
        logging('очки красный: ' + str(self.r_scores) + '-' + str(self.r_adv) + '-' + str(self.r_pen))
        logging('очки синий: ' + str(self.b_scores) + '-' + str(self.b_adv) + '-' + str(self.b_pen))

    # TODO: v2 other functions - to replace it to another file - make a refactoring all code

    def spin_manage(self, d_counter, d_key, l_isLap, num):
        try:
            # set all isLaps to False
            for key in l_isLap:
                d_counter[d_key][key] = False
                # search for checked box and set proper isLap
            for i in range(1, 9):
                if eval(f'self.ui.lap{i}').isChecked():
                    d_counter[d_key][f'is_lap_{num}_{i}'] = True

            d_counter[d_key][f'count{num}'] = self.ui.spinBox.value() - 1
            d_counter[d_key][f'inc_{num}'] = d_counter[d_key][f'count{num}'] * 2
            d_counter[d_key][f'inc1_{num}'] = d_counter[d_key][f'count{num}'] / 2
            self.on_off_spin(True)
        except KeyError:
            no_key_msg()

    def lap_init(self, lap, counter, main_key, max_count, num):
        # append is_laps flags to the dict as False
        for key in lap:
            counter[main_key][key] = False

        counter[main_key][f'is_lap_{num}_1'] = True
        self.ui.lap1.setChecked(True)
        logging(lap1)
        self.ui.spinBox.setMaximum(max_count)

    def new_dict_init(self, lap, d_counter, main_key, max_count, num):
        # create new dict for counters, laps and other lists, also count incrementing
        if main_key in d_counter:
            d_counter[main_key][f'st_inc_{num}'] += 1
        else:
            d_counter[main_key] = {
                f'count{num}': 0,
                f'inc_{num}': 0,
                f'inc1_{num}': 0,
                f'st_inc_{num}': 0,
                f'l_key_win_lose_{num}': [],
                f'd_win_lose_{num}': {},
                f'l_losers_{num}': [],
                f'l_is_lap_{num}': [],
                f'inc_r_laps_check_{num}': 0}

            self.lap_init(lap=lap, counter=d_counter, main_key=main_key, max_count=max_count, num=num)

    # if clicked for the first time the table should be initialised
    def check_new_counter(self, d_counter, main_key, table, wb, file_path, member_len, num, is_odd=False):
        if d_counter[main_key][f'st_inc_{num}'] == 0:
            self.init_sportsmen_list(table=table,
                                     end=eval(f'end_init_{num}'),
                                     s_list=d_counter[main_key][f'l_key_win_lose_{num}'],
                                     s_dict=d_counter[main_key][f'd_win_lose_{num}'])
            filling_cells(table=table,
                          end=eval(f'end_init_{num}'),
                          member_len=member_len,
                          sheet=wb,
                          file=file_path,
                          s_list=d_counter[main_key][f'l_key_win_lose_{num}'],
                          is_odd=is_odd
                          )

    def laps_disable(self, start=1, is_disabled=True):
        # on all radio laps btns
        for i in range(1, 9):
            eval(f'self.ui.lap{i}').setEnabled(True)
        # off extra radio laps btns
        if is_disabled:
            for i in range(start, 9):
                eval(f'self.ui.lap{i}').setDisabled(True)


