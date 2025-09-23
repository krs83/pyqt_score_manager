
default_cell = 'B22'

buttons4 = [f'self.ui.btn_4_{i}' for i in range(1, 10)]
buttons6 = [f'self.ui.btn_6_{i}' for i in range(1, 10)]
buttons7 = [f'self.ui.btn_7_{i}' for i in range(1, 10)]
buttons8 = [f'self.ui.btn_8_{i}' for i in range(1, 10)]
buttons9 = [f'self.ui.btn_9_{i}' for i in range(1, 10)]
buttons10 = [f'self.ui.btn_10_{i}' for i in range(1, 10)]
buttons12 = [f'self.ui.btn_12_{i}' for i in range(1, 10)]
buttons14 = [f'self.ui.btn_14_{i}' for i in range(1, 10)]
buttons16 = [f'self.ui.btn_16_{i}' for i in range(1, 10)]
buttons18 = [f'self.ui.btn_18_{i}' for i in range(1, 10)]
buttons24 = [f'self.ui.btn_24_{i}' for i in range(1, 10)]

# file name
file_name = '.\\Categories\\'

# ages
ages_file = ['age4_5.xlsx',
             'age6.xlsx',
             'age7.xlsx',
             'age8.xlsx',
             'age9.xlsx',
             'age10_11.xlsx',
             'age12_13.xlsx',
             'age14_15.xlsx',
             'age16_17.xlsx',
             'age18_23.xlsx',
             'age24.xlsx']
sample = 'sample.xlsx'

# css
active_btn = """ QWidget 
                        {color: rgb(0, 0, 0);
                        font: 11pt}
             """
non_active_btn = """ QWidget 
                        {font: 8pt}
             """

# quantity of participants for laps define
members_10_lap = 5
members_8_lap = 4
members_6_lap = 3
members_4_lap = 2
members_2_lap = 1
last = 99

# win cells
place_1 = 'F23'
place_2 = 'F24'
place_3 = 'F25'

# quantity of participants for laps show
members_10_show = 21
# members_9_show = 20
members_8_show = 18
# members_7_show = 17
members_6_show = 15
# members_5_show = 14
members_4_show = 12
# members_3_show = 11
members_2_show = 9

start_init = 23
end_init_10 = 33
end_init_9 = 32
end_init_8 = 31
end_init_7 = 30
end_init_6 = 29
end_init_5 = 28
end_init_4 = 27
end_init_3 = 26
end_init_2 = 25

end_lap = 'Конец тура'
lap1 = 'Круг №1'
lap2 = 'Круг №2'
lap3 = 'Круг №3'
lap4 = 'Круг №4'
lap5 = 'Круг №5'
lap6 = 'Круг №6'
lap7 = 'Круг №7'
lap8 = 'Круг №8'
finish = 'Финиш'

t = 'table-'
b = '-button-'
cancel = 'отмена выбора категории'

#messages
t_lose_msg = 'Проигравшие еще не определены'
lose_msg = 'Пожалуста, проведите предыдущие бои'
score_equal_msg = 'Пожалуйста, выставьте очки за текущий бой'
t_score_equal_msg = 'Все очки равны!!!'
