#!/usr/bin/python3

"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html
"""
import random

class LotoGameOver(Exception):
    pass

class Bilet:
    def __init__(self):
        #дополнено условием как в реальном лото, цифры из каждого десятка в строке встречаются не более 1 раза,
        #т.е. в строке не может быть 76 и 79 например
        self.digits = []
        usednums = [0]
        a=[x for x in range(10)]
        for i in range(3):
            istr = {}
            for d in random.sample(a,5):
                while True:
                    k = d*10+random.randint(0,9)
                    if k not in usednums:
                        break
                istr[d] = k
                usednums.append(k)
            self.digits.append(istr)

    def checkdig(self,dig,isDelete=False):
        for dstr in range(len(self.digits)):
            for i in self.digits[dstr]:
                try:
                    if int(self.digits[dstr][i]) == dig:
                        if isDelete == True:
                            self.digits[dstr][i] = '--'
                        return 0
                except ValueError:
                    pass
        return 1

    def __str__(self):
        result = ''
        countErr = 0
        for dstr in self.digits:
            for i in range(10):
                g = dstr.get(i)
                if g != None:
                    try:
                        g = int(g)
                        if g < 10:
                            result += '0%s ' % (g,)
                        else:
                            result += '%s ' % (g,)
                    except ValueError:
                        countErr += 1
                        result += '%s ' % (g,)
                else:
                    result += '   '
            result += '\n'
        if countErr == 15:
            raise LotoGameOver('Игра окончена!')
        return result

def randBar():
    z = [x for x in range(1,100)]
    random.shuffle(z)
    for i in range(len(z)):
        yield (z[i],len(z)-1-i)

if __name__ == "__main__":
    userLoto = Bilet()
    compLoto = Bilet()
    try:
        for b in randBar():
            print('Новый бочонок: %s (осталось %s)' % b)
            print('------ Ваша карточка -----')
            print(userLoto)
            print('--------------------------')
            print('-- Карточка компьютера ---')
            print(compLoto)
            print('--------------------------')
            while True:
                button = input('Зачеркнуть цифру? (y/n)')
                if button == 'y':
                    if userLoto.checkdig(b[0],True) == 1:
                        raise LotoGameOver('Нельзя вычеркнуть!\nБочонка с номером %s нет в вашей карточке, но вы попытались его вычеркнуть.\nВы проиграли!' % (b[0],))
                        pass                    
                    break
                elif button == 'n':
                    if userLoto.checkdig(b[0]) == 0:
                        raise LotoGameOver('Необходимо вычеркнуть!\nБочонок с номером %s есть в вашей карточке, но вы его не вычеркнули.\nВы проиграли!' % (b[0],)) 
                    break
            compLoto.checkdig(b[0],True)
    except LotoGameOver as e:
        print(e)
    
    

