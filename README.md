# HIF-ILK_Petri_Net
This repository supplements the "Petri net modeling of HIF-ILK Interaction using Continuous Petri Nets" paper by Laauwen et al. It contains CPN files of the paper's model, Charlie output files as well as figure's python script. 

HIF_original.cpn is the original petri network from Heiner and Sriram, converted in a continious petri network. 
HIF_intermediate.cpn is the modified network of the original which also contains a simplified "transcription" process producing ILK as well as a feedback loop as the ILK feedback loop as described in the paper.  
HIF_final additionally includes degradation terms for the feedback loop components with the final k-values described in the paper. 

The HIF-ILK_steady_state_plot.py is the python code used to plot the steady-stade plots in the paper. Using the Simulation-Mode of Snoopy on the CPN files, the steady-state values of components were obtained and manually recorded as numpy arrays to be plotted using this code. 
