# TODO: V2 при включении флага финиш ошибки а также при выборе несущест номера боя в кругу
import openpyxl

from Modules.excel_function import *
from Modules.flags import Flags
from Modules.utilities import *
from UI.counter_screen import Ui_MainWindow


class TableFor8(ExcelFunc):
    def __init__(self):
        super().__init__()
        self.age = sample
        self.btn = None
        self.index_age = 0
        self.ui = Ui_MainWindow()
        self.flags = Flags()

        self.d_counter8 = {}
        self.key = ''

        self.l_is_lap_8 = ['is_lap_8_1', 'is_lap_8_2', 'is_lap_8_3',
                           'is_lap_8_4', 'is_lap_8_5', 'is_lap_8_6']

        # first sample file init
        self.file_path_8 = f'{file_name}{self.age}'
        self.wb_8 = openpyxl.load_workbook(self.file_path_8)
        self.t_8 = self.wb_8.worksheets[self.index_age]

    def set_table_8(self, age, btn, table, main_key):
        logging(main_key)
        self.new_dict_init(lap=self.l_is_lap_8,
                           d_counter=self.d_counter8,
                           main_key=main_key,
                           max_count=members_8_lap,
                           num=8)

        self.key = main_key
        self.age = age
        self.btn = btn
        self.file_path_8 = f'{file_name}{age}'
        self.wb_8 = openpyxl.load_workbook(self.file_path_8)
        self.t_8 = self.wb_8.worksheets[table]

        self.check_new_counter(d_counter=self.d_counter8,
                               main_key=main_key,
                               table=self.t_8,
                               wb=self.wb_8,
                               file_path=self.file_path_8,
                               member_len=members_8_show,
                               num=8)
        print(self.d_counter8)

        self.show_on_board_t_8()

    def end_of_lap_8(self, num_lap):
        logging(end_lap)
        if num_lap == 2:
            logging(lap2)
            self.d_counter8[self.key]['is_lap_8_1'] = False
            self.d_counter8[self.key]['is_lap_8_2'] = True
            self.ui.lap1.setChecked(False)
            self.ui.lap2.setChecked(True)
            self.ui.spinBox.setMaximum(2)
        elif num_lap == 3:
            logging(lap3)
            self.d_counter8[self.key]['is_lap_8_2'] = False
            self.d_counter8[self.key]['is_lap_8_3'] = True
            self.ui.lap2.setChecked(False)
            self.ui.lap3.setChecked(True)
            self.ui.spinBox.setMaximum(2)
        elif num_lap == 4:
            logging(lap4)
            self.d_counter8[self.key]['is_lap_8_3'] = False
            self.d_counter8[self.key]['is_lap_8_4'] = True
            self.ui.lap3.setChecked(False)
            self.ui.lap4.setChecked(True)
            self.ui.spinBox.setMaximum(2)
        elif num_lap == 5:
            logging(lap5)
            self.d_counter8[self.key]['is_lap_8_4'] = False
            self.d_counter8[self.key]['is_lap_8_5'] = True
            self.ui.lap4.setChecked(False)
            self.ui.lap5.setChecked(True)
            self.ui.spinBox.setMaximum(1)
        elif num_lap == 6:
            logging(lap6)
            self.d_counter8[self.key]['is_lap_8_5'] = False
            self.d_counter8[self.key]['is_lap_8_6'] = True
            self.ui.lap5.setChecked(False)
            self.ui.lap6.setChecked(True)
        elif num_lap == last:
            logging(finish)
            self.d_counter8[self.key]['is_lap_8_6'] = False
            self.ui.lap6.setChecked(False)
            self.ui.lap_finish.setChecked(True)
            self.define_places(table=self.t_8, btn=self.btn, num=8)

        counter_reset(counter=self.d_counter8, key=self.key, num=8)

    def incrementation_8(self, end, num_lap, table=None, win_cell=None, score_cell=None,
                         s_losers=None, s_list=None, s_dict=None, as_losers_cell=None,
                         is_last_round=False, end_show_lap=None):

        if not self.equal_scores:
            counter_inc(counter=self.d_counter8, key=self.key, num=8)

        if self.d_counter8[self.key]['count8'] == end - 1:
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
                self.end_of_lap_8(num_lap)
            else:
                self.end_of_lap_8(num_lap)

    def laps_define_t_8(self):
        if self.d_counter8[self.key]['is_lap_8_1']:
            self.lap(table=self.t_8,
                     win_cell='D',
                     lose_cell='L',
                     score_cell='C',
                     end=members_8_lap,
                     is_loser=True,
                     count=self.d_counter8[self.key]['count8'],
                     s_list=self.d_counter8[self.key]['l_key_win_lose_8'],
                     s_dict=self.d_counter8[self.key]['d_win_lose_8'],
                     s_losers=self.d_counter8[self.key]['l_losers_8'],
                     inc=self.d_counter8[self.key]['inc_8'],
                     inc1=self.d_counter8[self.key]['inc1_8'])
            self.incrementation_8(end=members_8_lap, num_lap=2)
        elif self.d_counter8[self.key]['is_lap_8_2']:
            self.lap(table=self.t_8,
                     win_cell='J',
                     score_cell='M',
                     count=self.d_counter8[self.key]['count8'],
                     s_list=self.d_counter8[self.key]['l_key_win_lose_8'],
                     s_dict=self.d_counter8[self.key]['d_win_lose_8'],
                     s_losers=self.d_counter8[self.key]['l_losers_8'],
                     inc=self.d_counter8[self.key]['inc_8'],
                     inc1=self.d_counter8[self.key]['inc1_8'],
                     end=members_4_lap,
                     )
            self.incrementation_8(end=members_4_lap, num_lap=3)
        elif self.d_counter8[self.key]['is_lap_8_3']:
            self.lap(table=self.t_8,
                     win_cell='F',
                     lose_cell='J',
                     score_cell='E',
                     end=members_4_lap,
                     is_loser=True,
                     start_lose_cell=11,
                     count=self.d_counter8[self.key]['count8'],
                     s_list=self.d_counter8[self.key]['l_key_win_lose_8'],
                     s_dict=self.d_counter8[self.key]['d_win_lose_8'],
                     s_losers=self.d_counter8[self.key]['l_losers_8'],
                     inc=self.d_counter8[self.key]['inc_8'],
                     inc1=self.d_counter8[self.key]['inc1_8'])
            self.incrementation_8(end=members_4_lap, num_lap=4)
        elif self.d_counter8[self.key]['is_lap_8_4']:
            self.lap(table=self.t_8,
                     win_cell='H',
                     score_cell='K',
                     count=self.d_counter8[self.key]['count8'],
                     s_list=self.d_counter8[self.key]['l_key_win_lose_8'],
                     s_dict=self.d_counter8[self.key]['d_win_lose_8'],
                     s_losers=self.d_counter8[self.key]['l_losers_8'],
                     inc=self.d_counter8[self.key]['inc_8'],
                     inc1=self.d_counter8[self.key]['inc1_8'],
                     end=members_4_lap, )
            self.incrementation_8(end=members_4_lap, num_lap=5)
        elif self.d_counter8[self.key]['is_lap_8_5']:
            self.lap_for_finals(table=self.t_8,
                                score_cell='I',
                                s_list=self.d_counter8[self.key]['l_key_win_lose_8'],
                                s_dict=self.d_counter8[self.key]['d_win_lose_8'],
                                s_losers=self.d_counter8[self.key]['l_losers_8'])
            self.end_of_lap_8(num_lap=6)
        elif self.d_counter8[self.key]['is_lap_8_6']:
            self.lap_for_finals(table=self.t_8,
                                lose_cell='F',
                                score_cell='G',
                                is_final=True,
                                s_list=self.d_counter8[self.key]['l_key_win_lose_8'],
                                s_dict=self.d_counter8[self.key]['d_win_lose_8'],
                                s_losers=self.d_counter8[self.key]['l_losers_8'])
            self.end_of_lap_8(num_lap=last)

        if self.equal_scores:
            self.d_counter8[self.key]['count8'] += 0
        else:
            self.d_counter8[self.key]['count8'] += 1

        self.equal_scores = False
        self.flags.is_table[6] = False
        self.set_active_tables(btn=self.btn,
                               sheet=self.wb_8,
                               file=self.file_path_8)
        self.on_off_spin(False)

    def show_on_board_t_8(self):
        self.laps_disable(start=7)
        self.on_off_spin(True)

        self.flags.is_table[6] = True
        self.set_inactive_tables(btn=self.btn)
        self.ui.spinBox.setValue(self.d_counter8[self.key]['count8'] + 1)

        if self.d_counter8[self.key]['is_lap_8_1']:
            logging('Бой №' + str(self.d_counter8[self.key]['count8'] + 1))
            self.lap_show(table=self.t_8,
                          cell='B',
                          count=self.d_counter8[self.key]['count8'],
                          s_losers=self.d_counter8[self.key]['l_losers_8'],
                          is_draw_by_lot=False,
                          end=members_8_show)
        elif self.d_counter8[self.key]['is_lap_8_2']:
            logging('Бой №' + str(self.d_counter8[self.key]['count8'] + 1))
            self.lap_show(table=self.t_8,
                          cell='L',
                          count=self.d_counter8[self.key]['count8'],
                          s_losers=self.d_counter8[self.key]['l_losers_8'],
                          is_draw_by_lot=False,
                          end=members_4_show)
        elif self.d_counter8[self.key]['is_lap_8_3']:
            logging('Бой №' + str(self.d_counter8[self.key]['count8'] + 1))
            self.lap_show(table=self.t_8,
                          cell='D',
                          count=self.d_counter8[self.key]['count8'],
                          s_losers=self.d_counter8[self.key]['l_losers_8'],
                          is_draw_by_lot=False,
                          end=members_4_show)
        elif self.d_counter8[self.key]['is_lap_8_4']:
            logging('Бой №' + str(self.d_counter8[self.key]['count8'] + 1))
            self.lap_show(table=self.t_8,
                          cell='J',
                          count=self.d_counter8[self.key]['count8'],
                          s_losers=self.d_counter8[self.key]['l_losers_8'],
                          is_draw_by_lot=False,
                          end=members_4_show)
        elif self.d_counter8[self.key]['is_lap_8_5']:
            logging('Бой №' + str(self.d_counter8[self.key]['count8'] + 1))
            self.lap_show(table=self.t_8,
                          cell='H',
                          count=self.d_counter8[self.key]['count8'],
                          s_losers=self.d_counter8[self.key]['l_losers_8'],
                          is_draw_by_lot=False,
                          end=members_2_show)
        elif self.d_counter8[self.key]['is_lap_8_6']:
            logging('Бой №' + str(self.d_counter8[self.key]['count8'] + 1))
            self.lap_show(table=self.t_8,
                          cell='F',
                          count=self.d_counter8[self.key]['count8'],
                          s_losers=self.d_counter8[self.key]['l_losers_8'],
                          is_draw_by_lot=False,
                          end=members_2_show)

    def spin_manage_8(self):
        if self.key.__contains__(f'{t}8'):
            self.spin_manage(d_counter=self.d_counter8,
                             d_key=self.key,
                             l_isLap=self.l_is_lap_8,
                             num=8)
