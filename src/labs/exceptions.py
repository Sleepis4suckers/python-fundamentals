""" Exceptions Lab Homework - Leap Year """


def leap_year_lab(year: int):
    greeting = input('check if a year is a leap year \nPress enter')
    year = int(input('Please input year in question.'))
    # if year >= 1000:
    if year >= 1000:
        if year % 400 == 0 and year % 100 == 0:
            print(f'{year} is a leap year.')
        elif year % 4 == 0 and year % 100 != 0:
            print(f' {year} is a leap year.')
        else:
            print(f'{year} is not a leap year')
    else:
        print('Please enter a 4 digit number.')


if __name__ == '__main__':
    leap_year_lab(2000)
    