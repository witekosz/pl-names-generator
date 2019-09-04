from random import randint
from data_names import (
    FIRST_NAMES_F,
    FIRST_NAMES_M,
    LAST_NAMES_F,
    LAST_NAMES_M
)


def generate_people(number=25, gender='M'):
    """
    Function for generating people
    
    :param int number: Number of names to generate
    :param str recipient: Gender of names to generate (M, F, X)
    :return: list of names
    :rtype: list
    """

    if gender == 'M':
        list_first_names = FIRST_NAMES_M
        list_second_names = LAST_NAMES_M
    elif gender == 'F':
        list_first_names = FIRST_NAMES_F
        list_second_names = LAST_NAMES_F
    else:
        return "Provide valid gender type!"

    names_list = []
    for e in range(number):
        
        temp_name = list_first_names[randint(0, len(list_first_names)-1)]
        temp_surname = list_second_names[randint(0, len(list_second_names)-1)]
        temp_person = f"{temp_name} {temp_surname}"

        names_list.append(temp_person)
    
    return names_list
