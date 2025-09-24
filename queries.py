import sqlite3
from prettytable import PrettyTable

def f1():
    """Выведите список всех студентов.
    Атрибуты вывода: name, surname, age.

    """
    print("\n" + "="*50)
    print("ФУНКЦИЯ 1: Список всех студентов")
    print("="*50)
    con = sqlite3.connect("ursei.db")
    curs = con.cursor()

    curs.execute('''SELECT 
                 name, 
                 surname, 
                 age 
                 FROM student''')
    
    #получим имена столбцов из свойства description курсора
    col_names = [cn[0] for cn in curs.description]
    #получим данные
    rows = curs.fetchall()

    #Инициализируем таблицу c заголовками
    pt = PrettyTable(col_names)
    pt.align[col_names[0]] = "l" # Выравнивание столбца по левому краю
    pt.align[col_names[1]] = "l"

    #Добавим данные в таблицу
    for row in rows:
        pt.add_row(row)
    
    #Выводим таблицу
    print(pt)
    con.close()


def f2():
    """Выведите отсортированный по фамилиям список студентов из группы РЕК-201.
    Имя группы произвольно.
    Атрибуты вывода: "Группа", "Фамилия", "Имя".

    """
    print("\n" + "="*50)
    print("ФУНКЦИЯ 2: Студенты группы РЕК-201")
    print("="*50)
    con = sqlite3.connect("ursei.db")
    curs = con.cursor()

    curs.execute('''SELECT 
                 g.name as "Группа", 
                 s.surname as "Фамилия", 
                 s.name as "Имя"
                 FROM student s
                 JOIN "group" g ON s.group_id = g.id
                 WHERE g.name LIKE 'РЕК-201'
                 ORDER BY s.surname''')
    
    col_names = [cn[0] for cn in curs.description]
    rows = curs.fetchall()

    pt = PrettyTable(col_names)
    for col in col_names:
        pt.align[col] = "l"

    for row in rows:
        pt.add_row(row)
    
    print(pt)
    con.close()


def f3():
    """Выведите всех девушек, обучающихся на факультете 'Реклама'.
    Атрибуты вывода: Название факультета, фамилия.

    """
    print("\n" + "="*50)
    print("ФУНКЦИЯ 3: Девушки на факультете Реклама")
    print("="*50)
    con = sqlite3.connect("ursei.db")
    curs = con.cursor()

    curs.execute('''SELECT 
                 d.name as "Название факультета", 
                 s.surname as "Фамилия"
                 FROM student s
                 JOIN "group" g ON s.group_id = g.id
                 JOIN department d ON g.department_id = d.id
                 WHERE d.name = 'Реклама' AND s.gender = 'Женский'
                 ORDER BY s.surname''')
    
    col_names = [cn[0] for cn in curs.description]
    rows = curs.fetchall()

    pt = PrettyTable(col_names)
    for col in col_names:
        pt.align[col] = "l"

    for row in rows:
        pt.add_row(row)
    
    print(pt)
    con.close()


def f4():
    """Определите количество молодых людей, обучающихся на юридическом факультете.
    Атрибуты вывода: 'Кол-во молодых людей'. Количество строк: 1.

    """
    print("\n" + "="*50)
    print("ФУНКЦИЯ 4: Молодые люди на юридическом факультете")
    print("="*50)
    con = sqlite3.connect("ursei.db")
    curs = con.cursor()

    curs.execute('''SELECT 
                 COUNT(*) as "Кол-во молодых людей"
                 FROM student s
                 JOIN "group" g ON s.group_id = g.id
                 JOIN department d ON g.department_id = d.id
                 WHERE d.name = 'Юриспруденция' AND s.gender = 'Мужской' ''')
    
    col_names = [cn[0] for cn in curs.description]
    rows = curs.fetchall()

    pt = PrettyTable(col_names)
    for col in col_names:
        pt.align[col] = "l"

    for row in rows:
        pt.add_row(row)
    
    print(pt)
    con.close()


def f5():
    """Определите средний возраст студентов, обучающихся на юридическом факультете.
    Округлите результат до целого числа.
    Атрибуты вывода: 'Юр. фак-т. Средний возраст'. Количество строк: 1.

    """
    print("\n" + "="*50)
    print("ФУНКЦИЯ 5: Средний возраст на юридическом факультете")
    print("="*50)
    con = sqlite3.connect("ursei.db")
    curs = con.cursor()

    curs.execute('''SELECT 
                 ROUND(AVG(s.age)) as "Юр. фак-т. Средний возраст"
                 FROM student s
                 JOIN "group" g ON s.group_id = g.id
                 JOIN department d ON g.department_id = d.id
                 WHERE d.name = 'Юриспруденция' ''')
    
    col_names = [cn[0] for cn in curs.description]
    rows = curs.fetchall()

    pt = PrettyTable(col_names)
    for col in col_names:
        pt.align[col] = "l"

    for row in rows:
        pt.add_row(row)
    
    print(pt)
    con.close()


