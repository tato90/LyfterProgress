



nombre_hotel = (input('Ingrese el nombre del hotel: '))
numero_habitacion = int (input('Ingrese el numero de habitacion que desea ver: '))


hotel = {
        'nombre':nombre_hotel,
        'estrellas':'4',
        'habitaciones': [
            {
            'numero': 1,
            'piso':'1',
            'precio_por_noche': '100$',
            } ,
            {
            'numero': 2,
            'piso':'2',
            'precio_por_noche': '200$',
            } ,
            {
            'numero': 3,
            'piso': '3',
            'precio_por_noche': '300$',
            },
        ]
    }


for key, value in hotel.items():
    if (key == 'numero' and value == numero_habitacion):
        print(nombre_hotel)
  

