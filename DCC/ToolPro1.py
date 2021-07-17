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

class MyPanel1 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 491,353 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		Hsz1 = wx.BoxSizer( wx.HORIZONTAL )

		self.P1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_RAISED|wx.TAB_TRAVERSAL )
		Vsz1 = wx.BoxSizer( wx.VERTICAL )

		Vsz11 = wx.BoxSizer( wx.VERTICAL )

		self.lbl1 = wx.StaticText( self.P1, wx.ID_ANY, u"List of Addable Tools and Programs", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl1.Wrap( -1 )

		Vsz11.Add( self.lbl1, 0, wx.ALL|wx.EXPAND, 5 )

		TPL1Choices = []
		self.TPL1 = wx.ListBox( self.P1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, TPL1Choices, wx.LB_ALWAYS_SB|wx.LB_HSCROLL )
		Vsz11.Add( self.TPL1, 1, wx.ALL|wx.EXPAND, 5 )


		Vsz1.Add( Vsz11, 1, wx.EXPAND, 5 )

		Hsz11 = wx.BoxSizer( wx.HORIZONTAL )

		self.btn1 = wx.Button( self.P1, wx.ID_ANY, u"Update", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz11.Add( self.btn1, 0, wx.ALL, 5 )

		self.btn2 = wx.Button( self.P1, wx.ID_ANY, u"To site", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz11.Add( self.btn2, 0, wx.ALL, 5 )


		Vsz1.Add( Hsz11, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.P1.SetSizer( Vsz1 )
		self.P1.Layout()
		Vsz1.Fit( self.P1 )
		Hsz1.Add( self.P1, 1, wx.EXPAND |wx.ALL, 5 )

		self.P2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_RAISED|wx.TAB_TRAVERSAL )
		Vsz2 = wx.BoxSizer( wx.VERTICAL )

		Vsz21 = wx.BoxSizer( wx.VERTICAL )

		self.lbl2 = wx.StaticText( self.P2, wx.ID_ANY, u"Description :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl2.Wrap( -1 )

		Vsz21.Add( self.lbl2, 0, wx.ALL, 5 )

		self.Desc = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		Vsz21.Add( self.Desc, 1, wx.ALL|wx.EXPAND, 5 )


		Vsz2.Add( Vsz21, 1, wx.EXPAND, 5 )

		Hsz21 = wx.BoxSizer( wx.HORIZONTAL )

		self.btn3 = wx.Button( self.P2, wx.ID_ANY, u"Preview", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz21.Add( self.btn3, 0, wx.ALL, 5 )

		self.btn4 = wx.Button( self.P2, wx.ID_ANY, u"Open-source", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz21.Add( self.btn4, 0, wx.ALL, 5 )


		Vsz2.Add( Hsz21, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		Vsz3 = wx.BoxSizer( wx.VERTICAL )

		Hsz31 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl3 = wx.StaticText( self.P2, wx.ID_ANY, u"Menu id", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl3.Wrap( -1 )

		Hsz31.Add( self.lbl3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.mid = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz31.Add( self.mid, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.btn5 = wx.Button( self.P2, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		self.btn5.SetToolTip( u"List of menu and id number" )

		Hsz31.Add( self.btn5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz31, 1, wx.EXPAND, 5 )

		Hsz32 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl4 = wx.StaticText( self.P2, wx.ID_ANY, u"Menu name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl4.Wrap( -1 )

		Hsz32.Add( self.lbl4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.mnm = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.mnm.Enable( False )

		Hsz32.Add( self.mnm, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz32, 1, wx.EXPAND, 5 )

		Hsz33 = wx.BoxSizer( wx.HORIZONTAL )

		self.btn6 = wx.Button( self.P2, wx.ID_ANY, u"Quick add", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz33.Add( self.btn6, 0, wx.ALL, 5 )

		self.btn7 = wx.Button( self.P2, wx.ID_ANY, u"How Add", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz33.Add( self.btn7, 0, wx.ALL, 5 )


		Vsz3.Add( Hsz33, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		Vsz2.Add( Vsz3, 0, wx.EXPAND, 5 )


		self.P2.SetSizer( Vsz2 )
		self.P2.Layout()
		Vsz2.Fit( self.P2 )
		Hsz1.Add( self.P2, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( Hsz1 )
		self.Layout()

		# Connect Events
		self.TPL1.Bind( wx.EVT_LISTBOX, self.slctlst )
		self.TPL1.Bind( wx.EVT_LISTBOX_DCLICK, self.slctlst )
		self.btn1.Bind( wx.EVT_BUTTON, self.updatlst )
		self.btn2.Bind( wx.EVT_BUTTON, self.brwsurl )
		self.btn3.Bind( wx.EVT_BUTTON, self.prvw )
		self.btn4.Bind( wx.EVT_BUTTON, self.opnsrc )
		self.btn5.Bind( wx.EVT_BUTTON, self.mnulst )
		self.btn6.Bind( wx.EVT_BUTTON, self.quikad )
		self.btn7.Bind( wx.EVT_BUTTON, self.howad )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def slctlst( self, event ):
		event.Skip()


	def updatlst( self, event ):
		event.Skip()

	def brwsurl( self, event ):
		event.Skip()

	def prvw( self, event ):
		event.Skip()

	def opnsrc( self, event ):
		event.Skip()

	def mnulst( self, event ):
		event.Skip()

	def quikad( self, event ):
		event.Skip()

	def howad( self, event ):
		event.Skip()


