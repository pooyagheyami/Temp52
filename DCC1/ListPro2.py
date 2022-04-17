# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################
import os

import wx
import wx.xrc
import wx.dataview

from Config.Init import *
import Res.Allicons as icon

import Database.MenuSet2 as MS
import Database.PostGet as PG
import GUI.proman as pro
import importlib
#import importlib.util

import AI.Analiz
import AI.OpnSrc as OS
from AI.Analiz import *
from AI.Generats import *

_ = wx.GetTranslation

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

		self.Titr1 = wx.StaticText( self.P1, wx.ID_ANY, _(u"List of Programs and Tools can download"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Titr1.Wrap( -1 )

		Vsz2.Add( self.Titr1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.TLC1 = wx.dataview.TreeListCtrl( self.P1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.dataview.TL_DEFAULT_STYLE )
		self.TLC1.AppendColumn( _(u"Name"), 200, wx.ALIGN_LEFT, wx.COL_RESIZABLE )
		self.TLC1.AppendColumn( _(u"ID"), 25, wx.ALIGN_LEFT, wx.COL_RESIZABLE )

		Vsz2.Add( self.TLC1, 1, wx.EXPAND |wx.ALL, 5 )

		#Hsz1 = wx.BoxSizer( wx.HORIZONTAL )


		#Vsz2.Add( Hsz1, 0, wx.EXPAND, 5 )

		Hsz2 = wx.BoxSizer( wx.HORIZONTAL )

		self.CntSrv = wx.Button( self.P1, wx.ID_ANY, _(u"Connect to server "), wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz2.Add( self.CntSrv, 1, wx.ALL, 5 )


		Vsz2.Add( Hsz2, 0, wx.EXPAND, 5 )

		Hsz3 = wx.BoxSizer( wx.HORIZONTAL )

		self.btn1 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		#self.btn1.SetBitmap(wx.Bitmap(ICON16_PATH + u'application_add.png', wx.BITMAP_TYPE_ANY))
		self.btn1.SetBitmap(icon.application_add.GetBitmap())
		self.btn1.SetToolTip(_(u"Add"))
		Hsz3.Add( self.btn1, 0, wx.ALL, 5 )

		self.btn2 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		#self.btn2.SetBitmap(wx.Bitmap(ICON16_PATH + u'application_edit.png', wx.BITMAP_TYPE_ANY))
		self.btn2.SetBitmap(icon.application_edit.GetBitmap())
		self.btn2.SetToolTip(_(u"Edit"))
		Hsz3.Add( self.btn2, 0, wx.ALL, 5 )

		self.btn3 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		#self.btn3.SetBitmap(wx.Bitmap(ICON16_PATH + u'application_delete.png', wx.BITMAP_TYPE_ANY))
		self.btn3.SetBitmap(icon.application_delete.GetBitmap())
		self.btn3.SetToolTip(_(u"Delete"))
		Hsz3.Add( self.btn3, 0, wx.ALL, 5 )

		self.btn4 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		#self.btn4.SetBitmap(wx.Bitmap(ICON16_PATH + u'application_form.png', wx.BITMAP_TYPE_ANY))
		self.btn4.SetBitmap(icon.application_form.GetBitmap())
		self.btn4.SetToolTip(_(u"Preview"))
		Hsz3.Add( self.btn4, 0, wx.ALL, 5 )

		self.btn5 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		#self.btn5.SetBitmap(wx.Bitmap(ICON16_PATH + u'update.png', wx.BITMAP_TYPE_ANY))
		self.btn5.SetBitmap(icon.update.GetBitmap())
		self.btn5.SetToolTip(_(u"Update"))
		Hsz3.Add( self.btn5, 0, wx.ALL, 5 )

		self.btn6 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		#self.btn6.SetBitmap(wx.Bitmap(ICON16_PATH + u'application_put.png', wx.BITMAP_TYPE_ANY))
		self.btn6.SetBitmap(icon.application_put.GetBitmap())
		self.btn6.SetToolTip(_(u"Download"))
		Hsz3.Add( self.btn6, 0, wx.ALL, 5 )

		self.btn7 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		#self.btn7.SetBitmap(wx.Bitmap(ICON16_PATH + u'application_lightning.png', wx.BITMAP_TYPE_ANY))
		self.btn7.SetBitmap(icon.application_lightning.GetBitmap())
		self.btn7.SetToolTip(_(u"Generate"))
		Hsz3.Add( self.btn7, 0, wx.ALL, 5 )


		Vsz2.Add( Hsz3, 0, wx.EXPAND, 5 )


		self.P1.SetSizer( Vsz2 )
		self.P1.Layout()
		Vsz2.Fit( self.P1 )
		self.P2 = wx.Panel( self.Splt1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		Vsz3 = wx.BoxSizer( wx.VERTICAL )

		self.Titr2 = wx.StaticText( self.P2, wx.ID_ANY, _(u"Description"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Titr2.Wrap( -1 )

		Vsz3.Add( self.Titr2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		Hsz11 = wx.BoxSizer( wx.HORIZONTAL )

		self.Descr = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.TE_MULTILINE )
		Hsz11.Add( self.Descr, 1, wx.ALL|wx.EXPAND, 5 )


		Vsz3.Add( Hsz11, 1, wx.EXPAND, 5 )

		Hsz12 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl1 = wx.StaticText( self.P2, wx.ID_ANY, _(u"To Menu id "), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl1.Wrap( -1 )

		Hsz12.Add( self.lbl1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld1 = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz12.Add( self.fld1, 1, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )

		self.btn8 = wx.Button( self.P2, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		Hsz12.Add( self.btn8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz12, 0, wx.EXPAND, 5 )

		Hsz13 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl2 = wx.StaticText( self.P2, wx.ID_ANY, _(u"To Directory"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl2.Wrap( -1 )

		Hsz13.Add( self.lbl2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.dir2 = wx.DirPickerCtrl( self.P2, wx.ID_ANY, wx.EmptyString, _(u"Select a folder"), wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE|wx.DIRP_SMALL )
		Hsz13.Add( self.dir2, 1, wx.ALL, 5 )


		Vsz3.Add( Hsz13, 0, wx.EXPAND, 5 )

		Hsz14 = wx.BoxSizer( wx.HORIZONTAL )

		self.btn9 = wx.Button( self.P2, wx.ID_ANY, _(u"Download"), wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		Hsz14.Add( self.btn9, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.gug1 = wx.Gauge( self.P2, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.gug1.SetValue( 0 )
		Hsz14.Add( self.gug1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz14, 0, wx.EXPAND, 5 )

		self.lin1 = wx.StaticLine( self.P2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		Vsz3.Add( self.lin1, 0, wx.EXPAND |wx.ALL, 5 )

		Hsz15 = wx.BoxSizer( wx.HORIZONTAL )

		self.chk1 = wx.CheckBox( self.P2, wx.ID_ANY, _(u"Check it ..."), wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz15.Add( self.chk1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz15, 0, wx.EXPAND, 5 )

		Hsz16 = wx.BoxSizer( wx.VERTICAL )

		self.lbl3 = wx.StaticText( self.P2, wx.ID_ANY, _(u"Message"), wx.DefaultPosition, wx.DefaultSize, 0 )
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

		self.filllist()


		self.SetSizer( Vsz1 )
		self.Layout()

		# Connect Events
		self.TLC1.Bind(wx.dataview.EVT_DATAVIEW_SELECTION_CHANGED, self.slctitm, id=wx.ID_ANY)
		self.CntSrv.Bind( wx.EVT_BUTTON, self.consrv )
		self.btn1.Bind( wx.EVT_BUTTON, self.addit )
		self.btn2.Bind( wx.EVT_BUTTON, self.editit )
		self.btn3.Bind( wx.EVT_BUTTON, self.delit )
		self.btn4.Bind( wx.EVT_BUTTON, self.prw )
		self.btn5.Bind( wx.EVT_BUTTON, self.upd )
		self.btn6.Bind( wx.EVT_BUTTON, self.aply )
		self.btn7.Bind( wx.EVT_BUTTON, self.gnrt )
		self.btn8.Bind( wx.EVT_BUTTON, self.mnuid )
		self.dir2.Bind( wx.EVT_DIRPICKER_CHANGED, self.thsdir )
		self.btn9.Bind( wx.EVT_BUTTON, self.dnlod )
		self.chk1.Bind( wx.EVT_CHECKBOX, self.chkdon )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def filllist(self):

		Aroot = self.TLC1.GetRootItem()
		self.root1 = self.TLC1.AppendItem(Aroot, "Free Programs you can Download")
		self.root2 = self.TLC1.AppendItem(Aroot, "Programs in your Account")
		#self.root3 = self.TLC1.AppendItem(Aroot, "Programs you Upload for sell")
		self.root4 = self.TLC1.AppendItem(Aroot, "Ziped Programs you downloaded")
		self.root5 = self.TLC1.AppendItem(Aroot, "Programs file in your HDD ")

		dirct = ['Free','Account','Downloads']
		#roots = [self.root1,self.root2,self.root3,self.root4]
		roots = [self.root1, self.root2, self.root4]
		i=0
		for d in dirct:
			mylist = os.listdir(UTILITY_PATH+d+'\\')
			for fil in mylist:
				if fil != '__init__.py':
					myfil = fil.replace(UTILITY_PATH+d+'\\','')
					mychld = self.TLC1.AppendItem(roots[i],d)
					self.TLC1.SetItemText(mychld,0,myfil)
					self.TLC1.SetItemText(mychld,1,'>>>')
			i += 1
		dirdt2 = ['API','AUI','GUI','MLA','MLP','PRG']
		dcods = {'API':6122,'AUI':6155,'PRG':6111,'GUI':6177,'MLA':6133,'MLP':6144}
		for d in dirdt2:
			mylist = os.listdir(UTILITY_PATH+'Fount\\'+d+'\\')
			mychild = self.TLC1.AppendItem(self.root5, 'HardDisk')
			self.TLC1.SetItemText(mychild, 0, d)
			self.TLC1.SetItemText(mychild,1,str(dcods[d])[-3:])
			for file in mylist:
				if file != '__init__.py':
					#myfile = file #file.replace(UTILITY_PATH+'Fount\\'+d+'\\','')
					#mychild = self.TLC1.AppendItem(self.root5, 'HardDisk')
					child2 = self.TLC1.AppendItem(mychild, d)
					self.TLC1.SetItemText(child2,0,file)
					self.TLC1.SetItemText(child2,1,str(dcods[d]))


	def fillfilds(self, Data):
		self.Descr.SetValue(Data[0])
		self.fld1.SetValue(Data[1])
		self.dir2.SetPath(Data[2])
		self.Refresh()
		self.Layout()


	def slctitm(self, event):
		D = ['','','']
		self.fillfilds(D)
		itm = self.TLC1.GetSelection()
		txt = self.TLC1.GetItemText(itm, 0)
		cod = self.TLC1.GetItemText(itm, 1)
		par = self.TLC1.GetItemParent(itm)
		rot = self.TLC1.GetItemText(par, 0)
		#print(txt,cod,rot)
		if txt == 'API':
			Discrpt = "This group of program is very simple \n only for item that no need GUI frame or panel"
			Pathsrc = Src_api
		elif txt == 'AUI':
			Discrpt = "This group of program for Aui Pane file\n That you can use in application "
			Pathsrc = Src_aui
		elif txt == 'GUI':
			Discrpt = "This group of program only a designed Panel \n they used by other program in PRG source"
			Pathsrc = Src_gui
		elif txt == 'PRG':
			Discrpt = "This group of program run by menu item in app \n each menubar has a same subdirectory you create it"
			Pathsrc = Src_prg
		elif txt == 'MLA':
			Discrpt = "This group of program is for Machine Learning Algorithm\n you can use it in MLA part that use by MLP"
			Pathsrc = Src_mla
		elif txt == 'MLP':
			Discrpt = "Machine learning Panel has Design for Algorithm \n You can see help document for how to use it "
			Pathsrc = Src_mlp
		else:
			Discrpt = ""
			Pathsrc = ""


		D = [Discrpt,'',Pathsrc]
		self.fillfilds(D)
		if '.py' in txt:
			self.thsfile = UTILITY_PATH+'Fount\\'+rot+SLASH+txt
		else:
			self.thsfile = ''
		#print(self.thsfile)



	def consrv( self, event ):
		import socket
		host = socket.gethostbyname(socket.gethostname())
		print(host)
		event.Skip()


	def addit( self, event ):
		event.Skip()

	def editit( self, event ):
		itm = self.TLC1.GetSelection()
		par = self.TLC1.GetItemParent(itm)
		rot = self.TLC1.GetItemText(par, 0)
		if self.thsfile != '' and rot == "Programs file in your HDD ":
			self.Frm = wx.Frame(self, style=wx.CAPTION | wx.CLOSE_BOX | wx.FRAME_FLOAT_ON_PARENT | wx.TAB_TRAVERSAL)
			# self.Pnl = PyPanel(self.Frm, self.thsfile)
			self.Pnl = OS.SrcPanel(self.Frm, self.thsfile)
			self.Frm.SetMenuBar(OS.MyMenuBar1(u'Pro'))
			self.Frm.SetSize((700, 560))
			self.Frm.SetLabel(self.thsfile)
			self.Frm.Show()
		event.Skip()

	def delit( self, event ):
		if self.thsfile != '':
			answr = wx.MessageBox("Are you sure to Delete %s from your Hard Drive?"%self.thsfile,'Warrning', wx.YES_NO)
			if answr == 2:
				if os.path.isfile(self.thsfile):
					try:
						os.remove(self.thsfile)
						wx.MessageBox(_("File Successfully Remove from HardDisk"))
					except os.error:
						print(os.error)
				else:
					wx.MessageBox(_("File Open or dose not exist please close it or check Harddisk"))
		self.TLC1.DeleteAllItems()
		self.filllist()
		self.Refresh()
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



