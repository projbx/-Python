# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class Klass:
    def __init__(self,name):
        self.name = name #7A or 5B
        self.students = []
        self.teachers = []

class Student:
    def __init__(self,name,room,parents):
        self.name = name #ФИО
        self.room = room #класс - class = Klass
        self.parents = parents # например parents=[motherFIO,fatherFIO]

class Teacher:
    def __init__(self,name,lesson):
        self.name = name
        self.lesson = lesson

#Example
listOfKlasses = {'7A':Klass('7A'),'5B':Klass('5B')}
rawDataOfStudets = {'Иван':['7A','мамаИвана','папаИвана'],'Даша':['5B','мамаДаши','папаДаши']}
rawDataOfTeachers = {'Лелик':['eng','7A','5B'],'Болик':['math','7A','5B']}

for i in rawDataOfStudets:
    class_room = rawDataOfStudets[i][0]
    parents = rawDataOfStudets[i][1:]
    listOfKlasses[class_room].students.append(Student(i,class_room,parents))

for i in rawDataOfTeachers:
    lesson = rawDataOfTeachers[i][0]
    classes = rawDataOfTeachers[i][1:]
    for kl in classes:
        listOfKlasses[kl].teachers.append(Teacher(i,lesson))

# 1. Получить полный список всех классов школы
for elt in listOfKlasses:
    print elt

# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О."
for stud in listOfKlasses['7A'].students:
    print stud.name
    
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
for i in listOfKlasses:
    if 'Иван' in listOfKlasses[i].students:
        for teach in listOfKlasses[i].teachers:
            print teach.lesson
        break

    # 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе
print listOfKlasses['7A'].teachers
