# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class P19
###########################################################################

class P19 ( wx.Panel ):

	def __init__( self, parent, Data=[], id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 250,250 ), style = wx.BORDER_RAISED|wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.Data = Data

		Vsp19 = wx.BoxSizer( wx.VERTICAL )

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
		self.Btn1.Bind(wx.EVT_BUTTON, self.comput)
		self.Btn2.Bind(wx.EVT_BUTTON, self.shwplot)

	def __del__( self ):
		pass

	# Virtual event handlers, overide them in your derived class
	def comput(self, event):
		event.Skip()

	def shwplot(self, event):
		event.Skip()
