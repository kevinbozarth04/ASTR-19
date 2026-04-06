'''
Write a Python program that declares a class describing your favorite animal.
Have the data members of the class represent the following physical parameters of the animal:
length of the arms (float),
length of the legs (float),
number of eyes (int),
does it have a tail? (bool),
is it furry? (bool).
Write an initialization function that sets the values of the data members when an instance of the class is created.
Write a member function of the class to print out and describe the data members representing the physical characteristics of the animal.
'''

class FavoriteAnimal:
    def __init__(self, armLength, legLength, eyeCount, tailBool, furryBool):
        self.armLength = armLength
        self.legLength = legLength
        self.eyeCount = eyeCount
        self.tailBool = tailBool
        self.furryBool = furryBool

    def printData(self):
        print("Arm length (in):", self.armLength)
        print("Leg length (in):", self.legLength)
        print("Eye count:", self.eyeCount)
        print("Has a tail?:", self.tailBool)
        print("Is furry?:", self.furryBool)
        
def main():
    a = FavoriteAnimal(12, 12, 2, True, True)
    a.printData()

main()

# Kevin Bozarth
