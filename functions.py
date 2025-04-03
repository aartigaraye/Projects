# functions.py: function definitions for csw8 final project

def print_main_menu(menu):
    """
    Given a dictionary with the menu,
    prints the keys and values as the
    formatted options.
    Adds additional prints for decoration
    and outputs a question
    "What would you like to do?"
    """
    print("==========================")
    print("What would you like to do?")
    for key, value in menu.items():
        print(f'{key} - {value}')
    print("==========================")


def list_helper(list_menu, restaurant_menu_list, spicy_scale_map):
    """
    param: list_menu: dict for listing the available options
    param: restaurant_menu_list: list with dict for each dish in it
    param: spicy_scale_map: dict with numeric keys to indicate the spice level

    This is a helper function used to display the list of the restaurant menu
    if the len of the restaurant_menu is 0 then we print there is nothing
    to display
    else, we can display the options we have for the users to choose
    for example they can go for all menu
    or they could go for vegetarian only
    this function has a lot of scope for development because we can further
    add options like show dishes depeneding on your spice preferance or
    calories preferance.

    helper function:
    print_restaurant_menu
    """
    if len(restaurant_menu_list) == 0:
        print("WARNING: There is nothing to display!")
        # Pause before going back to the main menu
        input("::: Press Enter to continue")
    else:
        subopt = get_selection("List", list_menu)
        if subopt == 'A':
            print_restaurant_menu(restaurant_menu_list, spicy_scale_map, show_idx=True, start_idx=1)
        elif subopt == 'V':
            print_restaurant_menu(restaurant_menu_list, spicy_scale_map, show_idx=True, start_idx=1, vegetarian_only=True)

######## LIST OPTION ########

def get_selection(action, suboptions, to_upper=True, go_back=False):
    """
    param: action (string) - the action that the user
            would like to perform; printed as part of
            the function prompt
    param: suboptions (dictionary) - contains suboptions
            that are listed underneath the function prompt.
    param: to_upper (Boolean) - by default, set to True, so
            the user selection is converted to upper-case.
            If set to False, then the user input is used
            as-is.
    param: go_back (Boolean) - by default, set to False.
            If set to True, then allows the user to select the
            option M to return back to the main menu
    The function displays a submenu for the user to choose from.
    Asks the user to select an option using the input() function.
    Re-prints the submenu if an invalid option is given.
    Prints the confirmation of the selection by retrieving the
    description of the option from the suboptions dictionary.
    returns: the option selection (by default, an upper-case string).
            The selection be a valid key in the suboptions
            or a letter M, if go_back is True.
    """
    selection = None
    if go_back:
        if 'm' in suboptions or 'M' in suboptions:
            print("Invalid submenu, which contains M as a key.")
            return None
    while selection not in suboptions:
        print(f"::: What field would you like to {action.lower()}?")
        for key in suboptions:
            print(f"{key} - {suboptions[key]}")
        if go_back:
            selection = input(f"::: Enter your selection "
                              f"or press 'm' to return to the main menu\n> ")
        else:
            selection = input("::: Enter your selection\n> ")
        if to_upper:
            selection = selection.upper()  # to allow us to input lower- or upper-case letters
        if go_back and selection.upper() == 'M':
            return 'M'

    print(f"You selected |{selection}| to",
          f"{action.lower()} |{suboptions[selection]}|.")
    return selection

