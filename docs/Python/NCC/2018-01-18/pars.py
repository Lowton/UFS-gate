import os
import sys
import fnmatch
import shutil
import sqlite3

file = 'C:\\System\\NCC\\88920\\ncc0110.235'

root = 'C:\\System\\NCC\\88920\\files\\filtred\\'
pattern = 'ncc*.235'
outputfile = 'C:\\System\\NCC\\88920\\out_ru33.txt'

conn = sqlite3.connect('cage.db')
c = conn.cursor()

def __case_transaction(transact):
    if transact == '00':
        return 'Продажа товаров'
    elif transact == '01':
        return 'Выдача наличных'
    elif transact == '02':
        return 'Дебетное выравнивание'
    elif transact == '11':
        return 'Квази-наличные'
    elif transact == '16':
        return 'Безналичные удержания'
    elif transact == '18':
        return 'Безналичные платежи'
    elif transact == '19':
        return 'Комиссия за безналичные платежи'
    elif transact == '20':
        return 'Кредит общего вида'
    elif transact == '22':
        return 'Кредитное выравнивание'
    elif transact == '26':
        return 'Безналичное перечисление с другой карты'
    elif transact == '28':
        return 'Безналичные платежи (отмена)'
    elif transact == '29':
        return 'Внесение наличных'
    elif transact == '33':
        return 'Запрос мини-выписки '
    elif transact == '40':
        return 'Безналичное зачисление'
    else:
        return 'Какая-то лажа'

def __case_ps(ps):
    if ps == 'NCC  ':
        return 'НСС'
    elif ps == 'EFB2 ':
        return 'VISA'
    elif ps == 'NEFB2':
        return 'НСПК'
    else:
        return 'NONE'

def __case_cage(cage):
    c.execute('select * from Cage_list where cage = ?',(cage,))
    f = c.fetchone()
    return  f if f != None else (cage, 2, 666)

def __parse_result(data):
    c.execute('insert into result_ru33 values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',data)
    


def __summ(money):
    return float(money)/100

def __line_search(file):
    
    with open(file,'r',encoding='cp866') as file_ncc235:
        for line in file_ncc235:
            cage = line[23:29]
            #print(cage)
            money = line[101:117]
            curr = line[117:120]

            transact = line[198:204]
            case_tran = __case_transaction(transact[0:2])

            money2 = line[204:220]
            curr2 = line[220:223]

            if transact == '330000':
                money2 = line[138:155]
                curr2 = line[155:158]

            if curr2 != '810':
                money3 = line[223:238]
                curr3 = line[238:242]
            else:
                money3 = '0'
                curr3 = '810'

            ps = line[261:266]
            case_ps = __case_ps(ps)

            case_cage = __case_cage(cage)
            #print(case_cage)
            cage_num = case_cage[0]
            cage_client = 'ФЛ' if case_cage[1] == 0 else 'ЮЛ'
            cage_region = case_cage[2]
            
            sql_data = (cage, cage_num, cage_client, cage_region
                        ,money, __summ(money)
                        ,int(curr)
                        ,transact, case_tran
                        ,money2, __summ(money2)
                        ,money3, __summ(money3)
                        ,int(curr2), int(curr3)
                        ,ps, case_ps,)

            __parse_result(sql_data)
        
            out_data = '"' + file[-11:] + '";'
            #print(out_data)
            for i in sql_data:
                #print(out_data)
                out_data += '"' + str(i) + '";'
            out_data += '"' + line[:-1] + '"'

            with open(outputfile,'a') as outfile:
                try:
                    outfile.write(out_data + '\n')
                except UnicodeDecodeError:
                    outfile.write('UnicodeDecodeError\n')

#__line_search(file)

for folder, subdirs, files in os.walk(root):
  #print('c',folder)
  for filename in fnmatch.filter(files, pattern):
    fullname = os.path.join(folder, filename)
    print('f',fullname)
    year = folder[17:22]
    __line_search(fullname)


conn.commit()
conn.close()

