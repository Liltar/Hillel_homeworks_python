# 3. Даны два целых числа `A` и `В`.
# Выведите все числа от `A` до `B` включительно, в порядке возрастания, если `A < B`,
# или в порядке убывания в противном случае.
first_number = int(input('Enter a first number: '))
second_number = int(input('Enter a second number: '))
if first_number < second_number:
    for i in range(first_number, second_number + 1):
        print(i)
elif first_number > second_number:
    for i in range(first_number, second_number - 1, - 1):
        print(i)
else:
    print('No way!')