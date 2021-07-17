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

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 539,276 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		Vsz1 = wx.BoxSizer( wx.VERTICAL )

		Hsz1 = wx.WrapSizer( wx.HORIZONTAL, 0 )

		self.txt1 = wx.StaticText( self, wx.ID_ANY, u"Toolbar Id", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.txt1.Wrap( -1 )

		Hsz1.Add( self.txt1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz1.Add( self.fld1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.txt2 = wx.StaticText( self, wx.ID_ANY, u"Tool name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt2.Wrap( -1 )

		Hsz1.Add( self.txt2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz1.Add( self.fld2, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz1.Add( Hsz1, 1, wx.EXPAND, 5 )

		Hsz2 = wx.WrapSizer( wx.HORIZONTAL, 0 )

		self.txt3 = wx.StaticText( self, wx.ID_ANY, u"Toolbar Icon", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.txt3.Wrap( -1 )

		Hsz2.Add( self.txt3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.file1 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.png;*.bmp;*.jpg", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_SMALL )
		Hsz2.Add( self.file1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz2.Add( self.m_bitmap1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz1.Add( Hsz2, 1, wx.EXPAND, 5 )

		Hsz3 = wx.WrapSizer( wx.HORIZONTAL, 0 )

		self.txt4 = wx.StaticText( self, wx.ID_ANY, u"Short text", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.txt4.Wrap( -1 )

		Hsz3.Add( self.txt4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz3.Add( self.fld3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.txt5 = wx.StaticText( self, wx.ID_ANY, u"Long text", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt5.Wrap( -1 )

		Hsz3.Add( self.txt5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz3.Add( self.fld4, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		Vsz1.Add( Hsz3, 1, wx.EXPAND, 5 )

		Hsz4 = wx.WrapSizer( wx.HORIZONTAL, 0 )

		self.txt6 = wx.StaticText( self, wx.ID_ANY, u"Program", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.txt6.Wrap( -1 )

		Hsz4.Add( self.txt6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.file2 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*;*.py", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_SMALL )
		Hsz4.Add( self.file2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz4.Add( self.fld5, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz1.Add( Hsz4, 1, wx.EXPAND, 5 )

		Hsz5 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.Box1 = wx.CheckBox( self, wx.ID_ANY, u"Disable", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz5.Add( self.Box1, 0, wx.ALL, 5 )

		self.Box2 = wx.CheckBox( self, wx.ID_ANY, u"Hiden", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz5.Add( self.Box2, 0, wx.ALL, 5 )


		Vsz1.Add( Hsz5, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		Hsz6 = wx.WrapSizer( wx.HORIZONTAL, 0 )


		Hsz6.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btn1 = wx.Button( self, wx.ID_ANY, u"Cancle", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz6.Add( self.btn1, 0, wx.ALL, 5 )

		self.btn2 = wx.Button( self, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz6.Add( self.btn2, 0, wx.ALL, 5 )


		Vsz1.Add( Hsz6, 0, wx.EXPAND, 5 )


		self.SetSizer( Vsz1 )
		self.Layout()

		# Connect Events
		self.file1.Bind( wx.EVT_FILEPICKER_CHANGED, self.icnfil )
		self.file2.Bind( wx.EVT_FILEPICKER_CHANGED, self.prgfil )
		self.Box1.Bind( wx.EVT_CHECKBOX, self.disbl )
		self.Box2.Bind( wx.EVT_CHECKBOX, self.hidn )
		self.btn1.Bind( wx.EVT_BUTTON, self.cncl )
		self.btn2.Bind( wx.EVT_BUTTON, self.Doit )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def icnfil( self, event ):
		event.Skip()

	def prgfil( self, event ):
		event.Skip()

	def disbl( self, event ):
		event.Skip()

	def hidn( self, event ):
		event.Skip()

	def cncl( self, event ):
		q = self.GetParent()
		q.Close()

	def Doit( self, event ):
		event.Skip()