def print_restaurant_menu(restaurant_menu, spicy_scale_map, name_only=False, show_idx=True, start_idx=0, vegetarian_only=False):
    """
    param: restaurant_menu (list) - a list object that holds the dictionaries for each dish
    param: spicy_scale_map (dict) - a dictionary object that is expected
            to have the integer keys that correspond to the "level of spiciness."
    param: name_only (Boolean)
            If False, then only the name of the dish is printed.
            Otherwise, displays the formatted dish information.
    param: show_idx (Boolean)
            If False, then the index of the menu is not displayed.
            Otherwise, displays the "{idx + start_idx}." before the
            dish name, where idx is the 0-based index in the list.
    param: start_idx (int)
            an expected starting value for idx that
            gets displayed for the first dish, if show_idx is True.
    param:  vegetarian_only (Boolean)
            If set to False, prints all dishes, regardless of their
            is_vegetarian status ("yes/no" field status).
             If set to True , display only the dishes with
            "is_vegetarian" status set to "yes".
    returns: None; only prints the restaurant menu
    """
    idx = start_idx
    print("------------------------------------------")
   # Go through the dishes in the restaurant menu:
    for dish in restaurant_menu:
       # if vegetarian_only is True and the dish is not vegetarian, skip
        if vegetarian_only == True and dish["is_vegetarian"].lower() == 'no':
            continue

        # if the index of the task needs to be displayed (show_idx is True), print dish index only
        if show_idx == True:
            print(f"{idx}.", end=" ")

        # print the name of the dish
        if name_only == True:
            all_caps = dish['name'].upper()
            print(f"{all_caps}")

        # if name_only is False
        if name_only == False:
            print(f"{dish['name'].upper()}")
            print(f"* Calories: {dish['calories']}")
            print(f"* Price: {dish['price']:.1f}")
            print(f"* Is it vegetarian: {'yes' if dish['is_vegetarian'].lower() == 'yes' else 'no'}")
            print(f"* Spicy level: {spicy_scale_map[dish['spicy_level']]}")
            print()
        idx += 1

    print("------------------------------------------")

def is_num(val):
    """
    The function checks if `val` is a string;
    returns False if `val` is not a string.
    Otherwise, returns True if the string `val`
    contains a valid integer or a float.
    Returns False otherwise.
    """
    if type(val) == str:
        parts = val.split('.')
        if len(parts) == 1:
            return parts[0].isdigit()
        elif len(parts) == 2:
            return parts[0].isdigit() and parts[1].isdigit()
    return False
    


def is_valid_name(name_str):
    """
    param: name_str (string) - a text that is supposed to
            contain between 3 and 25 characters (inclusive
            of both)
    returns:
        - True if it's a text of the valid length
        - False, otherwise
    """
    if type(name_str) == str and (3 <= len(name_str) <= 25):
        return True
    else:
        return False


def is_valid_spicy_level(spicy_level_str, spicy_scale_map):
    """
    param: spicy_level_str (string) - a string that is
            expected to contain the level of spiciness
    param: spicy_scale_map (dict) - a dictionary that
            contains the mapping between the integer
            priority value of spiciness to its representation
            (e.g., key 1 might map to the spiciness value
            "non spicy")
    returns:
        - True if spicy_level_str is a text containing
            an integer value that maps to a key in the
            priority_map
        - False, otherwise
    """
    if type(spicy_level_str) == str and spicy_level_str.isdigit() and int(spicy_level_str) in spicy_scale_map:
        return True
    else:
        return False


def is_valid_is_vegetarian(vegetarian_str):
    """
    param: vegetarian_str (string) - a string that is
            expected to contain a text "yes" or "no"
    returns:
        - True if it's a text with the valid value
        - False, otherwise
    """
    if type(vegetarian_str) == str and vegetarian_str.lower() in ["yes", "no"]:
        return True
    else:
        return False


def is_valid_price(price_str):
    """
    param: price_str (string) - a string that
            contains a decimal number to represent price
    returns:
        - True if it's a text containing decimal number
        - False, otherwise
    """
    if type(price_str) == str and is_num(price_str):
        return True
    else:
        return False

def is_valid_calories(calories_str):
    """
    param: calories_str (str) - a string that is
            expected to represent calories
    returns:
        - True if it's a text containing integer value
        - False, otherwise
    """
    if type(calories_str) == str and calories_str.isdigit():
        return True
    else:
        return False

