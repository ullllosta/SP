start = str(input('������� Enter ��� ������ ���������� �����'))
name = str("���:"+input('������� ���: '))
fname = str("�������:"+input('������� �������: '))
year = str("�������:"+input('������� �������: '))
card = str('����� �����:'+input('������� ����� �����: '))
validity = str('���� �������� �����:'+input('������� ���� �������� �����: '))
code = str('���:'+input('������� ��� �� �������� �������: '))
file = [name, fname, year, card, validity, code]
file_total = open("file1.txt", "a")

for item in file:
    file_total.write("%s;\xa0\xa0" % item)
file_total.write('\n')
file_total.close()
file_total = open("file1.txt")
total = file_total.read()
print(total)