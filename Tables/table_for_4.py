import openpyxl

from Modules.excel_function import *
from Modules.flags import Flags
from Modules.utilities import *
from UI.counter_screen import Ui_MainWindow


class TableFor4(ExcelFunc):
    def __init__(self, ):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.age = sample
        self.btn = None
        self.index_age = 0
        self.flags = Flags()

        self.d_counter4 = {}
        self.key = ''

        self.l_is_lap_4 = ['is_lap_4_1', 'is_lap_4_2', 'is_lap_4_3']

        # first sample file init
        self.file_path_4 = f'{file_name}{self.age}'
        self.wb_4 = openpyxl.load_workbook(self.file_path_4)
        self.t_4 = self.wb_4.worksheets[self.index_age]

    def set_table_4(self, age, btn, table, main_key):
        logging(main_key)
        self.new_dict_init(lap=self.l_is_lap_4,
                           d_counter=self.d_counter4,
                           main_key=main_key,
                           max_count=members_4_lap,
                           num=4)

        self.key = main_key
        self.age = age
        self.btn = btn
        self.file_path_4 = f'{file_name}{age}'
        self.wb_4 = openpyxl.load_workbook(self.file_path_4)
        self.t_4 = self.wb_4.worksheets[table]

        self.check_new_counter(d_counter=self.d_counter4,
                               main_key=main_key,
                               table=self.t_4,
                               wb=self.wb_4,
                               file_path=self.file_path_4,
                               member_len=members_4_show,
                               num=4)

        self.show_on_board_t_4()

    def end_of_lap_4(self, num_lap):
        logging(end_lap)
        if num_lap == 2:
            logging(lap2)
            self.d_counter4[self.key]['is_lap_4_1'] = False
            self.d_counter4[self.key]['is_lap_4_2'] = True
            self.ui.lap1.setChecked(False)
            self.ui.lap2.setChecked(True)
        elif num_lap == 3:
            logging(lap3)
            self.d_counter4[self.key]['is_lap_4_2'] = False
            self.d_counter4[self.key]['is_lap_4_3'] = True
            self.ui.lap2.setChecked(False)
            self.ui.lap3.setChecked(True)
        elif num_lap == last:
            logging(finish)
            self.d_counter4[self.key]['is_lap_4_3'] = False
            self.ui.lap3.setChecked(False)
            self.ui.lap_finish.setChecked(True)
            self.define_places(table=self.t_4, btn=self.btn, num=4)

        counter_reset(counter=self.d_counter4, key=self.key, num=4)

    def incrementation_4(self, end, num_lap, table=None, win_cell=None, score_cell=None,
                         s_losers=None, s_list=None, s_dict=None, as_losers_cell=None,
                         is_last_round=False, end_show_lap=None):

        if not self.equal_scores:
            counter_inc(counter=self.d_counter4, key=self.key, num=4)

        if self.d_counter4[self.key]['count4'] == end - 1:
            if is_last_round:
                self.last_round(table=table, win_cell=win_cell,
                                score_cell=score_cell,
                                s_losers=s_losers,
                                s_list=s_list,
                                s_dict=s_dict,
                                as_losers_cell=as_losers_cell,
                                end=end,
                                end_show_lap=end_show_lap)
                self.end_of_lap_4(num_lap)
            else:
                self.end_of_lap_4(num_lap)

    def laps_define_t_4(self):
        if self.d_counter4[self.key]['is_lap_4_1']:
            self.lap(table=self.t_4,
                     win_cell='D',
                     score_cell='C',
                     is_loser=True,
                     lose_cell='F',
                     end=members_4_lap,
                     count=self.d_counter4[self.key]['count4'],
                     s_list=self.d_counter4[self.key]['l_key_win_lose_4'],
                     s_dict=self.d_counter4[self.key]['d_win_lose_4'],
                     s_losers=self.d_counter4[self.key]['l_losers_4'],
                     inc=self.d_counter4[self.key]['inc_4'],
                     inc1=self.d_counter4[self.key]['inc1_4'])
            self.incrementation_4(end=members_4_lap, num_lap=2)
        elif self.d_counter4[self.key]['is_lap_4_2']:
            self.lap_for_finals(table=self.t_4,
                                score_cell='G',
                                s_list=self.d_counter4[self.key]['l_key_win_lose_4'],
                                s_dict=self.d_counter4[self.key]['d_win_lose_4'],
                                s_losers=self.d_counter4[self.key]['l_losers_4'])
            self.end_of_lap_4(num_lap=3)
        elif self.d_counter4[self.key]['is_lap_4_3']:
            self.lap_for_finals(table=self.t_4,
                                lose_cell='F',
                                score_cell='E',
                                is_final=True,
                                s_list=self.d_counter4[self.key]['l_key_win_lose_4'],
                                s_dict=self.d_counter4[self.key]['d_win_lose_4'],
                                s_losers=self.d_counter4[self.key]['l_losers_4'])
            self.end_of_lap_4(num_lap=last)

        if self.equal_scores:
            self.d_counter4[self.key]['count4'] += 0
        else:
            self.d_counter4[self.key]['count4'] += 1

        self.equal_scores = False
        self.flags.is_table[2] = False
        self.set_active_tables(btn=self.btn,
                               sheet=self.wb_4,
                               file=self.file_path_4)
        self.on_off_spin(False)

    def show_on_board_t_4(self):
        self.laps_disable(start=4)
        self.on_off_spin(True)

        self.flags.is_table[2] = True
        self.set_inactive_tables(btn=self.btn)
        self.ui.spinBox.setValue(self.d_counter4[self.key]['count4'] + 1)

        if self.d_counter4[self.key]['is_lap_4_1']:
            logging('Бой №' + str(self.d_counter4[self.key]['count4'] + 1))
            self.lap_show(table=self.t_4,
                          cell='B',
                          count=self.d_counter4[self.key]['count4'],
                          s_losers=self.d_counter4[self.key]['l_losers_4'],
                          is_draw_by_lot=False,
                          end=members_4_show)
        elif self.d_counter4[self.key]['is_lap_4_2']:
            logging('Бой №' + str(self.d_counter4[self.key]['count4'] + 1))
            self.lap_show(table=self.t_4,
                          cell='F',
                          count=self.d_counter4[self.key]['count4'],
                          s_losers=self.d_counter4[self.key]['l_losers_4'],
                          is_draw_by_lot=False,
                          end=members_2_show)
        elif self.d_counter4[self.key]['is_lap_4_3']:
            logging('Бой №' + str(self.d_counter4[self.key]['count4'] + 1))
            self.lap_show(table=self.t_4,
                          cell='D',
                          count=self.d_counter4[self.key]['count4'],
                          s_losers=self.d_counter4[self.key]['l_losers_4'],
                          is_draw_by_lot=False,
                          end=members_2_show)

    def spin_manage_4(self):
        if self.key.__contains__(f'{t}4'):
            self.spin_manage(d_counter=self.d_counter4,
                             d_key=self.key,
                             l_isLap=self.l_is_lap_4,
                             num=4)
