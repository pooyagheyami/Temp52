#In the name of GOD
#Cust Function
#Regresion Problem
# -*- coding: utf-8 -*-
#!usr/bin/env python

from AI.Analiz import *

import numpy as np
from matplotlib import pyplot as plot
from mpl_toolkits.mplot3d import Axes3D

class Cust_Func:
	def __init__(self):
		pass

	def Comput(self, X, y, Theta):
		m = y.size
		costs = (X.dot(Theta) - y) ** 2
		return costs.sum() / (2.0 * m)

	def Gradient_descent(self, X, y, Theta, Alpha, num_iters):
		m = y.size
		J_history = np.zeros(num_iters)
		for i in range(num_iters):
			h = X.dot(Theta)
			errors = h - y
			delta = X.T.dot(errors)
			Theta -= (Alpha / m) * delta
			J_history[i] = self.Comput(X, y, Theta)
		return (Theta, J_history)


	def minimize(self):
		pass

	def update_theta(self):
		pass

	def __iter__(self):
		pass

	def __reduce__(self):
		pass

