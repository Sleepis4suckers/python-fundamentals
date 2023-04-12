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


def grading_score(grade: str):
    if grade.upper() == 'A':
        print('Excellent')
    elif grade.upper() == 'B':
        print('Very Good')
    elif grade.upper() == 'C':
        print('Average')
    else:
        print('Failed')


grading_score('b')