def get_new_menu_dish(dish_list, spicy_scale_map):
    '''
    validate each element of the list starting from "name" and until "spicy_level"
    If one of them fails, return the name of parameter
    e.g., "name" if "name" is not 3-25 characters long
    or "is_vegetarian" if that field is not set to boolean.
    If all validations pass, return the dictionary with the dish fields
    correctly set to the parameters.
    '''
    # [ "burrito", "500", "12.90", "yes", "2" ]
    if len(dish_list) != 5:
        return len(dish_list)
    
    name = dish_list[0]
    if not is_valid_name(name):
        return("name", name)
    
    calories = dish_list[1]
    if not is_valid_calories(calories):
        return("calories", calories)
    
    price = dish_list[2]
    if not is_valid_price(price):
        return("price", price)
    
    is_vegetarian = dish_list[3]
    if not is_valid_is_vegetarian(is_vegetarian):
        return("is_vegetarian", is_vegetarian)
        
    spice_level = dish_list[4]
    if not is_valid_spicy_level(spice_level, spicy_scale_map):
        return("spicy_level", spice_level)
    
    # if everything is valid
    return {'name': name, 'calories': int(calories), 'price': float(price), 'is_vegetarian': is_vegetarian, 'spicy_level': int(spice_level)}

def print_dish(dish, spicy_scale_map, name_only=False):
    """
    param: dish (dict) - a dictionary object that is expected to contain the following keys:
            - "dish": dish's name
            - "calories": calories for this dish
            - "price": price of this dish
            - "is_vegetarian": boolean whether this dish is for vegetarian
            - "spicy_level": integer that represents the level of spiciness
    param: spicy_scale_map (dict) - a dictionary object that is expected
            to have the integer keys that correspond to the "level of spiciness."
            values for each corresponding key are string description of the
            level of spiciness
    param: name_only (Boolean) - by default, set to False.
            If True, then only the name of the dish is printed.
            Otherwise, displays the formatted restaurant menues.
    returns: None; only prints the restaurant menu item
    """
    spicy_scale_map = {
        1: "Not spicy",
        2: "Low key spicy",
        3: "Hot",
        4: "Diabolical"
        }
    
    name = dish['name'].upper()
    calories = dish['calories']
    price = dish['price']
    is_vegetarian = "yes" if dish["is_vegetarian"] else "no"
    spicy_level = dish['spicy_level']

    if name_only == True:
        print(name)
    else:
        print(name)
        print("* Calories:", int(calories))
        print(f"* Price: {float(price):.1f}")
        print("* Is it vegetarian:", is_vegetarian)
        print("* Spicy level:", spicy_scale_map[spicy_level])
        print()
        

def add_helper(restaurant_menu_list, spicy_scale_map):
    """
    param: restaurant_menu_list: list with dictionary of each dish in it
    param: spicy_scale_map: dictionary with numerical keys to indicate the level
    of spice

    the funtion helps add new dishes to the menu
    the input should be in particular order
    name
    calories
    is_vegetarian
    price
    spicy_level

    it checks if the length of result_dict is 5, if it's not it breaks the while loop
    next it checks the type of the return from get_new_menu_dish, it is dict it appends the
    restaurant_menu_list to add the new dish

    helper function:
    get_new_menu_dish
    print_dish
    """
    continue_action = 'y'
    while continue_action == 'y':
        print("::: Enter each required field, separated by commas.")
        # * `name` : name of the dish
        #     * `calories`: number of calories per serving
        #     * 'is_vegetarian' : if the item is vegetarian
        #     * `price` : price of the item
        #     * 'spicy_level' : 1 - 4
        print("::: name of the dish, calories, price, is it vegetarian ( yes | no ), spicy_level ( 1-4 )")
        dish_data = input("> ")  # TODO: get and process the data into a list
        dish_values = [value.strip() for value in dish_data.split(",")]
        result_dict = get_new_menu_dish(dish_values, spicy_scale_map)

        if len(dish_values) != 5:
            print("WARNING: invalid number of fields!")
            print(f"You provided {len(dish_values)} instead of the expected 5.")
            break
        
        if type(result_dict) == dict:
            restaurant_menu_list.append(result_dict)  # TODO: add a new dish to the list of dish menus
            print(f"Successfully added a new dish!")
            print_dish(result_dict, spicy_scale_map)
        elif type(result_dict) == int:
            print(f"WARNING: invalid number of fields!")
            print(f"You provided {result_dict}, instead of the expected 5.\n")
        else:
            print(f"WARNING: invalid dish field: {result_dict}\n")

        print("::: Would you like to add another dish?", end=" ")
        continue_action = input("Enter 'y' to continue.\n> ")
        continue_action = continue_action.lower()

