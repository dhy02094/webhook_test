import numpy as np

x1, y1 = 0,0
x2, y2 = -1,1
x3, y3 = 3,3 

A = np.array([[x1,y1,1],[x2,y2,1],[x3,y3,1]])

area = abs(np.linalg.det(A)) / 2

print(area)
