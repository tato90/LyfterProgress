my_list=[]


cantidad_valores = int (input('Ingrese la cantidad de valores a ingresar: '))
contador = 0
while (contador<cantidad_valores):
    valor_ingresado = (input('Ingrese un valor: '))
    my_list.append(valor_ingresado)
    contador = contador + 1

print (my_list) 

print('Vamos a reemplazar el ultimo numero con el primero')

my_list.insert(0,my_list[len(my_list)-1])
my_list.append(my_list[1])
my_list.pop(1)
my_list.pop(len(my_list)-2)
print(my_list)
