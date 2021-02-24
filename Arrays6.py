import numpy as np
import csv

np.set_printoptions(formatter={'float': '{: 6.2f}'.format})

with open('AAPL-2017.csv', newline='') as f, open('AAPL-2016.csv', newline='') as f2:
    reader = csv.DictReader(f)
    reader2 = csv.DictReader(f2)
    people = np.empty((0, 6))
    people2 = np.empty((0, 6))

    for row in reader:
        oneRow = np.array([[row['Open'], row['High'], row['Low'], row['Close'], row['Adj Close'], row['Volume']]])
        people = np.append(people, oneRow, axis=0)

    for row in reader2:
        oneRow = np.array([[row['Open'], row['High'], row['Low'], row['Close'], row['Adj Close'], row['Volume']]])
        people2 = np.append(people2, oneRow, axis=0)

    people3 = np.delete(people, 250, 0)

    combined_years = np.concatenate((people3, people2)).astype(np.float64)

    #np.savetxt("combined_years.txt", combined_years, fmt="%10.2f", delimiter=",")
    #january = combined_years[0:20, 0:6]

    #question 2
    #january[0,5] = 100
    #print(combined_years[0])

    #question 3
    #print(combined_years[0:5, 0:6])

    #question 4
    max = people3.astype(np.float64).max(axis=0)
    min = people3.astype(np.float64).min(axis=0)
    print( max, "\n", min)

    #question 5
    print(people3[0:5, 1])
    print(people3[0:5, 2])