def delete_dish(in_list, idx, start_idx=0):
    """
    param: in_list - a list from which to remove a dish
    param: idx (str) - a string that is expected to
            contain a representation of an integer index
            of a dish in the provided list
    param: start_idx (int) - by default, set to 0;
            an expected starting value for idx that
            gets subtracted from idx for 0-based indexing
    The function first checks if the input list is empty.
    The function then calls is_valid_index() to verify
    that the provided index idx is a valid positive
    index that can access an element from in_list.
    On success, the function saves the dish from in_list
    and returns it after it is deleted from in_list.
    returns:
    If the input list is empty, return 0.
    If idx is not of type string, return None.
    If is_valid_index() returns False, return -1.
    Otherwise, on success, the function returns the element
    that was just removed from the input list.
    Helper functions:
    - is_valid_index()
    """

    if len(in_list) == 0:
        return 0

    if type(idx) != str:
        return None

    valid_index = is_valid_index(idx, in_list, start_idx)
    if valid_index == False:
        return -1

    idx = int(idx) - start_idx
    item = in_list.pop(idx)
    return item

def delete_helper(restaurant_menu_list, spicy_scale_map):
    """
    prarm: restaurant_menu_list: list with dictionaries of each dish in it
    param: spicy_Scale_map: dict: numeric keys measureing the level of spice

    depending on the uder input it deletes the entire menu list or specific
    dish from the menu
    furthermore, it also checks if the user_option is yes to confirm deleting the list.

    helper function:
    print_restarurant_menu
    """
    continue_action = 'y'
    while continue_action == 'y':
        if not restaurant_menu_list:
            print("WARNING: There is nothing to delete!")
            break
        print("Which dish would you like to delete?")
        print("Press A to delete the entire menu for this restaurant, M to cancel this operation")
        print_restaurant_menu(restaurant_menu_list, spicy_scale_map, name_only=True, show_idx=True, start_idx=1)
        user_option = input("> ")
        if user_option == "A" or user_option == "a":
            print(f"::: WARNING! Are you sure you want to delete the entire menu ?")
            print("::: Type Yes to continue the deletion.")
            user_option = input("> ")
            if user_option == "Yes":
                restaurant_menu_list = []
                print(f"Deleted the entire menu.")
            else:
                print(f"You entered '{user_option}' instead of Yes.")
                print("Canceling the deletion of the entire menu.")
            break
        elif user_option == 'M' or user_option == 'm':
            break
        result = delete_dish(restaurant_menu_list, user_option, 1)
        if type(result) == dict:
            print("Success!")
            print(f"Deleted the dish |{result['name']}|")
        elif result == 0:  # delete_item() returned an error
            print("WARNING: There is nothing to delete.")
        elif result == -1:  # is_valid_index() returned False
            print(f"WARNING: |{user_option}| is an invalid dish number!")

        print("::: Would you like to delete another dish?", end=" ")
        continue_action = input("Enter 'y' to continue.\n> ")
        continue_action = continue_action.lower()
    return restaurant_menu_list

