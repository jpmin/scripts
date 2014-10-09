# a script about finding the limit function of the value function

import numpy as np
import matplotlib.pyplot as plt

iteration_num = 20
state_num = 10

k0 = np.linspace(10, 0, state_num)
k = np.ones((state_num, 1))
for i in k:
	k[i] = k0[state_num- 1 - i]

v = np.ones((state_num, iteration_num))
for iterate in range(iteration_num):
	for state in range(state_num):
	 
