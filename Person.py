import numpy as np
import random


def generateRandomEye():
    """ Generates a random eye colour based on the probabilities outlined in the report """
    random_val = random.random()
    if 0 <= random_val < 0.7:
        return "Blue"
    elif 0.7 <= random_val < 0.8:
        return "Intermediate"
    else:
        return "Brown"


def generateRandomHair():
    """" Generates a random hair colour based on the probabilities outlined in the report """
    random_val = random.random()
    if 0 <= random_val < 0.73:
        return "Blond"
    else:
        return "Brown"


def generateRandomFaceWidth(mean_width=15.2, stdev_width=0.5):
    """" Generates a random face width based on the mean width described on Wikipedia and the standard deviation that
    was found in another paper. Do note, the standard derivation and mean width !! are not related !! so a better
    source is prefered! """
    return mean_width + np.random.normal() * stdev_width


class Person:
    """"A class which describes a random person.
    The constructor randomly decides the persons facial attributes."""

    def __init__(self):
        """" Constructor """
        self.eyeColor = generateRandomEye()

        self.hairColor = generateRandomHair()

        self.faceWidth = generateRandomFaceWidth()

    def isPersonEqual(self, secondperson, err):
        """" Returns True or False depending on whether or not the faces match. Faces match if the eye colour and
        hair tint match and if the width of the face is relatively close. """
        if self.eyeColor == secondperson.eyeColor \
                and self.hairColor == secondperson.hairColor \
                and secondperson.faceWidth - err <= self.faceWidth <= secondperson.faceWidth + err:
            return True
        return False
