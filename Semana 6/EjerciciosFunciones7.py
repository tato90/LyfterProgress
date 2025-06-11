def determina_primo ():
    my_list = []
    my_prime_list = []
    my_list_len = int (input('Ingrese la cantidad de numeros que desea analizar: '))
    for number in range (0,my_list_len):
        number = int (input('Ingrese un numero: '))
        my_list.append(number)
    for number in my_list:
         if number > 1:
            if number % 1 == 0:
                    my_prime_list.append(number)   
    print (my_prime_list)                

determina_primo()

