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

from AI.OpnFil import *
from AI.Analiz import *
from AI.Generats import *

from Config.Init import *

import Database.MenuSet2 as MS
import Database.PostGet as PG
import GUI.proman as pro
import importlib
###########################################################################
## Class MyPanel3
###########################################################################

class MyPanel1 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 544,450 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		Vsz1 = wx.BoxSizer( wx.VERTICAL )

		self.getMData = MS.GetData(u'Menu2.db', u'')
		self.setMDate = MS.SetData(u'', u'', u'')

		self.Splt1 = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D|wx.SP_LIVE_UPDATE|wx.SP_NO_XP_THEME|wx.SP_THIN_SASH )
		#self.Splt1.SetSashGravity( -1 )
		self.Splt1.Bind( wx.EVT_IDLE, self.Splt1OnIdle )

		self.P1 = wx.Panel( self.Splt1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		Vsz2 = wx.BoxSizer( wx.VERTICAL )

		self.lbl1 = wx.StaticText( self.P1, wx.ID_ANY, u"List of Programs:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl1.Wrap( -1 )

		Vsz2.Add( self.lbl1, 0, wx.ALL|wx.EXPAND, 5 )

		self.DVC1 = wx.dataview.DataViewCtrl( self.P1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		#self.filllist()

		self.Col1 = self.DVC1.AppendTextColumn( u"Name Program", 0, wx.dataview.DATAVIEW_CELL_INERT, 178, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.Col2 = self.DVC1.AppendTextColumn( u"ID", 1, wx.dataview.DATAVIEW_CELL_INERT, 45, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		Vsz2.Add( self.DVC1, 1, wx.ALL|wx.EXPAND, 5 )

		Hsz1 = wx.BoxSizer( wx.HORIZONTAL )

		self.btn1 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.btn1.SetBitmap( wx.Bitmap( ICON16_PATH + u'application_add.png', wx.BITMAP_TYPE_ANY ) )
		self.btn1.SetToolTip( u"Add" )

		Hsz1.Add( self.btn1, 0, wx.ALL, 5 )

		self.btn2 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.btn2.SetBitmap( wx.Bitmap( ICON16_PATH + u'application_edit.png', wx.BITMAP_TYPE_ANY ) )
		self.btn2.SetToolTip(u"Edit")
		Hsz1.Add( self.btn2, 0, wx.ALL, 5 )

		self.btn3 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.btn3.SetBitmap( wx.Bitmap( ICON16_PATH + u'application_delete.png', wx.BITMAP_TYPE_ANY ) )
		self.btn3.SetToolTip(u"Delete")
		Hsz1.Add( self.btn3, 0, wx.ALL, 5 )

		self.btn4 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.btn4.SetBitmap( wx.Bitmap( ICON16_PATH + u'application_form.png', wx.BITMAP_TYPE_ANY ))
		self.btn4.SetToolTip(u"Preview")
		Hsz1.Add( self.btn4, 0, wx.ALL, 5 )

		self.btn5 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.btn5.SetBitmap( wx.Bitmap( ICON16_PATH + u'update.png', wx.BITMAP_TYPE_ANY ) )
		self.btn5.SetToolTip(u"Update")
		Hsz1.Add( self.btn5, 0, wx.ALL, 5 )

		self.btn6 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.btn6.SetBitmap( wx.Bitmap( ICON16_PATH + u'accept_button.png', wx.BITMAP_TYPE_ANY ) )
		self.btn6.SetToolTip(u"Apply")
		Hsz1.Add( self.btn6, 0, wx.ALL, 5 )


		self.btn7 = wx.BitmapButton(self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize,wx.BU_AUTODRAW | 0)

		self.btn7.SetBitmap(wx.Bitmap(ICON16_PATH + u'application_lightning.png', wx.BITMAP_TYPE_ANY))
		self.btn7.SetToolTip(u"Generate")
		Hsz1.Add(self.btn7, 0, wx.ALL, 5)


		Vsz2.Add( Hsz1, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.P1.SetSizer( Vsz2 )
		self.P1.Layout()
		Vsz2.Fit( self.P1 )
		self.P2 = wx.Panel( self.Splt1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		Vsz3 = wx.BoxSizer( wx.VERTICAL )

		self.titr = wx.StaticText( self.P2, wx.ID_ANY, u"Description:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.titr.Wrap( -1 )

		Vsz3.Add( self.titr, 0, wx.ALL|wx.EXPAND, 5 )

		self.Desc = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		Vsz3.Add( self.Desc, 1, wx.ALL|wx.EXPAND, 5 )

		Hsz2 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl2 = wx.StaticText( self.P2, wx.ID_ANY, u"ID No.", wx.DefaultPosition, wx.Size( 58,-1 ), 0 )
		self.lbl2.Wrap( -1 )

		Hsz2.Add( self.lbl2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld1 = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		Hsz2.Add( self.fld1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.lbl3 = wx.StaticText( self.P2, wx.ID_ANY, u"Prog. No.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl3.Wrap( -1 )

		Hsz2.Add( self.lbl3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld2 = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		Hsz2.Add( self.fld2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz2, 0, wx.EXPAND, 5 )

		Hsz3 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl4 = wx.StaticText( self.P2, wx.ID_ANY, u"import ", wx.DefaultPosition, wx.Size( 58,-1 ), 0 )
		self.lbl4.Wrap( -1 )

		Hsz3.Add( self.lbl4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld3 = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz3.Add( self.fld3, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.codgnr = wx.Button( self.P2, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		Hsz3.Add( self.codgnr, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )


		Vsz3.Add( Hsz3, 0, wx.EXPAND, 5 )

		Hsz5 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl6 = wx.StaticText( self.P2, wx.ID_ANY, u"Directory", wx.DefaultPosition, wx.Size( 58,-1 ), 0 )
		self.lbl6.Wrap( -1 )

		Hsz5.Add( self.lbl6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.PrgDir1 = wx.DirPickerCtrl( self.P2, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE|wx.DIRP_SMALL )
		Hsz5.Add( self.PrgDir1, 1, wx.ALL, 5 )


		Vsz3.Add( Hsz5, 0, wx.EXPAND, 5 )

		Hsz4 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl5 = wx.StaticText( self.P2, wx.ID_ANY, u"Parameters", wx.DefaultPosition, wx.Size( 58,-1 ), 0 )
		self.lbl5.Wrap( -1 )

		Hsz4.Add( self.lbl5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld4 = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz4.Add( self.fld4, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz4, 0, wx.EXPAND, 5 )

		Hsz6 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl7 = wx.StaticText( self.P2, wx.ID_ANY, u"Link:", wx.DefaultPosition, wx.Size( 58,-1 ), 0 )
		self.lbl7.Wrap( -1 )

		Hsz6.Add( self.lbl7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld6 = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz6.Add( self.fld6, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.chk1 = wx.CheckBox( self.P2, wx.ID_ANY, u"Public it", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz6.Add( self.chk1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz6, 0, wx.EXPAND, 5 )

		self.lin1 = wx.StaticLine( self.P2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		Vsz3.Add( self.lin1, 0, wx.EXPAND |wx.ALL, 5 )

		Hsz10 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl8 = wx.StaticText( self.P2, wx.ID_ANY, u"Database:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl8.Wrap( -1 )

		Hsz10.Add( self.lbl8, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.probtn = wx.Button( self.P2, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		self.probtn.SetToolTip( u"Select Database Tabels and Fields for this program" )

		Hsz10.Add( self.probtn, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz10, 0, wx.EXPAND, 5 )

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
		self.DVC1.Bind( wx.dataview.EVT_DATAVIEW_ITEM_CONTEXT_MENU, self.conxmnu, id = wx.ID_ANY )
		self.DVC1.Bind( wx.dataview.EVT_DATAVIEW_ITEM_EDITING_DONE, self.endedit, id = wx.ID_ANY )
		self.btn1.Bind( wx.EVT_BUTTON, self.addit )
		self.btn2.Bind( wx.EVT_BUTTON, self.edtit )
		self.btn3.Bind( wx.EVT_BUTTON, self.delit )
		self.btn4.Bind( wx.EVT_BUTTON, self.updat )
		self.btn5.Bind( wx.EVT_BUTTON, self.gnrat )
		self.btn6.Bind( wx.EVT_BUTTON, self.prviw )
		self.codgnr.Bind( wx.EVT_BUTTON, self.prviw )
		self.PrgDir1.Bind( wx.EVT_DIRPICKER_CHANGED, self.slctdir )
		self.chk1.Bind( wx.EVT_CHECKBOX, self.public )
		self.probtn.Bind( wx.EVT_BUTTON, self.dblst )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def filllist(self):
		#self.DVC1.AppendTextColumn()
		self.my_data = self.getMData.AllHndl("join menubar on menubar.mbarid = handler.prgdir where handler.handlerid < 90000 ")
		print(self.my_data)
		data = [[m[1], m[0]] for m in self.my_data ]
		modal = wx.dataview.DataViewModel(self)
		modal.ItemsAdded(self.DVC1,data)
		print(model)
		self.DVC1.AssociateModel(model)


	def slctmnu( self, event ):
		event.Skip()

	def conxmnu( self, event ):
		event.Skip()

	def endedit( self, event ):
		event.Skip()

	def addit( self, event ):
		event.Skip()

	def edtit( self, event ):
		event.Skip()

	def delit( self, event ):
		event.Skip()

	def updat( self, event ):
		event.Skip()

	def gnrat( self, event ):
		event.Skip()

	def prviw( self, event ):
		event.Skip()


	def slctdir( self, event ):
		event.Skip()

	def public( self, event ):
		event.Skip()

	def dblst( self, event ):
		event.Skip()

	def Splt1OnIdle( self, event ):
		self.Splt1.SetSashPosition( 254 )
		self.Splt1.Unbind( wx.EVT_IDLE )


class Info(object):
	def __init__(self, dirct, para, pub, prgno):
		self.dirct = dirct
		self.para = para
		self.pub = pub
		self.prgno = prgno

	def __repr__(self):
		return "Program Directory: %s" % self.dirct


class Prog(object):
	def __init__(self, id, name):
		self.id = id
		self.name = name
		self.info = []

	def __repr__(self):
		return "Application :" + self.name

class ProgrmLsit(wx.dataview.DataViewModel):
	def __init__(self, Data):
		wx.dataview.DataViewModel.__init__(self)
		self.Data = Data

	def ItemsAdded(self, parent, items):
		pass

class MyProgramList(wx.dataview.PyDataViewModel):
	def __init__(self, Data):
		wx.dataview.PyDataViewModel.__init__(self)
		self.Data = Data
		self.UseWeakRefs(True)

	def GetColumnCount(self):
		return 2

	def GetColumnType(self, col):
		mapper = {
			0 : 'string',
			1 : 'string',

		}
		return mapper[col]

	def GetChildren(self, item, children):
		if not item:
			for app in self.Data:
				children.append(self.ObjectToItem(app))
			return len(self.Data)
		node = self.ItemToObject(item)
		if isinstance(node, Prog):
			for song in node.songs:
				children.append(self.ObjectToItem(song))
			return len(node.songs)
		return 0

	def IsContainer(self, item):
		if not item:
			return True
		node = self.ItemToObject(item)
		if isinstance(node, Prog):
			return True
		return False

	def GetParent(self, item):
		if not item:
			return wx.dataview.NullDataViewItem
		node = self.ItemToObject(item)
		if isinstance(node, Prog):
			return wx.dataview.NullDataViewItem
		elif isinstance(node, Info):
			for p in self.Data:
				if p.name == node.Info:
					return self.ObjectToItem(p)

	def HasValue(self, item, col):
		node = self.ItemToObject(item)
		if isinstance(node, Prog) and col > 0:
			return False
		return True

	def GetValue(self, item, col):
		node = self.ItemToObject(item)

		if isinstance(node, Prog):
			assert col == 0, "Unexpected column value for Genre objects"
			return node.name

		elif isinstance(node, Info):
			mapper = {0: node.id,
			          1: node.direct,
			          2: node.para,
			          3: node.pub,
			          4: node.prgno,
			          }
			return mapper[col]

		else:
			raise RuntimeError("unknown node type")

	def GetAttr(self, item, col, attr):
		node = self.ItemToObject(item)
		if isinstance(node, Prog):
			attr.SetColour('blue')
			attr.SetBold(True)
			return True
		return False

	def SetValue(self, variant, item, col):
		node = self.ItemToObject(item)
		if isinstance(node, Prog):
			if col == 1:
				node.dirct = value
			elif col == 2:
				node.para = value
			elif col == 3:
				node.pub = value
			elif col == 4:
				node.prgno = value
		return True