def save_menu_to_csv(restaurant_menu_list, filename):
    """
    param: restaurant_menu_list(list of dict) - The list shore dictionary of dishes 
    param: filename (str) - A string that ends with '.csv' which represents
               the name of the file to which to save the menu items. This file will
               be created if it is not present, otherwise, it will be overwritten.

    The function ensures that the last 4 characters of the filename are '.csv'.
    The function requires the `import csv` as well as `import os`.

    The function will use the `with` statement to open the file `filename`.
    After creating a csv writer object, the function uses a `for` loop
    to loop over every dishes dictionary in the dictionaries list and creates a new list
    containing only strings - this list is saved into the file by the csv writer
    object. The order of the elements in the dictionary is:
    * name
    * calories
    * price
    * is_vegetarian
    * spicy_level
    
    returns:
    -1 if the last 4 characters in `filename` are not '.csv'
    None if we are able to successfully write into `filename`
    """
    import csv
    import os

    if filename[-4:] != '.csv':
        return -1

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        for dish in restaurant_menu_list:
            new_dish = [dish['name'], dish['calories'], dish['price'], dish['is_vegetarian'], dish['spicy_level']]
            writer.writerow(new_dish)
    

def save_helper(restaurant_menu_list):
    """
    param: restaurant_menu_list: list with multiple dictionaries in it

    with the help of the save_menu_to_csv funtion this function
    checks if the user inputed filename ends with .csv
    if it does, it calls the save_menu_to_csv function to save the
    data in the given filename

    helper function:
    save_menu_to_csv
    """
    continue_action = 'y'
    while continue_action == 'y':
        print("You selected option S to > Save the data to file.")
        print("::: Enter the filename ending with '.csv'.")
        filename = input("> ")
        result = save_menu_to_csv(restaurant_menu_list, filename)  # TODO: Call the function with appropriate inputs and capture the output
        if result == -1:  # TODO
            print(f"WARNING: |{filename}| is an invalid file name!")  # TODO
            print("::: Would you like to try again?", end=" ")
            continue_action = input("Enter 'y' to try again.\n> ")
        else:
            print(f"Successfully saved restaurant menu to |{filename}|")
            break

def load_menu_from_csv(filename, restaurant_menu_list, spicy_scale_map):
    """
    param: filename (str) - the name of the file from which to read the contents.
    param: restaurant_menu_list (list) - A list of dish dictionary objects to which
            the dishes read from the provided filename are appended.
            If restaurant_menu_list is not empty, the existing menu items are not deleted.
    param: spicy_scale_map (dict) - a dictionary that contains the mapping
            between the integer priority value (key) to its representation
            (e.g., key 1 might map to the spicy value "Not Spicy" or "Low")
            Needed by the helper function (see below).

    The function ensures that the last 4 characters of the filename are '.csv'.
    The function requires the `import csv` (for csv.reader()) and `import os`
    (for `os.path.exists()).

    If the file exists, the function will use the `with` statement to open the
    `filename` in read mode.
    For each row in the csv file, the function will count each row (1-based counting) and
    proceed to create a new restaurant menu item using the `get_new_menu_dish()` function.
    - If the function `get_new_menu_dish()` returns a valid dish object (dictionary),
    it gets appended to the end of the `in_list`.
    - If the `get_new_menu_dish()` function returns an error, the 1-based
    row index gets recorded and added to the NEW list that is returned.
    E.g., if the file has a single row, and that row has invalid dish data,
    the function would return [1] to indicate that the first row caused an
    error; in this case, the `in_list` would not be modified.
    If there is more than one invalid row, they get excluded from the
    in_list and their indices are appended to the new list that's returned.

    returns:
    * -1, if the last 4 characters in `filename` are not '.csv'
    * None, if `filename` does not exist.
    * A new empty list, if the entire file is successfully read into the `in_list`.
    * A list that records the 1-based index of invalid rows detected when
      calling get_new_menu_dish().

    Helper functions:
    - get_new_menu_dish()    
    """
    import csv
    import os
    
    if not filename[-4:] == '.csv':
        return -1
    
    if not os.path.exists(filename):
        return None
    
    invalid_rows = []
    
    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file)
        
        for idx, row in enumerate(reader, start=1):
            new_menu = get_new_menu_dish(row, spicy_scale_map)
            
            if type(new_menu) == dict:
                restaurant_menu_list.append(new_menu)
            else:
                invalid_rows.append(idx)
            
    if invalid_rows != []:
        return invalid_rows
    else:
        return invalid_rows


