import matplotlib.pyplot as plt
import numpy as np

scores = np.array([
    65,70,75,80,85,90,95,100,55,60,65,70,75,80,85,90,95,100,55,60,65,70,75,80,85,90,95,100,55,60,65,70,75,80,85,90,95,100,55,60,65,70,75,85,90,95,100
])

plt.hist(scores, edgecolor="black")
plt.show()