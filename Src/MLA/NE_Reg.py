#In the name of GOD
#Supervised Learning
#Regresion Problem Normal Equesion
# -*- coding: utf-8 -*-
#!usr/bin/env python

import numpy as np
from matplotlib import pyplot as plot
from mpl_toolkits.mplot3d import Axes3D

class Normal_Equa:
	def __init__(self):
		pass

	def Comput_Theta(self, X_Matrix, y_Matrix):
		Theta = []
		m = np.size(X_Matrix[:,1])
		
		step1 = np.dot(X_Matrix.T, X_Matrix)
		step2 = np.linalg.pinv(step1)
		step3 = np.dot(step2, X_Matrix.T)
		Theta = np.dot(step3 ,y_Matrix.T)

		#Theta = np.dot(np.linalg.inv(np.dot(X_Matrix.T, X_Matrix)), np.dot(X_Matrix.T, y_Matrix))

		return Theta



