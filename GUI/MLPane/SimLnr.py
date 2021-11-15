# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

from . import MLUtil as MLU
from AI.ML.SL_Reg import *

import numpy as np
from matplotlib import pyplot as plot
from mpl_toolkits.mplot3d import Axes3D

###########################################################################
## Class P19
###########################################################################

class P19 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 250,250 ), style = wx.BORDER_RAISED|wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )


		self.flds = []
		self.idata = []
		self.Xdata = []
		self.Ydata = []

		Vsp19 = wx.BoxSizer( wx.VERTICAL )

		Hsz11 = wx.BoxSizer(wx.HORIZONTAL)

		self.lblm = wx.StaticText(self, wx.ID_ANY, u"m =  ", wx.DefaultPosition, wx.DefaultSize, 0)
		self.lblm.Wrap(-1)

		Hsz11.Add(self.lblm, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		self.Sc1 = wx.SpinCtrl(self, wx.ID_ANY, u"m", wx.DefaultPosition, wx.Size(60, -1), wx.SP_ARROW_KEYS, 0, 9999,
		                       0)
		Hsz11.Add(self.Sc1, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		self.lbl2 = wx.StaticText(self, wx.ID_ANY, u"Number of training", wx.DefaultPosition, wx.DefaultSize, 0)
		self.lbl2.Wrap(-1)

		Hsz11.Add(self.lbl2, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		self.btnm = wx.Button(self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT)
		Hsz11.Add(self.btnm, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		Vsp19.Add(Hsz11, 0, wx.EXPAND, 5)

		Hsz12 = wx.BoxSizer(wx.HORIZONTAL)

		self.lblx = wx.StaticText(self, wx.ID_ANY, u"x (Input/features)=  ", wx.DefaultPosition, wx.DefaultSize, 0)
		self.lblx.Wrap(-1)

		Hsz12.Add(self.lblx, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		self.fldx = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		Hsz12.Add(self.fldx, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		self.btnx = wx.Button(self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT)
		Hsz12.Add(self.btnx, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)
		self.btnx.SetToolTip(u"Independent variable")
		Vsp19.Add(Hsz12, 0, wx.EXPAND, 5)

		Hsz13 = wx.BoxSizer(wx.HORIZONTAL)

		self.lbly = wx.StaticText(self, wx.ID_ANY, u"y (Output/target)=  ", wx.DefaultPosition, wx.DefaultSize, 0)
		self.lbly.Wrap(-1)

		Hsz13.Add(self.lbly, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		self.fldy = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		Hsz13.Add(self.fldy, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		self.btny = wx.Button(self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT)
		Hsz13.Add(self.btny, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)
		self.btny.SetToolTip(u"Dependent variable")
		Vsp19.Add(Hsz13, 0, wx.EXPAND, 5)

		Hsz14 = wx.BoxSizer(wx.HORIZONTAL)

		self.lblt = wx.StaticText(self, wx.ID_ANY, u"Shows plot of Data you enter", wx.DefaultPosition,
		                          wx.DefaultSize, 0)
		self.lblt.Wrap(-1)

		Hsz14.Add(self.lblt, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		self.btntt = wx.Button(self, wx.ID_ANY, u"Show Plot", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT)
		Hsz14.Add(self.btntt, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		Vsp19.Add(Hsz14, 0, wx.EXPAND, 5)

		Hsz1 = wx.BoxSizer(wx.HORIZONTAL)

		self.Btn1 = wx.Button(self, wx.ID_ANY, u"Comput Thetas", wx.DefaultPosition, wx.DefaultSize, 0)
		Hsz1.Add(self.Btn1, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		Vsp19.Add(Hsz1, 0, wx.EXPAND, 5)

		Hsz2 = wx.BoxSizer(wx.HORIZONTAL)

		self.lbl1 = wx.StaticText(self, wx.ID_ANY, u"Theta 0", wx.DefaultPosition, wx.DefaultSize, 0)
		self.lbl1.Wrap(-1)

		Hsz2.Add(self.lbl1, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		self.fld1 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY)
		Hsz2.Add(self.fld1, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		Vsp19.Add(Hsz2, 0, wx.EXPAND, 5)

		Hsz3 = wx.BoxSizer(wx.HORIZONTAL)

		self.lbl2 = wx.StaticText(self, wx.ID_ANY, u"Theta 1", wx.DefaultPosition, wx.DefaultSize, 0)
		self.lbl2.Wrap(-1)

		Hsz3.Add(self.lbl2, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		self.fld2 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY)
		Hsz3.Add(self.fld2, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		Vsp19.Add(Hsz3, 0, wx.EXPAND, 5)

		Hsz4 = wx.BoxSizer(wx.HORIZONTAL)

		self.fld3 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY)
		Hsz4.Add(self.fld3, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		Vsp19.Add(Hsz4, 0, wx.EXPAND, 5)

		Hsz5 = wx.BoxSizer(wx.HORIZONTAL)

		self.Btn2 = wx.Button(self, wx.ID_ANY, u"Show Plot line", wx.DefaultPosition, wx.DefaultSize, 0)
		Hsz5.Add(self.Btn2, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL , 5)

		Vsp19.Add(Hsz5, 0, wx.EXPAND, 5)


		self.SetSizer( Vsp19 )
		self.Layout()

		# Connect Events
		self.btnm.Bind(wx.EVT_BUTTON, self.inptri)
		self.btnx.Bind(wx.EVT_BUTTON, self.inpx)
		self.btny.Bind(wx.EVT_BUTTON, self.inpy)
		self.btntt.Bind(wx.EVT_BUTTON, self.pltdata)
		self.Btn1.Bind(wx.EVT_BUTTON, self.comput)
		self.Btn2.Bind(wx.EVT_BUTTON, self.shwplot)

	def __del__( self ):
		pass

	# Virtual event handlers, overide them in your derived class
	def comput(self, event):
		mylnr = Simple_Leaner()
		X_seri = []
		Y_seri = []
		for D in self.idata:
			X_seri.append(float(D[0]))
			Y_seri.append(float(D[1]))
		Theta0 = mylnr.Theta0(X_seri,Y_seri)
		Theta1 = mylnr.Theta1(X_seri,Y_seri)

		self.Y = []

		self.fld1.SetValue(str(Theta0))
		self.fld2.SetValue(str(Theta1))
		self.fld3.SetValue('y = '+str(Theta0)+' + '+str(Theta1)+' . x1 ')
		for D in self.idata:
			self.Y.append(Theta0+Theta1*float(D[0]))
		event.Skip()

	def shwplot(self, event):
		#print('press btn plot')
		X = self.Xdata[:,1]
		y = self.Ydata.transpose()
		y1 = self.Y
		plot.plot(X, y, 'rx', markersize=10)
		plot.ylabel('data y')
		plot.xlabel('data x')
		plot.plot(X, y1, '-')
		plot.show()
		event.Skip()

	def inptri( self, event ):
		#print(self.idata)
		#print(self.flds)
		frm = wx.Dialog(self, -1)
		pnl = MLU.Yselect(frm, self.flds, self.idata)
		#pnl = MyPanel3(frm, self.flds, self.idata)
		frm.SetSize((500,220))
		frm.SetLabel(u'Data you use')
		frm.ShowModal()
		#frm.EndModal((pnl.xMtrx,pnl.yMtrx))
		Xm = pnl.xMtrx
		Ym = pnl.yMtrx
		frm.Destroy()
		self.Xdata= np.matrix(Xm)
		self.Ydata= np.matrix(Ym)

		self.fldx.SetValue( 'np.matrix(xdata)' )
		self.fldy.SetValue( 'np.matrix(ydata)' )


	def inpx( self, event ):
		frm = wx.Dialog(self, -1)
		pnl = MLU.ShowMatrix(frm, self.Xdata)
		#pnl = MyPanel4(frm,self.Xdata)
		frm.SetSize((300,180))
		frm.SetLabel(u'X matrix')
		frm.ShowModal()

		frm.Destroy()
		event.Skip()

	def inpy( self, event ):
		frm = wx.Dialog(self, -1)
		pnl = MLU.ShowMatrix(frm, self.Ydata)
		#pnl = MyPanel4(frm, self.Ydata)
		frm.SetSize((300, 180))
		frm.SetLabel(u'Y matrix')
		frm.ShowModal()

		frm.Destroy()

	def pltdata( self, event ):
		#print(self.Xdata[:,1],self.Ydata[:,0])
		X = self.Xdata[:,1]
		y = self.Ydata.transpose()
		plot.plot(X, y , 'rx', markersize=10)
		plot.ylabel('data y')
		plot.xlabel('data x')
		plot.show()
