from functions import *
from main import *

the_menu = {
        "L": "List",
        "A": "Add",
        "U" : "Update",
        "D" : "Delete",
        "H" : "Display restaurant expense rating",
        "S" : "Save the data to file",
        "R" : "Restore data from file",
        "Q" : "Quit this program"
        }

restaurant_menu_list = [
        {
    "name": "burrito",
    "calories": 500,
    "price": 12.90,
    "is_vegetarian": "yes",
    "spicy_level": 4
    },
        {
    "name": "rice bowl",
    "calories": 400,
    "price": 14.90,
    "is_vegetarian": "no",
    "spicy_level": 3
    },
        {
    "name": "margherita",
    "calories": 800,
    "price": 18.90,
    "is_vegetarian": "no",
    "spicy_level": 2
    }
        ]

list_menu = {
    "A": "complete menu",
    "V": "vegetarian dishes only",
    }

spicy_scale_map = {
    1: "Not spicy",
    2: "Low key spicy",
    3: "Hot",
    4: "Diabolical"
    }

assert the_menu["L"] == "List"
assert the_menu["Q"] == "Quit this program"

assert is_valid_name("a") == False
assert is_valid_name("bo") == False
assert is_valid_name(42) == False
assert is_valid_name(["soup"]) == False
assert is_valid_name("soup") == True

# testing get_new_menu_dish
input_dish = ['burrito', 500, '12.90', 'yes', '4']
spicy_scale_map = {
        1: "Not spicy",
        2: "Low key spicy",
        3: "Hot",
        4: "Diabolical"
        }
assert get_new_menu_dish(input_dish, spicy_scale_map) == ('calories', 500)
input_dish = ['burrito', '500', '12.90', 'yes', '10']
assert get_new_menu_dish(input_dish, spicy_scale_map) == ('spicy_level', '10')
input_dish = ['burrito', '500', '12.90', 'maybe', '4']
assert get_new_menu_dish(input_dish, spicy_scale_map) == ('is_vegetarian', 'maybe')

# testing for add helper


# for is_num
assert is_num("8") == True
assert is_num(8) == False
assert is_num("3.95") == True
assert is_num("8.1.1") == False
assert is_num("8.apple") == False

# for is_valid_spicy_level
test_list = [1,2,3,4]
assert is_valid_spicy_level("3",test_list) == True
assert is_valid_spicy_level(3, test_list) == False
assert is_valid_spicy_level("6", test_list) == False

# for is_valid_is_vegetarian
assert is_valid_is_vegetarian("yes") == True
assert is_valid_is_vegetarian("no") == True
assert is_valid_is_vegetarian("not sure") == False
assert is_valid_is_vegetarian('y') == False

# for is_valid_price
assert is_valid_price("tex dollars") == False
assert is_valid_price(10) == False
assert is_valid_price("10") == True
assert is_valid_price("10.9") == True

# is_valid_calories
assert is_valid_calories(109.32) == False
assert is_valid_calories(109) == False
assert is_valid_calories("109") == True
assert is_valid_calories("hundred") == False

#is_valid_index
test_list = [1,2,3,4]
assert is_valid_index("2", test_list) == True
assert is_valid_index(2, test_list) == False
assert is_valid_index("3", test_list, start_idx=1) == True
assert is_valid_index("three", test_list) == False

# update_menu_dish
assert update_menu_dish([{'name':'burrito', 'calories': 500, 'price': 12.9, 'is_vegetarian': 'yes', 'spicy_level': 4}], 0, {0:'a'}, 'spicy_level', '0') == -1
assert update_menu_dish([{'name':'burrito', 'calories': 500, 'price': 12.9, 'is_vegetarian': 'yes', 'spicy_level': 4}], 0, {1: "Not spicy",2: "Low key spicy",3: "Hot",4: "Diabolical"}, 'is_vegetarian', 'no' == {'name': 'burrito', 'calories': 500, 'price': 12.9, 'is_vegetarian': 'no', 'spicy_level': 4})
assert update_menu_dish([{'name':'burrito', 'calories': 500, 'price': 12.9, 'is_vegetarian': 'yes', 'spicy_level': 4}], 0, {0:'a'}, 'spicy_level', '6') == -1

# save_menu_to_csv
assert save_menu_to_csv([{'name': 'burrito', 'calories': 500, 'price': 12.9, 'is_vegetarian': 'yes', 'spicy_level': 2}], 'menu_dominoes.csv') == None
assert save_menu_to_csv([], 'menu.csv') == None
assert save_menu_to_csv([{'name': 'burrito', 'calories': 500, 'price': 12.9, 'is_vegetarian': 'yes', 'spicy_level': 2}, {'name': 'Enchilada', 'calories': 800, 'price': 15.5, 'is_vegetarian': 'no', 'spicy_level': 2}], 'menu.txt') == -1

# load_menu_from_csv
assert load_menu_from_csv('menu_dominoes.csv', [], {1: 'Not spicy', 2: 'Low key spicy', 3: 'Hot', 4: 'Diabolical'}) == []
tmp = []
assert load_menu_from_csv("", [], {1: 'Not spicy', 2: 'Low key spicy', 3: 'Hot', 4: 'Diabolical'}) == -1
assert load_menu_from_csv('menu_dominoes.csv', tmp, {1: 'Not spicy', 2: 'Low key spicy', 3: 'Hot', 4: 'Diabolical'}) == []
assert tmp == [{'name': 'burrito', 'calories': 500, 'price': 12.9, 'is_vegetarian': 'yes', 'spicy_level': 2}]

# delete_dish
assert delete_dish([], '0') == 0
assert delete_dish([{'name': 'burrito', 'calories': 500, 'price': 12.9, 'is_vegetarian': 'yes', 'spicy_level': 2}], 0) == None
assert delete_dish([{'name': 'burrito', 'calories': 500, 'price': 12.9, 'is_vegetarian': 'yes', 'spicy_level': 2}], "2") == -1
assert delete_dish([{'name': 'burrito', 'calories': 500, 'price': 12.9, 'is_vegetarian': 'yes', 'spicy_level': 2}, {'name': 'Enchilada', 'calories': 800, 'price': 15.5, 'is_vegetarian': 'no', 'spicy_level': 2}], "0") == {'name': 'burrito', 'calories': 500, 'price': 12.9, 'is_vegetarian': 'yes', 'spicy_level': 2}

assert delete_dish([{'name': 'burrito', 'calories': 500, 'price': 12.9, 'is_vegetarian': 'yes', 'spicy_level': 2}, {'name': 'Enchilada', 'calories': 800, 'price': 15.5, 'is_vegetarian': 'no', 'spicy_level': 2}], "1", 1) == {'name': 'burrito', 'calories': 500, 'price': 12.9, 'is_vegetarian': 'yes', 'spicy_level': 2}
