# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from Config.Init import *

###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 150,350 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		Vsz1 = wx.BoxSizer( wx.VERTICAL )

		self.btn1 = wx.Button( self, wx.ID_ANY, u"MenuBar", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.btn1.SetBitmap( wx.Bitmap( ICON16_PATH+u"menubar.png", wx.BITMAP_TYPE_ANY ) )
		Vsz1.Add( self.btn1, 0, wx.ALL|wx.EXPAND, 5 )

		self.btn2 = wx.Button( self, wx.ID_ANY, u"MenuItem", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.btn2.SetBitmap( wx.Bitmap( ICON16_PATH+u"menu_item.png", wx.BITMAP_TYPE_ANY ) )
		Vsz1.Add( self.btn2, 0, wx.ALL|wx.EXPAND, 5 )

		self.btn3 = wx.Button( self, wx.ID_ANY, u"ToolBar", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.btn3.SetBitmap( wx.Bitmap( ICON16_PATH+u"toolbar.png", wx.BITMAP_TYPE_ANY ) )
		Vsz1.Add( self.btn3, 0, wx.ALL|wx.EXPAND, 5 )

		self.btn4 = wx.Button( self, wx.ID_ANY, u"Database", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.btn4.SetBitmap( wx.Bitmap( ICON16_PATH+u"database.png", wx.BITMAP_TYPE_ANY ) )
		Vsz1.Add( self.btn4, 0, wx.ALL|wx.EXPAND, 5 )

		self.btn5 = wx.Button( self, wx.ID_ANY, u"Form", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.btn5.SetBitmap( wx.Bitmap( ICON16_PATH+u"form.png", wx.BITMAP_TYPE_ANY ) )
		Vsz1.Add( self.btn5, 0, wx.ALL|wx.EXPAND, 5 )

		self.btn6 = wx.Button( self, wx.ID_ANY, u"Panel", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.btn6.SetBitmap( wx.Bitmap( ICON16_PATH+u"panel.png", wx.BITMAP_TYPE_ANY ) )
		Vsz1.Add( self.btn6, 0, wx.ALL|wx.EXPAND, 5 )


		Vsz1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btnbak = wx.Button( self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		Vsz1.Add( self.btnbak, 0, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( Vsz1 )
		self.Layout()

		# Connect Events
		self.btn1.Bind( wx.EVT_BUTTON, self.Dombr )
		self.btn2.Bind( wx.EVT_BUTTON, self.Doitm )
		self.btn3.Bind( wx.EVT_BUTTON, self.Dotlb )
		self.btn4.Bind( wx.EVT_BUTTON, self.Dodbf )
		self.btn5.Bind( wx.EVT_BUTTON, self.Dofrm )
		self.btn6.Bind( wx.EVT_BUTTON, self.Dopnl )
		self.btnbak.Bind( wx.EVT_BUTTON, self.Docols )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Dombr( self, event ):
		from Temps.MenuDev1 import MyPanel3
		self.b = wx.Frame(self, style=wx.CAPTION | wx.CLOSE_BOX | wx.FRAME_FLOAT_ON_PARENT | wx.TAB_TRAVERSAL)
		self.panel = MyPanel3(self.b)
		self.b.SetSize((500, 180))
		self.b.Show()


	def Doitm( self, event ):
		from Temps.MenuDev1 import MyPanel1
		self.b = wx.Frame(self, style=wx.CAPTION | wx.CLOSE_BOX | wx.FRAME_FLOAT_ON_PARENT | wx.TAB_TRAVERSAL)
		self.panel = MyPanel1(self.b)
		self.b.SetSize((650, 300))
		self.b.Show()

	def Dotlb( self, event ):
		from GUI.API.ToolBar1 import MyPanel1
		self.b = wx.Frame(self, style=wx.CAPTION | wx.CLOSE_BOX | wx.FRAME_FLOAT_ON_PARENT | wx.TAB_TRAVERSAL)
		self.panel = MyPanel1(self.b)
		self.b.SetSize((540, 280))
		self.b.Show()

	def Dodbf( self, event ):
		event.Skip()

	def Dofrm( self, event ):
		event.Skip()

	def Dopnl( self, event ):
		event.Skip()

	def Docols( self, event ):
		q = self.GetParent()
		q.Close()
