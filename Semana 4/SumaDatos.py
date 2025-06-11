

nombre_usuario =  (input ('Ingrese su nombre: '))
apellido_usuario = (input ('Ingrese su apellido: '))
edad_usuario = int (input ('Ingrese su edad: '))
info_list = [nombre_usuario,apellido_usuario,edad_usuario]


if (edad_usuario>=18):
    mayor_edad = True
else:
    mayor_edad = False

print(f'Su nombre es {nombre_usuario} {apellido_usuario}')
print(f'Es usted mayor de edad? {mayor_edad}')



valor = int (input ('Ingrese el valor para ver el dato, 0 para nombre, 1 para apellido y 2 para la edad: '))

if (valor==0):
    print(info_list[0])
elif (valor==1):
    print(info_list[1])
elif (valor==2):
    print(info_list[2])


#Prueba string + string 

print('Su nombres es: ' + nombre_usuario + ' ' + apellido_usuario)

#Prueba string + int = Falla porq no se puede sumar int + string

#print('Su nombre y edad es: ' + nombre_usuario + edad_usuario)

#Prueba list + list 

print('Su nombre es: ' + info_list[0] + info_list[1])

#Prueba str + list 

print(nombre_usuario + info_list[1])

#Prueba float + int = realiza una suma ya que ambos son numeros

altura = 1.76
print(altura + edad_usuario)

#bool + bool = true + true = 2, true + false = 1, false + false = 0
mi_variable = False

print(mayor_edad + mi_variable )
