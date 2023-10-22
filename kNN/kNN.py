import numpy as np
import matplotlib.pyplot as plt

def kNN(k, group1, group2, data):
    def dist(p1, p2):
        return (np.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2))
    allPoints = np.empty(len(group1[0]) + len(group2[0]))
    for i in range (len(group1[0])):
        allPoints[i] = [[group1[0, i], group1[1, i]], 1]
    for i in range (len(group2[0])):
        allPoints[i + np.len(group1[0])] = [[group2[0, i], group2[1, i]], -1]
        
    for i in range(len(allPoints)):
        for i1 in range (i, len(allPoints)):
            if (dist(allPoints[i, 0], data) > dist(allPoints[i+1, 0], data)):
                temp = allPoints[i]
                allPoints[i] = allPoints[i+1]
                allPoints[i+1] = temp
    
    freq1 = 0
    freq2 = 0
    for i in range (k):
        if (allPoints[i, 1] == 1):
            freq1 += 1
        if (allPoints[i, 1] == -1):
            freq2 += 1
 
    result = 0
    if (freq1 > freq2):
        result = 1
    else:
        result = -1
        
    return result
                
group1 = np.array([np.random.random(10), np.random.random(10)])
group2 = np.array([-np.random.random(10), -np.random.random(10)])

plt.scatter(group1[0,:], group1[1,:], color = 'b')
plt.scatter(group2[0,:], group2[1,:], color = 'r')
plt.show()

group3 = np.array([np.random.random(10)-np.random.random(10), np.random.random(10)-np.random.random(10)])
plt.scatter(group3[0,:], group3[1,:], color = 'g')
plt.show()

k = 3
for i in range(np.shape(group3)[1]):
    result=kNN(k, group1, group2, [group3[0, i], group3[1, i]])
    if result > 0:
        color = 'g'
    elif result < 0:
        color = 'y'
    plt.scatter(group3[0, i], group3[1, i], color = color)
plt.show()