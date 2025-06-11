my_string = 'Pizza con piña'

index_string = len(my_string) - 1

#usando while

while (index_string >= 0):
    print(my_string[index_string])
    index_string = index_string - 1


#usando for y range

contador = len(my_string)-1
for letra in range (0,len(my_string)):
    print(my_string[contador])
    contador = contador - 1

