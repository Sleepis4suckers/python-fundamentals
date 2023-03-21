""" Lesson 6 - Control Flow Statements """

alpha = 0
beta = 42
charlie = None
delta = 0.0j

def example_bool():
    print(bool(alpha))
    print(bool(beta))
    print(type(charlie))
    print(bool(delta))




# example_bool()


def example_if(num):
    """ The basic if statement block will evaluate
    the condition. A true condition will execute
    the block of code inside the if statement.
    """
    print('Before if statement')
    if num >= 15:
        print('The value is 15 or higher')
    print('After if statement')


# example_if(10)


def basic_bool_if(value):
    """ A function can be used with an if statement
    as long as it returns True or False.
    """
    print('Before if statement')
    if(bool(value)):
        print('This value is True')
    print('After if statement')



# basic_bool_if(beta)

def basic_else(score: int) -> str:
    """ The else statement will execute when the if
    condition is false."""
    if score >= 10:
        return 'Score is 10 or higher'
    else:
        return 'Score is less than 10'


# print(basic_else(12))


def basic_elif(value2: int):
    """ This elif statement is used to chain
    if statements that are related to each other.
    """
    if value2 == beta:
        print('value is 42')
    elif value2 < beta:
        print('value is less than 42')


# basic_elif(40)


def basic_elif_else(num3: int):
    if num3 == 10:
        print('value is 10')
    elif num3 < 10:
        print('value is less than 10')
    else:
        print('value is greater than 10')


# basic_elif_else(10)


def basic_elif_chain(val):
    if val <= 50:
        print('value is less than 50')
    elif val <= 60:
        print('value is less than 60')
    elif val <= 70:
        print('value is less than 70')
    else:
        print('value is greater than 70')


# basic_elif_chain(51)


def basic_nested(num: int):
    """ You can nest if statements inside other
    if dtatements. The inner if will only be
    evaluated if the outer if statement is true.
    """
    total = 0
    if num < beta:
        if num < 15:
            total = num + beta
        else:
            total = num * beta
    else:
        total = num - beta
    print(total)


# basic_nested(10)


def basic_ternary(num1: int, num2: int) -> int:
    """ A ternary statement that checks a basic
    if and else evaluation. It is best used
    for simplified use cases.
    """
    return num1 if (num1 >num2) else num2


my_value = basic_ternary(10, 7)
# print(my_value)


def ternary_if_chain(num3: int, num4: int) -> str:
    """ This version of a ternary uses an if else chain.
    This style can be difficult to read when there is alot
    of data to evaluate.
    """
    return 'both num3 and num4 are equal' if (num3 == num4) else \
        'num3 is greater than num4' if (num3 > num4) else \
        'num3 is greater than num4'


# print(ternary_if_chain(10, 7))


def basic_logical_and():
    """ The logical and keyword when used with if statements,
    allows you to compare multiple operator conditions. each operator condition
    must evaluate to true, in order for the whole
    if statement to be true
    """
    apple, pear, grape = 10, 15, 5
    if apple < pear and grape < pear:
        print('pear is the high number')


# basic_logical_and()


def basic_logical_or(value1: int, value2: int) -> str:
    """ The logical or keyword when used with if statements
    allows you to compare multiple operator conditions.
    Only one operator condition has to be true for the whole
    if statement to be true.
    """

    if value1 > 5 or value2 < 20:
        return 'value 1 is greater than 5 or value2 is less than 20'
    else:
        return 'value1 is not greater than 5 and value2 is greater than 20'


print(basic_logical_or(14, 15))
