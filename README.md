# Wired-Emulator
This wired emulator in Python allows you to emulate wired directly in Python. This makes it easy to find bugs, flaws, and also speeds up the development time of games and other things on wired!
To work with this emulator, you must have knowledge of both python and wired. 
This emulator accommodates a lot of things with which you can create a lot of things, from simple doors to a computer.

Let's run through the code class player:
A class that emulates the player (name and position, everything you need for triggers)

get_name - returns the name of the emulated player
get_position - Returns the player current position(x - x coordinate, y - y coordinate, xy - list of x and y coordinates) 
set_position - changes the player position(x - x coordinate, y - y coordinate)

The position is used in a lot of things, we'll talk about that later.

class furni: A class that emulates fourties. There are several variables:

state_number - How many states can an item have
route_number - How many turns can an item have
current_state - Current state of the item
current_route - Current rotation of the item
x_pos, y_pos - Current position x/y coordinate

There are several methods for this class:

set_state - Changes the current state of the furni
set_route - Changes the current rotation of the furni 
get_position - Displays the current position(x - x coordinate, y - y coordinate, xy - list of x and y coordinates) 
set_position - Changes position (x - x coordinate, y - y coordinate)
