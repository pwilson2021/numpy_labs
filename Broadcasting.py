import numpy as np
import csv

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

projection_open = people3[0:250, 0]
projection_close = people2[0:250, 3]

before_projection = np.array((projection_open, projection_close), np.float64)
broadcast = np.array(([1.1],[1.2]))

projection = before_projection * broadcast

print(projection[0:5, 0:6])

