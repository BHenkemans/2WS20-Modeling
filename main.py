# Is Java not faster??
from Person import Person  # Custom person class
import numpy as np  # Numpy

amountOfPeople = 10000  # Amount of random "second" people that will be generated
amountOfExperiments = 100000  # Amount of random people that will be generated and compared
probArray = []  # Empty array which will store the results of the experiments

for i in range(amountOfExperiments):
    newPerson = Person()  # New person is generated
    match = 0  # Variable which will store the amount of matches
    for j in range(amountOfPeople):
        if newPerson.isPersonEqual(secondperson=Person(), err=0.1):  # If statement which checks if people match
            match += 1  # If a match occurs, increase the match counter
    probArray.append(match / amountOfPeople)  # At the end of an experiment, add the information to the array

averageProb = np.mean(probArray)  # Generate the average probability
print(averageProb)  # Print the average probability
