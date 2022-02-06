#In the name of GOD
#DB Generate Add line for Connect DB to Program
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
## Class MyPanel
###########################################################################

class TxtPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		Vsz1 = wx.BoxSizer( wx.VERTICAL )

		self.Txt = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_DONTWRAP|wx.TE_LEFT|wx.TE_MULTILINE )
		Vsz1.Add( self.Txt, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( Vsz1 )
		self.Layout()

		# Connect Events
		self.Txt.Bind(wx.EVT_RIGHT_DOWN, self.domnu)

	def __del__( self ):
		pass

	# Virtual event handlers, overide them in your derived class
	def domnu(self, event):
		m1 = wx.Menu()
		itm1  = wx.MenuItem(m1,wx.ID_ANY,u'Copy Select',wx.EmptyString, wx.ITEM_NORMAL )
		m1.Append(itm1)
		m1.AppendSeparator()
		itm2 = wx.MenuItem(m1, wx.ID_ANY, u'Select All', wx.EmptyString, wx.ITEM_NORMAL)
		m1.Append(itm2)
		m1.AppendSeparator()
		itm3 = wx.MenuItem(m1, wx.ID_ANY, u'Return ', wx.EmptyString, wx.ITEM_NORMAL)
		m1.Append(itm3)
		self.Bind(wx.EVT_MENU, self.doitm, id=itm1.GetId())
		self.Bind(wx.EVT_MENU, self.doitm, id=itm2.GetId())
		self.Bind(wx.EVT_MENU, self.doitm, id=itm3.GetId())
		self.PopupMenu(m1)
		m1.Destroy()

	def doitm(self, event):
		mnu = event.GetEventObject()
		#print(mnu.GetLabelText(event.GetId()))
		lbl = mnu.GetLabelText(event.GetId())
		if lbl == u'Copy Select':
			myslct = self.Txt.GetStringSelection()
			clipit = wx.TextDataObject()
			clipit.SetText(myslct)
			if wx.TheClipboard.Open():
				wx.TheClipboard.SetData(clipit)
				wx.TheClipboard.Flush()

			#print(myslct)
		elif lbl == u'Select All':
			self.Txt.SelectAll()

		elif lbl == u'Return ':
			q = self.GetParent()
			q.Close()
		else:
			print(u'error')







###########################################################################
## Class MyMenuBar2
###########################################################################

class MyMenuBar2 ( wx.MenuBar ):

	def __init__( self , whatmnu=u''):
		wx.MenuBar.__init__ ( self, style = 0 )

		self.mnu2 = wx.Menu()
		if whatmnu == u'prg':
			self.itm1 = wx.MenuItem( self.mnu2, wx.ID_ANY, u"Copy Select", wx.EmptyString, wx.ITEM_NORMAL )
			self.mnu2.Append( self.itm1 )
			self.Bind(wx.EVT_MENU, self.cpyslct, id=self.itm1.GetId())

		elif whatmnu == u'sql':
			self.itm2 = wx.MenuItem( self.mnu2, wx.ID_ANY, u"to SQL file", wx.EmptyString, wx.ITEM_NORMAL )
			self.mnu2.Append( self.itm2 )
			self.Bind(wx.EVT_MENU, self.tosql, id=self.itm2.GetId())
		else:
			pass

		self.mnu2.AppendSeparator()

		self.itm3 = wx.MenuItem( self.mnu2, wx.ID_ANY, u"Return", wx.EmptyString, wx.ITEM_NORMAL )
		self.mnu2.Append( self.itm3 )

		self.Append( self.mnu2, u"Tools" )


		# Connect Events
		#self.Bind( wx.EVT_MENU, self.cpyslct, id = self.itm1.GetId() )
		#self.Bind( wx.EVT_MENU, self.tosql, id = self.itm2.GetId() )
		self.Bind( wx.EVT_MENU, self.rtrn, id = self.itm3.GetId() )
		self.Bind( wx.EVT_UPDATE_UI, self.updat, id = self.itm3.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def cpyslct( self, event ):
		event.Skip()

	def tosql( self, event ):
		event.Skip()

	def rtrn( self, event ):
		q = self.GetParent()
		q.Close()

	def updat( self, event ):
		event.Skip()
