# Пользователь вводит трехзначное число. Найдите сумму его цифр.
some_input = (input('Enter a 3-digit number: '))
sum_of_digits = 0
for i in some_input:
    sum_of_digits += int(i)
print(sum_of_digits)
