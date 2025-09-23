import openpyxl

from Modules.excel_function import *
from Modules.flags import Flags
from Modules.utilities import *
from UI.counter_screen import Ui_MainWindow


class TableFor2(ExcelFunc):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.age = sample
        self.btn = None
        self.index_age = 0
        self.flags = Flags()

        self.d_counter2 = {}
        self.key = ''

        self.l_is_lap_2 = ['is_lap_2_1']

        # first sample file init
        self.file_path_2 = f'{file_name}{self.age}'
        self.wb_2 = openpyxl.load_workbook(self.file_path_2)
        self.t_2 = self.wb_2.worksheets[self.index_age]

    def set_table_2(self, age, btn, table, main_key):
        logging(main_key)
        self.new_dict_init(lap=self.l_is_lap_2,
                           d_counter=self.d_counter2,
                           main_key=main_key,
                           max_count=members_6_lap,
                           num=2)

        self.key = main_key
        self.age = age
        self.btn = btn
        self.file_path_2 = f'{file_name}{age}'
        self.wb_2 = openpyxl.load_workbook(self.file_path_2)
        self.t_2 = self.wb_2.worksheets[table]

        if self.d_counter2[main_key]['st_inc_2'] == 0:
            self.init_sportsmen_list(table=self.t_2,
                                     end=end_init_2,
                                     s_list=self.d_counter2[main_key]['l_key_win_lose_2'],
                                     s_dict=self.d_counter2[main_key]['d_win_lose_2'])
            self.draw_for_round_laps(table=self.t_2,
                                     s_list=self.d_counter2[main_key]['l_key_win_lose_2'],
                                     members=members_4_lap,
                                     sheet=self.wb_2,
                                     file=self.file_path_2
                                     )
        self.show_on_board_t_2()

    def end_of_lap_2(self, num_lap):
        if num_lap == last:
            self.d_counter2[self.key]['is_lap_2_1'] = False
            self.ui.lap1.setChecked(False)
            self.ui.lap_finish.setChecked(True)
            self.define_places(table=self.t_2, btn=self.btn, num=2,  is_places2=True)

        counter_reset(counter=self.d_counter2, key=self.key, num=2)

    def round_laps_check_2(self):
        l_key_win_lose_2 = self.d_counter2[self.key]['l_key_win_lose_2']
        wins = self.d_counter2[self.key]['d_win_lose_2']
        for j in l_key_win_lose_2:
            if self.d_counter2[self.key]['d_win_lose_2'][j]['Wins'] == 2:
                # определение победителя
                for i in l_key_win_lose_2:
                    if wins[i]['Wins'] == 2:
                        self.t_2[place_1] = i
                    elif wins[i]['Wins'] == 0 or wins[i]['Wins'] == 1:
                        self.t_2[place_2] = i
                self.end_of_lap_2(num_lap=last)

    def incrementation_2(self, end, num_lap, table=None, win_cell=None, score_cell=None,
                         s_losers=None, s_list=None, s_dict=None, as_losers_cell=None,
                         is_last_round=False, end_show_lap=None):

        if not self.equal_scores:
            counter_inc(counter=self.d_counter2, key=self.key, num=2)

        if self.d_counter2[self.key]['count2'] == end - 1:
            if is_last_round:
                self.last_round(table=table,
                                win_cell=win_cell,
                                score_cell=score_cell,
                                s_losers=s_losers,
                                s_list=s_list,
                                s_dict=s_dict,
                                as_losers_cell=as_losers_cell,
                                end=end,
                                end_show_lap=end_show_lap)
                self.end_of_lap_2(num_lap)
            else:
                self.end_of_lap_2(num_lap)

    def laps_define_t_2(self):
        if self.d_counter2[self.key]['is_lap_2_1']:
            self.round_lap(table=self.t_2,
                           score_cell='C',
                           end=members_6_show,
                           count=self.d_counter2[self.key]['count2'],
                           s_losers=self.d_counter2[self.key]['l_losers_2'],
                           s_list=self.d_counter2[self.key]['l_key_win_lose_2'],
                           s_dict=self.d_counter2[self.key]['d_win_lose_2'])
            self.round_laps_check_2()
            self.incrementation_2(end=members_6_show, num_lap=last)

        if self.equal_scores:
            self.d_counter2[self.key]['count2'] += 0
        else:
            self.d_counter2[self.key]['count2'] += 1

        self.equal_scores = False
        self.flags.is_table[0] = False
        self.set_active_tables(btn=self.btn,
                               sheet=self.wb_2,
                               file=self.file_path_2)
        self.on_off_spin(False)

    def show_on_board_t_2(self):
        self.laps_disable(start=2)
        self.on_off_spin(True)

        self.flags.is_table[0] = True
        self.set_inactive_tables(btn=self.btn)
        self.ui.spinBox.setValue(self.d_counter2[self.key]['count2'] + 1)

        if self.d_counter2[self.key]['is_lap_2_1']:
            logging('Бой №' + str(self.d_counter2[self.key]['count2'] + 1))
            self.lap_show(table=self.t_2,
                          cell='B',
                          count=self.d_counter2[self.key]['count2'],
                          s_losers=self.d_counter2[self.key]['l_losers_2'],
                          is_draw_by_lot=False,
                          end=members_6_show)

    def spin_manage_2(self):
        if self.key.__contains__(f'{t}2'):
            self.spin_manage(d_counter=self.d_counter2,
                             d_key=self.key,
                             l_isLap=self.l_is_lap_2,
                             num=2)

