def negative_filter():
    numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
    numbers_filter = [i for i in numbers if i <= 0]
    print(numbers_filter)

def one_dimensional_list():
    list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
    one_dimensional = [z for x in list_of_lists for y in x for z in y]
    print(one_dimensional)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

def flatten_list():
    output = [[name.upper(), name[:3].upper(), capital.upper()] for country in countries for name, capital in country]
    print(output)

def dict_list():
    output = [{"country": name.upper(), "city": capital.upper()} for country in countries for name, capital in country]
    print(output)

def list_of_concatenated_strings():
    names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
    output = [f"{name} {lastname}" for n in names for name, lastname in n]
    print(output)

linear_function = lambda x, m, b: m*x+b

if __name__ == "__main__":

    list_of_concatenated_strings()