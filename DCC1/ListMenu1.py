# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview

###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,450 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		Vsz1 = wx.BoxSizer( wx.VERTICAL )

		self.Splt1 = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D|wx.SP_LIVE_UPDATE|wx.SP_NO_XP_THEME|wx.SP_THIN_SASH )
		self.Splt1.SetSashGravity( -1 )
		self.Splt1.Bind( wx.EVT_IDLE, self.Splt1OnIdle )

		self.P1 = wx.Panel( self.Splt1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		Vsz2 = wx.BoxSizer( wx.VERTICAL )

		self.lbl1 = wx.StaticText( self.P1, wx.ID_ANY, u"List of menu:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl1.Wrap( -1 )

		Vsz2.Add( self.lbl1, 0, wx.ALL|wx.EXPAND, 5 )

		self.DVC1 = wx.dataview.DataViewCtrl( self.P1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Col1 = self.DVC1.AppendTextColumn( u"Name Menu", 0, wx.dataview.DATAVIEW_CELL_INERT, 178, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.Col2 = self.DVC1.AppendTextColumn( u"ID", 1, wx.dataview.DATAVIEW_CELL_INERT, 45, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		Vsz2.Add( self.DVC1, 1, wx.ALL|wx.EXPAND, 5 )

		Hsz1 = wx.BoxSizer( wx.HORIZONTAL )

		self.btn2 = wx.Button( self.P1, wx.ID_ANY, u"Return", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz1.Add( self.btn2, 0, wx.ALL, 5 )

		self.btn1 = wx.Button( self.P1, wx.ID_ANY, u"Select", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz1.Add( self.btn1, 0, wx.ALL, 5 )


		Vsz2.Add( Hsz1, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.P1.SetSizer( Vsz2 )
		self.P1.Layout()
		Vsz2.Fit( self.P1 )
		self.P2 = wx.Panel( self.Splt1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		Vsz3 = wx.BoxSizer( wx.VERTICAL )

		Hsz2 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl2 = wx.StaticText( self.P2, wx.ID_ANY, u"ID", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl2.Wrap( -1 )

		Hsz2.Add( self.lbl2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld1 = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.TE_READONLY )
		Hsz2.Add( self.fld1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.lbl3 = wx.StaticText( self.P2, wx.ID_ANY, u"Access", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl3.Wrap( -1 )

		Hsz2.Add( self.lbl3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld2 = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.TE_READONLY )
		Hsz2.Add( self.fld2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz2, 1, wx.EXPAND, 5 )

		Hsz3 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl4 = wx.StaticText( self.P2, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl4.Wrap( -1 )

		Hsz3.Add( self.lbl4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld3 = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		Hsz3.Add( self.fld3, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz3, 1, wx.EXPAND, 5 )

		Hsz4 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl5 = wx.StaticText( self.P2, wx.ID_ANY, u"ShortCut", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl5.Wrap( -1 )

		Hsz4.Add( self.lbl5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld4 = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		Hsz4.Add( self.fld4, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz4, 1, wx.EXPAND, 5 )

		Hsz5 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl6 = wx.StaticText( self.P2, wx.ID_ANY, u"Icon", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl6.Wrap( -1 )

		Hsz5.Add( self.lbl6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.btmp1 = wx.StaticBitmap( self.P2, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz5.Add( self.btmp1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


		Vsz3.Add( Hsz5, 1, wx.EXPAND, 5 )

		Hsz6 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl7 = wx.StaticText( self.P2, wx.ID_ANY, u"Status", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl7.Wrap( -1 )

		Hsz6.Add( self.lbl7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld6 = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		Hsz6.Add( self.fld6, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz6, 1, wx.EXPAND, 5 )

		Hsz7 = wx.BoxSizer( wx.HORIZONTAL )

		self.chk1 = wx.CheckBox( self.P2, wx.ID_ANY, u"Disable", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.chk1.Enable( False )

		Hsz7.Add( self.chk1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.chk2 = wx.CheckBox( self.P2, wx.ID_ANY, u"Hide", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.chk2.Enable( False )

		Hsz7.Add( self.chk2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz7, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.lin1 = wx.StaticLine( self.P2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		Vsz3.Add( self.lin1, 0, wx.EXPAND |wx.ALL, 5 )

		Hsz8 = wx.BoxSizer( wx.HORIZONTAL )

		self.rdio1 = wx.RadioButton( self.P2, wx.ID_ANY, u"Normal", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.rdio1.Enable( False )

		Hsz8.Add( self.rdio1, 0, wx.ALL, 5 )

		self.rdio2 = wx.RadioButton( self.P2, wx.ID_ANY, u"Check", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.rdio2.Enable( False )

		Hsz8.Add( self.rdio2, 0, wx.ALL, 5 )

		self.rdio3 = wx.RadioButton( self.P2, wx.ID_ANY, u"Radio", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.rdio3.Enable( False )

		Hsz8.Add( self.rdio3, 0, wx.ALL, 5 )


		Vsz3.Add( Hsz8, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		Hsz9 = wx.BoxSizer( wx.HORIZONTAL )

		self.rdio4 = wx.RadioButton( self.P2, wx.ID_ANY, u"Sub Menu", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.rdio4.Enable( False )

		Hsz9.Add( self.rdio4, 0, wx.ALL, 5 )


		Vsz3.Add( Hsz9, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.lin2 = wx.StaticLine( self.P2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		Vsz3.Add( self.lin2, 0, wx.EXPAND |wx.ALL, 5 )

		Hsz10 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl8 = wx.StaticText( self.P2, wx.ID_ANY, u"Program:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl8.Wrap( -1 )

		Hsz10.Add( self.lbl8, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.probtn = wx.Button( self.P2, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		self.probtn.SetToolTip( u"list of program can changed" )

		Hsz10.Add( self.probtn, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz10, 1, wx.EXPAND, 5 )

		Vsz4 = wx.BoxSizer( wx.VERTICAL )

		self.prgfld = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Vsz4.Add( self.prgfld, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		Vsz3.Add( Vsz4, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.P2.SetSizer( Vsz3 )
		self.P2.Layout()
		Vsz3.Fit( self.P2 )
		self.Splt1.SplitVertically( self.P1, self.P2, 0 )
		Vsz1.Add( self.Splt1, 1, wx.EXPAND, 5 )


		self.SetSizer( Vsz1 )
		self.Layout()

		# Connect Events
		self.DVC1.Bind( wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED, self.slctmnu, id = wx.ID_ANY )
		self.DVC1.Bind( wx.dataview.EVT_DATAVIEW_SELECTION_CHANGED, self.slctitm, id = wx.ID_ANY )
		self.btn2.Bind( wx.EVT_BUTTON, self.rtrn )
		self.btn1.Bind( wx.EVT_BUTTON, self.slct )
		self.probtn.Bind( wx.EVT_BUTTON, self.prglst )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def slctmnu( self, event ):
		event.Skip()

	def slctitm( self, event ):
		event.Skip()

	def rtrn( self, event ):
		event.Skip()

	def slct( self, event ):
		event.Skip()

	def prglst( self, event ):
		event.Skip()

	def Splt1OnIdle( self, event ):
		self.Splt1.SetSashPosition( 0 )
		self.Splt1.Unbind( wx.EVT_IDLE )


