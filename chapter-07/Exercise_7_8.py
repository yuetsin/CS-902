# Exercise 7.8

class Vehicle:
    def __init__(self, wheelNum, width, height, weight):
        self.wheelNum = wheelNum
        self.width = width
        self.height = height
        self.weight = weight
    def start(self):
        # Vehicle starts

    def stop(self):
        # Vehicle stops

    def destroy(self):
        # Vehicle Destroyed

class Car(Vehicle):
    def openDoor(self):
        # Car door open
    def changeWheel(self):
        # Car wheel changed

class Plane(Vehicle):
    def TakeOff(self):
        # Plane TakeOff
