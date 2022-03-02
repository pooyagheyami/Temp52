# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## Please DO NOT Change Panel name (P19)
###########################################################################

import wx
import wx.xrc

import os

import Src.MLA.NeruNet as NN
from scipy.io import loadmat
import numpy as np

###########################################################################
## Class P19 Temp Panel
###########################################################################

class P19 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 250,250 ), style = wx.BORDER_RAISED|wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		Vsp19 = wx.BoxSizer( wx.VERTICAL )

		Hsz1 = wx.BoxSizer( wx.HORIZONTAL )
		#you can add object in this BoxSizer
		self.lblm = wx.StaticText(self, wx.ID_ANY, u"m =  ", wx.DefaultPosition, wx.DefaultSize, 0)
		self.lblm.Wrap(-1)

		Hsz1.Add(self.lblm, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		self.Sc1 = wx.SpinCtrl(self, wx.ID_ANY, u"m", wx.DefaultPosition, wx.Size(60, -1), wx.SP_ARROW_KEYS, 0, 9999,
		                       0)
		Hsz1.Add(self.Sc1, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)


		Vsp19.Add( Hsz1, 0, wx.EXPAND, 5 )

		Hsz2 = wx.BoxSizer( wx.HORIZONTAL )
		# you can add object in this BoxSizer


		Vsp19.Add( Hsz2, 0, wx.EXPAND, 5 )

		Hsz3 = wx.BoxSizer( wx.HORIZONTAL )
		# you can add object in this BoxSizer


		Vsp19.Add( Hsz3, 0, wx.EXPAND, 5 )

		Hsz4 = wx.BoxSizer( wx.HORIZONTAL )
		# you can add object in this BoxSizer


		Vsp19.Add( Hsz4, 0, wx.EXPAND, 5 )

		Hsz5 = wx.BoxSizer( wx.HORIZONTAL )
		# you can add object in this BoxSizer

		Vsp19.Add( Hsz5, 0, wx.EXPAND, 5 )


		self.SetSizer( Vsp19 )
		self.Layout()

		# Connect Events
		self.Bind( wx.EVT_INIT_DIALOG, self.Start )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Start( self ):
		dlg = wx.FileDialog(self, message="Choose Database",
		                    defaultDir=os.getcwd(),defaultFile="",
		                    wildcard="All file(*.*)|*.*",
		                    style=wx.FD_OPEN | wx.FD_CHANGE_DIR)
		if dlg.ShowModal() == wx.ID_OK:
			paths = dlg.GetPaths()
		#print(paths)
		dlg.Destroy()
		data = loadmat(paths[0])
		#print(data)
		X = data['X']
		y = data['y'].flatten()
		sel = np.random.permutation(X)[:100]
		NN.display_data(sel)
		m = X.shape[0]
		print(m)

	def Test( self ):
		print('work it')

