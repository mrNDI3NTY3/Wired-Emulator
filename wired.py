import time
import random
class player():
    """
    This class allows you to emulate player actions
    """

    def __init__(self, name:str, x_pos:int, y_pos:int):
        self.PlayerName = name
        self.PlayerPosition = [x_pos, y_pos]

    def get_name(self) -> str:
        '''
        This function returned player name
        '''
        return self.PlayerName

    def get_position(self, mode:str)-> any:
        '''
        This function returned player position
        MODE:
        x -> Return X COORDINATE(int)
        y -> Return Y COORDINATE(int)
        xy -> Return X COORDINATE and Y COORDINATE(list)
        '''
        if mode == "x":
            return(self.PlayerPosition[0])
        elif mode == "y":
            return(self.PlayerPosition[1])
        elif mode == "xy":
            return(self.PlayerPosition)

    def set_position(self, mode:str, value:int)->None:
        '''
        This function change player position to the entered value(int)
        '''
        if mode == "x":
            self.PlayerPosition[0] = value
        if mode == "y":
            self.PlayerPosition[1] = value

class furni():
    """
        This class allows you to implement the interaction of triggers and objects in code

        Description of the variables that are passed to the class:
        state_number - How many states can an item have
        route_number - How many turns can an item have
        current_state - Current state of the item
        current_route - Current rotation of the item
        x_pos, y_pos - Current position x/y coordinate

    """
    def __init__(self, state_number:int,route_number:int, current_state:int ,current_route:int, x_pos:int, y_pos:int):
        if state_number < current_state:
            current_state = 1
        elif current_state < 1:
            current_state = state_number
        if current_route > route_number:
            current_route = 1
        if current_route < 1:
            current_route = route_number

        self.current_state = current_state
        self.current_route = current_route
        self.route_number = route_number
        self.state_number = state_number

        self.FurniPosition = [x_pos, y_pos]

    def set_state(self, state:int)-> None:
        """This function changes the current state of furni to the entered one"""
        if self.state_number < state:
            state = 1
        elif state < 1:
            state = self.state_number
        self.current_state = state

    def set_route(self, route:int)-> None:
        """This function changes the current direction of furni to the entered one"""
        if self.route_number < route:
            route = 1
        elif route < 1:
            route = self.route_number
        self.current_route = route

    def get_position(self, mode:str)-> any:
        '''
        This function returned furni position
        MODE:
        x -> Return X COORDINATE(int)
        y -> Return Y COORDINATE(int)
        xy -> Return X COORDINATE and Y COORDINATE(list)
        '''
        if mode == "x":
            return(self.FurniPosition[0])
        elif mode == "y":
            return(self.FurniPosition[1])
        elif mode == "xy":
            return(self.FurniPosition)

    def set_position(self, mode:str, value:int)->None:
        '''
        This function change furni position to the entered value(int)
        '''
        if mode == "x":
            self.FurniPosition[0] = value
        if mode == "y":
            self.FurniPosition[1] = value
    
    def get_state(self)-> int:
        return self.current_state

class trigger():

    def says_keyword(keyword:str, user_word:str)-> bool:
        """This function works as a trigger when a special word is written"""
        return keyword.lower() in user_word.lower()

    def furni_used(furni_used:bool)-> bool:
        """This function works as a trigger when the player interacts with the selected furni"""
        return furni_used

    def timer(second:float)->bool:
        """This function works like a timer trigger"""
        time.sleep(second)
        return True

class effect():
    def toggle_furni_state(obj:object)-> None:
        """This function works like an effect that doubleclicks on furni"""
        obj.set_state(obj.current_state+1)

    def rotate_furni(obj:object, route_in:int)-> None:
        """This function works as an effect that allows you to rotate and move the furni (movement is not available)"""
        if route_in ==  1:
            pass
        elif route_in == 2:
            obj.set_route(obj.current_route+1)
        elif route_in == 3:
            obj.set_route(obj.current_route-1)
        elif route_in == 4:
            obj.set_route(obj.current_route + random.choice([1, -1]))


    def teleporter(playr:object, furn:object)-> None:
        """This function works as an effect which can teleport player to furni"""
        playr.set_position("x", furn.get_position("x"))
        playr.set_position("y", furn.get_position("y"))

class condition():
    def player_on_furni(player_coordinate:list, furni_coordinate:list)-> bool:
        """This function works as a condition Which compares the position of the player and the furni and checks if the player is on the furni"""
        return player_coordinate == furni_coordinate
    def match_furni(obj:object, route:int, state:int)->bool:
        """This function works as a condition that can compare the saved direction, state and position with the current one in furni"""
        return (obj.current_route == route) == (obj.current_state == state)
