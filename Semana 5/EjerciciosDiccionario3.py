list_of_keys = ['access_level','age']
employee = {'name':'John','email':'john@ecorp.com','access_level':5,'age':28}


for index in list_of_keys:
    for key, value in list(employee.items()):
        if (index==key):
            employee.pop(key)

print(employee)