def load_helper(restaurant_menu_list, spicy_scale_map):
    """
    param: restaurant_menu_list: list with dictionaries in it
    param: spicy_scale_map: dictionary with numeric keys refering to the level
    of spice

    The function checks if the data in the given exists in a file

    depending on the returned value of the load_menu_from_csv, the
    function prints appropriate output

    helper function:
    load_menu_from_csv
    """
    continue_action = 'y'
    while continue_action == 'y':
        print("::: Enter the filename ending with '.csv'.")
        filename = input("> ")
        result = load_menu_from_csv(filename, restaurant_menu_list, spicy_scale_map)
        # TODO: Call the function with appropriate inputs and capture the output
        if type(result) == list and len(result) != 0:
            print(f"WARNING: |{filename}| contains invalid data!")
            print(f"The following rows from the file were not loaded:")
            for row in result:
                print(row)
            print("::: Would you like to try again?", end=" ")
            continue_action = input("Enter 'y' to try again.\n> ")
        elif result == -1:  # TODO
            print(f"WARNING: |{filename}| is an invalid file name!")  # TODO
            print("::: Would you like to try again?", end=" ")
            continue_action = input("Enter 'y' to try again.\n> ")
        elif result == None:
            print(f"WARNING: |{filename}| was not found!")
            print("::: Would you like to try again?", end=" ")
            continue_action = input("Enter 'y' to try again.\n> ")
        else:
            print(f"Successfully saved restaurant menu to |{filename}|")
            return result

def is_valid_index(idx, in_list, start_idx=0):
    """
    param: idx (str) - a string that is expected to
            contain an integer index to validate
    param: in_list - a list that the idx indexes
    param: start_idx (int) - by default, set to 0;
            an expected starting value for idx that
            gets subtracted from idx for 0-based indexing

    The function checks if the input string contains
    only digits and verifies that (idx - start_idx) is >= 0,
    which allows to retrieve an element from in_list.

    returns:
    - True, if idx is a numeric index >= start_idx
    that can retrieve an element from in_list.
    - False if idx is not a string that represents an
    integer value, if int(idx) is < start_idx,
    or if it exceeds the size of in_list.
    """
    if type(idx) == int:
        return False
    
    idx = str(idx)

    if not idx.isdigit():
        return False

    idx = int(idx) - start_idx

    if idx < 0 or idx >= len(in_list):
        return False
    else:
        return True
    

def update_menu_dish(restaurant_menu_list, idx, spicy_scale_map, field_key, field_info, start_idx=0):
    """
    param: restaurant_menu_list (list) - a menu that contains
            a list of dishes
    param: idx (str) - a string that is expected to contain an integer
            index of a restaurant in the input list
    param: spicy_scale_map (dict) - a dictionary that contains the mapping
            between the integer spiciness value (key) to its representation
            (e.g., key 1 might map to the priority value "non spicy")
            Needed if "field_key" is "priority" to validate its value.
    param: field_key (string) - a text expected to contain the name
            of a key in the info_list[idx] dictionary whose value needs to
            be updated with the value from field_info
    param: field_info (string) - a text expected to contain the value
            to validate and with which to update the dictionary field
            info_list[idx][field_key]. The string gets stripped of the
            whitespace and gets converted to the correct type, depending
            on the expected type of the field_key.
    param: start_idx (int) - by default, set to 0;
            an expected starting value for idx that
            gets subtracted from idx for 0-based indexing
    The function first calls one of its helper functions
    to validate the idx and the provided field.
    If validation succeeds, the function proceeds with the update.
    return:
    If info_list is empty, return 0.
    If the idx is invalid, return -1.
    If the field_key is invalid, return -2.
    If validation passes, return the dictionary info_list[idx].
    Otherwise, return the field_key.
    Helper functions:
    The function calls the following helper functions:
    - is_valid_index()
    Depending on the field_key, it also calls:
     - is_valid_name()
     - is_valid_calories()
     - is_valid_price()
     - is_valid_is_vegetarian()
     - is_valid_spicy_level()
    """

    if restaurant_menu_list == []:
        return 0

    if not is_valid_index(idx, restaurant_menu_list, start_idx):
        return -1

    idx = int(idx)
    idx -= start_idx
    
    if field_key not in restaurant_menu_list[idx]:
        return -2


    if field_key == 'name':
        if not is_valid_name(field_info):
            return field_key
        restaurant_menu_list[idx][field_key] = field_info

    elif field_key == 'calories':
        if not is_valid_calories(field_info):
            return field_key
        restaurant_menu_list[idx][field_key] = int(field_info)

    elif field_key == 'price':
        if not is_valid_price(field_info):
            return field_key
        restaurant_menu_list[idx][field_key] = float(field_info)

    elif field_key == 'is_vegetarian':
        if not is_valid_is_vegetarian(field_info):
            return field_key
        restaurant_menu_list[idx][field_key] = field_info

    elif field_key == 'spicy_level':
        if not is_valid_spicy_level(field_info, spicy_scale_map):
            return field_key
        restaurant_menu_list[idx][field_key] = int(field_info)

    return restaurant_menu_list[idx]
    
