import randomWalk as rw
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import time

mpl.use('macosx')

directions = 4
steps = 2
#probs = np.random.uniform(0, 1, (directions,))
probs = 1/directions * np.ones((directions,))
probs = probs / np.sum(probs)
randomWalk = rw.RandomWalk(directions, probs)
# walk = randomWalk.walk(steps)
sims = 100000
t1 = 0
t2 = 0
for i in range(sims):
    walk1 = randomWalk.walk(steps)
    walk2 = randomWalk.walk(steps)
    if np.isclose(np.sum((walk1[1, :] - walk2[1, :])**2), 0):
        t1 += 1
    elif np.isclose(np.sum((walk1[2, :] - walk2[2, :])**2), 0) and ~np.isclose(np.sum((walk1[1, :]-walk2[1, :])**2), 0):
        t2 += 2

print(t1/sims, t2/sims)



'''
randomWalk.plot(walk, 0, facecolor='#303030', axis_color='w')
randomWalk.probsplot()
rw.heatmap(walk, 10)
plt.show()
'''
'''
start = time.time()
walk = rw.simulateWalk(steps, directions)
rw.plotWalk(walk)
print("Time taken: ", time.time() - start)
'''
