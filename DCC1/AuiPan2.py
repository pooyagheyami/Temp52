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

import importlib

from Config.Init import *
import Database.MenuSet2 as MS
from GUI.AuiPanel.PAui import *

_ = wx.GetTranslation

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

		self.DVC1 = wx.dataview.TreeListCtrl( self.P1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Col1 = self.DVC1.AppendColumn( u"ID", 75, wx.ALIGN_LEFT, wx.COL_RESIZABLE )
		self.Col2 = self.DVC1.AppendColumn( u"Name Pane", 158, wx.ALIGN_LEFT, wx.COL_RESIZABLE )
		Vsz2.Add( self.DVC1, 1, wx.ALL|wx.EXPAND, 5 )

		self.MyMenu = MS.GetData(u'Menu2.db', u'')
		self.DoMenu = MS.SetData(u'', u'', u'')

		self.filllist()

		self.newpen = False
		self.s1 = 'Dock;FTTTTT'
		self.s2 = '-1;-1;0;0'
		self.bst_siz = '-1;-1'
		self.min_siz = '-1;-1'
		self.max_siz = '-1;-1'

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
		self.btn4.SetToolTip(u"Show")
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

		self.myInfo = wx.aui.AuiPaneInfo()

		# Connect Events
		#self.DVC1.Bind( wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED, self.slctmnu, id = wx.ID_ANY )
		self.DVC1.Bind( wx.dataview.EVT_DATAVIEW_SELECTION_CHANGED, self.actitm)
		self.btn1.Bind( wx.EVT_BUTTON, self.addit )
		self.btn2.Bind( wx.EVT_BUTTON, self.edtit )
		self.btn3.Bind( wx.EVT_BUTTON, self.delit )
		self.btn4.Bind( wx.EVT_BUTTON, self.prviw )
		self.btn5.Bind( wx.EVT_BUTTON, self.updat )
		self.btn6.Bind( wx.EVT_BUTTON, self.publc )
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
	def filllist(self):
		broot = self.DVC1.GetRootItem()
		mroot = self.DVC1.AppendItem(broot, 'AuiPanes')
		self.items = self.MyMenu.AllPanes()
		for itm in self.items:
			pnitm = self.DVC1.AppendItem(mroot, itm[1])
			self.DVC1.SetItemText(pnitm, 0, str(itm[0]))
			self.DVC1.SetItemText(pnitm, 1, itm[1])
		pass
	def actitm( self, event ):
		ps2 = self.DVC1.GetSelection()
		it2 =  self.DVC1.GetItemText(ps2,0)
		#print(ps2,it2)
		for tem in self.items:
			if int(it2) in tem:
				#print(tem)
				self.fillinfo(tem)

	def fillinfo(self, Data):
		self.fld1.SetValue(str(Data[0]))
		self.fld2.SetValue(Data[7])
		self.fld3.SetValue(Data[1])
		self.fld4.SetValue(Data[9])
		self.datastng = Data[10]
		#self.gnrsetting(self.datastng)
		self.fld6.SetValue(self.datastng)
		w,h = Data[3].split(';')
		self.wht.SetValue(w)
		self.hgt.SetValue(h)
		self.othrsiz = [Data[12],Data[13],Data[14]]

		self.chs1.SetStringSelection(Data[11])

		dokng,self.dokng = Data[15].split(';')
		self.chs2.SetStringSelection(dokng)

		self.chs3.SetStringSelection(Data[2])
		self.lyrspn.SetValue(Data[4])
		self.opsint = Data[16]

		mydir,myprgnm = self.MyMenu.RunHdnl(Data[6])[0]
		#print(mydir,myprgnm)
		self.prgfld.SetValue(myprgnm+'.py')
		self.lbl9.SetLabel(u"Directory: "+mydir)

	def fillnull(self):
		data = (0,'','','-1;-1',0,'',0,'','','','TTFFTTTFFFFT','','','','','Dock;FTTTTT','-1;-1;0;0')
		self.fillinfo(data)
		self.fld1.SetValue('')


	def slctmnu( self, event ):
		event.Skip()

	def addit( self, event ):
		self.fillnull()
		self.newpen = True
		event.Skip()

	def edtit( self, event ):
		Up1 = self.getdata()
		stng = self.fld6.GetValue()
		if Up1[0] != '':
			if self.prgfld.GetValue() != '':
				hndlid = self.findhndlr(self.prgfld.GetValue().replace('.py','')) #find handlerid

			#print(Up1)
			D1 = [int(Up1[0]), Up1[2], Up1[7], Up1[4], int(Up1[8]), codinfo, hndlid, Up1[1]]

		event.Skip()

	def delit( self, event ):
		#print(self.getdata())
		D = self.getdata()
		for i in self.items:
			if i[0] == int(D[0]):
				Delitem = i
				#print(Delitem)
				self.DoMenu.Table = u'pans'
				self.DoMenu.Delitem(u' pans.panid = %d '% Delitem[0] )
				self.DoMenu.Table = u'panifo'
				self.DoMenu.Delitem(u' panifo.paninfoid = "%s" '% Delitem[8])
				self.DoMenu.Table = u'access'
				self.DoMenu.Delitem(u' access.acclvlid = "%s"' % Delitem[7])

				wx.MessageBox(u' Pane delete from application successful')

		self.DVC1.DeleteAllItems()
		self.filllist()
		self.Refresh()

		event.Skip()

	def updat( self, event ):
		self.DVC1.DeleteAllItems()
		self.filllist()
		self.Refresh()
		event.Skip()

	def publc( self, event ):
		event.Skip()

	def prviw( self, event ):
		#mw = self.FindWindowByName('main')
		#mw.m_mgr.
		#print(self.fld3.GetValue())
		a2 = 'GUI.AuiPanel.'+self.fld3.GetValue()

		try:
			m = importlib.import_module(a2)
			self.Frm = wx.Frame(self, -1, pos=wx.DefaultPosition, size=wx.DefaultSize)
			self.pnl = m.MyPanel1(self.Frm, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
			self.Frm.Show()
		except ImportError as error:
			wx.MessageBox(error)
			print(error)
		event.Skip()

	def aplit( self, event ):
		#self.myInfo = wx.aui.AuiPaneInfo()
		Data1 = self.getdata()
		#print(Data1)
		#print(self.fld6.GetValue())
		stng = self.fld6.GetValue()
		#print(self.s1, self.s2)
		#print(self.fild)
		#print(self.bst_siz,self.min_siz,self.max_siz)
		if self.newpen:
			strng = 'abcdefghijklmnopqrstuvwxyz'
			codinfo = Data1[0]+strng[int(Data1[0][0])-1]+strng[int(Data1[0][1])]
			if self.prgfld.GetValue() == '':
				hndlid = 50000 + int(Data1[0])
				import shutil
				shutil.copyfile(GUI_PATH+'AuiPanel\\tempane.py',GUI_PATH+'AuiPanel\\'+Data1[2]+'.py')
			else:
				hndlid, hndldir = self.MyMenu.getHndlr(self.prgfld.GetValue().replace('.py',''))[0]
				if hndlid == '' or hndlid == None:
					hndlid == 50000

			D1 = [int(Data1[0]),Data1[2],Data1[7],Data1[4],int(Data1[8]),codinfo,hndlid,Data1[1]]
			self.DoMenu.Table = u'pans'
			self.DoMenu.Additem(u' panid, panname, pandok, pansiz, panlyr, paninfoid, handlerid, acclvlid ',D1)

			if self.chs2.GetStringSelection() != 'Dock':
				self.s1 = self.chs2.GetStringSelection()+';'+self.s1.split(';')[1]

			D2 = [codinfo,Data1[3],stng, Data1[5], self.bst_siz, self.min_siz, self.max_siz, self.s1, self.s2]
			self.DoMenu.Table = u'panifo'
			self.DoMenu.Additem(u' paninfoid, caption, setting, resize, bstsiz, minsiz, maxsiz, docking, position',D2)

			D3 = [Data1[1], 1, 'FFFF', 1]
			self.DoMenu.Table = u'access'
			self.DoMenu.Additem(u' acclvlid, userid, acclvl, disenable',D3)

			wx.MessageBox(u'A new Pane add to application ')

			self.DVC1.DeleteAllItems()
			self.filllist()
			self.Refresh()

			#createpenshow()

		else:
			wx.MessageBox(u'Please press Add bottom to make new pane')
		event.Skip()

	def gnrcod( self, event ):
		strng = 'abcdefghijklmnopqrstuvwxyz'
		lcod = self.items[-1][0]
		self.fld1.SetValue(str(int(lcod)+1))
		self.fld2.SetValue(str(int(lcod)+1)+'pn'+strng[(lcod+1)//10-1]+strng[(lcod+1)%10])


	def stngpn( self, event ):
		iwin = wx.Dialog(self, -1)
		pnl = MyPanel2(iwin,self.datastng)
		iwin.SetSize((500, 320))
		iwin.ShowModal()
		try:
			#print(pnl.e)
			self.gnrsetting(pnl.e)
			self.fild = self.crtsetsrt(pnl.e)
			self.fld6.SetValue(self.fild)
		except AttributeError:
			print('Cancel it')
			#print(pnl.PGrid1.GetPropertyValues())
			self.gnrsetting(pnl.PGrid1.GetPropertyValues())
			self.fild = self.crtsetsrt(pnl.PGrid1.GetPropertyValues())
			self.fld6.SetValue(self.fild)

		iwin.Destroy()

	def otrsiz( self, event ):
		iwin = wx.Dialog(self, -1)
		pnl = MyPanel3(iwin,self.othrsiz)
		iwin.SetSize((400, 250))
		iwin.ShowModal()
		print(pnl.PGrid1.GetPropertyValues())
		self.gnrsize(pnl.PGrid1.GetPropertyValues())
		self.crtsizsrt(pnl.PGrid1.GetPropertyValues())
		iwin.Destroy()

	def rezfix( self, event ):
		if self.chs1.GetSelection() == 1:
			self.wht.Disable()
			self.hgt.Disable()
		elif self.chs1.GetSelection() == 0:
			self.wht.Enable()
			self.hgt.Enable()


	def dokflt( self, event ):
		event.Skip()

	def lrtbc( self, event ):
		event.Skip()

	def dockabl(self, event):
		iwin = wx.Dialog(self, -1)
		pnl = MyPanel4(iwin)
		iwin.SetSize((400, 350))
		iwin.ShowModal()
		print(pnl.PGrid1.GetPropertyValues())
		self.gnrdock(pnl.PGrid1.GetPropertyValues(), self.chs2.GetStringSelection())
		self.s1, self.s2 = self.credoksrt(pnl.PGrid1.GetPropertyValues())
		iwin.Destroy()

	def prglst( self, event ):
		if wx.FindWindowByName(u'List of Program') == None:
			import DCC1.ProgDev2 as DP
			ifrm = wx.Frame(self, -1, style=wx.FRAME_FLOAT_ON_PARENT | wx.DEFAULT_FRAME_STYLE)
			pnl = DP.MyPanel1(ifrm,[self.GetParent()])
			ifrm.SetSize((555, 460))
			ifrm.SetTitle(u'List of Program')
			ifrm.Show()
			print(ifrm.TransferDataFromWindow())
		else:
			wx.MessageBox("Double Program: Please Close Program Develop then Do this item")
			pass

	def findhndlr(self, hndlrnm):
		if hndlrnm == '':
			return 50000
		else:
			codid, self.prgdir = self.MyMenu.getHndlr(hndlrnm)[0]
			return codid

	def getdata(self):
		D1 = self.fld1.GetValue()
		D2 = self.fld2.GetValue()
		D3 = self.fld3.GetValue()
		D4 = self.fld4.GetValue()
		#self.datastng = self.getseting()
		#self.fld6.SetValue('')
		#w, h = Data[3].split(';')
		w = self.wht.GetValue()
		h = self.hgt.GetValue()
		D5 = w+';'+h
		#self.othrsiz = self.getothrsiz()
		D6 = self.chs1.GetStringSelection()
		#dokng, self.dokng = Data[15].split(';')
		D7 = self.chs2.GetStringSelection()
		D8 = self.chs3.GetStringSelection()
		D9 = self.lyrspn.GetValue()
		#self.opsint = Data[16]
		return D1,D2,D3,D4,D5,D6,D7,D8,D9

	def getGnral(self):
		mydic = {}
		D = self.getdata()
		mydic['name'] = D[2]
		mydic['caption'] = D[3]
		mydic['fload_size'] = D[4]
		mydic['resize'] = D[5]
		mydic['dock'] = D[6]
		mydic['docking'] = D[7]
		mydic['layer'] = D[8]
		self.myInfo = AuiInfoGen1(mydic,self.myInfo)
		#return self.myInfo

	def gnrsetting(self, Data):
		self.myInfo = AuiInfoSet1(Data,self.myInfo)
		#return self.myInfo

	def gnrsize(self, Data):
		self.myInfo = AuiInfoSiz1(Data,self.myInfo)
		#return self.myInfo

	def gnrdock(self, Data, Dok):
		self.myInfo = AuiInfoDok1(Data, Dok,self.myInfo)
		#return self.myInfo

	def crtsetsrt(self, D):
		s = ''
		#print(D.values())
		for d in D.values():
			if d :
				s += 'T'
			else:
				s += 'F'
		#print(s)
		return s

	def crtsizsrt(self, D):
		self.bst_siz = str(D['best_size'].x)+';'+str(D['best_size'].y)
		self.min_siz = str(D['min_size'].x)+';'+str(D['min_size'].y)
		self.max_siz = str(D['max_size'].x)+';'+str(D['max_size'].y)

	def credoksrt(self, D):
		s1 = s2 = ''
		for d in D.values():
			if type(d) == list:
				s2 = str(d[0])+';'+str(d[1])
			elif type(d) == int:
				s2 += ';'+str(d)
			else:
				if d:
					s1 += 'T'
				else:
					s1 += 'F'
		s1 = self.chs2.GetStringSelection() + ';' + s1
		#print(s1,s2)
		return s1,s2


	def Splt1OnIdle( self, event ):
		self.Splt1.SetSashPosition( 254 )
		self.Splt1.Unbind( wx.EVT_IDLE )




###########################################################################
## Class MyPanel2
###########################################################################
import wx.propgrid as pg


class MyPanel2 ( wx.Panel ):

	def __init__( self, parent,Data='', id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,342 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		Vsz1 = wx.BoxSizer( wx.VERTICAL )

		self.Item = []

		if Data != '':
			for D in Data:
				if D == 'T':
					self.Item.append(True)
				if D == 'F':
					self.Item.append(False)
		else:
			self.Item = [True,True,False,False,True,True,True,False,False,False,False,True]


		items = [('caption_visible',self.Item[0]),('close_button',self.Item[1]),('maximize_button',self.Item[2]),('minimize_button',self.Item[3]),
		         ('pine_button',self.Item[4]),('pane_border',self.Item[5]),('show',self.Item[6]),('gripper',self.Item[7]),('center_pane',self.Item[8]),
		         ('default_pane',self.Item[9]),('toolbar_pane',self.Item[10]),('moveable',self.Item[11]) ]


		self.PGrid1 = pg.PropertyGrid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.propgrid.PG_DEFAULT_STYLE|wx.propgrid.PG_SPLITTER_AUTO_CENTER|wx.propgrid.PG_TOOLTIPS)

		self.PGrid1.Append(pg.PropertyCategory(u"AUI Info", u"AUI Info"))

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


#################################################################################
##  Size Property Class
##
#################################################################################
class SizeProperty(pg.PGProperty):
    """ Demonstrates a property with few children.
    """
    def __init__(self, label, name = pg.PG_LABEL, value=wx.Size(0, 0)):
        pg.PGProperty.__init__(self, label, name)

        value = self._ConvertValue(value)

        self.AddPrivateChild( pg.IntProperty("Width", value=value.x) )
        self.AddPrivateChild( pg.IntProperty("Height", value=value.y) )

        self.m_value = value
        #print(self.m_value)

    def GetClassName(self):
        return self.__class__.__name__

    def DoGetEditorClass(self):
        return pg.PropertyGridInterface.GetEditorByName("TextCtrl")

    def RefreshChildren(self):
        size = self.m_value
        self.Item(0).SetValue( size.x )
        self.Item(1).SetValue( size.y )

    def _ConvertValue(self, value):
        """ Utility convert arbitrary value to a real wx.Size.
        """
        import collections
        if isinstance(value, collections.Sequence) or hasattr(value, '__getitem__'):
            value = wx.Size(*value)
        return value

    def ChildChanged(self, thisValue, childIndex, childValue):
        size = self._ConvertValue(self.m_value)
        if childIndex == 0:
            size.x = childValue
        elif childIndex == 1:
            size.y = childValue
        else:
            raise AssertionError

        return size

###########################################################################
## Class MyPanel3
###########################################################################

class MyPanel3 ( wx.Panel ):

	def __init__( self, parent, LData, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 400,242 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		Vsz1 = wx.BoxSizer( wx.VERTICAL )
		print(LData)
		if LData == ['','','']:
			bsz = wx.Size(-1,-1)
			mnz = wx.Size(-1,-1)
			mxz = wx.Size(-1,-1)
		else:
			a,b = LData[0].split(';')
			bsz = wx.Size(int(a),int(b))
			a, b = LData[1].split(';')
			mnz = wx.Size(int(a),int(b))
			a, b = LData[2].split(';')
			mxz = wx.Size(int(a),int(b))

		self.PGrid1 = pg.PropertyGrid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.propgrid.PG_DEFAULT_STYLE|wx.propgrid.PG_SPLITTER_AUTO_CENTER|wx.propgrid.PG_TOOLTIPS)
		self.Item1 = self.PGrid1.Append( pg.PropertyCategory( u"Other Size", u"Other Size" ) )


		self.Item2 = self.PGrid1.Append( SizeProperty( u"best_size", u"best_size", value=bsz ) )
		self.Item3 = self.PGrid1.Append( SizeProperty( u"min_size", u"min_size", value=mnz ) )
		self.Item4 = self.PGrid1.Append( SizeProperty( u"max_size", u"max_size", value=mxz ) )

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
		q = self.GetParent()
		q.Close()

#################################################################################
##  Pos Property Class
##
#################################################################################
class PosProperty(pg.PGProperty):
    """ Demonstrates a property with few children.
    """
    def __init__(self, label, name = pg.PG_LABEL, value=wx.Position(0, 0)):
        pg.PGProperty.__init__(self, label, name)


        value = self._ConvertValue(value)

        self.AddPrivateChild( pg.IntProperty("X", value=value.Col) )
        self.AddPrivateChild( pg.IntProperty("Y", value=value.Row) )

        self.m_value = value
        #print(self.m_value)

    def GetClassName(self):
        return self.__class__.__name__

    def DoGetEditorClass(self):
        return pg.PropertyGridInterface.GetEditorByName("TextCtrl")

    def RefreshChildren(self):
        pos = self.m_value
        self.Item(0).SetValue( pos[0] )
        self.Item(1).SetValue( pos[1] )

    def _ConvertValue(self, value):
        """ Utility convert arbitrary value to a real wx.Size.
        """
        import collections
        if isinstance(value, collections.Sequence) or hasattr(value, '__getitem__'):
            value = wx.Position(*value)
        return value

    def ChildChanged(self, thisValue, childIndex, childValue):
        pos = self._ConvertValue(self.m_value)
        if childIndex == 0:
            pos.Row = childValue
        elif childIndex == 1:
            pos.Col = childValue
        else:
            raise AssertionError

        return pos


###########################################################################
## Class MyPanel4
###########################################################################

class MyPanel4 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,320 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		Vsz1 = wx.BoxSizer( wx.VERTICAL )

		self.data = [False,True,True,True,True,True]

		self.Items = [(u'dock_fixed',self.data[0]),(u'floatable',self.data[1]),(u'bottom Dockable',self.data[2]),
		              (u'Top Dockable',self.data[3]),(u'Left Dockable',self.data[4]),(u'Right Dockable',self.data[5])]

		self.PGrid1 = pg.PropertyGrid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.propgrid.PG_DEFAULT_STYLE|wx.propgrid.PG_SPLITTER_AUTO_CENTER|wx.propgrid.PG_TOOLTIPS)
		self.Item1 = self.PGrid1.Append( pg.PropertyCategory( u"Docking", u"Docking" ) )

		for itm in self.Items:
			self.PGrid1.Append( pg.BoolProperty(itm[0], itm[0], value=itm[1] ) )
			self.PGrid1.SetPropertyAttribute(itm[0], "UseCheckbox", True)


		self.Item3 = self.PGrid1.Append( PosProperty( u"pane_position", u"pane_position", value=wx.DefaultPosition ) )
		self.Item4 = self.PGrid1.Append( pg.IntProperty( u"aui_position", u"aui_position" ) )
		self.Item5 = self.PGrid1.Append( pg.IntProperty( u"aui_row", u"aui_row" ) )

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


