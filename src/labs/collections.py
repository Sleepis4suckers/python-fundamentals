# Task 1
""" Collections Homework """


pizzas = ['cheese', 'mushroom', 'four cheeses', 'basil', 'arugula & pear']

def fav_pizza_types():
    for pizza in pizzas:
        print(pizza)

fav_pizza_types()


def pizza_append_type():
    pizzas.append('margarita')
    for pizza in pizzas:
        print(pizzas)

pizza_append_type()


def pizza_append_type():
    pizzas.append('white truffle')
    for pizza in pizzas:
        print(pizzas)

pizza_append_type()





# Task 2
""" Just some of My Favorite Movies """

fav_movies = {1987: 'Wall Street', 2002: 'The Count of Monte Cristo', 2009: 'Public Enemies',
              2015: 'The Big Short', 2017: 'Papillon'}



def movie_year_keys():
    for key in fav_movies:
        print(key)


movie_year_keys()



def movie_values():
    """ Getting the values using bracket notation. [] from the key."""
    for movie in fav_movies:
        print(fav_movies[movie])


movie_values()

