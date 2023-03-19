# Task 1:
def pemdas_order():
    """ Operations Assignment with 10 + 32 * 12 / 3 using PEMDAS """
    pem1 = 10 + (32 * 12) / 3
    pem2 = (10 + 32) * 12 / 3
    print(f" {pem1}, {pem2} ")


pemdas_order()



# Task 2:
def arguments_op(value1, value2):
    """ Task 2 Writing a functions using 2 arguments"""
    print(f"Value1 before {value1}")
    value1 += value2
    print(f"Value1 after + {value1}")
    value1 %= value2
    print(f"Value1 after % {value1}")
    value1 *= value2
    print(f"Value1 after * { value1}")


arguments_op(13, 6)



# Task 3:
def argument2_op(value1, value2):
    """ Task 3 Writing a function using 2 arguments """
    print(f'{value1} == {value2} = {value1 == value2}')
    print(f'{value1} != {value2} = {value1 != value2}')
    print(f'{value1} >= {value2} = {value1 >= value2}')


argument2_op(13, 6)