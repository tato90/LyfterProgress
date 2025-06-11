def determine_uper_and_lower_case ():
    my_string = str (input('Ingrese su string: '))
    upper = 0
    lower = 0
    for value in my_string:
        if (value.isupper()):
            upper = upper + 1 
        else:
            lower = lower + 1
    
    print('Lower: ',lower)
    print('Upper: ',upper)

determine_uper_and_lower_case()

