Below are the original instructions:

Create an city-building simulation called CitySimTM.

Read the project requirements carefully. When the user starts your program, they should be prompted with an input for the size of the city.

size = int(input("Enter a city size:"))

The user is presented with a field of "grass".

The user is then prompted to input coordinates to build something. You can make it so that the coordinates can be input on the same line using the following command:



Since "try" catches errors, in order to quit your program you will have to minimize it. You can do ctrl-z instead of ctrl-c.

If the user were to input "3 0" and press enter, something new will be built on the 4th column and 1st row. The user will be presented with an updated city.



Next, if the user types  "2 1" then the city would update again. Notice that the new building (this time its a street) starts at "2 1" and the rest is filled in automatically.

And so on.

 

Requirements (read VERY carefully):

The user should be able to build at least three types of objects or building types. They can be houses, streets, and rivers, utilities, or something else entirely. They must all be various shapes and sizes. For example, a road might be represented by a horizontal or vertical 1x5 shape, while a house may have a 2x2 shape. You may allow the user a way of choosing what they build, or just have it randomized each turn. Furthermore, if the user inputs a coordinate that already has something build there, they will instead demolish the current object. Replace that spot(s) with one or more 'x' (see the image below).

You must have a way of increasing/decreasing population and revenue as the simulation progresses.

Your program must not crash if the user enters invalid input; instead, it simply prompts the user to try another input. Also, buildings should never be built out of index of the size of the city, otherwise the program will crash. To get full points, you must have 10 or fewer lines of code in your main "loop" (without using semicolons)! This can only be accomplished using functions. When printing your city, you may not simply print your city using Python's "print()" function. Instead, you must create your own print function. Your program may not print any sort of ' or [ ] symbols, which would occur if you are simply calling "print(city)"!

To achieve the highest score, you must implement at least one natural disaster: Add natural disasters that destroy parts of the city after some amount of turns! Maybe a fire destroys a house and spreads to nearby houses, or rainfall creates new rivers and destroys roads. To fulfill this, you may not simply randomly place 'x' around the map every once in a while. There must be some kind of “animation” corresponding to the disaster (i.e. a flood slowly fills the city, rather than just updating the area all at once).


You can be as creative as you want in fulfilling the requirements of this project. But, any adjustments and liberties you take with the requirements should present something as or more complex than what we are testing you for. An example program may look like this:



 

Or, it may look like this (see how to add background color to your text here Links to an external site.):


 

There is no specific way your CitySim simulation must "look."

Turn-in: Only turn in your Python or C code.

FYI: To clear the terminal, you can use:
import os
os.system('clear||cls')
