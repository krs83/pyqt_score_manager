import openpyxl

from Modules.excel_function import *
from Modules.flags import Flags
from Modules.utilities import *
from UI.counter_screen import Ui_MainWindow


class TableFor5(ExcelFunc):
    def __init__(self):
        super().__init__()
        self.age = sample
        self.btn = None
        self.index_age = 0
        self.ui = Ui_MainWindow()
        self.flags = Flags()

        self.d_counter5 = {}
        self.key = ''

        self.l_is_lap_5 = ['is_lap_5_1', 'is_lap_5_2', 'is_lap_5_3',
                           'is_lap_5_4', 'is_lap_5_5']

        # first sample file init
        self.file_path_5 = f'{file_name}{self.age}'
        self.wb_5 = openpyxl.load_workbook(self.file_path_5)
        self.t_5 = self.wb_5.worksheets[self.index_age]

    def set_table_5(self, age, btn, table, main_key):
        logging(main_key)
        self.new_dict_init(lap=self.l_is_lap_5,
                           d_counter=self.d_counter5,
                           main_key=main_key,
                           max_count=members_6_lap,
                           num=5)

        self.key = main_key
        self.age = age
        self.btn = btn
        self.file_path_5 = f'{file_name}{age}'
        self.wb_5 = openpyxl.load_workbook(self.file_path_5)
        self.t_5 = self.wb_5.worksheets[table]

        self.check_new_counter(d_counter=self.d_counter5,
                               main_key=main_key,
                               table=self.t_5,
                               wb=self.wb_5,
                               file_path=self.file_path_5,
                               member_len=members_6_show,
                               num=5,
                               is_odd=True)

        self.show_on_board_t_5()

    def end_of_lap_5(self, num_lap):
        logging(end_lap)
        if num_lap == 2:
            logging(lap2)
            self.d_counter5[self.key]['is_lap_5_1'] = False
            self.d_counter5[self.key]['is_lap_5_2'] = True
            self.ui.lap1.setChecked(False)
            self.ui.lap2.setChecked(True)
        elif num_lap == 3:
            logging(lap3)
            self.d_counter5[self.key]['is_lap_5_2'] = False
            self.d_counter5[self.key]['is_lap_5_3'] = True
            self.ui.lap2.setChecked(False)
            self.ui.lap3.setChecked(True)
        elif num_lap == 4:
            logging(lap4)
            self.d_counter5[self.key]['is_lap_5_3'] = False
            self.d_counter5[self.key]['is_lap_5_4'] = True
            self.ui.lap3.setChecked(False)
            self.ui.lap4.setChecked(True)
        elif num_lap == 5:
            logging(lap5)
            self.d_counter5[self.key]['is_lap_5_4'] = False
            self.d_counter5[self.key]['is_lap_5_5'] = True
            self.ui.lap4.setChecked(False)
            self.ui.lap5.setChecked(True)
        elif num_lap == last:
            logging(finish)
            self.d_counter5[self.key]['is_lap_5_5'] = False
            self.ui.lap5.setChecked(False)
            self.ui.lap_finish.setChecked(True)
            self.define_places(table=self.t_5, btn=self.btn, num=5)

        counter_reset(counter=self.d_counter5, key=self.key, num=5)

    def incrementation_5(self, end, num_lap, table=None, win_cell=None, score_cell=None,
                         s_losers=None, s_list=None, s_dict=None, as_losers_cell=None,
                         is_last_round=False, end_show_lap=None):

        if not self.equal_scores:
            counter_inc(counter=self.d_counter5, key=self.key, num=5)

        if self.d_counter5[self.key]['count5'] == end - 1:
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
                self.end_of_lap_5(num_lap)
            else:
                self.end_of_lap_5(num_lap)

    def laps_define_t_5(self):
        if self.d_counter5[self.key]['is_lap_5_1']:
            self.lap_with_late_loser_add(table=self.t_5,
                                         win_cell='D',
                                         score_cell='C',
                                         end=members_6_lap,
                                         count=self.d_counter5[self.key]['count5'],
                                         s_list=self.d_counter5[self.key]['l_key_win_lose_5'],
                                         s_dict=self.d_counter5[self.key]['d_win_lose_5'],
                                         s_losers=self.d_counter5[self.key]['l_losers_5'],
                                         inc=self.d_counter5[self.key]['inc_5'],
                                         inc1=self.d_counter5[self.key]['inc1_5'])
            self.incrementation_5(table=self.t_5,
                                  win_cell='D',
                                  score_cell='C',
                                  s_list=self.d_counter5[self.key]['l_key_win_lose_5'],
                                  s_dict=self.d_counter5[self.key]['d_win_lose_5'],
                                  s_losers=self.d_counter5[self.key]['l_losers_5'],
                                  as_losers_cell='J',
                                  num_lap=2,
                                  end=members_6_lap,
                                  is_last_round=True,
                                  end_show_lap=members_6_show)
        elif self.d_counter5[self.key]['is_lap_5_2']:
            self.lap(table=self.t_5,
                     win_cell='H',
                     score_cell='K',
                     end=members_2_lap,
                     count=self.d_counter5[self.key]['count5'],
                     s_list=self.d_counter5[self.key]['l_key_win_lose_5'],
                     s_dict=self.d_counter5[self.key]['d_win_lose_5'],
                     s_losers=self.d_counter5[self.key]['l_losers_5'],
                     inc=self.d_counter5[self.key]['inc_5'],
                     inc1=self.d_counter5[self.key]['inc1_5'])
            self.incrementation_5(end=members_2_lap, num_lap=3)
        elif self.d_counter5[self.key]['is_lap_5_3']:
            self.lap_with_late_loser_add(table=self.t_5,
                                         win_cell='F',
                                         score_cell='E',
                                         end=members_4_lap,
                                         count=self.d_counter5[self.key]['count5'],
                                         s_list=self.d_counter5[self.key]['l_key_win_lose_5'],
                                         s_dict=self.d_counter5[self.key]['d_win_lose_5'],
                                         s_losers=self.d_counter5[self.key]['l_losers_5'],
                                         inc=self.d_counter5[self.key]['inc_5'],
                                         inc1=self.d_counter5[self.key]['inc1_5'])
            self.incrementation_5(table=self.t_5,
                                  win_cell='F',
                                  score_cell='E',
                                  s_list=self.d_counter5[self.key]['l_key_win_lose_5'],
                                  s_dict=self.d_counter5[self.key]['d_win_lose_5'],
                                  s_losers=self.d_counter5[self.key]['l_losers_5'],
                                  as_losers_cell='H',
                                  num_lap=4,
                                  end=members_4_lap,
                                  is_last_round=True,
                                  end_show_lap=members_4_show)
        elif self.d_counter5[self.key]['is_lap_5_4']:
            self.lap_for_finals(table=self.t_5,
                                score_cell='I',
                                s_list=self.d_counter5[self.key]['l_key_win_lose_5'],
                                s_dict=self.d_counter5[self.key]['d_win_lose_5'],
                                s_losers=self.d_counter5[self.key]['l_losers_5'])
            self.end_of_lap_5(num_lap=5)
        elif self.d_counter5[self.key]['is_lap_5_5']:
            self.lap_for_finals(table=self.t_5,
                                lose_cell='F',
                                score_cell='G',
                                is_final=True,
                                s_list=self.d_counter5[self.key]['l_key_win_lose_5'],
                                s_dict=self.d_counter5[self.key]['d_win_lose_5'],
                                s_losers=self.d_counter5[self.key]['l_losers_5'])
            self.end_of_lap_5(num_lap=last)

        if self.equal_scores:
            self.d_counter5[self.key]['count5'] += 0
        else:
            self.d_counter5[self.key]['count5'] += 1

        self.equal_scores = False
        self.flags.is_table[3] = False
        self.set_active_tables(btn=self.btn,
                               sheet=self.wb_5,
                               file=self.file_path_5)
        self.on_off_spin(False)

    def show_on_board_t_5(self):
        self.laps_disable(start=6)
        self.on_off_spin(True)

        self.flags.is_table[3] = True
        self.set_inactive_tables(btn=self.btn)
        self.ui.spinBox.setValue(self.d_counter5[self.key]['count5'] + 1)

        if self.d_counter5[self.key]['is_lap_5_1']:
            logging('Бой №' + str(self.d_counter5[self.key]['count5'] + 1))
            self.lap_show(table=self.t_5,
                          cell='B',
                          count=self.d_counter5[self.key]['count5'],
                          s_losers=self.d_counter5[self.key]['l_losers_5'],
                          lot_cell='B15',
                          end=members_6_show)
        elif self.d_counter5[self.key]['is_lap_5_2']:
            logging('Бой №' + str(self.d_counter5[self.key]['count5'] + 1))
            self.lap_show(table=self.t_5,
                          cell='J',
                          count=self.d_counter5[self.key]['count5'],
                          s_losers=self.d_counter5[self.key]['l_losers_5'],
                          is_draw_by_lot=False,
                          end=members_4_show)
        elif self.d_counter5[self.key]['is_lap_5_3']:
            logging('Бой №' + str(self.d_counter5[self.key]['count5'] + 1))
            self.lap_show(table=self.t_5,
                          cell='D',
                          count=self.d_counter5[self.key]['count5'],
                          s_losers=self.d_counter5[self.key]['l_losers_5'],
                          lot_cell='D12',
                          end=members_4_show)
        elif self.d_counter5[self.key]['is_lap_5_4']:
            logging('Бой №' + str(self.d_counter5[self.key]['count5'] + 1))
            self.lap_show(table=self.t_5,
                          cell='H',
                          count=self.d_counter5[self.key]['count5'],
                          s_losers=self.d_counter5[self.key]['l_losers_5'],
                          is_draw_by_lot=False,
                          end=members_2_show)
        elif self.d_counter5[self.key]['is_lap_5_5']:
            logging('Бой №' + str(self.d_counter5[self.key]['count5'] + 1))
            self.lap_show(table=self.t_5,
                          cell='F',
                          count=self.d_counter5[self.key]['count5'],
                          s_losers=self.d_counter5[self.key]['l_losers_5'],
                          is_draw_by_lot=False,
                          end=members_2_show)

    def spin_manage_5(self):
        if self.key.__contains__(f'{t}5'):
            self.spin_manage(d_counter=self.d_counter5,
                             d_key=self.key,
                             l_isLap=self.l_is_lap_5,
                             num=5)
