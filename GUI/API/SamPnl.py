# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## You Can Edit This File : This is wrong >>> PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx

###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.Text1 = wx.StaticText( self, wx.ID_ANY, u"This is a Demo Frame", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.Text1.Wrap( -1 )

		self.Text1.SetFont( wx.Font( 45, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer1.Add( self.Text1, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.button1 = wx.Button( self, wx.ID_ANY, u"Okey", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.button1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		# Connect Events
		self.button1.Bind( wx.EVT_BUTTON, self.retrn )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def retrn( self, event ):
		q = self.GetParent()
		q.Close()


