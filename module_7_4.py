##"Форматирование строк"#module_7_4.py
##Задача "соперничество двух команд":
import string
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time)/tasks_total
time_avg = round(time_avg,1)
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'
#challenge_result = 'Победа команды Волшебники данных!'
print('В команде Мастера кода участников: %s !' %team1_num)
print('Итого сегодня в командах участников: %s и %s !' %(team1_num, team2_num))
print('Команда Волшебники данных решила задач: %s !' %score_2)
print('Сегодня было решено %s задач, в среднем по %s секунды на задачу!.' %(tasks_total, time_avg))
print('Результат битвы: %s' %challenge_result)
