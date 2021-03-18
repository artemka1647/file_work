from pprint import pprint

cook_book = {}

with open('recipes.txt') as f:
    while True:
        dish_name = f.readline().strip()
        if dish_name == "":
            break
        count = int(f.readline())
        ing_list = []
        for _ in range(count):
            ingr = f.readline().strip().split('|')
            ing_dict = {}
            ing_dict['ingredient_name'] = ingr[0]
            ing_dict['quantity'] = ingr[1]
            ing_dict['measure'] = ingr[2]
            ing_list.append(ing_dict)
        cook_book[dish_name] = ing_list
        f.readline()
# pprint(cook_book)

import os

with open('1.txt') as file:
    first_file = file.read()

with open('2.txt') as file:
    second_file = file.read()

with open('3.txt','w') as file:
    file.write('2.txt\n')
with open('3.txt','a') as file:
    file.write('1 строчка\n')
with open('3.txt','a') as file:
    file.write(second_file)
with open('3.txt','a') as file:
    file.write('1.txt\n')
with open('3.txt','a') as file:
    file.write('8 строк\n')
with open('3.txt','a') as file:
    file.write(first_file)
with open('3.txt') as f:
    print(f.read())