def day_list_comprehension():
    numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
    numbers_filter_negative = [i for i in numbers if i <= 0]
    print(numbers_filter_negative)

    list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
    list_unidimensional = [z for x in list_of_lists for y in x for z in y]
    print(list_unidimensional)


    list_of_tuple = [(x, 1, x**1, x**2, x**3, x**4) for x in range(11)]
    print(list_of_tuple)

    countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
    country_list = [[y[0].upper(), y[0][0:3].upper(), y[1].upper()] for x in countries for y in x]
    print(country_list)

    countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
    country_dict = [{"country":y[0] , "city":y[1] } for x in countries for y in x]
    print(country_dict)

    names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
    list_concatenated_names = [f"{y[0]} {y[1]}" for x in names for y in x]
    print(list_concatenated_names)

    


if __name__ == "__main__":
    day_list_comprehension()