import openpyxl

from Modules.excel_function import *
from Modules.flags import Flags
from Modules.utilities import *
from UI.counter_screen import Ui_MainWindow


class TableFor7(ExcelFunc):
    def __init__(self):
        super().__init__()
        self.age = sample
        self.btn = None
        self.index_age = 0
        self.ui = Ui_MainWindow()
        self.flags = Flags()

        self.d_counter7 = {}
        self.key = ''

        self.l_is_lap_7 = ['is_lap_7_1', 'is_lap_7_2', 'is_lap_7_3',
                           'is_lap_7_4', 'is_lap_7_5', 'is_lap_7_6']

        # first sample file init
        self.file_path_7 = f'{file_name}{self.age}'
        self.wb_7 = openpyxl.load_workbook(self.file_path_7)
        self.t_7 = self.wb_7.worksheets[self.index_age]

    def set_table_7(self, age, btn, table, main_key):
        logging(main_key)
        self.new_dict_init(lap=self.l_is_lap_7,
                           d_counter=self.d_counter7,
                           main_key=main_key,
                           max_count=members_8_lap,
                           num=7)

        self.key = main_key
        self.age = age
        self.btn = btn
        self.file_path_7 = f'{file_name}{age}'
        self.wb_7 = openpyxl.load_workbook(self.file_path_7)
        self.t_7 = self.wb_7.worksheets[table]

        self.check_new_counter(d_counter=self.d_counter7,
                               main_key=main_key,
                               table=self.t_7,
                               wb=self.wb_7,
                               file_path=self.file_path_7,
                               member_len=members_8_show,
                               num=7,
                               is_odd=True)

        self.show_on_board_t_7()

    def end_of_lap_7(self, num_lap):
        logging(end_lap)
        if num_lap == 2:
            logging(lap2)
            self.d_counter7[self.key]['is_lap_7_1'] = False
            self.d_counter7[self.key]['is_lap_7_2'] = True
            self.ui.lap1.setChecked(False)
            self.ui.lap2.setChecked(True)
        elif num_lap == 3:
            logging(lap3)
            self.d_counter7[self.key]['is_lap_7_2'] = False
            self.d_counter7[self.key]['is_lap_7_3'] = True
            self.ui.lap2.setChecked(False)
            self.ui.lap3.setChecked(True)
        elif num_lap == 4:
            logging(lap4)
            self.d_counter7[self.key]['is_lap_7_3'] = False
            self.d_counter7[self.key]['is_lap_7_4'] = True
            self.ui.lap3.setChecked(False)
            self.ui.lap4.setChecked(True)
        elif num_lap == 5:
            logging(lap5)
            self.d_counter7[self.key]['is_lap_7_4'] = False
            self.d_counter7[self.key]['is_lap_7_5'] = True
            self.ui.lap4.setChecked(False)
            self.ui.lap5.setChecked(True)
        elif num_lap == 6:
            logging(lap6)
            self.d_counter7[self.key]['is_lap_7_5'] = False
            self.d_counter7[self.key]['is_lap_7_6'] = True
            self.ui.lap5.setChecked(False)
            self.ui.lap6.setChecked(True)
        elif num_lap == last:
            logging(finish)
            self.d_counter7[self.key]['is_lap_7_6'] = False
            self.ui.lap6.setChecked(False)
            self.ui.lap_finish.setChecked(True)
            self.define_places(table=self.t_7, btn=self.btn, num=7)

        counter_reset(counter=self.d_counter7, key=self.key, num=7)

    def incrementation_7(self, end, num_lap, table=None, win_cell=None, score_cell=None,
                         s_losers=None, s_list=None, s_dict=None, as_losers_cell=None,
                         is_last_round=False, end_show_lap=None):

        if not self.equal_scores:
            counter_inc(counter=self.d_counter7, key=self.key, num=7)

        if self.d_counter7[self.key]['count7'] == end - 1:
            if is_last_round:
                self.last_round(table=table, win_cell=win_cell,
                                score_cell=score_cell,
                                s_losers=s_losers,
                                s_list=s_list,
                                s_dict=s_dict,
                                as_losers_cell=as_losers_cell,
                                end=end,
                                end_show_lap=end_show_lap)
                self.end_of_lap_7(num_lap)
            else:
                self.end_of_lap_7(num_lap)

    def laps_define_t_7(self):
        if self.d_counter7[self.key]['is_lap_7_1']:
            self.lap_with_late_loser_add(table=self.t_7,
                                         win_cell='D',
                                         score_cell='C',
                                         end=members_8_lap,
                                         count=self.d_counter7[self.key]['count7'],
                                         s_list=self.d_counter7[self.key]['l_key_win_lose_7'],
                                         s_dict=self.d_counter7[self.key]['d_win_lose_7'],
                                         s_losers=self.d_counter7[self.key]['l_losers_7'],
                                         inc=self.d_counter7[self.key]['inc_7'],
                                         inc1=self.d_counter7[self.key]['inc1_7'])
            self.incrementation_7(table=self.t_7,
                                  win_cell='D',
                                  score_cell='C',
                                  s_list=self.d_counter7[self.key]['l_key_win_lose_7'],
                                  s_dict=self.d_counter7[self.key]['d_win_lose_7'],
                                  s_losers=self.d_counter7[self.key]['l_losers_7'],
                                  as_losers_cell='L',
                                  num_lap=2,
                                  end=members_8_lap,
                                  is_last_round=True,
                                  end_show_lap=members_8_show)
        elif self.d_counter7[self.key]['is_lap_7_2']:
            self.lap(table=self.t_7,
                     win_cell='J',
                     score_cell='M',
                     count=self.d_counter7[self.key]['count7'],
                     s_list=self.d_counter7[self.key]['l_key_win_lose_7'],
                     s_dict=self.d_counter7[self.key]['d_win_lose_7'],
                     s_losers=self.d_counter7[self.key]['l_losers_7'],
                     inc=self.d_counter7[self.key]['inc_7'],
                     inc1=self.d_counter7[self.key]['inc1_7'],
                     end=members_4_lap, )
            self.incrementation_7(end=members_4_lap, num_lap=3)
        elif self.d_counter7[self.key]['is_lap_7_3']:
            self.lap(table=self.t_7,
                     win_cell='F',
                     lose_cell='J',
                     score_cell='E',
                     end=members_4_lap,
                     is_loser=True,
                     start_lose_cell=11,
                     count=self.d_counter7[self.key]['count7'],
                     s_list=self.d_counter7[self.key]['l_key_win_lose_7'],
                     s_dict=self.d_counter7[self.key]['d_win_lose_7'],
                     s_losers=self.d_counter7[self.key]['l_losers_7'],
                     inc=self.d_counter7[self.key]['inc_7'],
                     inc1=self.d_counter7[self.key]['inc1_7'])
            self.incrementation_7(end=members_4_lap, num_lap=4)
        elif self.d_counter7[self.key]['is_lap_7_4']:
            self.lap(table=self.t_7,
                     win_cell='H',
                     score_cell='K',
                     end=members_4_lap,
                     count=self.d_counter7[self.key]['count7'],
                     s_list=self.d_counter7[self.key]['l_key_win_lose_7'],
                     s_dict=self.d_counter7[self.key]['d_win_lose_7'],
                     s_losers=self.d_counter7[self.key]['l_losers_7'],
                     inc=self.d_counter7[self.key]['inc_7'],
                     inc1=self.d_counter7[self.key]['inc1_7'])
            self.incrementation_7(end=members_4_lap, num_lap=5)
        elif self.d_counter7[self.key]['is_lap_7_5']:
            self.lap_for_finals(table=self.t_7,
                                score_cell='I',
                                s_list=self.d_counter7[self.key]['l_key_win_lose_7'],
                                s_dict=self.d_counter7[self.key]['d_win_lose_7'],
                                s_losers=self.d_counter7[self.key]['l_losers_7'])
            self.end_of_lap_7(num_lap=6)
        elif self.d_counter7[self.key]['is_lap_7_6']:
            self.lap_for_finals(table=self.t_7,
                                lose_cell='F',
                                score_cell='G',
                                is_final=True,
                                s_list=self.d_counter7[self.key]['l_key_win_lose_7'],
                                s_dict=self.d_counter7[self.key]['d_win_lose_7'],
                                s_losers=self.d_counter7[self.key]['l_losers_7'])
            self.end_of_lap_7(num_lap=last)

        if self.equal_scores:
            self.d_counter7[self.key]['count7'] += 0
        else:
            self.d_counter7[self.key]['count7'] += 1

        self.equal_scores = False
        self.flags.is_table[5] = False
        self.set_active_tables(btn=self.btn,
                               sheet=self.wb_7,
                               file=self.file_path_7)
        self.on_off_spin(False)

    def show_on_board_t_7(self):
        self.laps_disable(start=7)
        self.on_off_spin(True)

        self.flags.is_table[5] = True
        self.set_inactive_tables(btn=self.btn)
        self.ui.spinBox.setValue(self.d_counter7[self.key]['count7'] + 1)

        if self.d_counter7[self.key]['is_lap_7_1']:
            logging('Бой №' + str(self.d_counter7[self.key]['count7'] + 1))
            self.lap_show(table=self.t_7,
                          cell='B',
                          count=self.d_counter7[self.key]['count7'],
                          s_losers=self.d_counter7[self.key]['l_losers_7'],
                          lot_cell='B18',
                          end=members_8_show)
        elif self.d_counter7[self.key]['is_lap_7_2']:
            logging('Бой №' + str(self.d_counter7[self.key]['count7'] + 1))
            self.lap_show(table=self.t_7,
                          cell='L',
                          count=self.d_counter7[self.key]['count7'],
                          s_losers=self.d_counter7[self.key]['l_losers_7'],
                          lot_cell='L12',
                          end=members_4_show)
        elif self.d_counter7[self.key]['is_lap_7_3']:
            logging('Бой №' + str(self.d_counter7[self.key]['count7'] + 1))
            self.lap_show(table=self.t_7,
                          cell='D',
                          count=self.d_counter7[self.key]['count7'],
                          s_losers=self.d_counter7[self.key]['l_losers_7'],
                          is_draw_by_lot=False,
                          end=members_4_show)
        elif self.d_counter7[self.key]['is_lap_7_4']:
            logging('Бой №' + str(self.d_counter7[self.key]['count7'] + 1))
            self.lap_show(table=self.t_7,
                          cell='J',
                          count=self.d_counter7[self.key]['count7'],
                          s_losers=self.d_counter7[self.key]['l_losers_7'],
                          is_draw_by_lot=False,
                          end=members_4_show)
        elif self.d_counter7[self.key]['is_lap_7_5']:
            logging('Бой №' + str(self.d_counter7[self.key]['count7'] + 1))
            self.lap_show(table=self.t_7,
                          cell='H',
                          count=self.d_counter7[self.key]['count7'],
                          s_losers=self.d_counter7[self.key]['l_losers_7'],
                          is_draw_by_lot=False,
                          end=members_2_show)
        elif self.d_counter7[self.key]['is_lap_7_6']:
            logging('Бой №' + str(self.d_counter7[self.key]['count7'] + 1))
            self.lap_show(table=self.t_7,
                          cell='F',
                          count=self.d_counter7[self.key]['count7'],
                          s_losers=self.d_counter7[self.key]['l_losers_7'],
                          is_draw_by_lot=False,
                          end=members_2_show)

    def spin_manage_7(self):
        if self.key.__contains__(f'{t}7'):
            self.spin_manage(d_counter=self.d_counter7,
                             d_key=self.key,
                             l_isLap=self.l_is_lap_7,
                             num=7)
