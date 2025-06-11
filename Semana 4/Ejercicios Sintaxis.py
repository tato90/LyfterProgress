nombre = str (input ('Ingrese su nombre : '))
apellido_usuario = str (input ('Ingrese su apellido: '))
edad_usuario = int (input ('Ingrese su edad: '))


if (edad_usuario>18):
    categoria = 'Adulto'
elif (edad_usuario<18):
    categoria = 'Menor de edad'
print (f'Hola {nombre} {apellido_usuario}, su edad es {edad_usuario}, su categoria es {categoria}')

import random
numero_suerte = random.randint(0,10)
numero_usuario = int (input('Ingrese su numero: '))
while(numero_suerte!=numero_usuario):
    print ('Intente de nuevo ')
    numero_usuario = int (input('Ingrese su numero: '))
if(numero_suerte==numero_usuario):
    print ('Numero acertado ')
    

print ('Ahora probaremos cual es el mayor numero de 3')
numero_uno = int (input('Ingrese su primer numero: '))
numero_dos= int (input('Ingrese su segundo numero: '))
numero_tres = int (input('Ingrese su tercer numero: '))

if(numero_uno>numero_dos and numero_uno>numero_tres):
    print ('El mayor es el primer numero')
if(numero_dos>numero_tres and numero_dos>numero_uno):
    print ('El mayor es el segundo numero')
if(numero_tres>numero_dos and numero_tres>numero_uno):
    print ('El mayor es el tercer numero')

print ('Comenzaremos con sus notas')
cantidad_notas = int (input('Ingrese su cantidad de notas: '))
contador = 0
cantidad_aprobadas = 0
cantidad_desaprobadas = 0
suma_aprobadas = 0
suma_desaprobadas = 0
promedio_aprobadas = 0
promedio_desaprobadas = 0
while (contador<cantidad_notas):
    nota = int(input('Ingrese su nota: '))
    if (nota>=70):
        cantidad_aprobadas = cantidad_aprobadas + 1
        suma_aprobadas = suma_aprobadas + nota
        promedio_aprobadas = suma_aprobadas/cantidad_aprobadas
        contador = contador + 1
    if (nota<70):
        cantidad_desaprobadas = cantidad_desaprobadas + 1
        suma_desaprobadas = suma_desaprobadas + nota
        promedio_desaprobadas = suma_desaprobadas/cantidad_desaprobadas
        contador = contador + 1

print (f'Su cantidad de notas aprobadas es {cantidad_aprobadas}')
print (f'El promedio de aprobadas es  {promedio_aprobadas}')
print (f'Su cantidad de notas desaprobadas es {cantidad_desaprobadas}')
print (f'El promedio de desaprobadas es {promedio_desaprobadas}')
print (f'El promedio de todas es {(suma_aprobadas+suma_desaprobadas)/cantidad_notas}')

