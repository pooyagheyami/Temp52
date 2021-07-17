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
## Class MyPanel4
###########################################################################

class MyPanel1 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 558,450 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		Vsz1 = wx.BoxSizer( wx.VERTICAL )

		self.Splt1 = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D|wx.SP_LIVE_UPDATE|wx.SP_NO_XP_THEME|wx.SP_THIN_SASH )
		#self.Splt1.SetSashGravity( -1 )
		self.Splt1.Bind( wx.EVT_IDLE, self.Splt1OnIdle )

		self.P1 = wx.Panel( self.Splt1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		Vsz2 = wx.BoxSizer( wx.VERTICAL )

		self.lbl1 = wx.StaticText( self.P1, wx.ID_ANY, u"List of toolbar:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl1.Wrap( -1 )

		Vsz2.Add( self.lbl1, 0, wx.ALL|wx.EXPAND, 5 )

		self.DVC1 = wx.dataview.DataViewCtrl( self.P1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Col1 = self.DVC1.AppendTextColumn( u"Name ToolBar", 0, wx.dataview.DATAVIEW_CELL_INERT, 178, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.Col2 = self.DVC1.AppendTextColumn( u"ID", 1, wx.dataview.DATAVIEW_CELL_INERT, 45, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		Vsz2.Add( self.DVC1, 1, wx.ALL|wx.EXPAND, 5 )

		Hsz1 = wx.BoxSizer( wx.HORIZONTAL )

		self.btn1 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.btn1.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_NEW, wx.ART_OTHER ) )
		Hsz1.Add( self.btn1, 0, wx.ALL, 5 )

		self.btn2 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.btn2.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_UNDO, wx.ART_OTHER ) )
		Hsz1.Add( self.btn2, 0, wx.ALL, 5 )

		self.btn3 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.btn3.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_DELETE, wx.ART_OTHER ) )
		Hsz1.Add( self.btn3, 0, wx.ALL, 5 )

		self.btn4 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.btn4.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_PLUS, wx.ART_OTHER ) )
		Hsz1.Add( self.btn4, 0, wx.ALL, 5 )

		self.btn5 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.btn5.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_MINUS, wx.ART_OTHER ) )
		Hsz1.Add( self.btn5, 0, wx.ALL, 5 )

		self.btn6 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.btn6.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_REDO, wx.ART_OTHER ) )
		Hsz1.Add( self.btn6, 0, wx.ALL, 5 )


		Vsz2.Add( Hsz1, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.P1.SetSizer( Vsz2 )
		self.P1.Layout()
		Vsz2.Fit( self.P1 )
		self.P2 = wx.Panel( self.Splt1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		Vsz3 = wx.BoxSizer( wx.VERTICAL )

		self.titr = wx.StaticText( self.P2, wx.ID_ANY, u"Group:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.titr.Wrap( -1 )

		Vsz3.Add( self.titr, 0, wx.ALL|wx.EXPAND, 5 )

		self.grup = wx.SpinCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		Vsz3.Add( self.grup, 0, wx.ALL, 5 )

		Hsz2 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl2 = wx.StaticText( self.P2, wx.ID_ANY, u"ID", wx.DefaultPosition, wx.Size( 54,-1 ), 0 )
		self.lbl2.Wrap( -1 )

		Hsz2.Add( self.lbl2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld1 = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		Hsz2.Add( self.fld1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.lbl3 = wx.StaticText( self.P2, wx.ID_ANY, u"Access", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl3.Wrap( -1 )

		Hsz2.Add( self.lbl3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld2 = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		Hsz2.Add( self.fld2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.codgnr = wx.Button( self.P2, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		Hsz2.Add( self.codgnr, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz2, 1, wx.EXPAND, 5 )

		Hsz3 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl4 = wx.StaticText( self.P2, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.Size( 54,-1 ), 0 )
		self.lbl4.Wrap( -1 )

		Hsz3.Add( self.lbl4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld3 = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz3.Add( self.fld3, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz3, 1, wx.EXPAND, 5 )

		Hsz5 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl6 = wx.StaticText( self.P2, wx.ID_ANY, u"Icon", wx.DefaultPosition, wx.Size( 54,-1 ), 0 )
		self.lbl6.Wrap( -1 )

		Hsz5.Add( self.lbl6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.IcnFile1 = wx.FilePickerCtrl( self.P2, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_SMALL )
		Hsz5.Add( self.IcnFile1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz5, 1, wx.EXPAND, 5 )

		self.btmp1 = wx.StaticBitmap( self.P2, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		Vsz3.Add( self.btmp1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		Hsz4 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl5 = wx.StaticText( self.P2, wx.ID_ANY, u"Short text", wx.DefaultPosition, wx.Size( 54,-1 ), 0 )
		self.lbl5.Wrap( -1 )

		Hsz4.Add( self.lbl5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld4 = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz4.Add( self.fld4, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz4, 1, wx.EXPAND, 5 )

		Hsz6 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl7 = wx.StaticText( self.P2, wx.ID_ANY, u"Long text", wx.DefaultPosition, wx.Size( 54,-1 ), 0 )
		self.lbl7.Wrap( -1 )

		Hsz6.Add( self.lbl7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld6 = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz6.Add( self.fld6, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz6, 1, wx.EXPAND, 5 )

		Hsz7 = wx.BoxSizer( wx.HORIZONTAL )

		self.chk1 = wx.CheckBox( self.P2, wx.ID_ANY, u"Disable", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz7.Add( self.chk1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.chk2 = wx.CheckBox( self.P2, wx.ID_ANY, u"Hide", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz7.Add( self.chk2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz7, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.lin1 = wx.StaticLine( self.P2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		Vsz3.Add( self.lin1, 0, wx.EXPAND |wx.ALL, 5 )

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
		Vsz4.Add( self.prgfld, 0, wx.ALL|wx.EXPAND, 5 )

		self.lbl9 = wx.StaticText( self.P2, wx.ID_ANY, u"Directory:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl9.Wrap( -1 )

		Vsz4.Add( self.lbl9, 0, wx.ALL, 5 )


		Vsz3.Add( Vsz4, 1, wx.EXPAND, 5 )


		self.P2.SetSizer( Vsz3 )
		self.P2.Layout()
		Vsz3.Fit( self.P2 )
		self.Splt1.SplitVertically( self.P1, self.P2, 244 )
		Vsz1.Add( self.Splt1, 1, wx.EXPAND, 5 )


		self.SetSizer( Vsz1 )
		self.Layout()

		# Connect Events
		self.DVC1.Bind( wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED, self.slctmnu, id = wx.ID_ANY )
		self.btn1.Bind( wx.EVT_BUTTON, self.addit )
		self.btn2.Bind( wx.EVT_BUTTON, self.edtit )
		self.btn3.Bind( wx.EVT_BUTTON, self.delit )
		self.btn4.Bind( wx.EVT_BUTTON, self.newgrp )
		self.btn5.Bind( wx.EVT_BUTTON, self.delgrp )
		self.btn6.Bind( wx.EVT_BUTTON, self.adlin )
		self.codgnr.Bind( wx.EVT_BUTTON, self.gnrcod )
		self.IcnFile1.Bind( wx.EVT_FILEPICKER_CHANGED, self.chgicn )
		self.chk1.Bind( wx.EVT_CHECKBOX, self.disbl )
		self.chk2.Bind( wx.EVT_CHECKBOX, self.hidit )
		self.probtn.Bind( wx.EVT_BUTTON, self.prglst )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def slctmnu( self, event ):
		event.Skip()

	def addit( self, event ):
		event.Skip()

	def edtit( self, event ):
		event.Skip()

	def delit( self, event ):
		event.Skip()

	def newgrp( self, event ):
		event.Skip()

	def delgrp( self, event ):
		event.Skip()

	def adlin( self, event ):
		event.Skip()

	def gnrcod( self, event ):
		event.Skip()

	def chgicn( self, event ):
		event.Skip()

	def disbl( self, event ):
		event.Skip()

	def hidit( self, event ):
		event.Skip()

	def prglst( self, event ):
		event.Skip()

	def Splt1OnIdle( self, event ):
		self.Splt1.SetSashPosition( 244 )
		self.Splt1.Unbind( wx.EVT_IDLE )


