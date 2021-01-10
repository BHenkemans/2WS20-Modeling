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


def generatePupillaryWidth(mean_width=63.2, stdev_width=3.5):
    return mean_width + np.random.normal() * stdev_width


def generateIsFemale():
    """" Generates a gender. If the gender is female, the gender will be True"""
    random_val = random.random()
    if random_val <= 0.50581395348:
        return True
    return False


def generateHasIphone():
    """ Decides whether or not someone has an iPhone """
    random_val = random.random()
    if random_val <= 0.3673:
        return True
    return False


def generateDistNoseLip(mean=1.5, stdev=0.15):
    """ Generates distance between nose and lip"""
    return mean + np.random.normal() * stdev


def generateLengthHead(mean=20, stdev=2.0):
    """ Generates length head"""
    return mean + np.random.normal() * stdev


def generateWidthEarringToEarring(mean=17.5, stdev=2):
    """" Generates distance between earrings"""
    return mean + np.random.normal() * stdev


def generateDistNoseChin(mean=7, stdev=1):
    """" Generates distance between nose and chin"""
    return mean + np.random.normal() * stdev


def generateForehead(mean=8, stdev=1):
    """" Generates a length of the forehead"""
    return mean + np.random.normal() * stdev


class Person:
    """"A class which describes a random person.
    The constructor randomly decides the persons facial attributes."""

    def __init__(self):
        """" Constructor """
        self.eyeColor = generateRandomEye()

        self.hairColor = generateRandomHair()

        self.faceWidth = generateRandomFaceWidth()

        self.pupillaryWidth = generatePupillaryWidth()

        self.isFemale = generateIsFemale()

        self.hasIphone = generateHasIphone()

        self.distNoseLip = generateDistNoseLip()

        self.lengthHead = generateLengthHead()

        self.widthEarringToEarring = generateWidthEarringToEarring()

        self.distNoseChin = generateDistNoseChin()

        self.lengthForehead = generateForehead()


    def isVulnerable(self):
        """" Returns if a person has an iPhone and hence is vulnerable to a doppleganger"""
        return self.hasIphone
