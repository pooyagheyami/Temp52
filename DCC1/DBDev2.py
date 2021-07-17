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
## Class MyPanel6
###########################################################################

class MyPanel1 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,450 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		Vsz1 = wx.BoxSizer( wx.VERTICAL )

		self.Splt1 = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D|wx.SP_LIVE_UPDATE|wx.SP_NO_XP_THEME|wx.SP_THIN_SASH )
		self.Splt1.Bind( wx.EVT_IDLE, self.Splt1OnIdle )

		self.P1 = wx.Panel( self.Splt1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		Vsz2 = wx.BoxSizer( wx.VERTICAL )

		self.lbl0 = wx.StaticText( self.P1, wx.ID_ANY, u"Select database", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl0.Wrap( -1 )

		Vsz2.Add( self.lbl0, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.dbfile = wx.FilePickerCtrl( self.P1, wx.ID_ANY, wx.EmptyString, u"Select Database file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_OPEN|wx.FLP_SMALL )
		Vsz2.Add( self.dbfile, 0, wx.ALL|wx.EXPAND, 5 )

		self.lbl1 = wx.StaticText( self.P1, wx.ID_ANY, u"List of Tabel:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl1.Wrap( -1 )

		Vsz2.Add( self.lbl1, 0, wx.ALL, 5 )

		self.DVC1 = wx.dataview.DataViewCtrl( self.P1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Col1 = self.DVC1.AppendTextColumn( u"Name", 0, wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.Col2 = self.DVC1.AppendTextColumn( u"Name", 0, wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.Col3 = self.DVC1.AppendTextColumn( u"Name", 0, wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		Vsz2.Add( self.DVC1, 1, wx.ALL|wx.EXPAND, 5 )

		Hsz1 = wx.BoxSizer( wx.HORIZONTAL )

		self.btn1 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.btn1.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_NEW, wx.ART_OTHER ) )
		self.btn1.SetToolTip( u"Add" )

		Hsz1.Add( self.btn1, 0, wx.ALL, 5 )

		self.btn2 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		Hsz1.Add( self.btn2, 0, wx.ALL, 5 )

		self.btn3 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		Hsz1.Add( self.btn3, 0, wx.ALL, 5 )

		self.btn4 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		Hsz1.Add( self.btn4, 0, wx.ALL, 5 )

		self.btn5 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		Hsz1.Add( self.btn5, 0, wx.ALL, 5 )

		self.btn6 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		Hsz1.Add( self.btn6, 0, wx.ALL, 5 )


		Vsz2.Add( Hsz1, 0, wx.EXPAND, 5 )


		self.P1.SetSizer( Vsz2 )
		self.P1.Layout()
		Vsz2.Fit( self.P1 )
		self.P2 = wx.Panel( self.Splt1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		Vsz3 = wx.BoxSizer( wx.VERTICAL )

		self.lbl2 = wx.StaticText( self.P2, wx.ID_ANY, u"List of fields", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl2.Wrap( -1 )

		Vsz3.Add( self.lbl2, 0, wx.ALL|wx.EXPAND, 5 )

		self.DVC1 = wx.dataview.DataViewCtrl( self.P2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Col1 = self.DVC1.AppendTextColumn( u"Name", 0, wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.Col2 = self.DVC1.AppendTextColumn( u"Name", 0, wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		Vsz3.Add( self.DVC1, 1, wx.ALL|wx.EXPAND, 5 )

		Hsz2 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl3 = wx.StaticText( self.P2, wx.ID_ANY, u"Method in program", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl3.Wrap( -1 )

		Hsz2.Add( self.lbl3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		chs1Choices = [ u"set", u"get", u"both" ]
		self.chs1 = wx.Choice( self.P2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, chs1Choices, 0 )
		self.chs1.SetSelection( 0 )
		Hsz2.Add( self.chs1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz2, 0, wx.EXPAND, 5 )

		Hsz3 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl4 = wx.StaticText( self.P2, wx.ID_ANY, u"Program Statments", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl4.Wrap( -1 )

		Hsz3.Add( self.lbl4, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.btnps = wx.Button( self.P2, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		Hsz3.Add( self.btnps, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz3, 0, wx.EXPAND, 5 )

		self.fldprg = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		Vsz3.Add( self.fldprg, 1, wx.ALL|wx.EXPAND, 5 )

		Hsz4 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl5 = wx.StaticText( self.P2, wx.ID_ANY, u"SQL  Statments", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl5.Wrap( -1 )

		Hsz4.Add( self.lbl5, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.btnss = wx.Button( self.P2, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		Hsz4.Add( self.btnss, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz4, 0, wx.EXPAND, 5 )

		self.fldsql = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		Vsz3.Add( self.fldsql, 1, wx.ALL|wx.EXPAND, 5 )

		Hsz5 = wx.BoxSizer( wx.HORIZONTAL )

		self.btn7 = wx.Button( self.P2, wx.ID_ANY, u"To CVS", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz5.Add( self.btn7, 0, wx.ALL, 5 )

		self.btn8 = wx.Button( self.P2, wx.ID_ANY, u"To Excel", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz5.Add( self.btn8, 0, wx.ALL, 5 )

		self.btn9 = wx.Button( self.P2, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		self.btn9.SetToolTip( u"Extended" )

		Hsz5.Add( self.btn9, 0, wx.ALL, 5 )


		Vsz3.Add( Hsz5, 0, wx.EXPAND, 5 )


		self.P2.SetSizer( Vsz3 )
		self.P2.Layout()
		Vsz3.Fit( self.P2 )
		self.Splt1.SplitVertically( self.P1, self.P2, 232 )
		Vsz1.Add( self.Splt1, 1, wx.EXPAND, 5 )


		self.SetSizer( Vsz1 )
		self.Layout()

		# Connect Events
		self.DVC1.Bind( wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED, self.slctitm, id = wx.ID_ANY )
		self.btn1.Bind( wx.EVT_BUTTON, self.Addit )
		self.btn2.Bind( wx.EVT_BUTTON, self.edtit )
		self.btn3.Bind( wx.EVT_BUTTON, self.delit )
		self.btn4.Bind( wx.EVT_BUTTON, self.comit )
		self.btn5.Bind( wx.EVT_BUTTON, self.recomt )
		self.btn6.Bind( wx.EVT_BUTTON, self.brows )
		self.DVC1.Bind( wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED, self.slctitm, id = wx.ID_ANY )
		self.chs1.Bind( wx.EVT_CHOICE, self.chgmtd )
		self.btnps.Bind( wx.EVT_BUTTON, self.prgstm )
		self.btnss.Bind( wx.EVT_BUTTON, self.sqlstm )
		self.btn7.Bind( wx.EVT_BUTTON, self.tocvs )
		self.btn8.Bind( wx.EVT_BUTTON, self.toexl )
		self.btn9.Bind( wx.EVT_BUTTON, self.extnd )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def slctitm( self, event ):
		event.Skip()

	def Addit( self, event ):
		event.Skip()

	def edtit( self, event ):
		event.Skip()

	def delit( self, event ):
		event.Skip()

	def comit( self, event ):
		event.Skip()

	def recomt( self, event ):
		event.Skip()

	def brows( self, event ):
		event.Skip()


	def chgmtd( self, event ):
		event.Skip()

	def prgstm( self, event ):
		event.Skip()

	def sqlstm( self, event ):
		event.Skip()

	def tocvs( self, event ):
		event.Skip()

	def toexl( self, event ):
		event.Skip()

	def extnd( self, event ):
		event.Skip()

	def Splt1OnIdle( self, event ):
		self.Splt1.SetSashPosition( 232 )
		self.Splt1.Unbind( wx.EVT_IDLE )


