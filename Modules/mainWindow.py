# TODO: V3 полностью перестроить все файлы чтобы исключить циклического импорта и по правилам архитектуры питона

from PyQt5 import QtWidgets

from Modules.buttons import *
from Modules.flags import Flags
from Modules.scores import Scores
from Modules.timer import ScoreTimer
from Modules.messages import *
from Tables.table_for_10 import TableFor10
from Tables.table_for_2 import TableFor2
from Tables.table_for_3 import TableFor3
from Tables.table_for_4 import TableFor4
from Tables.table_for_5 import TableFor5
from Tables.table_for_6 import TableFor6
from Tables.table_for_7 import TableFor7
from Tables.table_for_8 import TableFor8
from Tables.table_for_9 import TableFor9
from UI.counter_screen import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow, ScoreTimer, Scores, TabButtons,
                 TableFor2, TableFor3,
                 TableFor4, TableFor5,
                 TableFor6, TableFor7,
                 TableFor8, TableFor9,
                 TableFor10):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()

        self.flags = Flags()
        self.button = TabButtons()
        self.isTools = True

        self.ui.setupUi(self)

        self.ui.btn_send_results.setDisabled(True)
        self.ui.b_fin_cancel.setDisabled(True)
        self.ui.r_fin_cancel.setDisabled(True)

        self.ui.b_btn_scores_add.clicked.connect(self.blue_scores_add)
        self.ui.b_btn_scores_sub.clicked.connect(self.blue_scores_sub)
        self.ui.b_btn_adv_add.clicked.connect(self.blue_adv_add)
        self.ui.b_btn_adv_sub.clicked.connect(self.blue_adv_sub)
        self.ui.b_btn_pen_add.clicked.connect(self.blue_pen_add)
        self.ui.b_btn_pen_sub.clicked.connect(self.blue_pen_sub)
        self.ui.r_btn_scores_add.clicked.connect(self.red_scores_add)
        self.ui.r_btn_scores_sub.clicked.connect(self.red_scores_sub)
        self.ui.r_btn_adv_add.clicked.connect(self.red_adv_add)
        self.ui.r_btn_adv_sub.clicked.connect(self.red_adv_sub)
        self.ui.r_btn_pen_add.clicked.connect(self.red_pen_add)
        self.ui.r_btn_pen_sub.clicked.connect(self.red_pen_sub)

        # Timer block
        self.ui.lcd_timer.display('03:00')
        self.ui.btn_timer_start.clicked.connect(self.start_timer)
        self.ui.btn_timer_reset.clicked.connect(self.stop_timer)
        self.ui.btn_min2.clicked.connect(self.set_2min)
        self.ui.btn_min3.clicked.connect(self.set_3min)
        self.ui.btn_min4.clicked.connect(self.set_4min)
        self.ui.btn_min5.clicked.connect(self.set_5min)

        # switch off extra tabs in tabWidget
        self.tabs_manager()

        # set usable buttons and hide extra ones
        self.set_tab_buttons(age_file=ages_file[0], age_btn_num=4,
                             l_btns=self.button.btns_age4, l_index=self.button.index_age4)
        self.set_tab_buttons(age_file=ages_file[1], age_btn_num=6,
                             l_btns=self.button.btns_age6, l_index=self.button.index_age6)
        self.set_tab_buttons(age_file=ages_file[2], age_btn_num=7,
                             l_btns=self.button.btns_age7, l_index=self.button.index_age7)
        self.set_tab_buttons(age_file=ages_file[3], age_btn_num=8,
                             l_btns=self.button.btns_age8, l_index=self.button.index_age8)
        self.set_tab_buttons(age_file=ages_file[4], age_btn_num=9,
                             l_btns=self.button.btns_age9, l_index=self.button.index_age9)
        self.set_tab_buttons(age_file=ages_file[5], age_btn_num=10, l_btns=self.button.btns_age10,
                             l_index=self.button.index_age10)
        self.set_tab_buttons(age_file=ages_file[6], age_btn_num=12, l_btns=self.button.btns_age12,
                             l_index=self.button.index_age12)
        self.set_tab_buttons(age_file=ages_file[7], age_btn_num=14, l_btns=self.button.btns_age14,
                             l_index=self.button.index_age14)
        self.set_tab_buttons(age_file=ages_file[8], age_btn_num=16, l_btns=self.button.btns_age16,
                             l_index=self.button.index_age16)
        self.set_tab_buttons(age_file=ages_file[9], age_btn_num=18, l_btns=self.button.btns_age18,
                             l_index=self.button.index_age18)
        self.set_tab_buttons(age_file=ages_file[10], age_btn_num=24, l_btns=self.button.btns_age24,
                             l_index=self.button.index_age24)

        # buttons' handlers
        self.handler_btns(age=ages_file[0], l_btns=self.button.btns_age4, l_index=self.button.index_age4)
        self.handler_btns(age=ages_file[1], l_btns=self.button.btns_age6, l_index=self.button.index_age6)
        self.handler_btns(age=ages_file[2], l_btns=self.button.btns_age7, l_index=self.button.index_age7)
        self.handler_btns(age=ages_file[3], l_btns=self.button.btns_age8, l_index=self.button.index_age8)
        self.handler_btns(age=ages_file[4], l_btns=self.button.btns_age9, l_index=self.button.index_age9)
        self.handler_btns(age=ages_file[5], l_btns=self.button.btns_age10, l_index=self.button.index_age10)
        self.handler_btns(age=ages_file[6], l_btns=self.button.btns_age12, l_index=self.button.index_age12)
        self.handler_btns(age=ages_file[7], l_btns=self.button.btns_age14, l_index=self.button.index_age14)
        self.handler_btns(age=ages_file[8], l_btns=self.button.btns_age16, l_index=self.button.index_age16)
        self.handler_btns(age=ages_file[9], l_btns=self.button.btns_age18, l_index=self.button.index_age18)
        self.handler_btns(age=ages_file[10], l_btns=self.button.btns_age24, l_index=self.button.index_age24)

        # table buttons switcher
        self.ui.btn_send_results.clicked.connect(self.switcher)
        # cancel fight and move backward
        self.ui.btn_backward.clicked.connect(self.backward)
        # reset the scores
        self.ui.r_btn_reset.clicked.connect(self.reset)
        self.ui.b_btn_reset.clicked.connect(self.reset)
        # finalization handlers +100 scores and win
        self.ui.r_fin.clicked.connect(self.r_finalization)
        self.ui.b_fin.clicked.connect(self.b_finalization)
        # finalization cancel buttons
        self.ui.b_fin_cancel.clicked.connect(lambda state: self.b_finalization_cancel(scores=self.b_old_scores))
        self.ui.r_fin_cancel.clicked.connect(lambda state: self.r_finalization_cancel(scores=self.r_old_scores))

        # spin button manage
        self.spin_handlers()

        # hiden block of tools to change fight num
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_laps)
        self.ui.btn_tool.clicked.connect(self.tools)

    # switch from laps view to choose fight view
    def tools(self):
        if self.isTools:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_fight_num)
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_laps)
        self.isTools = not self.isTools

    def switcher(self):
        if self.flags.is_table[8]:
            self.laps_define_t_10()
        elif self.flags.is_table[7]:
            self.laps_define_t_9()
        elif self.flags.is_table[6]:
            self.laps_define_t_8()
        elif self.flags.is_table[5]:
            self.laps_define_t_7()
        elif self.flags.is_table[4]:
            self.laps_define_t_6()
        elif self.flags.is_table[3]:
            self.laps_define_t_5()
        elif self.flags.is_table[2]:
            self.laps_define_t_4()
        elif self.flags.is_table[1]:
            self.laps_define_t_3()
        elif self.flags.is_table[0]:
            self.laps_define_t_2()

    def tabs_manager(self):
        tab_index_search()
        # delete unusable tabs
        for i in range(len(age_list_unuse) - 1, -1, -1):  # loop works in backward order otherwise order mixing
            self.ui.tabWidget.removeTab(age_list_unuse[i])
