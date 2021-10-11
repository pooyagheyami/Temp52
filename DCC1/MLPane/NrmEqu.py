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
## Class P192
###########################################################################

class P19 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 250,250 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		Vsp19 = wx.BoxSizer( wx.VERTICAL )

		Hsz1 = wx.BoxSizer( wx.HORIZONTAL )

		self.lblr = wx.StaticText( self, wx.ID_ANY, u"LR a :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblr.Wrap( -1 )

		self.lblr.SetToolTip( u"Learning ratting" )

		Hsz1.Add( self.lblr, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Rate = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 0.01, 0.01 )
		self.Rate.SetDigits( 3 )
		Hsz1.Add( self.Rate, 0, wx.ALL, 5 )


		Vsp19.Add( Hsz1, 0, wx.EXPAND, 5 )

		Hsz2 = wx.BoxSizer( wx.HORIZONTAL )

		self.lblI = wx.StaticText( self, wx.ID_ANY, u"Iteration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblI.Wrap( -1 )

		Hsz2.Add( self.lblI, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_spinCtrl1 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		Hsz2.Add( self.m_spinCtrl1, 0, wx.ALL, 5 )


		Vsp19.Add( Hsz2, 0, wx.EXPAND, 5 )

		Hsz3 = wx.BoxSizer( wx.HORIZONTAL )

		self.btn1 = wx.Button( self, wx.ID_ANY, u"Hyp. Plot", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz3.Add( self.btn1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsp19.Add( Hsz3, 0, wx.EXPAND, 5 )

		Hsz4 = wx.BoxSizer( wx.HORIZONTAL )

		self.btn2 = wx.Button( self, wx.ID_ANY, u"Cost. Plot", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz4.Add( self.btn2, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsp19.Add( Hsz4, 0, wx.EXPAND, 5 )

		Hsz5 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl3 = wx.StaticText( self, wx.ID_ANY, u"Theta ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl3.Wrap( -1 )

		Hsz5.Add( self.lbl3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl10 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		Hsz5.Add( self.m_textCtrl10, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsp19.Add( Hsz5, 0, wx.EXPAND, 5 )


		self.SetSizer( Vsp19 )
		self.Layout()

		# Connect Events
		self.btn1.Bind( wx.EVT_BUTTON, self.hplt )
		self.btn2.Bind( wx.EVT_BUTTON, self.cstplt )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def hplt( self, event ):
		event.Skip()

	def cstplt( self, event ):
		event.Skip()

