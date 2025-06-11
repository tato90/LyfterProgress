my_list=[]


cantidad_valores = int (input('Ingrese la cantidad de valores a ingresar: '))
contador = 0
while (contador<cantidad_valores):
    valor_ingresado = int (input('Ingrese un valor: '))
    my_list.append(valor_ingresado)
    contador = contador + 1

print('Vamos a eliminar los numeros impares')

contador = 0
while (contador<len(my_list)):
    if (my_list[contador]%2 != 0):
        my_list.pop(contador)
        contador = contador + 1
    else:
        contador = contador + 1

print(my_list)

