# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################
import os

import wx
#import wx.xrc
import wx.dataview
import wx.stc as stc

import Database.MenuSet2 as MS
#from . import MitemFrm2 as MF

from Config.Init import *
import Res.Allicons as icon

_ = wx.GetTranslation

###########################################################################
## Class MyPanel2
###########################################################################

class MyPanel1 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 570,450 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		Vsz1 = wx.BoxSizer( wx.VERTICAL )

		self.Splt1 = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D|wx.SP_LIVE_UPDATE|wx.SP_NO_XP_THEME|wx.SP_THIN_SASH )
		#self.Splt1.SetSashGravity( -1 )
		self.Splt1.Bind( wx.EVT_IDLE, self.Splt1OnIdle )

		self.P1 = wx.Panel( self.Splt1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		Vsz2 = wx.BoxSizer( wx.VERTICAL )

		self.lbl1 = wx.StaticText( self.P1, wx.ID_ANY, _(u"List of menu:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl1.Wrap( -1 )

		Vsz2.Add( self.lbl1, 0, wx.ALL|wx.EXPAND, 5 )

		#self.DVC1 = wx.dataview.DataViewTreeCtrl( self.P1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.DVC1 = wx.dataview.TreeListCtrl(self.P1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_HAS_BUTTONS|wx.TR_DEFAULT_STYLE)
		self.Col1 = self.DVC1.AppendColumn( _(u"ID"),  95, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.Col2 = self.DVC1.AppendColumn( _(u"Name Menu"),  158, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		Vsz2.Add( self.DVC1, 1, wx.ALL|wx.EXPAND, 5 )

		self.MyMenu = MS.GetData(u'Menu2.db', u'')
		self.DoMenu = MS.SetData(u'', u'', u'')

		self.newone = False
		self.newsub = False

		self.fillList()

		Hsz1 = wx.BoxSizer( wx.HORIZONTAL )

		self.btn1 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		#self.btn1.SetBitmap( wx.Bitmap( ICON16_PATH + u'add.png', wx.BITMAP_TYPE_ANY ) )
		self.btn1.SetBitmap(icon.add.GetBitmap())
		self.btn1.SetToolTip(_(u"Add"))
		Hsz1.Add( self.btn1, 0, wx.ALL, 5 )

		self.btn2 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		#self.btn2.SetBitmap( wx.Bitmap( ICON16_PATH + u'edit_button.png', wx.BITMAP_TYPE_ANY ) )
		self.btn2.SetBitmap(icon.edit_button.GetBitmap())
		self.btn2.SetToolTip(_(u"Edit"))
		Hsz1.Add( self.btn2, 0, wx.ALL, 5 )

		self.btn3 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		#self.btn3.SetBitmap( wx.Bitmap( ICON16_PATH + u'delete.png', wx.BITMAP_TYPE_ANY ) )
		self.btn3.SetBitmap(icon.delete.GetBitmap())
		self.btn3.SetToolTip(_(u"Delete"))
		Hsz1.Add( self.btn3, 0, wx.ALL, 5 )

		self.btn4 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		#self.btn4.SetBitmap( wx.Bitmap( ICON16_PATH + u'separator.png', wx.BITMAP_TYPE_ANY ))
		self.btn4.SetBitmap(icon.separator.GetBitmap())
		self.btn4.SetToolTip(_(u"Seperator"))
		Hsz1.Add( self.btn4, 0, wx.ALL, 5 )

		self.btn5 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		#self.btn5.SetBitmap(wx.Bitmap( ICON16_PATH + u'update.png', wx.BITMAP_TYPE_ANY ) )
		self.btn5.SetBitmap(icon.update.GetBitmap())
		self.btn5.SetToolTip(_(u"Update"))
		Hsz1.Add( self.btn5, 0, wx.ALL, 5 )

		self.btn6 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		#self.btn6.SetBitmap(wx.Bitmap( ICON16_PATH + u'information.png', wx.BITMAP_TYPE_ANY ) )
		self.btn6.SetBitmap(icon.information.GetBitmap())
		self.btn6.SetToolTip(_(u"Info"))
		Hsz1.Add( self.btn6, 0, wx.ALL, 5 )

		self.btn7 = wx.BitmapButton(self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize,
									wx.BU_AUTODRAW | 0)

		#self.btn7.SetBitmap(wx.Bitmap(ICON16_PATH + u'accept_button.png', wx.BITMAP_TYPE_ANY))
		self.btn7.SetBitmap(icon.accept_button.GetBitmap())
		self.btn7.SetToolTip(_(u"Apply"))
		Hsz1.Add(self.btn7, 0, wx.ALL, 5)


		Vsz2.Add( Hsz1, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.P1.SetSizer( Vsz2 )
		self.P1.Layout()
		Vsz2.Fit( self.P1 )
		self.P2 = wx.Panel( self.Splt1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		Vsz3 = wx.BoxSizer( wx.VERTICAL )

		self.titr = wx.StaticText( self.P2, wx.ID_ANY, _(u"MenuBar:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.titr.Wrap( -1 )

		Vsz3.Add( self.titr, 0, wx.ALL|wx.EXPAND, 5 )

		Hsz2 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl2 = wx.StaticText( self.P2, wx.ID_ANY, _(u"ID"), wx.DefaultPosition, wx.Size( 47,-1 ), 0 )
		self.lbl2.Wrap( -1 )

		Hsz2.Add( self.lbl2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld1 = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		Hsz2.Add( self.fld1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.lbl3 = wx.StaticText( self.P2, wx.ID_ANY, _(u"Access"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl3.Wrap( -1 )

		Hsz2.Add( self.lbl3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld2 = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		Hsz2.Add( self.fld2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.codgnr = wx.Button( self.P2, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		self.codgnr.SetToolTip( _(u"Code Generator") )

		Hsz2.Add( self.codgnr, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz2, 1, wx.EXPAND, 5 )

		Hsz3 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl4 = wx.StaticText( self.P2, wx.ID_ANY, _(u"Name"), wx.DefaultPosition, wx.Size( 47,-1 ), 0 )
		self.lbl4.Wrap( -1 )

		Hsz3.Add( self.lbl4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld3 = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz3.Add( self.fld3, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz3, 1, wx.EXPAND, 5 )

		Hsz5 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl6 = wx.StaticText( self.P2, wx.ID_ANY, _(u"Icon"), wx.DefaultPosition, wx.Size( 47,-1 ), 0 )
		self.lbl6.Wrap( -1 )

		Hsz5.Add( self.lbl6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.iconfile = wx.FilePickerCtrl( self.P2, wx.ID_ANY, wx.EmptyString, _(u"Select a file"),  u"*.png;*.bmp;*.jpg", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_SMALL )
		Hsz5.Add( self.iconfile, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz5, 1, wx.EXPAND, 5 )

		#self.icon1 = wx.StaticBitmap( self.P2, wx.ID_ANY, wx.Bitmap(ICONS_PATH + u"image.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.icon1 = wx.StaticBitmap(self.P2, wx.ID_ANY, icon.image.GetBitmap(),wx.DefaultPosition, wx.DefaultSize, 0)
		Vsz3.Add( self.icon1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		Hsz4 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl5 = wx.StaticText( self.P2, wx.ID_ANY, _(u"ShortCut"), wx.DefaultPosition, wx.Size( 47,-1 ), 0 )
		self.lbl5.Wrap( -1 )

		Hsz4.Add( self.lbl5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld4 = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz4.Add( self.fld4, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz4, 1, wx.EXPAND, 5 )

		Hsz6 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl7 = wx.StaticText( self.P2, wx.ID_ANY, _(u"Status"), wx.DefaultPosition, wx.Size( 47,-1 ), 0 )
		self.lbl7.Wrap( -1 )

		Hsz6.Add( self.lbl7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld6 = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz6.Add( self.fld6, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz6, 1, wx.EXPAND, 5 )

		Hsz7 = wx.BoxSizer( wx.HORIZONTAL )

		self.chk1 = wx.CheckBox( self.P2, wx.ID_ANY, _(u"Disable"), wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz7.Add( self.chk1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.chk2 = wx.CheckBox( self.P2, wx.ID_ANY, _(u"Hide"), wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz7.Add( self.chk2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz7, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.lin1 = wx.StaticLine( self.P2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		Vsz3.Add( self.lin1, 0, wx.EXPAND |wx.ALL, 5 )

		Hsz8 = wx.BoxSizer( wx.HORIZONTAL )

		self.rdio1 = wx.RadioButton( self.P2, wx.ID_ANY, _(u"Normal"), wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz8.Add( self.rdio1, 0, wx.ALL, 5 )

		self.rdio2 = wx.RadioButton( self.P2, wx.ID_ANY, _(u"Check"), wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz8.Add( self.rdio2, 0, wx.ALL, 5 )

		self.rdio3 = wx.RadioButton( self.P2, wx.ID_ANY, _(u"Radio"), wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz8.Add( self.rdio3, 0, wx.ALL, 5 )


		Vsz3.Add( Hsz8, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		Hsz9 = wx.BoxSizer( wx.HORIZONTAL )

		self.rdio4 = wx.RadioButton( self.P2, wx.ID_ANY, _(u"Sub Menu"), wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz9.Add( self.rdio4, 0, wx.ALL, 5 )


		Vsz3.Add( Hsz9, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.lin2 = wx.StaticLine( self.P2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		Vsz3.Add( self.lin2, 0, wx.EXPAND |wx.ALL, 5 )

		Hsz10 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl8 = wx.StaticText( self.P2, wx.ID_ANY, _(u"Program:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl8.Wrap( -1 )

		Hsz10.Add( self.lbl8, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.probtn = wx.Button( self.P2, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		self.probtn.SetToolTip( _(u"list of program can changed") )

		Hsz10.Add( self.probtn, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz10, 1, wx.EXPAND, 5 )

		Vsz4 = wx.BoxSizer( wx.VERTICAL )

		self.prgfld = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Vsz4.Add( self.prgfld, 0, wx.ALL|wx.EXPAND, 5 )

		self.lbl9 = wx.StaticText( self.P2, wx.ID_ANY, _(u"Directory:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl9.Wrap( -1 )

		Vsz4.Add( self.lbl9, 0, wx.ALL, 5 )


		Vsz3.Add( Vsz4, 1, wx.EXPAND, 5 )


		self.P2.SetSizer( Vsz3 )
		self.P2.Layout()
		Vsz3.Fit( self.P2 )
		self.Splt1.SplitVertically( self.P1, self.P2, 0 )
		Vsz1.Add( self.Splt1, 1, wx.EXPAND, 5 )


		self.SetSizer( Vsz1 )
		self.Layout()

		# Connect Events
		self.DVC1.Bind( wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED, self.slctmnu, id = wx.ID_ANY )
		self.DVC1.Bind( wx.dataview.EVT_DATAVIEW_ITEM_CONTEXT_MENU, self.conmenu, id = wx.ID_ANY )
		self.DVC1.Bind( wx.dataview.EVT_DATAVIEW_ITEM_EDITING_DONE, self.endedit, id = wx.ID_ANY )
		self.DVC1.Bind( wx.dataview.EVT_DATAVIEW_SELECTION_CHANGED, self.slcchng, id = wx.ID_ANY )
		self.btn1.Bind( wx.EVT_BUTTON, self.addit )
		self.btn2.Bind( wx.EVT_BUTTON, self.edtit )
		self.btn3.Bind( wx.EVT_BUTTON, self.delit )
		self.btn4.Bind( wx.EVT_BUTTON, self.sprit )
		self.btn5.Bind( wx.EVT_BUTTON, self.bakit )
		self.btn6.Bind( wx.EVT_BUTTON, self.forit )
		self.btn7.Bind( wx.EVT_BUTTON, self.aplit)
		self.codgnr.Bind( wx.EVT_BUTTON, self.gnrcod )
		self.iconfile.Bind( wx.EVT_FILEPICKER_CHANGED, self.icnslct )
		self.chk1.Bind( wx.EVT_CHECKBOX, self.disbl )
		self.chk2.Bind( wx.EVT_CHECKBOX, self.hidit )
		self.rdio1.Bind( wx.EVT_RADIOBUTTON, self.normnu )
		self.rdio2.Bind( wx.EVT_RADIOBUTTON, self.chkmnu )
		self.rdio3.Bind( wx.EVT_RADIOBUTTON, self.rdomnu )
		self.rdio4.Bind( wx.EVT_RADIOBUTTON, self.submnu )
		self.probtn.Bind( wx.EVT_BUTTON, self.prglst )

	def __del__( self ):
		pass

	def fillnull(self):
	    self.titr.SetLabel(_(u'MenuBar: '))
	    self.fld1.SetValue('')
	    self.fld2.SetValue('')
	    self.fld3.SetValue('')
	    self.iconfile.SetPath('')
	    #self.icon1.SetBitmap(wx.Bitmap(ICONS_PATH + u"image.png", wx.BITMAP_TYPE_ANY))
	    self.icon1.SetBitmap(icon.image.GetBitmap())
	    self.fld4.SetValue('')
	    self.fld6.SetValue('')
	    self.prgfld.SetValue('')
	    self.lbl9.SetLabel(_('Directory: '))


	# Virtual event handlers, overide them in your derived class
	def slctmnu( self, event ):
		self.ps = ps = self.DVC1.GetSelections()
		self.itmcod = self.DVC1.GetItemText(ps[0], 0)
		self.itmnam = self.DVC1.GetItemText(ps[0], 1)
		#print(self.itmcod,self.itmnam, ps)

		if int(self.itmcod) < 1000 and int(self.itmcod) % 10 == 1:
			data = self.MyMenu.gBarItm(int(self.itmcod))
			#print(data)
			#self.Cbar(None)
			pass
		elif int(self.itmcod) > 1000:
			data = self.MyMenu.getmItem(int(self.itmcod))
			#print(data)
			# print(self.itmnam)
			#self.edtit(None)
		else:
			print(self.itmnam, self.itmcod)
		event.Skip()


	def fillList(self):
		broot = self.DVC1.GetRootItem()
		#roots = self.MyMenu.AllBar("where mbarid < 9999")
		roots = self.MyMenu.AllBar()
		subrot = self.MyMenu.AllSub(" Where mitem.itemtyp = 'S' ")

		def getSubmenu(itmid, chditm, titl):
			subitems = self.MyMenu.ShowItem(itmid)
			for sub in subitems:
				subitm = self.DVC1.AppendItem(chditm, titl)
				self.DVC1.SetItemText(subitm, 0, str(sub[1]))
				self.DVC1.SetItemText(subitm, 1, str(sub[3]))
				if sub[6] == 'S':
					getSubmenu(sub[1], subitm, sub[3])
				else:
					self.DVC1.SetItemText(subitm, 1, sub[3])

		for r in roots:
			grp_roots = self.DVC1.AppendItem(broot, 'Bar Menu')
			self.DVC1.SetItemText(grp_roots, 0, str(r[0]))
			self.DVC1.SetItemText(grp_roots, 1, r[1])
			items = self.MyMenu.ShowItem(r[0])
			for i in items:
				chditm = self.DVC1.AppendItem(grp_roots, 'Items Menu')
				self.DVC1.SetItemText(chditm, 0, str(i[1]))
				if i[6] == 'S':
					getSubmenu(i[1], chditm, i[3])
				if i[3] == None or i[3] == '':
					self.DVC1.SetItemText(chditm, 1, '---')
				else:
					self.DVC1.SetItemText(chditm, 1, str(i[3]))

	def conmenu( self, event ):
		#print('Context Menu')
		self.barmnu = wx.Menu()
		self.barmnu.Append(10,_('New Menu Bar'))
		self.Bind(wx.EVT_MENU,self.Nbar,id=10)
		self.barmnu.Append(20,_('Edit Menu Bar'))
		self.Bind(wx.EVT_MENU, self.Cbar, id=20)
		self.barmnu.Append(30,_('Delete Menu bar'))
		self.Bind(wx.EVT_MENU, self.Dbar, id=30)

		self.PopupMenu(self.barmnu)
		self.barmnu.Destroy()
		event.Skip()


	def endedit( self, event ):
		event.Skip()

	def slcchng( self, event ):
		ps = self.DVC1.GetSelections()
		self.itmcod = self.DVC1.GetItemText(ps[0], 0)
		#print(self.itmcod)
		self.fillflds(int(self.itmcod))
		event.Skip()

	def fillflds(self, code):
		self.fillnull()
		if code < 1000 and code % 10 == 1:
			self.bardata = data = self.MyMenu.AmenuBar(ext=u'and mbarid = %d' %code)[0]
			#print(data)
			self.titr.SetLabel(_(u'MenuBar: ')+data[1])
			self.fld1.SetValue(str(data[0]))
			self.fld2.SetValue(data[3])
			self.fld3.SetValue(data[1])
			self.iconfile.SetPath('')
			#self.icon1.SetBitmap(wx.Bitmap(ICONS_PATH + u"image.png", wx.BITMAP_TYPE_ANY ))
			self.icon1.SetBitmap(icon.image.GetBitmap())
			self.fld4.SetValue('')
			self.fld6.SetValue('')
			mydir = self.MyMenu.GetDirCod(data[2])[0][0]
			#print(mydir)
			self.lbl9.SetLabel(_('Directory: ')+mydir)
			if data[7] != 1:
				self.chk1.SetValue(1)
		if code > 1000:
			self.disableall(0)
			self.itmdata = self.bardata = data = self.MyMenu.getmItem(code)[0]
			#print(data)
			if data[3] == 'S':
				bn = (data[2],)
			else:
				if self.bardata[0] < 1000:
					bn = self.MyMenu.gBarN(data[0])[0]
				else:
					bn = (self.MyMenu.getmItem(self.bardata[0])[0][2],)
			#print(bn)
			self.titr.SetLabel(_(u'MenuBar: ')+bn[0])
			self.fld1.SetValue(str(data[1]))
			if data[11] != '' and data[11] != None:
				self.fld2.SetValue(data[11])
			if data[2] != '' and data[2] != None:
				self.fld3.SetValue(data[2])
			if data[2] == None:
				self.fld3.SetValue('-----')
				self.disableall(1)
			if data[8] != '' and data[8] != None:
				self.iconfile.SetPath(ICONS_MENU+data[8])
				self.icon1.SetBitmap(wx.Bitmap(ICONS_MENU+data[8],wx.BITMAP_TYPE_ANY))
			if data[9] != '' and data[9] != None:
				self.fld4.SetValue(data[9])
			if data[7] != '' and data[7] != None:
				self.fld6.SetValue(data[7])
			if data[3] == 'N':
				self.rdio1.SetValue(1)
			elif data[3] == 'C':
				self.rdio2.SetValue(1)
			elif data[3] == 'R':
				self.rdio3.SetValue(1)
			elif data[3] == 'S':
				self.rdio4.SetValue(1)
			else:
				pass
			if data[16] != 1 and data[16] != None:
				self.chk1.SetValue(1)

			if data[17] != None:
				mydir = self.MyMenu.GetDirCod(data[19])[0][0]
				self.prgfld.SetValue(data[18])
				self.lbl9.SetLabel(_('Directory: ')+mydir)


	def addit( self, event ):
		#print(self.itmcod)
		if int(self.itmcod) < 1000:
			self.newone = True
			#print('newone')
		elif int(self.itmcod) > 1000:
			#print(self.itmdata)
			if self.itmdata[3] == 'S':
				self.newsub = True
				#print('newsub')
		else:
			wx.MessageBox(_('Some things wrong!'))

		self.fld1.SetValue('')
		self.fld2.SetValue('')
		self.fld3.SetValue('')
		self.iconfile.SetPath(ICONS_MENU )
		#self.icon1.SetBitmap(wx.Bitmap(ICONS_PATH + u"image.png", wx.BITMAP_TYPE_ANY))
		self.icon1.SetBitmap(icon.image.GetBitmap())
		self.fld4.SetValue('')
		self.fld6.SetValue('')
		self.rdio1.SetValue(1)
		self.rdio2.SetValue(0)
		self.rdio3.SetValue(0)
		self.rdio4.SetValue(0)
		self.chk1.SetValue(0)
		self.chk2.SetValue(0)
		self.prgfld.SetValue('')
		self.lbl9.SetLabel(_('Directory: '))
		event.Skip()

	def edtit( self, event ):
		#print(self.bardata)
		if self.bardata[2] == None:
			wx.MessageBox(_('You can NOT edit Separator line'))
			return 1
		U = self.getfild()
		#print(U)
		#print(self.prgfld.GetValue())
		hnd = self.prgfld.GetValue().replace('.py', '')
		Hndlid = self.findhandler(hnd)


		self.DoMenu.Table = u'mitem'
		self.DoMenu.Upditem(u'itemname = ?, itemtyp = ? , handlerid = ?  where itemid = %d' % self.bardata[1],[U[2], U[6], Hndlid])

		self.DoMenu.Table = u'extended'
		self.DoMenu.Upditem(u'status = ?, icon = ?, shortcut = ? , help = ?  where extid = "%s" ' % self.bardata[4],
		                      [U[5], U[3].replace(ICONS_MENU, ''), U[4], U[5]])

		self.DoMenu.Table = u'access'
		self.DoMenu.Upditem(u'acclvl = ? , disenable = ?  where acclvlid = "%s" ' % self.bardata[11], [U[8], U[7]])

		self.ChngMnu(U)

		wx.MessageBox(_('Menu Edited Successfully'))

		self.DVC1.DeleteAllItems()
		self.fillList()
		self.Refresh()
		self.Layout()


	def delit( self, event ):
		#print('del it',self.itmcod)
		myitmdel = self.MyMenu.getmItem(int(self.itmcod))[0]
		#print(myitmdel)
		if myitmdel[3] == 'S' and self.MyMenu.gBarItm(int(myitmdel[1])) != []:
			wx.MessageBox(_('Please remove the sub menu item first!'))
		else:
			self.DoMenu.Table = u'mitem'
			self.DoMenu.Delitem(u'mitem.itemid = %d' % myitmdel[1])

			self.DoMenu.Table = u'extended'
			self.DoMenu.Delitem(u'extended.extid = "%s"' % myitmdel[4])

			self.DoMenu.Table = u'access'
			self.DoMenu.Delitem(u'access.acclvlid = "%s"' % myitmdel[11])

			self.delmenu()

			self.DVC1.DeleteAllItems()
			self.fillList()
			self.Refresh()
			self.Layout()

		event.Skip()

	def sprit( self, event ):
		#print('Seperat',self.bardata)
		britm = self.MyMenu.gBarItm(int(self.bardata[0]))[-1]

		self.DoMenu.Table = 'mitem'
		self.DoMenu.Additem(u'mbarid, itemid', [britm[0], int(britm[1]) + 1])
		mw = self.FindWindowByName('main')
		mb = mw.GetMenuBar()

		mb.AddSepar(self.bardata[1])

		self.DVC1.DeleteAllItems()
		self.fillList()
		self.Refresh()
		self.Layout()
		event.Skip()

	def bakit( self, event ):
		self.DVC1.DeleteAllItems()
		self.fillList()
		self.Refresh()
		event.Skip()

	def forit( self, event ):
		mw = self.FindWindowByName('main')
		mb = mw.GetMenuBar().GetMenus()
		lmb = mb
		#print(lmb)
		for itm in lmb:
			#print(itm[0].GetMenuItems())
			for i in itm[0].GetMenuItems():
				#print(i.GetId())
				print(i.GetItemLabel())

	def aplit( self, event ):
		D = self.getfild()
		#print(D, self.newsub, self.newone)
		if self.newone:
			extid = D[0][0] + D[0][-1] + D[6] + D[2][-1] + D[2][0] + D[0][1:]
			#print(extid)
			if self.prgfld.GetValue() == '':
				hndid = 10001
			else:
				hndid = self.getHandel(self.prgfld.GetValue(), self.lbl9.GetLabel().split(_('Directory: '))[1])
			if self.newsub:
				BrM = int(self.itmcod)
			else:
				BrM = self.bardata[0]

			Dsri1 = [BrM, int(D[0]), D[2], D[6], extid, hndid]
			Dsri2 = [extid, D[5], D[3], D[4], D[5], D[1], 1]

			self.Add2Menu(D)

			Dsri3 = [D[1], 1, D[8], D[7]]
			self.DoMenu.Table = u'mitem'
			self.DoMenu.Additem(u'mbarid, itemid, itemname, itemtyp, extid, handlerid ', Dsri1)
			self.DoMenu.Table = u'extended'
			self.DoMenu.Additem(u'extid, status, icon, shortcut, help, acclvlid, grpid', Dsri2)
			self.DoMenu.Table = u'access'
			self.DoMenu.Additem(u'acclvlid, userid, acclvl, disenable', Dsri3)
			#self.Add2Menu(D)
			wx.MessageBox(_(u'you successful add menu '))

			self.DVC1.DeleteAllItems()
			self.fillList()
			self.Refresh()
			self.newone = False

		elif self.newsub:
			extid = D[0][0] + D[0][-1] + D[6] + D[2][-1] + D[2][0] + D[0][1:]
			# print(extid)
			if self.prgfld.GetValue() == '':
				hndid = 10001
			else:
				hndid = self.getHandel(self.prgfld.GetValue(), self.lbl9.GetLabel().split(_('Directory: '))[1])
			BrM = int(self.itmcod)
			Dsri1 = [BrM, int(D[0]), D[2], D[6], extid, hndid]
			Dsri2 = [extid, D[5], D[3], D[4], D[5], D[1], 1]
			#print(D[7],D[8])

			self.Add2Menu(D)

			Dsri3 = [D[1], 1, D[8], D[7]]
			self.DoMenu.Table = u'mitem'
			self.DoMenu.Additem(u'mbarid, itemid, itemname, itemtyp, extid, handlerid ', Dsri1)
			self.DoMenu.Table = u'extended'
			self.DoMenu.Additem(u'extid, status, icon, shortcut, help, acclvlid, grpid', Dsri2)
			self.DoMenu.Table = u'access'
			self.DoMenu.Additem(u'acclvlid, userid, acclvl, disenable', Dsri3)
			#self.Add2Menu(D)
			wx.MessageBox(_(u'you successful add menu '))

			self.DVC1.DeleteAllItems()
			self.fillList()
			self.Refresh()
		else:
			wx.MessageBox(_(u'Please Use Edit icon or first Add item'))

		event.Skip()

	def disableall(self,Do):
		if Do:
			self.titr.Disable()
			self.fld1.Disable()
			self.fld2.Disable()
			self.fld3.Disable()
			self.iconfile.Disable()
			self.icon1.Disable()
			self.fld4.Disable()
			self.fld6.Disable()
			self.prgfld.Disable()
			self.lbl9.Disable()
		else:
			self.titr.Enable()
			self.fld1.Enable()
			self.fld2.Enable()
			self.fld3.Enable()
			self.iconfile.Enable()
			self.icon1.Enable()
			self.fld4.Enable()
			self.fld6.Enable()
			self.prgfld.Enable()
			self.lbl9.Enable()


	def chkshrtcut(self,Data):
	    if Data[4] != '':
		    return Data[2] + '\t' + Data[4]
	    else:
		    return Data[2]

	def Add2Menu(self, D):
		mw = self.FindWindowByName('main')
		#mb = mw.GetMenuBar()
		#lmb = mb.GetMenus()
		#print(self.bardata,D)
		#mnuitm = [i[0] for i in lmb if self.bardata[1] in i]
		#print(mnuitm,lmb,mb)
		#print(mw.menu)
		mb = mw.menu
		if D[6] == 'N':
			if type(self.bardata[1]) == str:
				mb.AddItem2(self.bardata[1],D)
			elif type(self.bardata[1]) == int and type(self.bardata[2]) == str:
				mb.AddItem2(self.bardata[2], D, self.bardata[3])

		if D[6] == 'S':
			if type(self.bardata[1]) == str:
				mb.AddSubMenu2(self.bardata[1],D)
			elif type(self.bardata[1]) == int and type(self.bardata[2]) == str:
				mb.AddSubMenu2(self.bardata[2], D, self.bardata[3])


		#if D[6] == 'N':
		#	if type(self.bardata[1]) == str:
		#		mb.AddItem(self.bardata[1],D)
		#	elif type(self.bardata[1]) == int and type(self.bardata[2]) == str:
		#		mb.AddItem(self.bardata[2], D, self.bardata[3])
		if D[6] == 'C':
			mb.AddCheck(self.bardata[1],D)
		if D[6] == 'R':
			mb.AddRadio(self.bardata[1],D)
		#if D[6] == 'S':
		#	if type(self.bardata[1]) == str:
		#		mb.AddSubMenu(self.bardata[1],D)
		#	elif type(self.bardata[1]) == int and type(self.bardata[2]) == str:
		#		mb.AddSubMenu(self.bardata[2], D, self.bardata[3])

	def ChngMnu(self, D):
		mw = self.FindWindowByName('main')
		mb = mw.GetMenuBar()
		lmb = mb.GetMenus()
		mitm = mb.FindItemById(self.bardata[1])
		#print(mitm)
		mnu = mitm.GetMenu()
		#print(mb)
		#print(mnu)
		if D[6] == 'S':
			#mb.CngSubMenu(mitm,D,1)
			mitm.SetSubMenu(mnu)
			wx.MessageBox(_('Please Close Application Now!'))
		#print(mitm.IsSubMenu())
		if D[4] != '':
			lbl = D[2] + '\t' + D[4]
		else:
			lbl = D[2]
		mitm.SetItemLabel(lbl)
		if D[3] != '':
			mitm.SetBitmap(wx.Bitmap(ICONS_MENU+D[3], wx.BITMAP_TYPE_ANY))
		if D[5] != '':
			mitm.SetHelp(D[5])
		mitm.Enable(not D[7])


	def delmenu(self):
		mw = self.FindWindowByName('main')
		mb = mw.GetMenuBar()
		lmb = mb.GetMenus()

		mitm = mb.FindItemById(self.bardata[1])
		#print(mitm)
		if mitm == None:
			for l in lmb:
				#print(l[0].GetMenuItems())
				for lbl in l[0].GetMenuItems():
					if self.bardata[2] in lbl.GetItemLabel():
						#print(lbl.IsSubMenu())
						mnu = lbl.GetMenu()
						mnu.DestroyItem(lbl)
		else:
			mnu = mitm.GetMenu()
			mnu.Delete(self.bardata[1])


	def gnrcod( self, event ):
		if self.fld1.GetValue() == '':
			scod = int(str(self.bardata[0])[0])
			barcod = self.MyMenu.AllBar(u" where menubar.mbarid/100 = %d " %scod)[0][0]
			#print(barcod)
			britm = self.MyMenu.gItem(int(barcod), "or mitem.mbarid > %d and mitem.mbarid < %d" % (int(scod*1000), int(str(scod)+'999')) )
			#print(britm,type(britm))
			if britm != []:
				#print(britm[-1][1] + 1)
				self.fld1.SetValue(str(britm[-1][1] + 1))
				if type(self.bardata[1]) == str:
					cd = self.bardata[1][0].lower() + self.bardata[1][-1].lower()
				elif type(self.bardata[2]) == str:
					cd = self.bardata[2][0].lower() + self.bardata[2][-1].lower()
				else:
					cd = 'aa'
				self.fld2.SetValue(str(britm[-1][1] + 1)[0] + str(britm[-1][1] + 1)[-2:] + cd)
			else:
				#print(britm)
				self.fld1.SetValue(str(self.bardata[0]) + '1')
				self.fld2.SetValue(str(self.bardata[0])[0] + '1' + str(self.bardata[0])[-1] + self.bardata[1][0].lower() + self.bardata[1][-1].lower())
		event.Skip()

	def icnslct( self, event ):
		if RES_PATH not in self.iconfile.GetPath():
			#print(self.iconfile.GetPath())
			CopyIcon(self.iconfile.GetPath())
		self.icon1.SetBitmap(wx.Bitmap(self.iconfile.GetPath(), wx.BITMAP_TYPE_ANY))
		event.Skip()

	def disbl( self, event ):
		if self.dis_enb == 1:
			self.dis_enb = 0
		else:
			self.dis_enb = 1
		event.Skip()

	def hidit( self, event ):
		if self.shw_hid == 1:
			self.shw_hid = 0
		else:
			self.shw_hid = 1
		event.Skip()

	def normnu( self, event ):
		event.Skip()

	def chkmnu( self, event ):
		event.Skip()

	def rdomnu( self, event ):
		event.Skip()

	def submnu( self, event ):
		event.Skip()

	def prglst( self, event ):
		#print(wx.FindWindowByName(u'List of Program'))
		#print(self.GetParent())
		if wx.FindWindowByName(u'List of Program') == None:
			import DCC1.ProgDev2 as DP
			ifrm = wx.Frame(self, -1, style=wx.FRAME_FLOAT_ON_PARENT | wx.DEFAULT_FRAME_STYLE)
			pnl = DP.MyPanel1(ifrm,[self.GetParent()])
			ifrm.SetSize((555, 460))
			ifrm.SetTitle(u'List of Program')
			ifrm.Show()
			#print( 'transfer:',ifrm.TransferDataFromWindow() )
			#print(ifrm.IsUnlinked())
		else:
			wx.MessageBox(_("Double Program: Please Close Program Develop then Do this item"))
		event.Skip()

	def getHandel(self, imodel, pathfile):
		# print(imodel,pathfile)
		pr = self.getMData.AllHndl()
		# m = imodel.split('.')[1]
		for p in pr:
			if imodel in p:
				return p[0]
		return 99000

	def findhandler(self, hndlrnm):
		if hndlrnm == '':
			return 99000
		else:
			codid , self.prgdir = self.MyMenu.getHndlr(hndlrnm)[0]
			return codid

	def getfild(self):
		Data1 = self.fld1.GetValue()
		Data2 = self.fld2.GetValue()
		Data3 = self.fld3.GetValue()
		Data4 = self.iconfile.GetPath().split(SLASH)[-1]
		Data5 = self.fld4.GetValue()
		Data6 = self.fld6.GetValue()
		if self.rdio1.GetValue():
			Data7 = 'N'
		elif self.rdio2.GetValue():
			Data7 = 'C'
		elif self.rdio3.GetValue():
			Data7 = 'R'
		elif self.rdio4.GetValue():
			Data7 = 'S'
		else:
			Data7 = ''
		if self.chk1.GetValue():
			Data8 = 0
		else:
			Data8 = 1
		if self.chk2.GetValue():
			Data9 = '0000'
		else:
			Data9 = 'FFFF'
		return [Data1, Data2, Data3, Data4, Data5, Data6, Data7, Data8, Data9]

	def Splt1OnIdle( self, event ):
		self.Splt1.SetSashPosition( 0 )
		self.Splt1.Unbind( wx.EVT_IDLE )

	def Nbar(self, event):
		title = _("Note:   Avoid duplicate code for create and choose the correct format [991] [99az] \
	             A list of definition and access codes can be viewed at the last button in first row [...] \
	             You can use the same directories for the several menu bar . ")
		self.Frm = wx.Dialog(self)
		self.Pnl = MyPanel3(self.Frm, ['', '', '', '', [(u'', u'', u'', u'')]], _('Create'), title)
		self.Frm.SetSize((500, 235))
		self.Frm.SetTitle(_('New Menu Bar'))
		self.Frm.ShowModal()
		self.DVC1.DeleteAllItems()
		self.fillList()
		self.Refresh()
		self.Layout()
		self.Frm.Destroy()

	def Cbar(self, event):
		title = _("Note:   Avoid duplicate code for changes and choose the correct format [991] [99az] \
	             A list of definition and access codes can be viewed at the last button in first row [...]\
	             You can use the same directories for the several menu bar . ")
		ps = self.DVC1.GetSelections()

		self.itmcod = self.DVC1.GetItemText(ps[0], 0)
		self.itmnam = self.DVC1.GetItemText(ps[0], 1)

		dd = [self.bardata[1], str(self.bardata[0]), self.bardata[3], self.bardata[2], [(self.bardata[4:])]]
		#print(dd)
		#self.itmdir = self.DVC1.GetItemText(ps[0], 2)
		#self.itmacc = self.DVC1.GetItemText(ps[0], 3)
		#self.accrcd = self.MyMenu.Acclvl(self.itmacc)
		#dd = [self.itmnam, self.itmcod, self.itmacc, self.itmdir, self.accrcd]
		self.Frm = wx.Dialog(self)
		self.Pnl = MyPanel3(self.Frm, dd, _('Change'), title)
		self.Frm.SetSize((500, 235))
		self.Frm.SetTitle(_('Change Menu Bar'))
		self.Frm.ShowModal()
		self.DVC1.DeleteAllItems()
		self.fillList()
		self.Refresh()
		self.Layout()
		self.Frm.Destroy()

	def Dbar(self, event):
		title = _(" Note : that by deleting the menu bar, all the items below it will also be removed \
	              Only the programs attached to the items will not be removed and the code will remain \
	              You can assign them to other items or create a new item . ")
		ps = self.DVC1.GetSelections()
		self.itmcod = self.DVC1.GetItemText(ps[0], 0)
		self.itmnam = self.DVC1.GetItemText(ps[0], 1)

		dd = [self.bardata[1],str(self.bardata[0]),self.bardata[3],self.bardata[2],[(self.bardata[4:])]]
		#print(dd)
		#self.accrcd = self.MyMenu.Acclvl(self.itmacc)
		#dd = [self.itmnam, self.itmcod, self.itmacc, self.itmdir, self.accrcd]
		self.Frm = wx.Dialog(self)
		self.Pnl = MyPanel3(self.Frm, dd, _('Delete'), title)
		self.Frm.SetSize((500, 235))
		self.Frm.SetTitle(_('Delete Menu Bar'))
		self.Frm.ShowModal()
		if self.Pnl.Action:
			wx.MessageBox(_(u'Menu Bar and Access and Sub Item successfully Deleted'))
		self.DVC1.DeleteAllItems()
		self.fillList()
		self.Refresh()
		self.Layout()
		self.Frm.Destroy()

###########################################################################
## Class MyPanel3
###########################################################################

class MyPanel3 ( wx.Panel ):

    def __init__( self, parent,Data,Buttom ,title,id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,235 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        self.Data = Data
        self.Buttom = Buttom
        self.GetMenu = MS.GetData(u'Menu2.db',u'')
        self.SetMenu = MS.SetData(u'',u'',u'')
        self.Action = False
        self.box1val = 1
        self.box2val = 'FFFF'
        self.oldbar = self.Data[0]


        Vsz1 = wx.BoxSizer(wx.VERTICAL)

        Vst = wx.BoxSizer(wx.VERTICAL)

        self.title = wx.StaticText(self, wx.ID_ANY, title, wx.DefaultPosition, wx.DefaultSize,0)
        self.title.Wrap(1)
        Vst.Add(self.title, 1, wx.ALL | wx.EXPAND, 5)

        Vsz1.Add(Vst, 1, wx.EXPAND, 5)

        Hsz1 = wx.BoxSizer(wx.HORIZONTAL)

        self.txt1 = wx.StaticText(self, wx.ID_ANY, _(u"Bar name"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.txt1.Wrap(-1)

        Hsz1.Add(self.txt1, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.fld1 = wx.TextCtrl(self, wx.ID_ANY, self.Data[0], wx.DefaultPosition, wx.DefaultSize, 0)
        Hsz1.Add(self.fld1, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.txt2 = wx.StaticText(self, wx.ID_ANY, _(u"ID"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.txt2.Wrap(-1)

        Hsz1.Add(self.txt2, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.fld2 = wx.TextCtrl(self, wx.ID_ANY, self.Data[1], wx.DefaultPosition, wx.Size(50, -1), 0)
        Hsz1.Add(self.fld2, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.txt3 = wx.StaticText(self, wx.ID_ANY, _(u"Access"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.txt3.Wrap(-1)

        Hsz1.Add(self.txt3, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.fld3 = wx.TextCtrl(self, wx.ID_ANY, self.Data[2], wx.DefaultPosition, wx.Size(50, -1), 0)
        Hsz1.Add(self.fld3, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.atobtn = wx.Button(self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT)
        Hsz1.Add(self.atobtn, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)
        self.atobtn.SetToolTip(_(u"Automatic code generate"))

        Vsz1.Add(Hsz1, 0, wx.EXPAND, 5)

        Hsz2 = wx.BoxSizer(wx.HORIZONTAL)

        self.txt4 = wx.StaticText(self, wx.ID_ANY, _(u"Directory"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.txt4.Wrap(-1)

        Hsz2.Add(self.txt4, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.dirct = wx.DirPickerCtrl(self, wx.ID_ANY, SRC_PATH+u'prg'+SLASH+self.Data[3][4:], _(u"Select a folder"), wx.DefaultPosition,
                                      wx.DefaultSize, wx.DIRP_DEFAULT_STYLE | wx.DIRP_SMALL)
        Hsz2.Add(self.dirct, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        Vsz1.Add(Hsz2, 0, wx.EXPAND, 5)

        Hsz3 = wx.BoxSizer(wx.HORIZONTAL)

        self.box1 = wx.CheckBox(self, wx.ID_ANY, _(u"Disable"), wx.DefaultPosition, wx.DefaultSize, 0)
        Hsz3.Add(self.box1, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.box2 = wx.CheckBox(self, wx.ID_ANY, _(u"Hiden"), wx.DefaultPosition, wx.DefaultSize, 0)
        Hsz3.Add(self.box2, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        if self.Data[4][0][2] == '0000':
            self.box2.SetValue(True)
        if self.Data[4][0][3] == 0:
            self.box1.SetValue(True)

        Vsz1.Add(Hsz3, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        Hsz4 = wx.BoxSizer(wx.HORIZONTAL)

        Hsz4.Add((0, 0), 1, wx.EXPAND, 5)

        self.btn1 = wx.Button(self, wx.ID_ANY, _(u"Cancle"), wx.DefaultPosition, wx.DefaultSize, 0)
        Hsz4.Add(self.btn1, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.btn2 = wx.Button(self, wx.ID_ANY, Buttom, wx.DefaultPosition, wx.DefaultSize, 0)
        Hsz4.Add(self.btn2, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        Vsz1.Add(Hsz4, 0, wx.EXPAND, 5)

        self.SetSizer(Vsz1)
        self.Layout()

        # Connect Events
        self.atobtn.Bind( wx.EVT_BUTTON, self.atocod )
        self.dirct.Bind(wx.EVT_DIRPICKER_CHANGED, self.bardir)
        self.box1.Bind(wx.EVT_CHECKBOX, self.disbar)
        self.box2.Bind(wx.EVT_CHECKBOX, self.hidbar)
        self.btn1.Bind(wx.EVT_BUTTON, self.cancl)
        self.btn2.Bind(wx.EVT_BUTTON, self.doit)

    def __del__(self):
        pass

        # Virtual event handlers, overide them in your derived class

    def atocod(self, event):
        if self.Buttom == _('Create'):
            allbar = self.GetMenu.AllBar('where mbarid < 9999')
            #print(allbar)
            if allbar != [] :
                #print(allbar[-1][0]+100)
                alphabt = '_abcdefghijklmnopqrstuvwxyz'
                lnumstr = str(allbar[-1][0]+100)[0]
                rnumstr = str(allbar[-1][0]+100)[-1]
                self.fld2.SetValue(str(allbar[-1][0]+100))
                self.fld3.SetValue(lnumstr+rnumstr+alphabt[int(lnumstr)]+alphabt[int(rnumstr)])
            else:

                self.fld2.SetValue(str(101))
                self.fld3.SetValue('11aa')

    def bardir(self, event):
        mydir = event.GetEventObject().GetPath()
        mydir.replace(Src_prg,u"Src.prg.")
        #print(mydir)

        self.newdir = mydir.replace(Src_prg,u"Src.prg.")
        #print(self.newdir)

    def finddir(self, data):
	    #print(data)
	    aldir = self.GetMenu.AllGuiDir()
	    for dr in aldir:
		    if data in dr:
			    #print(dr)
			    return dr[1]
	    return ''

    def disbar(self, event):
        if event.GetEventObject().GetValue():
            self.box1val = 0
        else:
            self.box1val = 1
        #print(self.box1val)

    def hidbar(self, event):
        if event.GetEventObject().GetValue():
            self.box2val = '0000'
        else:
            self.box2val = 'FFFF'
        #print(self.box2val)

    def cancl(self, event):
        self.Action = False
        q = self.GetParent()
        q.Close()

    def doit(self, event):
	    mw = self.FindWindowByName('main')
	    if mw.GetMenuBar() != None:
		    mb = mw.GetMenuBar()
		    pass
	    else:
		    mb = mw.NewMenu()
		    pass

	    if event.GetEventObject().GetLabel() == _('Create'):
		    data1 = self.fld1.GetValue()
		    data2 = self.fld2.GetValue()
		    data3 = self.fld3.GetValue()
		    mydir = self.dirct.GetPath()
		    self.newdir = mydir.replace(Src_prg, u"Src.prg.")
		    self.hdddir = mydir.replace(Src_prg, u'..\\Src\\prg\\')
		    if self.finddir(self.hdddir) != '':
			    dircod = self.finddir(self.hdddir)
			    #dircod = self.GetMenu.GetDirCod(self.newdir)
			    #print(dircod)
			    pass
		    else:
			    dircod = str(data2)+'1'
			    self.SetMenu.Table = u'Guidir'
			    self.SetMenu.Additem(u' Dir, prgdir, hdddir', (self.newdir,dircod,self.hdddir))
			    os.mkdir(mydir)
			    os.chdir(mydir)
			    with open(u'__init__.py',u'w+') as f:
				    f.write('')

			    pass
		    #print(dircod)
		    self.SetMenu.Table = u'menubar'
		    self.SetMenu.Additem(u'mbarid , mbarname , mbardir ,  acclvlid ', (data2,data1,dircod,data3))
		    data4 = self.box1val
		    data5 = self.box2val
		    self.SetMenu.Table = u'access'
		    self.SetMenu.Additem(u'acclvlid , userid , acclvl , disenable ',(data3, 1, data5, data4))

		    mb.Append(wx.Menu(),data1)

	    elif event.GetEventObject().GetLabel() == _('Change'):
		    data1 = self.fld1.GetValue()
		    mydir = self.dirct.GetPath()
		    self.newdir = mydir.replace(Src_prg,u"Src.prg.")
		    self.hdddir = mydir.replace(Src_prg, u'..\\Src\\')
		    if self.finddir(self.hdddir) != '':
			    dircod = self.GetMenu.GetDirCod(self.hdddir)
			    #print(dircod)
			    pass
		    else:
			    dircod = str(data2) + '1'
			    self.SetMenu.Table = u'Guidir'
			    self.SetMenu.Additem(u' Dir, prgdir, hdddir', (self.newdir, dircod, self.hdddir))
			    os.mkdir(mydir)
			    os.chdir(mydir)
			    with open(u'__init__.py', u'w+') as f:
				    f.write('')

		    self.SetMenu.Table = u'menubar'
		    self.SetMenu.Upditem(u'mbarname = ? , mbardir = ?  where mbarid = %s ' % self.Data[1],(data1,dircod))
		    data4 = self.box1val
		    data5 = self.box2val
		    #print(data5,data4)
		    self.SetMenu.Table = u'access'
		    self.SetMenu.Upditem(u'acclvl = ? , disenable = ? where acclvlid = "%s" ' % self.Data[2],(data5, int(data4)))
		    mb.SetMenuLabel(mb.FindMenu(self.oldbar),data1)


	    elif event.GetEventObject().GetLabel() == _('Delete'):
		    self.SetMenu.Table = u'menubar'
		    self.SetMenu.Delitem(u" menubar.mbarid = %s" % self.Data[1] )
		    self.SetMenu.Table = u'access'
		    self.SetMenu.Delitem(u" access.acclvlid = '%s' "% self.Data[2])
		    if len(self.GetMenu.gBarItm(self.Data[1])) != 0:
			    for itm in self.GetMenu.gBarItm(self.Data[1]):
				    self.SetMenu.Table = u'mitem'
				    self.SetMenu.Delitem(u" mitem.itemid = %s " % itm[1] )
				    self.SetMenu.Table = u'extended'
				    self.SetMenu.Delitem(u" extended.extid = '%s' " % itm[2])
				    self.SetMenu.Table = u'access'
				    self.SetMenu.Delitem(u" access.acclvlid = '%s' "% itm[3])


		    mb.Remove(mb.FindMenu(self.Data[0]))

	    else:
		    event.Skip()

	    self.Action = True
	    q = self.GetParent()
	    q.Close()