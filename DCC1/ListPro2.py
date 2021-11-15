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

from Config.Init import *

import Database.MenuSet2 as MS
import Database.PostGet as PG
import GUI.proman as pro
import importlib
import importlib.util

###########################################################################
## Class MyPanel7
###########################################################################

class MyPanel1 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 570,470 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		Vsz1 = wx.BoxSizer( wx.VERTICAL )

		self.getMData = MS.GetData(u'Menu2.db', u'')
		self.setMDate = MS.SetData(u'', u'', u'')

		self.Splt1 = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D|wx.SP_LIVE_UPDATE|wx.SP_NO_XP_THEME|wx.SP_THIN_SASH )
		self.Splt1.Bind( wx.EVT_IDLE, self.Splt1OnIdle )

		self.P1 = wx.Panel( self.Splt1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		Vsz2 = wx.BoxSizer( wx.VERTICAL )

		self.Titr1 = wx.StaticText( self.P1, wx.ID_ANY, u"List of Programs and Tools can download", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Titr1.Wrap( -1 )

		Vsz2.Add( self.Titr1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.TLC1 = wx.dataview.TreeListCtrl( self.P1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.dataview.TL_DEFAULT_STYLE )
		self.TLC1.AppendColumn( u"ID", wx.COL_WIDTH_DEFAULT, wx.ALIGN_LEFT, wx.COL_RESIZABLE )
		self.TLC1.AppendColumn( u"Name", wx.COL_WIDTH_DEFAULT, wx.ALIGN_LEFT, wx.COL_RESIZABLE )

		Vsz2.Add( self.TLC1, 1, wx.EXPAND |wx.ALL, 5 )

		#Hsz1 = wx.BoxSizer( wx.HORIZONTAL )


		#Vsz2.Add( Hsz1, 0, wx.EXPAND, 5 )

		Hsz2 = wx.BoxSizer( wx.HORIZONTAL )

		self.CntSrv = wx.Button( self.P1, wx.ID_ANY, u"Connect to server ", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz2.Add( self.CntSrv, 1, wx.ALL, 5 )


		Vsz2.Add( Hsz2, 0, wx.EXPAND, 5 )

		Hsz3 = wx.BoxSizer( wx.HORIZONTAL )

		self.btn1 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		self.btn1.SetBitmap(wx.Bitmap(ICON16_PATH + u'application_add.png', wx.BITMAP_TYPE_ANY))
		self.btn1.SetToolTip(u"Add")
		Hsz3.Add( self.btn1, 0, wx.ALL, 5 )

		self.btn2 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		self.btn2.SetBitmap(wx.Bitmap(ICON16_PATH + u'application_edit.png', wx.BITMAP_TYPE_ANY))
		self.btn2.SetToolTip(u"Edit")
		Hsz3.Add( self.btn2, 0, wx.ALL, 5 )

		self.btn3 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		self.btn3.SetBitmap(wx.Bitmap(ICON16_PATH + u'application_delete.png', wx.BITMAP_TYPE_ANY))
		self.btn3.SetToolTip(u"Delete")
		Hsz3.Add( self.btn3, 0, wx.ALL, 5 )

		self.btn4 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		self.btn4.SetBitmap(wx.Bitmap(ICON16_PATH + u'application_form.png', wx.BITMAP_TYPE_ANY))
		self.btn4.SetToolTip(u"Preview")
		Hsz3.Add( self.btn4, 0, wx.ALL, 5 )

		self.btn5 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		self.btn5.SetBitmap(wx.Bitmap(ICON16_PATH + u'update.png', wx.BITMAP_TYPE_ANY))
		self.btn5.SetToolTip(u"Update")
		Hsz3.Add( self.btn5, 0, wx.ALL, 5 )

		self.btn6 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		self.btn6.SetBitmap(wx.Bitmap(ICON16_PATH + u'application_put.png', wx.BITMAP_TYPE_ANY))
		self.btn6.SetToolTip(u"Download")
		Hsz3.Add( self.btn6, 0, wx.ALL, 5 )

		self.btn7 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		self.btn7.SetBitmap(wx.Bitmap(ICON16_PATH + u'application_lightning.png', wx.BITMAP_TYPE_ANY))
		self.btn7.SetToolTip(u"Generate")
		Hsz3.Add( self.btn7, 0, wx.ALL, 5 )


		Vsz2.Add( Hsz3, 0, wx.EXPAND, 5 )


		self.P1.SetSizer( Vsz2 )
		self.P1.Layout()
		Vsz2.Fit( self.P1 )
		self.P2 = wx.Panel( self.Splt1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		Vsz3 = wx.BoxSizer( wx.VERTICAL )

		self.Titr2 = wx.StaticText( self.P2, wx.ID_ANY, u"Description", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Titr2.Wrap( -1 )

		Vsz3.Add( self.Titr2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		Hsz11 = wx.BoxSizer( wx.HORIZONTAL )

		self.Descr = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.TE_MULTILINE )
		Hsz11.Add( self.Descr, 1, wx.ALL|wx.EXPAND, 5 )


		Vsz3.Add( Hsz11, 1, wx.EXPAND, 5 )

		Hsz12 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl1 = wx.StaticText( self.P2, wx.ID_ANY, u"To Menu id ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl1.Wrap( -1 )

		Hsz12.Add( self.lbl1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld1 = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz12.Add( self.fld1, 1, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )

		self.btn1 = wx.Button( self.P2, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		Hsz12.Add( self.btn1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz12, 0, wx.EXPAND, 5 )

		Hsz13 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl2 = wx.StaticText( self.P2, wx.ID_ANY, u"To Directory", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl2.Wrap( -1 )

		Hsz13.Add( self.lbl2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.dir2 = wx.DirPickerCtrl( self.P2, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE|wx.DIRP_SMALL )
		Hsz13.Add( self.dir2, 1, wx.ALL, 5 )


		Vsz3.Add( Hsz13, 0, wx.EXPAND, 5 )

		Hsz14 = wx.BoxSizer( wx.HORIZONTAL )

		self.btn3 = wx.Button( self.P2, wx.ID_ANY, u"Download", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		Hsz14.Add( self.btn3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.gug1 = wx.Gauge( self.P2, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.gug1.SetValue( 0 )
		Hsz14.Add( self.gug1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz14, 0, wx.EXPAND, 5 )

		self.lin1 = wx.StaticLine( self.P2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		Vsz3.Add( self.lin1, 0, wx.EXPAND |wx.ALL, 5 )

		Hsz15 = wx.BoxSizer( wx.HORIZONTAL )

		self.chk1 = wx.CheckBox( self.P2, wx.ID_ANY, u"Check it ...", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz15.Add( self.chk1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz15, 0, wx.EXPAND, 5 )

		Hsz16 = wx.BoxSizer( wx.VERTICAL )

		self.lbl3 = wx.StaticText( self.P2, wx.ID_ANY, u"Message", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl3.Wrap( -1 )

		Hsz16.Add( self.lbl3, 0, wx.ALL, 5 )

		self.msag = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_BESTWRAP|wx.TE_MULTILINE )
		Hsz16.Add( self.msag, 1, wx.ALL|wx.EXPAND, 5 )


		Vsz3.Add( Hsz16, 1, wx.EXPAND, 5 )


		self.P2.SetSizer( Vsz3 )
		self.P2.Layout()
		Vsz3.Fit( self.P2 )
		self.Splt1.SplitVertically( self.P1, self.P2, 266 )
		Vsz1.Add( self.Splt1, 1, wx.EXPAND, 5 )


		self.SetSizer( Vsz1 )
		self.Layout()

		# Connect Events
		self.CntSrv.Bind( wx.EVT_BUTTON, self.consrv )
		self.btn1.Bind( wx.EVT_BUTTON, self.addit )
		self.btn2.Bind( wx.EVT_BUTTON, self.editit )
		self.btn3.Bind( wx.EVT_BUTTON, self.delit )
		self.btn4.Bind( wx.EVT_BUTTON, self.prw )
		self.btn5.Bind( wx.EVT_BUTTON, self.upd )
		self.btn6.Bind( wx.EVT_BUTTON, self.aply )
		self.btn7.Bind( wx.EVT_BUTTON, self.gnrt )
		self.btn1.Bind( wx.EVT_BUTTON, self.mnuid )
		self.dir2.Bind( wx.EVT_DIRPICKER_CHANGED, self.thsdir )
		self.btn3.Bind( wx.EVT_BUTTON, self.dnlod )
		self.chk1.Bind( wx.EVT_CHECKBOX, self.chkdon )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def consrv( self, event ):
		event.Skip()

	def addit( self, event ):
		event.Skip()

	def editit( self, event ):
		event.Skip()

	def delit( self, event ):
		event.Skip()

	def prw( self, event ):
		event.Skip()

	def upd( self, event ):
		event.Skip()

	def aply( self, event ):
		event.Skip()

	def gnrt( self, event ):
		event.Skip()

	def mnuid( self, event ):
		event.Skip()

	def thsdir( self, event ):
		event.Skip()

	def dnlod( self, event ):
		event.Skip()

	def chkdon( self, event ):
		event.Skip()

	def Splt1OnIdle( self, event ):
		self.Splt1.SetSashPosition( 266 )
		self.Splt1.Unbind( wx.EVT_IDLE )


