#By Cody Sperling
#there are 2 disasters, each turn each of them have a 5% chance of spawning



#Importing libraries

import numpy
import time
import os
import random



#creating matrix size of user choice and defining global variables


revenue = 0
population_total = 0

try:
    size = int(input("Input a size of the matrix: "))

except:
    print("type a number")
    size = int(input("Input a size of the matrix: "))

landscape = numpy.full((size,size),"\033[32;42m.")



#printing matrix


def print_matrix(landscape,population_total,revenue):
    os.system("cls")
    for column in range(len(landscape)):
        for row in range(len(landscape[column])):
            print(landscape[column][row],end="")
        print("\033[37m")
    print(f"\033[40mYour town's population is {population_total}") 
    print(f"Your town's revenue is {revenue}")


#disaster 1
def tornado(landscape,population_total,revenue):
#random spawn for tornado
    path = random.randint(0,size-2)
    increment = 0


    while increment+1 <= size-1:

#checks if tornado will hit a store or house and updates variables
        if landscape[path][increment+1] == "\033[32;40m$":
            revenue = sub_revenue(revenue)


        elif landscape[path][increment+1] == "\033[31;47m#":
            population_total = sub_pop(population_total)
#keeps population from being negative
            if population_total < 0:
                population_total = 0

        if landscape[path+1][increment+1] == "\033[32;40m$":
            revenue = sub_revenue(revenue)


        elif landscape[path][increment+1] == "\033[31;47m#":
            population_total = sub_pop(population_total)
            if population_total < 0:
                population_total = 0

        print_matrix(landscape,population_total,revenue)
        print("Oh no there is a tornado!")
        time.sleep(.5)
        os.system("cls")
#updates tornados next position
        landscape[path][increment] = "\033[90;42m@"
        landscape[path+1][increment] = "\033[90;42m@"
        landscape[path+1][increment+1] = "\033[90;42m@"
        landscape[path][increment+1] = "\033[90;42m@"
#updates the spot behind the tornado
        if increment > 0:
            landscape[path][increment-1] = "\033[32;42m."
            landscape[path+1][increment-1] = "\033[32;42m."
#tells tornado where to stop
        if increment == (size-2):
            
            landscape[path][increment] = "\033[32;42m."
            landscape[path+1][increment] = "\033[32;42m."
            landscape[path+1][increment+1] = "\033[32;42m."
            landscape[path][increment+1] = "\033[32;42m."


        increment += 1


    return population_total,revenue





#disaster 2

def flood(landscape,population_total,revenue):

    population_total = 0
    revenue -= 50000
    p = 0

    while p <= (size-1):

        print_matrix(landscape,population_total,revenue)
        print("Oh no there is a flood!")
        time.sleep(.5)
        os.system("cls")

        for i in range(len(landscape)):
            landscape[p][i] = "\033[36;44m~"
        p += 1

    print_matrix(landscape,population_total,revenue)
    print("Oh no there is a flood!")
    time.sleep(2)
    p = len(landscape)-1

        
    while p >= 0:
        
        print_matrix(landscape,population_total,revenue)
        print("Oh no there is a flood!")
        time.sleep(.5)
        os.system("cls")

        for i in range(len(landscape)):
            landscape[p][i] = "\033[32;42m."

        p-=1

    return population_total,revenue





def shop_add(landscape,population_total,revenue):



    try:
        row,column = [int(i) for i in input("Where do you want to build the shop? Upper left is 0 0 (Enter column # row #): ").split()]

# currently only adds shop if whole thing can fit
        if (0 <= row) and (0 <= column) and (column+3 < size) and (row < size):


            if landscape[column][row] == "\033[32;42m.":
                landscape[column][row] = "\033[32;40m$"
                revenue = add_revenue(revenue)


#checks if it is building over current housing so it can subtract population
            elif landscape[column][row] == "\033[31;47m#":
                landscape[column][row] = "\033[31;42mX"
                population_total = sub_pop(population_total)
#makes sure population isn't negative
                if population_total < 0:
                    population_total = 0

