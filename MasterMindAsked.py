# The definition of ALL_COLORS is repeated here. That repetition can
# be avoided, but it would lead us to far at this point.
ALL_COLORS = ("red", "green", "blue", "yellow", "orange", "white")
from random import *

def get_nb_black_white_matches(given, guess):
    """ Return the number of black and white matches of the guessed
    combination with respect to the given combination. The first
    element in the resulting tuple reflects the number of correct colors
    on their positions (black matches). The second element reflects
    the number of correct colors not on their position (white matches)."""
#return (number of correct colors on position, number of correct colors on wrong position)
    black_matches = 0
    white_matches = 0
    memory = []

    for i in range(0, 4):
        if given[i] == guess[i]:
            memory.append(i)
            black_matches += 1
        for k in range(0, 4):
            if given[i] == guess[k] and i != k and k not in memory:
                white_matches += 1
                memory.append(k)
    return black_matches, white_matches

def create_combination(nb_elements):
    """ Return a random combination involving the number of elements."""
    color = []
    for k in range(0, nb_elements):
        random_number = randint(0, len(ALL_COLORS)-1)
        color.append(ALL_COLORS[random_number])
    return color



# ! on the board, each row will consist of 4 circles representing 1 guess
# ! in total 10 rows should be drawn (as the user is given 10 guesses)
# ! You can create a circle by using the function:
# !     canvas.create_oval(x0, y0, x1, y1)
# ! It takes two pairs of coordinates: the top left and bottom right
# ! corners of the bounding rectangle. The (0,0) point is located in the
# ! top left corner of the canvas. We assume that each bounding square has
# ! a size of 30x30 and that all the circles are separated by 10 pixels
# ! from each other, and from the border (see picture in assignment).
# ! For example, the method call (with actual parameters) that generates
# ! the second circle of the third guess will look like:
# !         canvas.create_oval(50, 90, 80, 120)
# ! Later on in the program we modify the ovals to change color depending on
# ! the color that is selected by the person playing.
# ! In order to easily retrieve the correct oval, we expect that the function
# ! you implement here returns a nested list (i.e. a matrix) of
# ! the following form:
# !         [[circle1_guess1, circle2_guess1, ...],
# !          [circle1_guess2, ...],
# !          ...,
# !          [circle4_guess10]]
# ! The second circle of the third guess would for example be stored at:
# !          ovals[2][1] = canvas.create_oval(50, 90, 80, 120)
# ! Instead of approaching the nested list as a matrix, you can also
# ! treat it as a list of lists
# !          e.g. ovals[2].append(...)
# ! Note that the method create_oval has an implementation that
# ! takes 5 parameters. The fifth parameter has name 'fill' and allows
# ! you to assign a color (as a string) to it.
# ! Make sure that all the circles you draw get the fill color "grey".
def create_empty_circles(canvas, number_of_circles, max_number_of_moves):
    """ Return a matrix containing grey ovals that are correctly initialized
        at their required location."""
    ovals = []
    for i in range (0,max_number_of_moves):
        ovals.append([0]*number_of_circles)

    for i in range(0, max_number_of_moves):
        for k in range(0, 4):
            x0 = 10 + 40 * k
            y0 = 10 + 40 * i
            x1 = 40 + 40 * k
            y1 = 40 + 40 * i
            circle = canvas.create_oval(x0, y0, x1, y1, fill = "grey")
            ovals[i][k] = circle
    return ovals
###############################################################################
# EXTRA

def any_color_in_combination(colors, given):
    """ Returns true if at least one color in colors is part of the
    given combination. False otherwise."""
    matches = 0
    for k in range(0,len(given)):
        for i in range(0,len(colors)):
            if colors[i] == given[k]:
                matches += 1

    if matches > 0:
        return True
    else:
        return False

def all_colors_in_combination(colors, given):
    """ Returns true if all the colors in colors are part of the
    given combination. False otherwise."""
    check = [0, 0, 0, 0]
    for k in range(0,4):
        for i in range(0,4):
            if colors[i] == given[k]:
                check[k] = 1
    if check == [1, 1, 1, 1]:
        return True
    else:
        return False

def is_sublist_of(sublist, given):
    """ Returns whether the sublist is part of the given combination.
    The order of the sublist must also correspond to the order of the
    corresponding part in the given combination."""

    for i in range(0, len(given)):
        for k in range(0, len(sublist)):
            if given[i+k] == sublist[k]:
                return True
    return False