def f6():
    """Выведите студентов количество, обучающихся на каждом факультете.
    Атрибуты вывода: 'Факультет', 'Количество'. Количество строк должно быть 
    равно количеству факультетов.

    """
    print("\n" + "="*50)
    print("ФУНКЦИЯ 6: Количество студентов по факультетам")
    print("="*50)
    con = sqlite3.connect("ursei.db")
    curs = con.cursor()

    curs.execute('''SELECT 
                 d.name as "Факультет", 
                 COUNT(s.id) as "Количество"
                 FROM department d
                 JOIN "group" g ON d.id = g.department_id
                 JOIN student s ON g.id = s.group_id
                 GROUP BY d.name
                 ORDER BY "Количество" DESC''')
    
    col_names = [cn[0] for cn in curs.description]
    rows = curs.fetchall()

    pt = PrettyTable(col_names)
    for col in col_names:
        pt.align[col] = "l"

    for row in rows:
        pt.add_row(row)
    
    print(pt)
    con.close()


def f7():
    """Выведите средний возраст студентов, обучающихся на каждом факультете.
    Результат округлите до 2-х знаков после точки.
    Атрибуты вывода: 'Факультет', 'Средний возраст'.

    """
    print("\n" + "="*50)
    print("ФУНКЦИЯ 7: Средний возраст по факультетам")
    print("="*50)
    con = sqlite3.connect("ursei.db")
    curs = con.cursor()

    curs.execute('''SELECT 
                 d.name as "Факультет", 
                 ROUND(AVG(s.age), 2) as "Средний возраст"
                 FROM department d
                 JOIN "group" g ON d.id = g.department_id
                 JOIN student s ON g.id = s.group_id
                 GROUP BY d.name
                 ORDER BY d.name''')
    
    col_names = [cn[0] for cn in curs.description]
    rows = curs.fetchall()

    pt = PrettyTable(col_names)
    for col in col_names:
        pt.align[col] = "l"

    for row in rows:
        pt.add_row(row)
    
    print(pt)
    con.close()


def f8():
    """Выведите список студентов, которые не обучаются на юридическом факультете.
    Атрибуты вывода: 'Факультет', 'Группа', 'ФИО'. Атрибут ФИО  должен состоять из фамилии,
    первой буквы имени и точки (напр. Иванов И.).
    
    """
    print("\n" + "="*50)
    print("ФУНКЦИЯ 8: Студенты не юридического факультета")
    print("="*50)
    con = sqlite3.connect("ursei.db")
    curs = con.cursor()

    curs.execute('''SELECT 
                 d.name as "Факультет", 
                 g.name as "Группа", 
                 s.surname || ' ' || substr(s.name, 1, 1) || '.' as "ФИО"
                 FROM student s
                 JOIN "group" g ON s.group_id = g.id
                 JOIN department d ON g.department_id = d.id
                 WHERE d.name != 'Юриспруденция'
                 ORDER BY d.name, g.name, s.surname''')
    
    col_names = [cn[0] for cn in curs.description]
    rows = curs.fetchall()

    pt = PrettyTable(col_names)
    for col in col_names:
        pt.align[col] = "l"

    for row in rows:
        pt.add_row(row)
    
    print(pt)
    con.close()


def f9():
    """Выведите список студентов юридического факультета, у которых возраст
    меньше среднего по факультету.
    Атрибуты вывода: 'Факультет', 'Фамилия', 'Возраст'.

    """
    print("\n" + "="*50)
    print("ФУНКЦИЯ 9: Студенты юрфака с возрастом меньше среднего")
    print("="*50)
    con = sqlite3.connect("ursei.db")
    curs = con.cursor()

    curs.execute('''SELECT 
                 d.name as "Факультет", 
                 s.surname as "Фамилия", 
                 s.age as "Возраст"
                 FROM student s
                 JOIN "group" g ON s.group_id = g.id
                 JOIN department d ON g.department_id = d.id
                 WHERE d.name = 'Юриспруденция' 
                 AND s.age < (SELECT AVG(age) FROM student s2
                             JOIN "group" g2 ON s2.group_id = g2.id
                             JOIN department d2 ON g2.department_id = d2.id
                             WHERE d2.name = 'Юриспруденция')
                 ORDER BY s.age''')
    
    col_names = [cn[0] for cn in curs.description]
    rows = curs.fetchall()

    pt = PrettyTable(col_names)
    for col in col_names:
        pt.align[col] = "l"

    for row in rows:
        pt.add_row(row)
    
    print(pt)
    con.close()


