#In the name of GOD
#please put your code under here
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
## Class MyPanel1
###########################################################################
OPERATIONS = ('/', '*', '-', '+')
DIGITS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9','.')

class MyPanel1 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 329,450 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.Result = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.Result, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"C", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		self.m_button1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer3.Add( self.m_button1, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"/", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer3.Add( self.m_button2, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button3 = wx.Button( self, wx.ID_ANY, u"*", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer3.Add( self.m_button3, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button4 = wx.Button( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer3.Add( self.m_button4, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		gSizer1 = wx.GridSizer( 3, 3, 0, 0 )

		self.m_button9 = wx.Button( self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		gSizer1.Add( self.m_button9, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button10 = wx.Button( self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		gSizer1.Add( self.m_button10, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button11 = wx.Button( self, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		gSizer1.Add( self.m_button11, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button12 = wx.Button( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		gSizer1.Add( self.m_button12, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button13 = wx.Button( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		gSizer1.Add( self.m_button13, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button14 = wx.Button( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		gSizer1.Add( self.m_button14, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button15 = wx.Button( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		gSizer1.Add( self.m_button15, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button16 = wx.Button( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		gSizer1.Add( self.m_button16, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button17 = wx.Button( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		gSizer1.Add( self.m_button17, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer5.Add( gSizer1, 3, wx.EXPAND, 5 )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button7 = wx.Button( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer7.Add( self.m_button7, 2, wx.ALL|wx.EXPAND, 5 )

		self.m_button8 = wx.Button( self, wx.ID_ANY, u".", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer7.Add( self.m_button8, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer5.Add( bSizer7, 1, wx.EXPAND, 5 )


		bSizer4.Add( bSizer5, 3, wx.EXPAND, 5 )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"+", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer6.Add( self.m_button5, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button6 = wx.Button( self, wx.ID_ANY, u"=", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer6.Add( self.m_button6, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer4.Add( bSizer6, 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer4, 3, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

	def __del__( self ):
		pass
