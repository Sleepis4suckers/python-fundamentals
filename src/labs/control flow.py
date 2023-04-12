# Task1
""" if_else using str"""

def if_else_lab_str(grade: int) -> str:
    if grade == 100:
        return 'Grade is equal to 100'
    else:
        return 'Grade is not equal to 100'

# print(if_else_lab_str(80))


""" if_else using int"""
def if_else_lab_num(grade: int):
    if grade == 100:
        print('100')
    else:
        print('0')

# print(if_else_lab_num(25))




# Task2


def if_else_elif_grade(grade: int) -> str:
    if grade >= 100:
        print('Excellent')
    elif grade >= 85:
        print('Very good')
    elif grade >= 75:
        print('Good')
    elif grade <= 60:
        print('Average')
    else:
        print('Not A valid Grade')


print(if_else_elif_grade(50))
