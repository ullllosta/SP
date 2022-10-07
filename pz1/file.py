start = str(input('Нажмите Enter для начала заполнения формы'))
name = str("Имя:"+input('Введите Имя: '))
fname = str("Фамилия:"+input('Введите Фамилию: '))
year = str("Возраст:"+input('Введите возраст: '))
card = str('Номер карты:'+input('Введите номер карты: '))
validity = str('Срок действия карты:'+input('Введите срок действия карты: '))
code = str('Код:'+input('Введите код на обратной стороне: '))
file = [name, fname, year, card, validity, code]
file_total = open("file1.txt", "a")

for item in file:
    file_total.write("%s;\xa0\xa0" % item)
file_total.write('\n')
file_total.close()
file_total = open("file1.txt")
total = file_total.read()
print(total)