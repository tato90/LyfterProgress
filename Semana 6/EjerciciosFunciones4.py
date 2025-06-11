def print_viceversa():
    my_string = input(str('Ingrese su frase: '))
    index_string = len(my_string) - 1
    while (index_string >= 0):
        print(my_string[index_string])
        index_string = index_string - 1

print_viceversa()