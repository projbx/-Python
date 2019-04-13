# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    pre_res_num = number*10**ndigits//1
    last_dig = number*10**(ndigits+1)//1%10
    if last_dig>=5:
        pre_res_num += 1
    res_num = pre_res_num/10**ndigits
    return res_num


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    if len(str(ticket_number))>6:
        return 'Ошибка! Номер билета больше шести знаков'
    part1 = 0
    part2 = 0
    is_part2 = True
    a = ticket_number//10
    b = ticket_number%10
    k=0
    while a != 0:
        print(part1)
        print(part2)
        if is_part2:
            part2 += b
            k+=1
            if k==3:
                is_part2 = False
        else:
            part1 += b
        b = a%10
        a = a//10
    if is_part2:
        part2 += b
    else:
        part1 +=b
    print(part1)
    print(part2)
    if part1 == part2:
        return 'lucky'
    else:
        return 'not_lucky'



print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
print(lucky_ticket(1232156))
