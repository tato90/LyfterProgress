def sum_list():
    numbers = [10, 20, 30, 40, 50]
    total = 0
    for num in numbers:
        total = total + num
    print("The sum of the numbers is:", total)

sum_list()

def sum_list_b(my_list):
    my_list=[1,2,3,4,5]
    return sum(my_list)

sum_list_b()