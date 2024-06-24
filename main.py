from logger import logger


# Книга рецептов
@logger
def get_cook_book():
    with open('recipes.txt', encoding='utf-8') as f:
        cook_book = {}
        for line in f:
            dish_name = line.strip()
            ingredients_list = []
            ingredients_quantity = f.readline()
            for item in range(int(ingredients_quantity)):
                ingredient_name, quantity, measure = f.readline().split(' | ')
                ingredients_list.append(
                    {'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure.strip()})
            cook_book[dish_name] = ingredients_list
            f.readline()
    return cook_book


if __name__ == '__main__':
    get_cook_book()