#checks if it is building over a store so it can subtract revenue
            elif landscape[column][row] == "\033[32;40m$":
                landscape[column][row] = "\033[31;42mX"
                revenue = sub_revenue(revenue)

            else:
                landscape[column][row] = "\033[31;42mX"





            if landscape[column+1][row] == "\033[32;42m.":
                landscape[column+1][row] = "\033[32;40m$"
                revenue = add_revenue(revenue)

            elif landscape[column+1][row] == "\033[31;47m#":
                landscape[column+1][row] = "\033[31;42mX"
                population_total = sub_pop(population_total)
                if population_total < 0:
                    population_total = 0

            elif landscape[column+1][row] == "\033[32;40m$":
                landscape[column+1][row] = "\033[31;42mX"
                revenue = sub_revenue(revenue)

            else:
                landscape[column+1][row] = "\033[31;42mX"







            if landscape[column+2][row] == "\033[32;42m.":
                landscape[column+2][row] = "\033[32;40m$"
                revenue = add_revenue(revenue)

            elif landscape[column+2][row] == "\033[31;47m#":
                landscape[column+2][row] = "\033[31;42mX"
                population_total = sub_pop(population_total)
                if population_total < 0:
                    population_total = 0


            elif landscape[column+2][row] == "\033[32;40m$":
                landscape[column+2][row] = "\033[31;42mX"
                revenue = sub_revenue(revenue)


            else:
                landscape[column+2][row] = "\033[31;42mX"





            if landscape[column+3][row] == "\033[32;42m.":
                landscape[column+3][row] = "\033[32;40m$"
                revenue = add_revenue(revenue)

            elif landscape[column+3][row] == "\033[31;47m#":
                landscape[column+3][row] = "\033[31;42mX"
                population_total = sub_pop(population_total)
                if population_total < 0:
                    population_total = 0


            elif landscape[column+3][row] == "\033[32;40m$":
                landscape[column+3][row] = "\033[31;42mX"
                revenue = sub_revenue(revenue)


            else:
                landscape[column+3][row] = "\033[31;42mX"






#user tried to pick something outside the range
        else:
            print("Invalid")
            time.sleep(1)
    

        return population_total,revenue


#user either didn't put 2 numbers or tried to use letters
    except:
        print("Not a correct input")
        time.sleep(1)
        return population_total,revenue        
        
    











def house_add(landscape,population_total,revenue):


    try:
        row, column = [int(i) for i in input("Where do you want to build the house? Upper left is 0 0 (Enter column # row #): ").split()]


# currently only adds house if whole thing can fit
        if (0 <= row) and (row < size-1) and (column < size-1) and (0 <= column):


            if landscape[column][row] == "\033[32;42m.":
                landscape[column][row] = "\033[31;47m#"
                population_total = add_pop(population_total)
#checks if building over a house
            elif landscape[column][row] == "\033[31;47m#":
                landscape[column][row] = "\033[31;42mX"
                population_total = sub_pop(population_total)
                if population_total < 0:
                    population_total = 0

#checks if building over a store
            elif landscape[column][row] == "\033[32;40m$":
                landscape[column][row] = "\033[31;42mX"
                revenue = sub_revenue(revenue)
            else:
                landscape[column][row] = "\033[31;42mX"




            if landscape[column+1][row] == "\033[32;42m.":
                landscape[column+1][row] = "\033[31;47m#"
                population_total = add_pop(population_total)

            elif landscape[column+1][row] == "\033[31;47m#":
                landscape[column+1][row] = "\033[31;42mX"
                population_total = sub_pop(population_total)
                if population_total < 0:
                    population_total = 0


            elif landscape[column+1][row] == "\033[32;40m$":
                landscape[column+1][row] = "\033[31;42mX"
                revenue = sub_revenue(revenue)
            else:
                landscape[column+1][row] = "\033[31;42mX"





            if landscape[column][row+1] == "\033[32;42m.":
                landscape[column][row+1] = "\033[31;47m#"
                population_total = add_pop(population_total)

            elif landscape[column][row+1] == "\033[31;47m#":
                landscape[column][row+1] = "\033[31;42mX"
                population_total = sub_pop(population_total)
                if population_total < 0:
                    population_total = 0

            elif landscape[column][row+1] == "\033[32;40m$":
                landscape[column][row+1] = "\033[31;42mX"
                revenue = sub_revenue(revenue)
            else:
                landscape[column][row+1] = "\033[31;42mX"




            if landscape[column+1][row+1] == "\033[32;42m.":
                landscape[column+1][row+1] = "\033[31;47m#"
                population_total = add_pop(population_total)

            elif landscape[column+1][row+1] == "\033[31;47m#":
                landscape[column+1][row+1] = "\033[31;42mX"
                population_total = sub_pop(population_total)
                if population_total < 0:
                    population_total = 0


            elif landscape[column+1][row+1] == "\033[32;40m$":
                landscape[column+1][row+1] = "\033[31;42mX"
                revenue = sub_revenue(revenue)

            else:
                landscape[column+1][row+1] = "\033[31;42mX"


        else:
            print("Invalid")
            time.sleep(1)
    

        return population_total,revenue



    except:
        print("Not a correct input")
        time.sleep(1)
        return population_total,revenue        
        
    






def street_add(landscape,population_total,revenue):


    try:
        
        row,column = [int(i) for i in input("Where do you want to build the street? Upper left is 0 0 (Enter column # row #): ").split()]




