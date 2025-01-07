# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 22:12:44 2024

@author: vikdi
"""

import numpy as np 
import matplotlib.pyplot as plt
oxy = np.arange(0.1,1,0.1)
print(oxy)
# hif_0 = np.array([223.78,172.27,120.77,69.32,18.22,0.32,0.14,0.09,0.07])
# hif_1 = np.array([300,248.05,195.89,143.29,89.48,0.38,0.14,0.09,0.07])

# ilk_0 = np.array([0.18,0.18,0.17,0.17,0.13,0.01,0.01,0,0])
# ilk_1 = np.array([0.13,0.13,0.13,0.14,0.12,0.01,0,0,0])

# hif_0 = np.array([223.78,172.27,120.77,69.32,18.22,0.32,0.14,0.09,0.07])
# hif_1 = np.array([549.21, 508.55, 467.27, 424.92, 380.18, 326.12, 0.19, 0.11, 0.08])

# ilk_0 = np.array([0.18,0.18,0.17,0.17,0.13,0.01,0.01,0,0])
# ilk_1 = np.array([3.05, 3.05, 3.05, 3.04, 3.04, 3.03, 0.12, 0.08, 0.07])

hif_original = np.array([115.29, 94.07, 72.85, 51.65, 30.50, 9.73, 0.55, 0.23, 0.15])
hif_intermediate = np.array([299.99, 248.05, 195.89, 143.29, 89.48, 0.38, 0.14, 0.09, 0.07])
hif_final = np.array([757.26, 705.30, 653.27, 601.16, 548.91, 496.50, 0.19, 0.11, 0.08])

# ilk_original = np.array([])
ilk_intermediate = np.array([0.13, 0.13, 0.13, 0.13, 0.12, 0.01, 0.00, 0.00, 0.00])
ilk_final = np.array([3.07, 3.07, 3.06, 3.06, 3.06, 3.05, 0.12, 0.08, 0.07])

p_Akt_intermediate = np.array([0.13, 0.13, 0.13, 0.13, 0.12, 0.01, 0.00, 0.00, 0.00])
p_Akt_final = np.array([6.42, 6.41, 6.41, 6.40, 6.39, 6.38, 0.26, 0.18, 0.15])

p_mTOR_intermediate = np.array([0.13, 0.13, 0.13, 0.13, 0.12, 0.01, 0.00, 0.00, 0.00])
p_mTOR_final = np.array([0.89, 0.89, 0.89, 0.89, 0.89, 0.89, 0.04, 0.02, 0.02])

plt.plot(oxy,hif_original,c = 'b',label = "Original network")
plt.plot(oxy,hif_intermediate,c = 'r',label = "Intermediate network")
plt.plot(oxy,hif_final,c = 'g',label = "Final network")
plt.grid()
plt.xlabel("Oxygen [a.u.]")
plt.ylabel("HIF steady state [a.u.]")
plt.legend()
plt.title("HIF response to hypoxia")
plt.show()

# plt.plot(oxy,ilk_0,c = 'b',label = "no feedback loop")
plt.plot(oxy,ilk_intermediate,c = 'r',label = "ILK")
plt.plot(oxy,p_Akt_intermediate,c = 'c',label = "p_473S_Akt")
plt.plot(oxy,p_mTOR_intermediate,c = 'm',label = "p_mTOR")
plt.xlabel("Oxygen [a.u.]")
plt.ylabel("Intermediate network proteins steady state [a.u.]")
plt.legend()
plt.title("Intermediate network proteins response to hypoxia")
plt.show()

plt.plot(oxy,ilk_final,c = 'r',label = "ILK")
plt.plot(oxy,p_Akt_final,c = 'c',label = "p_473S_Akt")
plt.plot(oxy,p_mTOR_final,c = 'm',label = "p_mTOR")
plt.xlabel("Oxygen [a.u.]")
plt.ylabel("Final network proteins steady state [a.u.]")
plt.legend()
plt.title("Final  network proteins response to hypoxia")
plt.show()
