import numpy as np
import csv

with open('AAPL-2017.csv', newline='') as f, open('AAPL-2016.csv', newline='') as f2:
    reader = csv.DictReader(f)
    reader2 = csv.DictReader(f2)
    people = np.empty((0, 1))
    people2 = np.empty((0, 1))

    for row in reader:
        oneRow = np.array([[row['Volume']]])
        people = np.append(people, oneRow, axis=0)

    for row in reader2:
        oneRow = np.array([[row['Volume']]])
        people2 = np.append(people2, oneRow, axis=0)

    people3 = np.delete(people, 250, 0)

    #print(people3.sum())
    #print(np.sum(people, dtype=np.int32))
    #print(type(people3))

    # Summing the volume for 2016

    # Converting to float
    sum_for_2016 = np.array(people3).astype(np.float)
    volume_and_new_stock_2016 = sum_for_2016.sum(axis=0)
    print(volume_and_new_stock_2016)

    # Summing the volume for  2017
    # Converting to float
    sum_for_2017 = np.array(people2).astype(np.float)
    volume_and_new_stock_2017 = sum_for_2017.sum(axis=0)
    print(volume_and_new_stock_2017)

    print("Change from 2017-2016: ", volume_and_new_stock_2017 - volume_and_new_stock_2016)
    #print(volume_and_new_stock_2017 - volume_and_new_stock_2016)

