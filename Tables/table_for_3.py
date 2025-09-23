import openpyxl

from Modules.excel_function import *
from Modules.flags import Flags
from Modules.utilities import *
from UI.counter_screen import Ui_MainWindow


class TableFor3(ExcelFunc):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.age = sample
        self.btn = None
        self.index_age = 0
        self.flags = Flags()

        self.d_counter3 = {}
        self.key = ''

        self.l_is_lap_3 = ['is_lap_3_1', 'is_lap_3_2', 'is_lap_3_3']

        # first sample file init
        self.file_path_3 = f'{file_name}{self.age}'
        self.wb_3 = openpyxl.load_workbook(self.file_path_3)
        self.t_3 = self.wb_3.worksheets[self.index_age]

    def set_table_3(self, age, btn, table, main_key):
        logging(main_key)
        self.new_dict_init(lap=self.l_is_lap_3,
                           d_counter=self.d_counter3,
                           main_key=main_key,
                           max_count=members_6_lap,
                           num=3)

        self.key = main_key
        self.age = age
        self.btn = btn
        self.file_path_3 = f'{file_name}{age}'
        self.wb_3 = openpyxl.load_workbook(self.file_path_3)
        self.t_3 = self.wb_3.worksheets[table]

        if self.d_counter3[main_key]['st_inc_3'] == 0:
            self.init_sportsmen_list(table=self.t_3,
                                     end=end_init_3,
                                     s_list=self.d_counter3[main_key]['l_key_win_lose_3'],
                                     s_dict=self.d_counter3[main_key]['d_win_lose_3'])
            self.draw_for_round_laps(table=self.t_3,
                                     s_list=self.d_counter3[main_key]['l_key_win_lose_3'],
                                     sheet=self.wb_3,
                                     file=self.file_path_3)
        self.show_on_board_t_3()

    def end_of_lap_3(self, num_lap):
        logging(end_lap)
        if num_lap == 2:
            logging(lap2)
            self.d_counter3[self.key]['is_lap_3_1'] = False
            self.d_counter3[self.key]['is_lap_3_2'] = True
            self.ui.lap1.setChecked(False)
            self.ui.lap2.setChecked(True)
        elif num_lap == 3:
            logging(lap3)
            self.d_counter3[self.key]['is_lap_3_2'] = False
            self.d_counter3[self.key]['is_lap_3_3'] = True
            self.ui.lap2.setChecked(False)
            self.ui.lap3.setChecked(True)
        elif num_lap == last:
            logging(finish)
            self.d_counter3[self.key]['is_lap_3_1'] = False
            self.d_counter3[self.key]['is_lap_3_2'] = False
            self.d_counter3[self.key]['is_lap_3_3'] = False
            self.ui.lap1.setChecked(False)
            self.ui.lap2.setChecked(False)
            self.ui.lap3.setChecked(False)
            self.ui.lap_finish.setChecked(True)
            self.define_places(table=self.t_3, btn=self.btn, num=3)

        counter_reset(counter=self.d_counter3, key=self.key, num=3)

    def round_laps_check_3(self):
        l_losers_3 = sorted(self.d_counter3[self.key]['l_losers_3'])
        d_win_lose_3 = sorted(self.d_counter3[self.key]['d_win_lose_3'])
        inc_r_laps_check_3 = self.d_counter3[self.key]['inc_r_laps_check_3']
        wins = self.d_counter3[self.key]['d_win_lose_3']

        # проверка на окончание кругов
        if self.d_counter3[self.key]['count3'] == members_6_lap - 1:
            if d_win_lose_3 != l_losers_3:
                # определение победителя
                for i in self.d_counter3[self.key]['d_win_lose_3']:
                    if wins[i]['Wins'] == 2 + inc_r_laps_check_3:
                        self.t_3[place_1] = i
                    if wins[i]['Wins'] == 1 + inc_r_laps_check_3:
                        self.t_3[place_2] = i
                    if wins[i]['Wins'] == 0 + inc_r_laps_check_3:
                        self.t_3[place_3] = i
                self.end_of_lap_3(num_lap=last)
            else:
                self.d_counter3[self.key]['inc_r_laps_check_3'] += 1

    def incrementation_3(self, end, num_lap, table=None, win_cell=None, score_cell=None,
                         s_losers=None, s_list=None, s_dict=None, as_losers_cell=None,
                         is_last_round=False, end_show_lap=None):

        if not self.equal_scores:
            counter_inc(counter=self.d_counter3, key=self.key, num=3)

        if self.d_counter3[self.key]['count3'] == end - 1:
            if is_last_round:
                self.last_round(table=table, win_cell=win_cell,
                                score_cell=score_cell,
                                s_losers=s_losers,
                                s_list=s_list,
                                s_dict=s_dict,
                                as_losers_cell=as_losers_cell,
                                end=end,
                                end_show_lap=end_show_lap)
                self.end_of_lap_3(num_lap)
            else:
                self.end_of_lap_3(num_lap)

    def laps_define_t_3(self):
        if self.d_counter3[self.key]['is_lap_3_1']:
            self.round_lap(table=self.t_3,
                           score_cell='C',
                           end=members_6_show,
                           count=self.d_counter3[self.key]['count3'],
                           s_list=self.d_counter3[self.key]['l_key_win_lose_3'],
                           s_dict=self.d_counter3[self.key]['d_win_lose_3'],
                           s_losers=self.d_counter3[self.key]['l_losers_3'])
            self.round_laps_check_3()
            self.incrementation_3(end=members_6_lap, num_lap=2)
        elif self.d_counter3[self.key]['is_lap_3_2']:
            self.round_lap(table=self.t_3,
                           score_cell='E',
                           end=members_6_show,
                           count=self.d_counter3[self.key]['count3'],
                           s_list=self.d_counter3[self.key]['l_key_win_lose_3'],
                           s_dict=self.d_counter3[self.key]['d_win_lose_3'],
                           s_losers=self.d_counter3[self.key]['l_losers_3'])
            self.round_laps_check_3()
            self.incrementation_3(end=members_6_lap, num_lap=3)
        elif self.d_counter3[self.key]['is_lap_3_3']:
            self.round_lap(table=self.t_3,
                           score_cell='G',
                           end=members_6_show,
                           count=self.d_counter3[self.key]['count3'],
                           s_list=self.d_counter3[self.key]['l_key_win_lose_3'],
                           s_dict=self.d_counter3[self.key]['d_win_lose_3'],
                           s_losers=self.d_counter3[self.key]['l_losers_3'])
            self.round_laps_check_3()
            self.incrementation_3(end=members_6_lap, num_lap=1)

        if self.equal_scores:
            self.d_counter3[self.key]['count3'] += 0
        else:
            self.d_counter3[self.key]['count3'] += 1

        self.equal_scores = False
        self.flags.is_table[1] = False
        self.set_active_tables(btn=self.btn,
                               sheet=self.wb_3,
                               file=self.file_path_3)
        self.on_off_spin(False)

    def show_on_board_t_3(self):
        self.laps_disable(start=4)
        self.on_off_spin(True)

        self.flags.is_table[1] = True
        self.set_inactive_tables(btn=self.btn)
        self.ui.spinBox.setValue(self.d_counter3[self.key]['count3'] + 1)

        if self.d_counter3[self.key]['is_lap_3_1']:
            logging('Бой №' + str(self.d_counter3[self.key]['count3'] + 1))
            self.lap_show(table=self.t_3,
                          cell='B',
                          count=self.d_counter3[self.key]['count3'],
                          s_losers=self.d_counter3[self.key]['l_losers_3'],
                          is_draw_by_lot=False,
                          end=members_6_show)
        if self.d_counter3[self.key]['is_lap_3_2']:
            self.draw_for_round_laps(table=self.t_3,
                                     s_list=self.d_counter3[self.key]['l_key_win_lose_3'],
                                     cell='D',
                                     sheet=self.wb_3,
                                     file=self.file_path_3
                                     )
            logging('Бой №' + str(self.d_counter3[self.key]['count3'] + 1))
            self.lap_show(table=self.t_3,
                          cell='D',
                          count=self.d_counter3[self.key]['count3'],
                          s_losers=self.d_counter3[self.key]['l_losers_3'],
                          is_draw_by_lot=False,
                          end=members_6_show)
        if self.d_counter3[self.key]['is_lap_3_3']:
            self.draw_for_round_laps(table=self.t_3,
                                     s_list=self.d_counter3[self.key]['l_key_win_lose_3'],
                                     cell='F',
                                     sheet=self.wb_3,
                                     file=self.file_path_3
                                     )
            logging('Бой №' + str(self.d_counter3[self.key]['count3'] + 1))
            self.lap_show(table=self.t_3,
                          cell='F',
                          count=self.d_counter3[self.key]['count3'],
                          s_losers=self.d_counter3[self.key]['l_losers_3'],
                          is_draw_by_lot=False,
                          end=members_6_show)

    def spin_manage_3(self):
        if self.key.__contains__(f'{t}3'):
            self.spin_manage(d_counter=self.d_counter3,
                             d_key=self.key,
                             l_isLap=self.l_is_lap_3,
                             num=3)
