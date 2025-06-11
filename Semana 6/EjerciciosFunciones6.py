def ordena_strings (): 
    my_string = input('Ingrese sus string separados de guion: ')
    my_list= my_string.split("-")
    #print(my_list)
    my_sorted_list = sorted(my_list)
    #print(my_sorted_list)
    my_new_string= list(map(str, my_sorted_list))
    delimeter_hiphen='-'
    print(delimeter_hiphen.join(my_new_string))


ordena_strings()