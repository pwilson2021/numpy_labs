import numpy as np
import csv

with open('AAPL-2017.csv', newline='') as f:
    reader = csv.DictReader(f)
    people = np.empty((0, 6))
    count = 0;
    for row in reader:
        oneRow = np.array([[row['Open'], row['High'], row['Low'], row['Close'], row['Adj Close'], row['Volume']]])
        people = np.append(people, oneRow, axis=0)
        # if (count < 2):
        #     print(people, '\n', '-' * 10, "New People", '-' * 10)
        #     count += 1




# #print(people)
# print("The dimension of people:", np.ndim(people))
# print("The shape of people:", np.shape(people))