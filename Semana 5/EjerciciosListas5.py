my_list=[]


cantidad_valores = 10
contador = 0
while (contador<cantidad_valores):
    valor_ingresado = int (input('Ingrese un valor: '))
    my_list.append(valor_ingresado)
    contador = contador + 1

print(my_list)

contador = 0

for numero in my_list:
    mayor = max(my_list)
print(mayor)

