import openpyxl

from Modules.excel_function import *
from Modules.flags import Flags
from Modules.utilities import *
from UI.counter_screen import Ui_MainWindow


class TableFor6(ExcelFunc):
    def __init__(self):
        super().__init__()
        self.age = sample
        self.btn = None
        self.index_age = 0
        self.ui = Ui_MainWindow()
        self.flags = Flags()

        self.d_counter6 = {}
        self.key = ''

        self.l_is_lap_6 = ['is_lap_6_1', 'is_lap_6_2', 'is_lap_6_3',
                           'is_lap_6_4', 'is_lap_6_5', 'is_lap_6_6']

        # first sample file init
        self.file_path_6 = f'{file_name}{self.age}'
        self.wb_6 = openpyxl.load_workbook(self.file_path_6)
        self.t_6 = self.wb_6.worksheets[self.index_age]

    def set_table_6(self, age, btn, table, main_key):
        logging(main_key)
        self.new_dict_init(lap=self.l_is_lap_6,
                           d_counter=self.d_counter6,
                           main_key=main_key,
                           max_count=members_6_lap,
                           num=6)

        self.key = main_key
        self.age = age
        self.btn = btn
        self.file_path_6 = f'{file_name}{age}'
        self.wb_6 = openpyxl.load_workbook(self.file_path_6)
        self.t_6 = self.wb_6.worksheets[table]

        self.check_new_counter(d_counter=self.d_counter6,
                               main_key=main_key,
                               table=self.t_6,
                               wb=self.wb_6,
                               file_path=self.file_path_6,
                               member_len=members_6_show,
                               num=6)

        self.show_on_board_t_6()

    def end_of_lap_6(self, num_lap):
        logging(end_lap)
        if num_lap == 2:
            logging(lap2)
            self.d_counter6[self.key]['is_lap_6_1'] = False
            self.d_counter6[self.key]['is_lap_6_2'] = True
            self.ui.lap1.setChecked(False)
            self.ui.lap2.setChecked(True)
        elif num_lap == 3:
            logging(lap3)
            self.d_counter6[self.key]['is_lap_6_2'] = False
            self.d_counter6[self.key]['is_lap_6_3'] = True
            self.ui.lap2.setChecked(False)
            self.ui.lap3.setChecked(True)
        elif num_lap == 4:
            logging(lap4)
            self.d_counter6[self.key]['is_lap_6_3'] = False
            self.d_counter6[self.key]['is_lap_6_4'] = True
            self.ui.lap3.setChecked(False)
            self.ui.lap4.setChecked(True)
        elif num_lap == 5:
            logging(lap5)
            self.d_counter6[self.key]['is_lap_6_4'] = False
            self.d_counter6[self.key]['is_lap_6_5'] = True
            self.ui.lap4.setChecked(False)
            self.ui.lap5.setChecked(True)
        elif num_lap == 6:
            logging(lap6)
            self.d_counter6[self.key]['is_lap_6_5'] = False
            self.d_counter6[self.key]['is_lap_6_6'] = True
            self.ui.lap5.setChecked(False)
            self.ui.lap6.setChecked(True)
        elif num_lap == last:
            logging(finish)
            self.d_counter6[self.key]['is_lap_6_6'] = False
            self.ui.lap6.setChecked(False)
            self.ui.lap_finish.setChecked(True)
            self.define_places(table=self.t_6, btn=self.btn, num=6)

        counter_reset(counter=self.d_counter6, key=self.key, num=6)

    def incrementation_6(self, end, num_lap, table=None, win_cell=None, score_cell=None,
                         s_losers=None, s_list=None, s_dict=None, as_losers_cell=None,
                         is_last_round=False, end_show_lap=None):

        if not self.equal_scores:
            counter_inc(counter=self.d_counter6, key=self.key, num=6)

        if self.d_counter6[self.key]['count6'] == end - 1:
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
                self.end_of_lap_6(num_lap)
            else:
                self.end_of_lap_6(num_lap)

    def laps_define_t_6(self):
        if self.d_counter6[self.key]['is_lap_6_1']:
            self.lap(table=self.t_6,
                     win_cell='D',
                     lose_cell='L',
                     score_cell='C',
                     end=members_8_lap,
                     is_loser=True,
                     count=self.d_counter6[self.key]['count6'],
                     s_list=self.d_counter6[self.key]['l_key_win_lose_6'],
                     s_dict=self.d_counter6[self.key]['d_win_lose_6'],
                     s_losers=self.d_counter6[self.key]['l_losers_6'],
                     inc=self.d_counter6[self.key]['inc_6'],
                     inc1=self.d_counter6[self.key]['inc1_6'])
            self.incrementation_6(end=members_6_lap, num_lap=2)
        elif self.d_counter6[self.key]['is_lap_6_2']:
            self.lap(table=self.t_6,
                     win_cell='J',
                     score_cell='M',
                     end=members_4_lap,
                     count=self.d_counter6[self.key]['count6'],
                     s_list=self.d_counter6[self.key]['l_key_win_lose_6'],
                     s_dict=self.d_counter6[self.key]['d_win_lose_6'],
                     s_losers=self.d_counter6[self.key]['l_losers_6'],
                     inc=self.d_counter6[self.key]['inc_6'],
                     inc1=self.d_counter6[self.key]['inc1_6'])
            self.incrementation_6(end=members_4_lap, num_lap=3)
        elif self.d_counter6[self.key]['is_lap_6_3']:
            self.lap_with_late_loser_add(table=self.t_6,
                                         win_cell='F',
                                         score_cell='E',
                                         end=members_4_lap,
                                         count=self.d_counter6[self.key]['count6'],
                                         s_list=self.d_counter6[self.key]['l_key_win_lose_6'],
                                         s_dict=self.d_counter6[self.key]['d_win_lose_6'],
                                         s_losers=self.d_counter6[self.key]['l_losers_6'],
                                         inc=self.d_counter6[self.key]['inc_6'],
                                         inc1=self.d_counter6[self.key]['inc1_6'])
            self.incrementation_6(table=self.t_6,
                                  win_cell='F',
                                  score_cell='E',
                                  s_list=self.d_counter6[self.key]['l_key_win_lose_6'],
                                  s_dict=self.d_counter6[self.key]['d_win_lose_6'],
                                  s_losers=self.d_counter6[self.key]['l_losers_6'],
                                  as_losers_cell='J',
                                  num_lap=4,
                                  end=members_4_lap,
                                  is_last_round=True,
                                  end_show_lap=members_4_show)
        elif self.d_counter6[self.key]['is_lap_6_4']:
            self.lap(table=self.t_6,
                     win_cell='H',
                     score_cell='K',
                     end=members_4_lap,
                     count=self.d_counter6[self.key]['count6'],
                     s_list=self.d_counter6[self.key]['l_key_win_lose_6'],
                     s_dict=self.d_counter6[self.key]['d_win_lose_6'],
                     s_losers=self.d_counter6[self.key]['l_losers_6'],
                     inc=self.d_counter6[self.key]['inc_6'],
                     inc1=self.d_counter6[self.key]['inc1_6'])
            self.incrementation_6(end=members_4_lap, num_lap=5)
        elif self.d_counter6[self.key]['is_lap_6_5']:
            self.lap_for_finals(table=self.t_6,
                                score_cell='I',
                                s_list=self.d_counter6[self.key]['l_key_win_lose_6'],
                                s_dict=self.d_counter6[self.key]['d_win_lose_6'],
                                s_losers=self.d_counter6[self.key]['l_losers_6'])
            self.end_of_lap_6(num_lap=6)
        elif self.d_counter6[self.key]['is_lap_6_6']:
            self.lap_for_finals(table=self.t_6,
                                lose_cell='F',
                                score_cell='G',
                                is_final=True,
                                s_list=self.d_counter6[self.key]['l_key_win_lose_6'],
                                s_dict=self.d_counter6[self.key]['d_win_lose_6'],
                                s_losers=self.d_counter6[self.key]['l_losers_6'])
            self.end_of_lap_6(num_lap=last)

        self.set_active_tables(btn=self.btn,
                               sheet=self.wb_6,
                               file=self.file_path_6)

        if self.equal_scores:
            self.d_counter6[self.key]['count6'] += 0
        else:
            self.d_counter6[self.key]['count6'] += 1

        self.equal_scores = False
        self.flags.is_table[4] = False

        self.on_off_spin(False)

    def show_on_board_t_6(self):
        self.laps_disable(start=7)
        self.on_off_spin(True)

        self.flags.is_table[4] = True
        self.set_inactive_tables(btn=self.btn)
        self.ui.spinBox.setValue(self.d_counter6[self.key]['count6'] + 1)
        print('count is', self.d_counter6[self.key]['count6'])

        if self.d_counter6[self.key]['is_lap_6_1']:
            logging('Бой №' + str(self.d_counter6[self.key]['count6'] + 1))
            self.lap_show(table=self.t_6,
                          cell='B',
                          count=self.d_counter6[self.key]['count6'],
                          s_losers=self.d_counter6[self.key]['l_losers_6'],
                          is_draw_by_lot=False,
                          end=members_6_show)
        elif self.d_counter6[self.key]['is_lap_6_2']:
            logging('Бой №' + str(self.d_counter6[self.key]['count6'] + 1))
            self.lap_show(table=self.t_6,
                          cell='L',
                          count=self.d_counter6[self.key]['count6'],
                          s_losers=self.d_counter6[self.key]['l_losers_6'],
                          lot_cell='L12',
                          end=members_4_show)
        elif self.d_counter6[self.key]['is_lap_6_3']:
            logging('Бой №' + str(self.d_counter6[self.key]['count6'] + 1))
            self.lap_show(table=self.t_6,
                          cell='D',
                          count=self.d_counter6[self.key]['count6'],
                          s_losers=self.d_counter6[self.key]['l_losers_6'],
                          lot_cell='D12',
                          end=members_4_show)
        elif self.d_counter6[self.key]['is_lap_6_4']:
            logging('Бой №' + str(self.d_counter6[self.key]['count6'] + 1))
            self.lap_show(table=self.t_6,
                          cell='J',
                          count=self.d_counter6[self.key]['count6'],
                          s_losers=self.d_counter6[self.key]['l_losers_6'],
                          lot_cell='J12',
                          end=members_4_show)
        elif self.d_counter6[self.key]['is_lap_6_5']:
            logging('Бой №' + str(self.d_counter6[self.key]['count6'] + 1))
            self.lap_show(table=self.t_6,
                          cell='H',
                          count=self.d_counter6[self.key]['count6'],
                          s_losers=self.d_counter6[self.key]['l_losers_6'],
                          is_draw_by_lot=False,
                          end=members_2_show)
        elif self.d_counter6[self.key]['is_lap_6_6']:
            logging('Бой №' + str(self.d_counter6[self.key]['count6'] + 1))
            self.lap_show(table=self.t_6,
                          cell='F',
                          count=self.d_counter6[self.key]['count6'],
                          s_losers=self.d_counter6[self.key]['l_losers_6'],
                          is_draw_by_lot=False,
                          end=members_2_show)

    def spin_manage_6(self):
        if self.key.__contains__(f'{t}6'):
            self.spin_manage(d_counter=self.d_counter6,
                             d_key=self.key,
                             l_isLap=self.l_is_lap_6,
                             num=6)