#checks if road can fit
        if (0 <= column) and (0 <= row) and (row+6 < size) and (column < size):

            if landscape[column][row] == "\033[32;42m.":
                landscape[column][row] = "\033[33;40m="
            elif landscape[column][row] == "\033[31;47m#":
                landscape[column][row] = "\033[31;42mX"
                population_total = sub_pop(population_total)
                if population_total < 0:
                    population_total = 0

            elif landscape[column][row] == "\033[32;40m$":
                landscape[column][row] = "\033[31;42mX"
                revenue = sub_revenue(revenue)

            else:
                landscape[column][row] = "\033[31;42mX"
            


            if landscape[column][row+1] == "\033[32;42m.":
                landscape[column][row+1] = "\033[33;40m="
            elif landscape[column][row+1] == "\033[31;47m#":
                landscape[column][row+1] = "\033[31;42mX"
                population_total = sub_pop(population_total)
                if population_total < 0:
                    population_total = 0

            elif landscape[column][row+1] == "\033[32;40m$":
                landscape[column][row+1] = "\033[31;42mX"
                revenue = sub_revenue(revenue)
            else:
                landscape[column][row+1] = "\033[31;42mX"




            if landscape[column][row+2] == "\033[32;42m.":
                landscape[column][row+2] = "\033[33;40m="
            elif landscape[column][row+2] == "\033[31;47m#":
                landscape[column][row+2] = "\033[31;42mX"
                population_total = sub_pop(population_total)
                if population_total < 0:
                    population_total = 0

            elif landscape[column][row+2] == "\033[32;40m$":
                landscape[column][row+2] = "\033[31;42mX"
                revenue = sub_revenue(revenue)
            else:
                landscape[column][row+2] = "\033[31;42mX"



            if landscape[column][row+3] == "\033[32;42m.":
                landscape[column][row+3] = "\033[33;40m="
            elif landscape[column][row+3] == "\033[31;47m#":
                landscape[column][row+3] = "\033[31;42mX"
                population_total = sub_pop(population_total)
                if population_total < 0:
                    population_total = 0

            elif landscape[column][row+3] == "\033[32;40m$":
                landscape[column][row+3] = "\033[31;42mX"
                revenue = sub_revenue(revenue)
            else:
                landscape[column][row+3] = "\033[31;42mX"



            if landscape[column][row+4] == "\033[32;42m.":
                landscape[column][row+4] = "\033[33;40m="
            elif landscape[column][row+4] == "\033[31;47m#":
                landscape[column][row+4] = "\033[31;42mX"
                population_total = sub_pop(population_total)
                if population_total < 0:
                    population_total = 0

            elif landscape[column][row+4] == "\033[32;40m$":
                landscape[column][row+4] = "\033[31;42mX"
                revenue = sub_revenue(revenue)
            else:
                landscape[column][row+4] = "\033[31;42mX"




            if landscape[column][row+5] == "\033[32;42m.":
                landscape[column][row+5] = "\033[33;40m="
            elif landscape[column][row+5] == "\033[31;47m#":
                landscape[column][row+5] = "\033[31;42mX"
                population_total = sub_pop(population_total)
                if population_total < 0:
                    population_total = 0

            elif landscape[column][row+5] == "\033[32;40m$":
                landscape[column][row+5] = "\033[31;42mX"
                revenue = sub_revenue(revenue)

            else:
                landscape[column][row+5] = "\033[31;42mX"




            if landscape[column][row+6] == "\033[32;42m.":
                landscape[column][row+6] = "\033[33;40m="
            elif landscape[column][row+6] == "\033[31;47m#":
                landscape[column][row+6] = "\033[31;42mX"
                population_total = sub_pop(population_total)
                if population_total < 0:
                    population_total = 0

            elif landscape[column][row+6] == "\033[32;40m$":
                landscape[column][row+6] = "\033[31;42mX"
                revenue = sub_revenue(revenue)
            else:
                landscape[column][row+6] = "\033[31;42mX"


#user entered pair outside the range
        else:
            print("Invalid")
            time.sleep(1)

        return population_total,revenue

    except:
        print("Not a correct input")
        time.sleep(1)
        return population_total,revenue





#decides the next build or disaster
def roll_number(landscape,population_total,revenue):


#30% house, 30% street, 30% shop, 5% flood, 5% tornado
    number = random.randint(1,100)

    if number <= 30:
        population_total,revenue = house_add(landscape,population_total,revenue)

    elif number <= 60:
        population_total,revenue = street_add(landscape,population_total,revenue)
    elif number <= 90:
        population_total,revenue = shop_add(landscape,population_total,revenue)

    elif number <= 95:
        population_total,revenue = tornado(landscape,population_total,revenue)


    elif number <= 100:
        population_total,revenue = flood(landscape,population_total,revenue)


    return population_total,revenue


def add_pop(population_total):

    ppl_in_house = random.randint(1,7)
    population_total += ppl_in_house

    return population_total


def sub_pop(population_total):
    ppl_removed = random.randint(1,7)
    population_total -= ppl_removed
    return population_total


def sub_revenue(revenue):

    y = random.randint(1000,10000)
    revenue -= y

    return revenue


def add_revenue(revenue):
    x = random.randint(1000,10000)
    revenue += x
    return revenue


# main program


while True:
#prints matrix
    print_matrix(landscape,population_total,revenue)
    time.sleep(.5)
#update matrix
    population_total, revenue = roll_number(landscape,population_total,revenue)
    os.system("cls")
    time.sleep(.1)



