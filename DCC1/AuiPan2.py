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

###########################################################################
## Class MyPanel5
###########################################################################

class MyPanel1 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 557,450 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		Vsz1 = wx.BoxSizer( wx.VERTICAL )

		self.Splt1 = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D|wx.SP_LIVE_UPDATE|wx.SP_NO_XP_THEME|wx.SP_THIN_SASH )
		#self.Splt1.SetSashGravity( -1 )
		self.Splt1.Bind( wx.EVT_IDLE, self.Splt1OnIdle )

		self.P1 = wx.Panel( self.Splt1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		Vsz2 = wx.BoxSizer( wx.VERTICAL )

		self.lbl1 = wx.StaticText( self.P1, wx.ID_ANY, u"List of Panes:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl1.Wrap( -1 )

		Vsz2.Add( self.lbl1, 0, wx.ALL|wx.EXPAND, 5 )

		self.DVC1 = wx.dataview.DataViewCtrl( self.P1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Col1 = self.DVC1.AppendTextColumn( u"ID", 0, wx.dataview.DATAVIEW_CELL_INERT, 45, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.Col2 = self.DVC1.AppendTextColumn( u"Name Pane", 1, wx.dataview.DATAVIEW_CELL_INERT, 178, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		Vsz2.Add( self.DVC1, 1, wx.ALL|wx.EXPAND, 5 )

		Hsz1 = wx.BoxSizer( wx.HORIZONTAL )

		self.btn1 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.btn1.SetBitmap(wx.Bitmap( ICON16_PATH + u'add.png', wx.BITMAP_TYPE_ANY ) )
		self.btn1.SetToolTip(u"Add")
		Hsz1.Add( self.btn1, 0, wx.ALL, 5 )

		self.btn2 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.btn2.SetBitmap( wx.Bitmap( ICON16_PATH + u'edit_button.png', wx.BITMAP_TYPE_ANY ) )
		self.btn2.SetToolTip(u"Edit")
		Hsz1.Add( self.btn2, 0, wx.ALL, 5 )

		self.btn3 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.btn3.SetBitmap( wx.Bitmap( ICON16_PATH + u'delete.png', wx.BITMAP_TYPE_ANY ) )
		self.btn3.SetToolTip(u"Delete")
		Hsz1.Add( self.btn3, 0, wx.ALL, 5 )

		self.btn4 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.btn4.SetBitmap( wx.Bitmap( ICON16_PATH + u'watch_window.png', wx.BITMAP_TYPE_ANY ) )
		self.btn4.SetToolTip(u"")
		Hsz1.Add( self.btn4, 0, wx.ALL, 5 )

		self.btn5 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.btn5.SetBitmap( wx.Bitmap( ICON16_PATH + u'update.png', wx.BITMAP_TYPE_ANY ) )
		self.btn5.SetToolTip(u"Update")
		Hsz1.Add( self.btn5, 0, wx.ALL, 5 )

		self.btn6 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.btn6.SetBitmap( wx.Bitmap( ICON16_PATH + u'information.png', wx.BITMAP_TYPE_ANY ) )
		self.btn6.SetToolTip(u"Info")
		Hsz1.Add( self.btn6, 0, wx.ALL, 5 )

		self.btn7 = wx.BitmapButton(self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW | 0)

		self.btn7.SetBitmap(wx.Bitmap(ICON16_PATH + u'accept_button.png', wx.BITMAP_TYPE_ANY))
		self.btn7.SetToolTip(u"Apply")
		Hsz1.Add(self.btn7, 0, wx.ALL, 5)


		Vsz2.Add( Hsz1, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.P1.SetSizer( Vsz2 )
		self.P1.Layout()
		Vsz2.Fit( self.P1 )
		self.P2 = wx.Panel( self.Splt1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		Vsz3 = wx.BoxSizer( wx.VERTICAL )

		self.titr = wx.StaticText( self.P2, wx.ID_ANY, u"Pane Info:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.titr.Wrap( -1 )

		Vsz3.Add( self.titr, 0, wx.ALL|wx.EXPAND, 5 )

		Hsz2 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl2 = wx.StaticText( self.P2, wx.ID_ANY, u"ID", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.lbl2.Wrap( -1 )

		Hsz2.Add( self.lbl2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld1 = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		Hsz2.Add( self.fld1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.lbl3 = wx.StaticText( self.P2, wx.ID_ANY, u"Access", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl3.Wrap( -1 )

		Hsz2.Add( self.lbl3, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld2 = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		Hsz2.Add( self.fld2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.codgnr = wx.Button( self.P2, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		Hsz2.Add( self.codgnr, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz2, 1, wx.EXPAND, 5 )

		Hsz3 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl4 = wx.StaticText( self.P2, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.lbl4.Wrap( -1 )

		Hsz3.Add( self.lbl4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld3 = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz3.Add( self.fld3, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz3, 1, wx.EXPAND, 5 )

		Hsz4 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl5 = wx.StaticText( self.P2, wx.ID_ANY, u"Caption", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.lbl5.Wrap( -1 )

		Hsz4.Add( self.lbl5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld4 = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz4.Add( self.fld4, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz4, 1, wx.EXPAND, 5 )

		Hsz6 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl7 = wx.StaticText( self.P2, wx.ID_ANY, u"Setting", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl7.Wrap( -1 )

		Hsz6.Add( self.lbl7, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.stgbtn = wx.Button( self.P2, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		Hsz6.Add( self.stgbtn, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz6, 1, wx.EXPAND, 5 )

		self.fld6 = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		Vsz3.Add( self.fld6, 1, wx.ALL|wx.EXPAND, 5 )

		self.lin1 = wx.StaticLine( self.P2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		Vsz3.Add( self.lin1, 0, wx.EXPAND |wx.ALL, 5 )

		Hsz7 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl12 = wx.StaticText( self.P2, wx.ID_ANY, u"Size", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl12.Wrap( -1 )

		Hsz7.Add( self.lbl12, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.wht = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		Hsz7.Add( self.wht, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.hgt = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		Hsz7.Add( self.hgt, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.sizbtn = wx.Button( self.P2, wx.ID_ANY, u"Other Size", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz7.Add( self.sizbtn, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz7, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		Hsz8 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl10 = wx.StaticText( self.P2, wx.ID_ANY, u"resize", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl10.Wrap( -1 )

		Hsz8.Add( self.lbl10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		chs1Choices = [ u"Resizable", u"Fixed" ]
		self.chs1 = wx.Choice( self.P2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, chs1Choices, 0 )
		self.chs1.SetSelection( 0 )
		Hsz8.Add( self.chs1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.lbl6 = wx.StaticText( self.P2, wx.ID_ANY, u"dock", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl6.Wrap( -1 )

		Hsz8.Add( self.lbl6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		chs2Choices = [ u"Dock", u"Float" ]
		self.chs2 = wx.Choice( self.P2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, chs2Choices, 0 )
		self.chs2.SetSelection( 0 )
		Hsz8.Add( self.chs2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz8, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		Hsz9 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl11 = wx.StaticText( self.P2, wx.ID_ANY, u"Docking", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl11.Wrap( -1 )

		Hsz9.Add( self.lbl11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		chs3Choices = [ u"Top", u"Center", u"Left", u"Right", u"Bottom" ]
		self.chs3 = wx.Choice( self.P2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, chs3Choices, 0 )
		self.chs3.SetSelection( 2 )
		Hsz9.Add( self.chs3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.dokbtn = wx.Button(self.P2, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT)
		Hsz9.Add(self.dokbtn, 0, wx.ALL, 5)

		self.lbl13 = wx.StaticText(self.P2, wx.ID_ANY, u"Layer", wx.DefaultPosition, wx.DefaultSize, 0)
		self.lbl13.Wrap(-1)

		Hsz9.Add(self.lbl13, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		self.lyrspn = wx.SpinCtrlDouble(self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(40, -1),
		                                wx.ALIGN_CENTER_HORIZONTAL | wx.SP_ARROW_KEYS, 0, 9, 0.000000, 1)
		self.lyrspn.SetDigits(0)
		Hsz9.Add(self.lyrspn, 0, wx.ALL, 5)


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
		Vsz4.Add( self.prgfld, 0, wx.ALL|wx.EXPAND, 5 )

		self.lbl9 = wx.StaticText( self.P2, wx.ID_ANY, u"Directory:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl9.Wrap( -1 )

		Vsz4.Add( self.lbl9, 0, wx.ALL, 5 )


		Vsz3.Add( Vsz4, 1, wx.EXPAND, 5 )


		self.P2.SetSizer( Vsz3 )
		self.P2.Layout()
		Vsz3.Fit( self.P2 )
		self.Splt1.SplitVertically( self.P1, self.P2, 254 )
		Vsz1.Add( self.Splt1, 1, wx.EXPAND, 5 )


		self.SetSizer( Vsz1 )
		self.Layout()

		# Connect Events
		self.DVC1.Bind( wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED, self.slctmnu, id = wx.ID_ANY )
		self.btn1.Bind( wx.EVT_BUTTON, self.addit )
		self.btn2.Bind( wx.EVT_BUTTON, self.edtit )
		self.btn3.Bind( wx.EVT_BUTTON, self.delit )
		self.btn4.Bind( wx.EVT_BUTTON, self.updat )
		self.btn5.Bind( wx.EVT_BUTTON, self.publc )
		self.btn6.Bind( wx.EVT_BUTTON, self.prviw )
		self.btn7.Bind( wx.EVT_BUTTON, self.aplit )
		self.codgnr.Bind( wx.EVT_BUTTON, self.gnrcod )
		self.stgbtn.Bind( wx.EVT_BUTTON, self.stngpn )
		self.sizbtn.Bind( wx.EVT_BUTTON, self.otrsiz )
		self.chs1.Bind( wx.EVT_CHOICE, self.rezfix )
		self.chs2.Bind( wx.EVT_CHOICE, self.dokflt )
		self.chs3.Bind( wx.EVT_CHOICE, self.lrtbc )
		self.dokbtn.Bind(wx.EVT_BUTTON, self.dockabl)
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

	def updat( self, event ):
		event.Skip()

	def publc( self, event ):
		event.Skip()

	def prviw( self, event ):
		event.Skip()

	def aplit( self, event ):
		event.Skip()

	def gnrcod( self, event ):
		event.Skip()

	def stngpn( self, event ):
		iwin = wx.Dialog(self, -1)
		pnl = MyPanel2(iwin)
		iwin.SetSize((500, 320))
		iwin.ShowModal()
		print(pnl.e)

		iwin.Destroy()

	def otrsiz( self, event ):
		event.Skip()

	def rezfix( self, event ):
		event.Skip()

	def dokflt( self, event ):
		event.Skip()

	def lrtbc( self, event ):
		event.Skip()

	def dockabl(self, event):
		event.Skip()

	def prglst( self, event ):
		event.Skip()

	def Splt1OnIdle( self, event ):
		self.Splt1.SetSashPosition( 254 )
		self.Splt1.Unbind( wx.EVT_IDLE )




###########################################################################
## Class MyPanel2
###########################################################################
import wx.propgrid as pg


class MyPanel2 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,342 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		Vsz1 = wx.BoxSizer( wx.VERTICAL )

		self.Item = []
		items = [('caption_visible',True),('close_button',True),('maximize_button',False),('minimize_button',False),
		         ('pine_button',True),('pane_border',True),('show',True),('gripper',False),('center_pane',False),
		         ('default_pane',False),('toolbar_pane',False),('moveable',True) ]


		self.PGrid1 = pg.PropertyGrid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.propgrid.PG_DEFAULT_STYLE|wx.propgrid.PG_SPLITTER_AUTO_CENTER|wx.propgrid.PG_TOOLTIPS)

		self.PGrid1.Append(pg.PropertyCategory(u"AUI", u"AUI"))

		for itm in items:
			#self.Item.append( self.PGrid1.Append( pg.BoolProperty( itm[0], itm[0], value=itm[1]) )  )
			self.PGrid1.Append(pg.BoolProperty(itm[0], itm[0], value=itm[1]))
			self.PGrid1.SetPropertyAttribute(itm[0],"UseCheckbox", True)


		Vsz1.Add( self.PGrid1, 1, wx.ALL|wx.EXPAND, 5 )

		Hsz1 = wx.BoxSizer( wx.HORIZONTAL )

		self.btn1 = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz1.Add( self.btn1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.btn2 = wx.Button( self, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz1.Add( self.btn2, 0, wx.ALL, 5 )


		Vsz1.Add( Hsz1, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( Vsz1 )
		self.Layout()

		# Connect Events
		self.btn1.Bind( wx.EVT_BUTTON, self.cncl )
		self.btn2.Bind( wx.EVT_BUTTON, self.okit )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def cncl( self, event ):
		q = self.GetParent()
		q.Close()

	def okit( self, event ):
		self.e = self.PGrid1.GetPropertyValues()
		print(self.e)
		q = self.GetParent()
		q.Close()



###########################################################################
## Class MyPanel3
###########################################################################

class MyPanel3 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,342 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		Vsz1 = wx.BoxSizer( wx.VERTICAL )

		self.PGrid1 = pg.PropertyGrid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.propgrid.PG_DEFAULT_STYLE|wx.propgrid.PG_SPLITTER_AUTO_CENTER|wx.propgrid.PG_TOOLTIPS)
		self.Item1 = self.PGrid1.Append( pg.PropertyCategory( u"Name", u"Name" ) )
		self.Item2 = self.PGrid1.Append( pg.BoolProperty( u"Name", u"Name" ) )
		self.Item3 = self.PGrid1.Append( pg.BoolProperty( u"Name", u"Name" ) )
		self.m_propertyGridItem4 = self.PGrid1.Append( pg.BoolProperty( u"Name", u"Name" ) )
		self.m_propertyGridItem5 = self.PGrid1.Append( pg.StringProperty( u"Name", u"Name" ) )
		self.m_propertyGridItem6 = self.PGrid1.Append( pg.StringProperty( u"Name", u"Name" ) )
		self.m_propertyGridItem7 = self.PGrid1.Append( pg.StringProperty( u"Name", u"Name" ) )
		self.m_propertyGridItem8 = self.PGrid1.Append( pg.StringProperty( u"Name", u"Name" ) )
		self.m_propertyGridItem9 = self.PGrid1.Append( pg.StringProperty( u"Name", u"Name" ) )
		self.m_propertyGridItem10 = self.PGrid1.Append( pg.StringProperty( u"Name", u"Name" ) )
		self.m_propertyGridItem11 = self.PGrid1.Append( pg.StringProperty( u"Name", u"Name" ) )
		self.m_propertyGridItem12 = self.PGrid1.Append( pg.StringProperty( u"Name", u"Name" ) )
		self.m_propertyGridItem13 = self.PGrid1.Append( pg.StringProperty( u"Name", u"Name" ) )
		Vsz1.Add( self.PGrid1, 1, wx.ALL|wx.EXPAND, 5 )

		Hsz1 = wx.BoxSizer( wx.HORIZONTAL )

		self.btn1 = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz1.Add( self.btn1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.btn2 = wx.Button( self, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz1.Add( self.btn2, 0, wx.ALL, 5 )


		Vsz1.Add( Hsz1, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( Vsz1 )
		self.Layout()

		# Connect Events
		self.btn1.Bind( wx.EVT_BUTTON, self.cncl )
		self.btn2.Bind( wx.EVT_BUTTON, self.okit )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def cncl( self, event ):
		q = self.GetParent()
		q.Close()

	def okit( self, event ):
		event.Skip()