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

class MyPanel1 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 303,192 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.Text1 = wx.StaticText( self, wx.ID_ANY, u"Please Write Data1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Text1.Wrap( -1 )

		bSizer2.Add( self.Text1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.Ctrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.Ctrl1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.Text2 = wx.StaticText( self, wx.ID_ANY, u"Please Write Data2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Text2.Wrap( -1 )

		bSizer2.Add( self.Text2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.Ctrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.Ctrl2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer1.Add( bSizer2, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"apply", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer1.Add( bSizer3, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.Docancel )
		self.m_button2.Bind( wx.EVT_BUTTON, self.Doapply )

	def __del__( self ):
		pass

	# Virtual event handlers, overide them in your derived class
	def getData( self ):
		pass

	def Docancel( self, event ):
		q = self.GetParent()
		q.Close()

	def Doapply( self, event ):
		q = self.GetParent()
		q.Close()



