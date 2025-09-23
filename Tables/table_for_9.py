import openpyxl

from Modules.excel_function import *
from Modules.flags import Flags
from Modules.utilities import *
from UI.counter_screen import Ui_MainWindow


class TableFor9(ExcelFunc):
    def __init__(self):
        super().__init__()
        self.age = sample
        self.btn = None
        self.index_age = 0
        self.ui = Ui_MainWindow()
        self.flags = Flags()

        self.d_counter9 = {}
        self.key = ''

        self.l_is_lap_9 = ['is_lap_9_1', 'is_lap_9_2', 'is_lap_9_3', 'is_lap_9_4',
                           'is_lap_9_5', 'is_lap_9_6', 'is_lap_9_7', 'is_lap_9_8']

        # first sample file init
        self.file_path_9 = f'{file_name}{self.age}'
        self.wb_9 = openpyxl.load_workbook(self.file_path_9)
        self.t_9 = self.wb_9.worksheets[self.index_age]

    def set_table_9(self, age, btn, table, main_key):
        logging(main_key)
        self.new_dict_init(lap=self.l_is_lap_9,
                           d_counter=self.d_counter9,
                           main_key=main_key,
                           max_count=members_10_lap,
                           num=9)

        self.key = main_key
        self.age = age
        self.btn = btn
        self.file_path_9 = f'{file_name}{age}'
        self.wb_9 = openpyxl.load_workbook(self.file_path_9)
        self.t_9 = self.wb_9.worksheets[table]

        self.check_new_counter(d_counter=self.d_counter9,
                               main_key=main_key,
                               table=self.t_9,
                               wb=self.wb_9,
                               file_path=self.file_path_9,
                               member_len=members_10_show,
                               num=9,
                               is_odd=True)
        print(main_key)

        self.show_on_board_t_9()

    def end_of_lap_9(self, num_lap):
        logging(end_lap)
        if num_lap == 2:
            logging(lap2)
            self.d_counter9[self.key]['is_lap_9_1'] = False
            self.d_counter9[self.key]['is_lap_9_2'] = True
            self.ui.lap1.setChecked(False)
            self.ui.lap2.setChecked(True)
            self.ui.spinBox.setMaximum(2)
        elif num_lap == 3:
            logging(lap3)
            self.d_counter9[self.key]['is_lap_9_2'] = False
            self.d_counter9[self.key]['is_lap_9_3'] = True
            self.ui.lap2.setChecked(False)
            self.ui.lap3.setChecked(True)
            self.ui.spinBox.setMaximum(3)
        elif num_lap == 4:
            logging(lap4)
            self.d_counter9[self.key]['is_lap_9_3'] = False
            self.d_counter9[self.key]['is_lap_9_4'] = True
            self.ui.lap3.setChecked(False)
            self.ui.lap4.setChecked(True)
            self.ui.spinBox.setMaximum(2)
        elif num_lap == 5:
            logging(lap5)
            self.d_counter9[self.key]['is_lap_9_4'] = False
            self.d_counter9[self.key]['is_lap_9_5'] = True
            self.ui.lap4.setChecked(False)
            self.ui.lap5.setChecked(True)
            self.ui.spinBox.setMaximum(2)
        elif num_lap == 6:
            logging(lap6)
            self.d_counter9[self.key]['is_lap_9_5'] = False
            self.d_counter9[self.key]['is_lap_9_6'] = True
            self.ui.lap5.setChecked(False)
            self.ui.lap6.setChecked(True)
            self.ui.spinBox.setMaximum(2)
        elif num_lap == 7:
            logging(lap7)
            self.d_counter9[self.key]['is_lap_9_6'] = False
            self.d_counter9[self.key]['is_lap_9_7'] = True
            self.ui.lap6.setChecked(False)
            self.ui.lap7.setChecked(True)
            self.ui.spinBox.setMaximum(1)
        elif num_lap == 8:
            logging(lap8)
            self.d_counter9[self.key]['is_lap_9_7'] = False
            self.d_counter9[self.key]['is_lap_9_8'] = True
            self.ui.lap7.setChecked(False)
            self.ui.lap8.setChecked(True)
            self.ui.spinBox.setMaximum(1)
        elif num_lap == last:
            logging(finish)
            self.d_counter9[self.key]['is_lap_9_8'] = False
            self.ui.lap8.setChecked(False)
            self.ui.lap_finish.setChecked(True)
            self.define_places(table=self.t_9, btn=self.btn, num=9)

        counter_reset(counter=self.d_counter9, key=self.key, num=9)

    def incrementation_9(self, end, num_lap, table=None, win_cell=None, score_cell=None,
                         s_losers=None, s_list=None, s_dict=None, as_losers_cell=None,
                         is_last_round=False, end_show_lap=None):

        if not self.equal_scores:
            counter_inc(counter=self.d_counter9, key=self.key, num=9)

        if self.d_counter9[self.key]['count9'] == end - 1:
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
                self.end_of_lap_9(num_lap)
            else:
                self.end_of_lap_9(num_lap)

    def laps_define_t_9(self):
        if self.d_counter9[self.key]['is_lap_9_1']:
            self.lap_with_late_loser_add(table=self.t_9,
                                         count=self.d_counter9[self.key]['count9'],
                                         s_list=self.d_counter9[self.key]['l_key_win_lose_9'],
                                         s_dict=self.d_counter9[self.key]['d_win_lose_9'],
                                         s_losers=self.d_counter9[self.key]['l_losers_9'],
                                         inc=self.d_counter9[self.key]['inc_9'],
                                         inc1=self.d_counter9[self.key]['inc1_9'],
                                         win_cell='D',
                                         score_cell='C',
                                         end=members_10_lap,
                                         )
            self.incrementation_9(table=self.t_9,
                                  win_cell='D',
                                  score_cell='C',
                                  s_list=self.d_counter9[self.key]['l_key_win_lose_9'],
                                  s_dict=self.d_counter9[self.key]['d_win_lose_9'],
                                  s_losers=self.d_counter9[self.key]['l_losers_9'],
                                  as_losers_cell='P',
                                  num_lap=2,
                                  end=members_10_lap,
                                  end_show_lap=members_10_show,
                                  is_last_round=True)
        elif self.d_counter9[self.key]['is_lap_9_2']:
            self.lap(table=self.t_9,
                     win_cell='N',
                     score_cell='Q',
                     count=self.d_counter9[self.key]['count9'],
                     s_list=self.d_counter9[self.key]['l_key_win_lose_9'],
                     s_dict=self.d_counter9[self.key]['d_win_lose_9'],
                     s_losers=self.d_counter9[self.key]['l_losers_9'],
                     inc=self.d_counter9[self.key]['inc_9'],
                     inc1=self.d_counter9[self.key]['inc1_9'],
                     end=members_4_lap, )
            self.incrementation_9(end=members_4_lap, num_lap=3)
        elif self.d_counter9[self.key]['is_lap_9_3']:
            self.lap_with_late_loser_add(table=self.t_9,
                                         win_cell='F',
                                         score_cell='E',
                                         count=self.d_counter9[self.key]['count9'],
                                         s_list=self.d_counter9[self.key]['l_key_win_lose_9'],
                                         s_dict=self.d_counter9[self.key]['d_win_lose_9'],
                                         s_losers=self.d_counter9[self.key]['l_losers_9'],
                                         inc=self.d_counter9[self.key]['inc_9'],
                                         inc1=self.d_counter9[self.key]['inc1_9'],
                                         end=members_6_lap, )
            self.incrementation_9(table=self.t_9,
                                  win_cell='F',
                                  score_cell='E',
                                  s_list=self.d_counter9[self.key]['l_key_win_lose_9'],
                                  s_dict=self.d_counter9[self.key]['d_win_lose_9'],
                                  s_losers=self.d_counter9[self.key]['l_losers_9'],
                                  as_losers_cell='N',
                                  num_lap=4,
                                  end=members_6_lap,
                                  is_last_round=True,
                                  end_show_lap=members_6_show)
        elif self.d_counter9[self.key]['is_lap_9_4']:
            self.lap(table=self.t_9,
                     win_cell='L',
                     score_cell='O',
                     count=self.d_counter9[self.key]['count9'],
                     s_list=self.d_counter9[self.key]['l_key_win_lose_9'],
                     s_dict=self.d_counter9[self.key]['d_win_lose_9'],
                     s_losers=self.d_counter9[self.key]['l_losers_9'],
                     inc=self.d_counter9[self.key]['inc_9'],
                     inc1=self.d_counter9[self.key]['inc1_9'],
                     end=members_4_lap, )
            self.incrementation_9(end=members_4_lap, num_lap=5)
        elif self.d_counter9[self.key]['is_lap_9_5']:
            self.lap_with_late_loser_add(table=self.t_9,
                                         win_cell='H',
                                         score_cell='G',
                                         count=self.d_counter9[self.key]['count9'],
                                         s_list=self.d_counter9[self.key]['l_key_win_lose_9'],
                                         s_dict=self.d_counter9[self.key]['d_win_lose_9'],
                                         s_losers=self.d_counter9[self.key]['l_losers_9'],
                                         inc=self.d_counter9[self.key]['inc_9'],
                                         inc1=self.d_counter9[self.key]['inc1_9'],
                                         end=members_4_lap, )
            self.incrementation_9(table=self.t_9,
                                  win_cell='H',
                                  score_cell='G',
                                  s_list=self.d_counter9[self.key]['l_key_win_lose_9'],
                                  s_dict=self.d_counter9[self.key]['d_win_lose_9'],
                                  s_losers=self.d_counter9[self.key]['l_losers_9'],
                                  as_losers_cell='L',
                                  num_lap=6,
                                  end=members_4_lap,
                                  is_last_round=True,
                                  end_show_lap=members_4_show)
        elif self.d_counter9[self.key]['is_lap_9_6']:
            self.lap(table=self.t_9,
                     win_cell='J',
                     score_cell='M',
                     count=self.d_counter9[self.key]['count9'],
                     s_list=self.d_counter9[self.key]['l_key_win_lose_9'],
                     s_dict=self.d_counter9[self.key]['d_win_lose_9'],
                     s_losers=self.d_counter9[self.key]['l_losers_9'],
                     inc=self.d_counter9[self.key]['inc_9'],
                     inc1=self.d_counter9[self.key]['inc1_9'],
                     end=members_4_lap, )
            self.incrementation_9(end=members_4_lap, num_lap=7)
        elif self.d_counter9[self.key]['is_lap_9_7']:
            self.lap_for_finals(table=self.t_9,
                                score_cell='K',
                                s_list=self.d_counter9[self.key]['l_key_win_lose_9'],
                                s_dict=self.d_counter9[self.key]['d_win_lose_9'],
                                s_losers=self.d_counter9[self.key]['l_losers_9'])
            self.end_of_lap_9(num_lap=8)
        elif self.d_counter9[self.key]['is_lap_9_8']:
            self.lap_for_finals(table=self.t_9,
                                lose_cell='F',
                                score_cell='I',
                                is_final=True,
                                s_list=self.d_counter9[self.key]['l_key_win_lose_9'],
                                s_dict=self.d_counter9[self.key]['d_win_lose_9'],
                                s_losers=self.d_counter9[self.key]['l_losers_9'])
            self.end_of_lap_9(num_lap=last)

        if self.equal_scores:
            self.d_counter9[self.key]['count9'] += 0
        else:
            self.d_counter9[self.key]['count9'] += 1

        self.equal_scores = False
        self.flags.is_table[7] = False
        self.set_active_tables(btn=self.btn,
                               sheet=self.wb_9,
                               file=self.file_path_9)
        self.on_off_spin(False)

    def show_on_board_t_9(self):
        self.laps_disable(is_disabled=False)
        self.on_off_spin(True)

        self.flags.is_table[7] = True
        self.set_inactive_tables(btn=self.btn)
        self.ui.spinBox.setValue(self.d_counter9[self.key]['count9'] + 1)

        if self.d_counter9[self.key]['is_lap_9_1']:
            logging('Бой №' + str(self.d_counter9[self.key]['count9'] + 1))
            self.lap_show(table=self.t_9,
                          cell='B',
                          count=self.d_counter9[self.key]['count9'],
                          s_losers=self.d_counter9[self.key]['l_losers_9'],
                          lot_cell='B21',
                          end=members_10_show,
                          rand_num=3)
        elif self.d_counter9[self.key]['is_lap_9_2']:
            logging('Бой №' + str(self.d_counter9[self.key]['count9'] + 1))
            self.lap_show(table=self.t_9,
                          cell='P',
                          count=self.d_counter9[self.key]['count9'],
                          s_losers=self.d_counter9[self.key]['l_losers_9'],
                          is_draw_by_lot=False,
                          end=members_4_show)
        elif self.d_counter9[self.key]['is_lap_9_3']:
            logging('Бой №' + str(self.d_counter9[self.key]['count9'] + 1))
            self.lap_show(table=self.t_9,
                          cell='D',
                          count=self.d_counter9[self.key]['count9'],
                          s_losers=self.d_counter9[self.key]['l_losers_9'],
                          lot_cell='D15',
                          rand_num=1,
                          end=members_6_show)
        elif self.d_counter9[self.key]['is_lap_9_4']:
            logging('Бой №' + str(self.d_counter9[self.key]['count9'] + 1))
            self.lap_show(table=self.t_9,
                          cell='N',
                          count=self.d_counter9[self.key]['count9'],
                          s_losers=self.d_counter9[self.key]['l_losers_9'],
                          is_draw_by_lot=False,
                          end=members_4_show)
        elif self.d_counter9[self.key]['is_lap_9_5']:
            logging('Бой №' + str(self.d_counter9[self.key]['count9'] + 1))
            self.lap_show(table=self.t_9,
                          cell='F',
                          count=self.d_counter9[self.key]['count9'],
                          s_losers=self.d_counter9[self.key]['l_losers_9'],
                          lot_cell='F12',
                          end=members_4_show)
        elif self.d_counter9[self.key]['is_lap_9_6']:
            logging('Бой №' + str(self.d_counter9[self.key]['count9'] + 1))
            self.lap_show(table=self.t_9,
                          cell='L',
                          count=self.d_counter9[self.key]['count9'],
                          s_losers=self.d_counter9[self.key]['l_losers_9'],
                          lot_cell='L12',
                          end=members_4_show)
        elif self.d_counter9[self.key]['is_lap_9_7']:
            logging('Бой №' + str(self.d_counter9[self.key]['count9'] + 1))
            self.lap_show(table=self.t_9,
                          cell='J',
                          count=self.d_counter9[self.key]['count9'],
                          s_losers=self.d_counter9[self.key]['l_losers_9'],
                          is_draw_by_lot=False,
                          end=members_2_show)
        elif self.d_counter9[self.key]['is_lap_9_8']:
            logging('Бой №' + str(self.d_counter9[self.key]['count9'] + 1))
            self.lap_show(table=self.t_9,
                          cell='H',
                          count=self.d_counter9[self.key]['count9'],
                          s_losers=self.d_counter9[self.key]['l_losers_9'],
                          is_draw_by_lot=False,
                          end=members_2_show)

    def spin_manage_9(self):
        if self.key.__contains__(f'{t}9'):
            self.spin_manage(d_counter=self.d_counter9,
                             d_key=self.key,
                             l_isLap=self.l_is_lap_9,
                             num=9)
