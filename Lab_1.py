import re

ex = input('Введите номер задания!'+'\n')
string = '*******'
reg = ''
if ex == '1':
    string = 'Белеет парус одинокой в тумане моря голубом! Что ищет он в стране далекой? Что кинул он в краю родном?'
    print(string)
    reg = re.split(r'[.?!...]', string)
    print(reg)
elif ex == '2':
    string = 'Редиску редиска редиской нехорошего человека нехорошему человеку Нехороший человек'
    print(string)
    reg = re.sub(r'([Рр]едиск\w{1,2}\b)|([Нн]ехорош\w{2,3}\b человек\w{0,2}\b)', '*давайте жить дружно*', string)
    print(reg)
elif ex == '3':
    while "".join(reg) != string:
        string = input('Введите пароль: ' + '\n')
        reg = re.findall(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[.?!]).{6,}$', string)
    print('Пароль принят!!!')
elif ex == '4':
    while "".join(reg) != string:
        string = input('Введите e-mail: ' + '\n')
        reg = re.findall(r'^[A-Za-z0-9._-]+@[A-Za-z0-9-]+.+.[A-Za-z]{2,4}$', string)
    print('E-mail введён правильно!!!')
elif ex == '5':
    string = 'Французы вторглись в наши земли 02-6-12. Мы дали им сражение у Бородино 26-08-1812'
    print(string)
    reg = re.sub('(\d|[0-2]\d|3[0-1])\-(1[0-2]|\d|0\d)\-(\d{4}|\d{2})', r'\3-\2-\1', string)
    print(reg)
else:
    print('Необходимо ввести номер от 1 до 5!!!')