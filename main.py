from Person import Person  # Custom person class
import time
import csv

start = time.time()  # Start timer

amountOfPeople = 100  # Amount of random "second" people that will be generated
amountOfExperiments = 100000  # Amount of random people that will be generated and compared

with open('result.csv', 'w', newline='', encoding='utf-8') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',', quotechar='|',quoting=csv.QUOTE_MINIMAL)  # CSV writer
    filewriter.writerow(['experiment', 'amountpeople', 'match'])  # Initialize CSV-file

    for i in range(amountOfExperiments):
        newPerson = Person()  # New person is generated
        match = 0  # Variable which will store the amount of matches
        for j in range(amountOfPeople):
            if newPerson.isPersonEqual(secondperson=Person(), err=0.1):  # If statement which checks if people match
                match += 1  # If a match occurs, increase the match counter
        filewriter.writerow([i, amountOfPeople, match])  # Write experiment result to CSV file

end = time.time()  # End timer
print("{time: .2f}s elapsed".format(time=end - start))  # Print time elapsed
