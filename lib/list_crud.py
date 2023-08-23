def create_an_empty_list():
    return []

def create_a_list():
    new_list = [1, 2, 3, 4]  # Replace these elements with your desired elements
    return new_list

def add_element_to_end_of_list(lst, element):
    lst.append(element)
    return lst


def add_element_to_start_of_list(lst, element):
    lst.insert(0, element)
    return lst

def remove_element_from_end_of_list(lst):
    lst.pop()
    return lst

def remove_element_from_start_of_list(lst):
    del lst[0]
    return lst

def retrieve_first_element_from_list(input_list):
    return input_list[0]

def retrieve_element_from_index(input_list, index):
    return input_list[index]

def retrieve_last_element_from_list(input_list):
    return input_list[-1]

empty_list = create_an_empty_list()
print(empty_list)

my_list = create_a_list()
print(my_list)

add_element_to_end_of_list(my_list, 5)
print(my_list)

add_element_to_start_of_list(my_list, 0)
print(my_list)

remove_element_from_end_of_list(my_list)
print(my_list)

remove_element_from_start_of_list(my_list)
print(my_list)

first_element = retrieve_first_element_from_list(my_list)
print(first_element)

element_at_index = retrieve_element_from_index(my_list, 1)
print(element_at_index)

last_element = retrieve_last_element_from_list(my_list)
print(last_element)
