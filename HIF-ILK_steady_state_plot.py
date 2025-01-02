# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 22:12:44 2024

@author: vikdi
"""

import numpy as np 
import matplotlib.pyplot as plt
oxy = np.arange(0.1,1,0.1)

hif_0 = np.array([223.78,172.27,120.77,69.32,18.22,0.32,0.14,0.09,0.07])
hif_1 = np.array([300,248.05,195.89,143.29,89.48,0.38,0.14,0.09,0.07])
hif_2 = np.array([])

ilk_0 = np.array([0.18,0.18,0.17,0.17,0.13,0.01,0.01,0,0])
ilk_1 = np.array([0.13,0.13,0.13,0.14,0.12,0.01,0,0,0])
ilk_2 = np.array([])

plt.plot(oxy,hif_0,c = 'b',label = "no feedback loop")
plt.plot(oxy,hif_1,c = 'r',label = "with feedback loop")
plt.grid()
plt.xlabel("Oxygen [a.u.]")
plt.ylabel("HIF steady state [a.u.]")
plt.legend()
plt.title("HIF response to hypoxia")
plt.show()

#plt.plot(oxy,ilk_0,c = 'b',label = "no feedback loop")
plt.plot(oxy,ilk_1,c = 'r',label = "ILK")
plt.plot(oxy,ilk_1,c = 'c',label = "p-Akt")
plt.plot(oxy,ilk_1,c = 'm',label = "p-mTOR")
plt.xlabel("Oxygen [a.u.]")
plt.ylabel("Feedback loop proteins steady state [a.u.]")
plt.legend()
plt.title("Feedback loop proteins response to hypoxia")
plt.show()