def update_helper(restaurant_menu_list, spicy_scale_map):
    """
    param: restaurant_menu_list: list with dictionaries for each dish
    param: spicy_Scale_map: dictionary with numeric keys to indicate the level of spice

    this function helps us update the restaurant_menu_list depending on the
    user_option. If they want to change the calories or the spice level
    or any other element of the restaurant menu list, they can do it
    using this function
    
    helper functions:
    print_restaurant_menu
    is_valid_index
    get_selection
    update_menu_dish
    print_dish
    """
    continue_action = 'y'
    while continue_action == 'y':
        if len(restaurant_menu_list) == 0: #TODO
            print("WARNING: There is nothing to update!")
            break
        print("::: Which dish would you like to update?")
        print_restaurant_menu(restaurant_menu_list, spicy_scale_map, name_only=True, show_idx=True, start_idx=1)
        print("::: Enter the number corresponding to the dish.")
        user_option = input("> ")
        if is_valid_index(user_option, restaurant_menu_list): #TODO - check to see if the number is valid
            dish_idx = int(user_option) - 1
            subopt = get_selection("update", restaurant_menu_list[dish_idx], to_upper=False, go_back=True)
            if subopt == 'M' or subopt == 'm':  # if the user changed their mind
                break
            print(f"::: Enter a new value for the field |{subopt}|") # TODO
            field_info = input("> ")
            result = update_menu_dish(restaurant_menu_list, dish_idx, spicy_scale_map, subopt, field_info) #TODO
            if type(result) == dict:
                print(f"Successfully updated the field |{subopt}|:") # TODO
                print_dish(result, spicy_scale_map)  # TODO
            else:  # update_menu_dish() returned an error
                print(f"WARNING: invalid information for the field |{subopt}|!") # TODO
                print(f"The menu was not updated.")
        else:  # is_valid_index() returned False
            print(f"WARNING: |{user_option}| is an invalid dish number!") # TODO

        print("::: Would you like to update another menu dish?", end=" ")
        continue_action = input("Enter 'y' to continue.\n> ")
        continue_action = continue_action.lower()
        # ---------------------------------------------------------------

def get_restaurant_expense_rating(restaurant_menu_list):
    """
    param: restaurant_menu_list - a list of restaurants and their dishes (list of dicts)
    
    Computes the average price of all the items on the menu and display the expense rating of the restaurant.
    average_price < 10 -> Expense rating is : $
    10 <= average_price < 20 -> Expense rating is : $$
    average_price >= 20: Expense rating is : $$$
    
    returns: the average price of the items as a float
    """

    prices = []

    for dish in restaurant_menu_list:
        if 'price' in dish:
            prices.append(dish['price'])

    avg_price = sum(prices) / len(prices)

    if avg_price < 10:
        expense_rating = '$'
    elif 10 <= avg_price < 20:
        expense_rating = '$$'
    elif avg_price >= 20:
        expense_rating = '$$$'

    print(f"Expense rating is : {expense_rating}")
    print()
    return float(avg_price)