def f10():
    """Выведите список студентов, у которых фамилия начинается на букву 'К'.
    Атрибуты вывода: 'Факультет', 'Группа', 'Фамилия'.

    """
    print("\n" + "="*50)
    print("ФУНКЦИЯ 10: Студенты с фамилией на 'К'")
    print("="*50)
    con = sqlite3.connect("ursei.db")
    curs = con.cursor()

    curs.execute('''SELECT 
                 d.name as "Факультет", 
                 g.name as "Группа", 
                 s.surname as "Фамилия"
                 FROM student s
                 JOIN "group" g ON s.group_id = g.id
                 JOIN department d ON g.department_id = d.id
                 WHERE s.surname LIKE 'К%'
                 ORDER BY d.name, g.name, s.surname''')
    
    col_names = [cn[0] for cn in curs.description]
    rows = curs.fetchall()

    pt = PrettyTable(col_names)
    for col in col_names:
        pt.align[col] = "l"

    for row in rows:
        pt.add_row(row)
    
    print(pt)
    con.close()


def f11():
    """Выведите список студентов группы РЕК-201 (имя группы произвольно),
    у которых имя заканчивается на букву 'й' (напр. Аркадий).
    Атрибуты вывода: 'Группа', 'Имя', 'Фамилия'.

    """
    print("\n" + "="*50)
    print("ФУНКЦИЯ 11: Студенты РЕК-201 с именами на 'й'")
    print("="*50)
    con = sqlite3.connect("ursei.db")
    curs = con.cursor()

    curs.execute('''SELECT 
                 g.name as "Группа", 
                 s.name as "Имя", 
                 s.surname as "Фамилия"
                 FROM student s
                 JOIN "group" g ON s.group_id = g.id
                 WHERE g.name = 'РЕК-201' AND s.name LIKE '%й'
                 ORDER BY s.surname''')
    
    col_names = [cn[0] for cn in curs.description]
    rows = curs.fetchall()

    pt = PrettyTable(col_names)
    for col in col_names:
        pt.align[col] = "l"

    for row in rows:
        pt.add_row(row)
    
    print(pt)
    con.close()


def f12():
    '''Выведите студента с самой длинной по количеству символов фамилией.
    Атрибуты вывода: "Фамилия", "Кол-во символов"

    '''
    print("\n" + "="*50)
    print("ФУНКЦИЯ 12: Студент с самой длинной фамилией")
    print("="*50)
    con = sqlite3.connect("ursei.db")
    curs = con.cursor()

    curs.execute('''SELECT 
                 surname as "Фамилия", 
                 LENGTH(surname) as "Кол-во символов"
                 FROM student
                 ORDER BY LENGTH(surname) DESC
                 LIMIT 1''')
    
    col_names = [cn[0] for cn in curs.description]
    rows = curs.fetchall()

    pt = PrettyTable(col_names)
    for col in col_names:
        pt.align[col] = "l"

    for row in rows:
        pt.add_row(row)
    
    print(pt)
    con.close()


def f13():
    '''Выведите уникальный список женских имен и количество их повторений.
    Список должен быть отсортирован по количеству повторений в порядке убывания.
    Атрибуты вывода: "Имя", "Кол-во повторений"

    '''
    print("\n" + "="*50)
    print("ФУНКЦИЯ 13: Женские имена и их повторения")
    print("="*50)
    con = sqlite3.connect("ursei.db")
    curs = con.cursor()

    curs.execute('''SELECT 
                 name as "Имя", 
                 COUNT(*) as "Кол-во повторений"
                 FROM student
                 WHERE gender = 'Женский'
                 GROUP BY name
                 ORDER BY COUNT(*) DESC, name''')
    
    col_names = [cn[0] for cn in curs.description]
    rows = curs.fetchall()

    pt = PrettyTable(col_names)
    for col in col_names:
        pt.align[col] = "l"

    for row in rows:
        pt.add_row(row)
    
    print(pt)
    con.close()


def f14():
    '''Выведите 3 последние записи из таблицы student.
    Сортировку не использовать.
    Атрибуты вывода: id, surname

    '''
    print("\n" + "="*50)
    print("ФУНКЦИЯ 14: 3 последние записи студентов")
    print("="*50)
    con = sqlite3.connect("ursei.db")
    curs = con.cursor()

    curs.execute('''SELECT 
                 id, 
                 surname
                 FROM student
                 WHERE id IN (SELECT id FROM student 
                 EXCEPT 
                 SELECT id FROM student LIMIT (SELECT COUNT(*) FROM student) - 3)''')
    
    col_names = [cn[0] for cn in curs.description]
    rows = curs.fetchall()

    pt = PrettyTable(col_names)
    for col in col_names:
        pt.align[col] = "l"

    for row in rows:
        pt.add_row(row)
    
    print(pt)
    con.close()


func_register = {
    '1': f1,
    '2': f2,
    '3': f3,
    '4': f4,
    '5': f5,
    '6': f6,
    '7': f7,
    '8': f8,
    '9': f9,
    '10': f10,
    '11': f11,
    '12': f12,
    '13': f13,
    '14': f14
}
