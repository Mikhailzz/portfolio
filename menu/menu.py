from pprint import pprint

file_path = "menu.txt"


def make_cook_book(name_file):
    cook_book = {}
    with open(name_file, encoding='UTF-8') as file:
        for line in file:
            dish = line.strip()
            count_ingridient = int(file.readline())
            ingredient_list = []
            for i in range(count_ingridient):
                ingr = file.readline().split(' | ')
                ingredients = {'ingredient_name': ingr[0].strip(), 'quantity': int(ingr[1]), 'measure': ingr[2].strip()}
                ingredient_list.append(ingredients)
            cook_book[dish] = ingredient_list
            file.readline()
    file.close()
    return cook_book


pprint(make_cook_book(file_path), width=70)


def get_shop_list_by_dishes(dishes: list, person_count=1):
    cook_book = make_cook_book(file_path)
    shop_list = {}
    for elem in dishes:
        for ingredients in cook_book.get(elem, []):
            ingr_name = ingredients['ingredient_name']
            ingr_count = ingredients['quantity']
            ingr_mea = ingredients['measure']
            if ingr_name in shop_list:
                shop_list[ingr_name]['quantity'] += ingr_count * person_count
            else:
                shop_list[ingr_name] = {'quantity': ingr_count * person_count, 'measure': ingr_mea}

    return shop_list


print()
pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2), width=100)

