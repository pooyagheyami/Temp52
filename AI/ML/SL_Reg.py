#In the name of GOD
#Supervised Learning
#Regresion Problem
# -*- coding: utf-8 -*-
#!usr/bin/env python


class Simple_Leaner:
	def __init__(self):
		pass

	def MSE(self, y_seri, y_orgi ):
		n = len(y_orgi)
		ysum = 0
		for i in range(n):
			ysum += (y_seri[i] - y_orgi[i])**2
		return ysum / n


	def Get_Approach(self, N_seri):
		if len(N_seri) == 0:
			return -1
		N_bar = 0
		for N in N_seri:
			try:
				N_bar += float(N)
			except FloatingPointError:
				return -1

		return N_bar / len(N_seri)

	def Theta1(self, x_seri, y_seri):
		n = len(x_seri)
		hsum = 0
		hsqr = 0
		x_bar = self.Get_Approach(x_seri)
		y_bar = self.Get_Approach(y_seri)
		for i in range(n):
			hsum += (x_seri[i]-x_bar)*(y_seri[i]-y_bar)
			hsqr += (x_seri[i]-x_bar)**2
		return hsum / hsqr

	def Theta0(self, x_seri, y_seri):
		y_bar = self.Get_Approach(y_seri)
		x_bar = self.Get_Approach(x_seri)
		theta1 = self.Theta1(x_seri,y_seri)
		return y_bar - (theta1 * x_bar)
