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

    sum_for_2016 = np.array(people3).astype(np.float64)
    volume_and_new_stock_2016 = sum_for_2016.sum(axis=0)

    sum_for_2017 = np.array(people2).astype(np.float64)
    volume_and_new_stock_2017 = sum_for_2017.sum(axis=0)

    change = volume_and_new_stock_2017 - volume_and_new_stock_2016

    print(change)

