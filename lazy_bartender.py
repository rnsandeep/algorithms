# problem explantion: https://medium.com/analytics-vidhya/lazy-bartender-problem-return-the-fewest-number-of-drinks-he-must-learn-in-order-to-satisfy-all-549777e83496
preferences1 = {
        0:[0,1,3,6],
        1:[1,4,7],
        2:[2,4,7,5],
        3:[3,2,5],
        4:[5,8],
        }

preferences = {
        0:[ 3,7,5,2, 9],
        1: [5],
        2:[2,3],
        3:[4],
        4:[3,4,3,5,7,4]
        }

import numpy as np

a = np.zeros((5, 10)).astype(int)

print(a)

for key in preferences:
    prefs = preferences[key]

    a[key, prefs] = 1

print(a, np.sum(a, axis=0))

items = []
while(np.sum(np.sum(a, axis=0)) != 0):
     max_item = np.argmax(np.sum(a, axis=0))
     print(max_item)
     indexes = np.where(a[:, max_item] == 1)
     items.append(max_item)
     a[indexes,:] = 0

print("min items required:", len(items))
