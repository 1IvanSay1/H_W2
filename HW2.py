from pprint import pprint
import re
import csv
with open("D:\IT\Проекты\Домашки\phonebook_raw.csv", 'r', encoding="utf8") as file:
  reader = csv.reader(file, delimiter=",")
  contacts_list = list(reader)
X = r'([А-Я][a-я]+)\s*[,]*([А-Я][a-я]+)\s*[,]*([А-Я][a-я]+\s*)'
Y = r'\1,\2,\3'
C = r'([,]+)'
V = r'(\+7|8)\s*\(*(\d{3,3})\)*\s*[-]*(\d{3,3})\s*[-]*\s*(\d{2,2})\s*[-]*\s*(\d+)(\s*)(\(*(([а-я.]+)\s*(\d+))\)*)*'
B = r'+7(\2)\3-\4-\5\6\9\10'
xro = []
for i in contacts_list:
  page_string = ','.join(i)
  list0 = re.sub(X, Y, page_string)
  list1 = re.sub(C, r',', list0)
  list2 = re.sub(V, B, list1)
  list2_list = list2.split(",")
  xro.append(list2_list)

with open("phonebook_raw", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(xro)
