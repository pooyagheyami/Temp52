#In the name of GOD
#open source file of algorithm or panle algorithm
# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.stc as stc

from Config.Init import *

import keyword

if wx.Platform == '__WXMSW__':
    faces = {'times': 'Times New Roman',
             'mono': 'Courier New',
             'helv': 'Arial',
             'other': 'Comic Sans MS',
             'size': 10,
             'size2': 8,
             }
elif wx.Platform == '__WXMAC__':
    faces = {'times': 'Times New Roman',
             'mono': 'Monaco',
             'helv': 'Arial',
             'other': 'Comic Sans MS',
             'size': 12,
             'size2': 10,
             }
else:
    faces = {'times': 'Times',
             'mono': 'Courier',
             'helv': 'Helvetica',
             'other': 'new century schoolbook',
             'size': 12,
             'size2': 10,
             }


class PythonSTC(stc.StyledTextCtrl):
    fold_symbols = 2

    def __init__(self, parent, PyFile):
        stc.StyledTextCtrl.__init__(self, parent)

        self.CmdKeyAssign(ord('B'), stc.STC_SCMOD_CTRL, stc.STC_CMD_ZOOMIN)
        self.CmdKeyAssign(ord('N'), stc.STC_SCMOD_CTRL, stc.STC_CMD_ZOOMOUT)

        self.SetLexer(stc.STC_LEX_PYTHON)
        self.SetKeyWords(0, " ".join(keyword.kwlist))

        self.SetProperty("fold", "1")
        self.SetProperty("tab.timmy.whinge.level", "1")
        self.SetMargins(0, 0)

        self.SetViewWhiteSpace(False)
        # self.SetBufferedDraw(False)
        # self.SetViewEOL(True)
        # self.SetEOLMode(stc.STC_EOL_CRLF)
        # self.SetUseAntiAliasing(True)

        # Global default styles for all languages
        self.StyleSetSpec(stc.STC_STYLE_DEFAULT, "face:%(helv)s,size:%(size)d" % faces)
        self.StyleClearAll()  # Reset all to be like the default

        # Global default styles for all languages
        self.StyleSetSpec(stc.STC_STYLE_DEFAULT, "face:%(helv)s,size:%(size)d" % faces)
        self.StyleSetSpec(stc.STC_STYLE_LINENUMBER, "back:#C0C0C0,face:%(helv)s,size:%(size2)d" % faces)
        self.StyleSetSpec(stc.STC_STYLE_CONTROLCHAR, "face:%(other)s" % faces)
        self.StyleSetSpec(stc.STC_STYLE_BRACELIGHT, "fore:#FFFFFF,back:#0000FF,bold")
        self.StyleSetSpec(stc.STC_STYLE_BRACEBAD, "fore:#000000,back:#FF0000,bold")

        # Python styles
        # Default
        self.StyleSetSpec(stc.STC_P_DEFAULT, "fore:#000000,face:%(helv)s,size:%(size)d" % faces)
        # Comments
        self.StyleSetSpec(stc.STC_P_COMMENTLINE, "fore:#007F00,face:%(other)s,size:%(size)d" % faces)
        # Number
        self.StyleSetSpec(stc.STC_P_NUMBER, "fore:#007F7F,size:%(size)d" % faces)
        # String
        self.StyleSetSpec(stc.STC_P_STRING, "fore:#7F007F,face:%(helv)s,size:%(size)d" % faces)
        # Single quoted string
        self.StyleSetSpec(stc.STC_P_CHARACTER, "fore:#7F007F,face:%(helv)s,size:%(size)d" % faces)
        # Keyword
        self.StyleSetSpec(stc.STC_P_WORD, "fore:#00007F,bold,size:%(size)d" % faces)
        # Triple quotes
        self.StyleSetSpec(stc.STC_P_TRIPLE, "fore:#7F0000,size:%(size)d" % faces)
        # Triple double quotes
        self.StyleSetSpec(stc.STC_P_TRIPLEDOUBLE, "fore:#7F0000,size:%(size)d" % faces)
        # Class name definition
        self.StyleSetSpec(stc.STC_P_CLASSNAME, "fore:#0000FF,bold,underline,size:%(size)d" % faces)
        # Function or method name definition
        self.StyleSetSpec(stc.STC_P_DEFNAME, "fore:#007F7F,bold,size:%(size)d" % faces)
        # Operators
        self.StyleSetSpec(stc.STC_P_OPERATOR, "bold,size:%(size)d" % faces)
        # Identifiers
        self.StyleSetSpec(stc.STC_P_IDENTIFIER, "fore:#000000,face:%(helv)s,size:%(size)d" % faces)
        # Comment-blocks
        self.StyleSetSpec(stc.STC_P_COMMENTBLOCK, "fore:#7F7F7F,size:%(size)d" % faces)
        # End of line where string is not closed
        self.StyleSetSpec(stc.STC_P_STRINGEOL, "fore:#000000,face:%(mono)s,back:#E0C0E0,eol,size:%(size)d" % faces)

        self.SetCaretForeground("BLUE")

        # register some images for use in the AutoComplete box.
        # self.RegisterImage(1, images.Smiles.GetBitmap())
        # self.RegisterImage(2,
        #    wx.ArtProvider.GetBitmap(wx.ART_NEW, size=(16,16)))
        # self.RegisterImage(3,
        #    wx.ArtProvider.GetBitmap(wx.ART_COPY, size=(16,16)))

        with open(PyFile) as fobj:
            text = fobj.read()

        self.SetText(text)

    def slctal(self):
        self.SelectAll()

###########################################################################
## Class MyPanel2
###########################################################################

class SrcPanel ( wx.Panel ):

	def __init__( self, parent, pyFile, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 680,455 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		Vsz1 = wx.BoxSizer( wx.VERTICAL )

		Hsz1 = wx.BoxSizer( wx.HORIZONTAL )

		self.pyFile = pyFile
		self.ischanged = False

		self.SrcAlg = PythonSTC(self, pyFile)

		#self.SrcAlg.

		Hsz1.Add( self.SrcAlg, 1, wx.EXPAND |wx.ALL, 5 )

		Vsz1.Add( Hsz1, 1, wx.EXPAND, 5 )

		self.SetSizer( Vsz1 )
		self.Layout()


		self.Bind(wx.stc.EVT_STC_CHARADDED, self.editfile, id=wx.ID_ANY)
		self.SrcAlg.Bind(wx.EVT_CHAR_HOOK, self.kyhok)



	def __del__( self ):
		pass


	def editfile(self, event):
		if self.SrcAlg.GetUndoCollection() and not self.ischanged:
			ilbl = self.GetParent().GetLabel()
			self.GetParent().SetLabel(u'*' + ilbl )
			self.ischanged = True

	def kyhok(self, event):
		#print(u'hook',self.ischanged)
		self.editfile(event)
		event.Skip()

	def newstc(self, pyFile):
		self.SrcAlg.ClearAll()
		with open(pyFile) as fobj:
			text = fobj.read()
		self.SrcAlg.SetText(text)
		#self.SrcAlg.SetTextRaw(pyFile)

	def opnstc(self, pyFile):
		self.SrcAlg.ClearAll()
		with open(pyFile) as fobj:
			text = fobj.read()
		self.SrcAlg.SetText(text)






###########################################################################
## Class MyMenuBar1
###########################################################################

class MyMenuBar1 ( wx.MenuBar ):

	def __init__( self , extmnu=u''):
		wx.MenuBar.__init__ ( self, style = 0 )

		mymnu = {u"File": [(61,u'New',u'',self.newsrc),(62,u'Open...',u'',self.opnsrc),(63,u'',u'',u''),(64,u'Save',u'',self.savsrc),
		                   (65,u'Save As...',u'',self.savasit),(66,u'',u'',u''),(67,u'Close',u'',self.closit)],
		         u"Edit": [(71,u'Cut',u'',self.cutit),(72,u'Copy',u'',self.copyit),(73,u'Paste',u'',self.pastit),
		                   (74,u'',u'',u''),(75,u'Select All',u'',self.slctal)] }
		if extmnu == u'Pro':
			mymnu[u'Add'] = [(81,u'line-close',u'add close code to button function',self.clos_lin),
			                 (82,u'line-getdata',u'get data from fields textctrl ',self.get_lin),
			                 (83,u'line-putdata',u'put data to fields textctrl',self.put_lin),
			                 (84,u'line-fillnull',u'fill empty record in all data',self.null_lin)]

		elif extmnu == u'ML':
			mymnu[u'Add'] = [(91,u'Import Numpy',u'',self.impnum),(92,u'Import matplotlib',u'',self.impmat),
			                 (93,u'Import Axes 3D',u'',self.impa3d)]
			mymnu[u'ML Dev'] = [(50,u'Add this file',u'',self.toML)]
		elif extmnu == u'AL':
			mymnu[u'Add'] = [(91,u'Import Numpy',u'',self.impnum),(92,u'Import matplotlib',u'',self.impmat),
			                 (93,u'Import Axes 3D',u'',self.impa3d),(94,u'',u'',u''),
			                 (95,u'ML Utility(Y select)',u'',self.impmlu),(96,u'ML Utility(Show Matrix)',u'',self.impmlu)]
			mymnu[u'ML Dev'] = [(50, u'Add this file', u'', self.toML)]

		self.Itms = []
		m = 0
		self.Mnus = []
		s = 0

		for mn in mymnu:
			self.Mnus.append( wx.Menu() )
			for it in mymnu[mn]:
				if it[1] != u'':
					self.Itms.append( wx.MenuItem(self.Mnus[s], it[0], it[1], it[2], wx.ITEM_NORMAL) )
					self.Mnus[s].Append(self.Itms[m])
					self.Bind(wx.EVT_MENU, it[3], id=it[0])
					m += 1
				else:
					self.Mnus[s].AppendSeparator()
			self.Append(self.Mnus[s], mn)
			s += 1

		if extmnu == u"Pro":
			self.DfDir = GUI_PATH
		elif extmnu == u'ML':
			self.DfDir = AI_PATH+'ML\\'
		elif extmnu == u'AL':
			self.DfDir = GUI_PATH+"MLPane\\"
		else:
			self.DfDir = MAP

		self.Bind(wx.EVT_MENU_OPEN, self.Doinit, id=self.GetId())


	def __del__(self):
		pass

	# Virtual event handlers, overide them in your derived class
	def Doinit(self, event):
		frm = self.GetFrame()
		#print(frm)
		self.pnl = frm.GetChildren()[0]
		self.pyfile = self.pnl.pyFile
		self.SrcTxt = self.pnl.SrcAlg

	def newsrc(self, event):
		#print(self.pyfile)
		#print(self.pnl.ischanged)
		if self.pnl.ischanged:
			iyesno = wx.MessageBox(u'Do you like to save change',style=wx.YES_NO)
			#print(iyesno)
			if iyesno == 8:
				return
			else:
				#print(self.pyfile,self.pnl.pyFile)
				self.savsrc(event)
				self.pnl.ischanged = False
				self.pnl.pyFile = u'untitle'
				self.newsrc(event)
		else:
			if u'untitle' in self.pyfile.lower():
				wx.MessageBox(u'Please work in this file or close it then use new file')
			else:
				#print(u'untitle file')
				if self.DfDir == GUI_PATH+"MLPane\\":
					self.pnl.newstc(GUI_PATH + u'MLPane\\Untitle.py')
				else:
					self.pnl.newstc(GUI_PATH+u'Temp\\untitle.py')
				self.GetParent().SetLabel(u'untitle')
		event.Skip()

	def opnsrc(self, event):
		with wx.FileDialog(self, "Open a file", defaultDir=self.DfDir,wildcard="Python files (*.py)|*.py",
		                   style=wx.FD_OPEN) as fileDialog:
			if fileDialog.ShowModal() == wx.ID_CANCEL:
				return
			pathname = fileDialog.GetPath()
			#self.pyfile = pathname
			self.pnl.pyFile = pathname
			self.pnl.opnstc(pathname)
			self.GetParent().SetLabel(pathname)
		event.Skip()

	def savsrc(self, event):
		if u'untitle.py' in self.pyfile:
			with wx.FileDialog(self, "Save new file", defaultDir=self.DfDir,wildcard="Python files (*.py)|*.py",
			                   style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:
				if fileDialog.ShowModal() == wx.ID_CANCEL:
					return  # the user changed their mind
				# save the current contents in the file
				pathname = fileDialog.GetPath()
				# print(pathname)
				self.SrcTxt.SaveFile(pathname)
		else:
			self.SrcTxt.SaveFile(self.pyfile)
			wx.MessageBox(u'You save to file change successful.')
		event.Skip()

	def savasit(self, event):
		with wx.FileDialog(self, "Save As new file", defaultDir=self.DfDir, wildcard="Python files (*.py)|*.py",
		                   style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:
			if fileDialog.ShowModal() == wx.ID_CANCEL:
				return  # the user changed their mind
			# save the current contents in the file
			pathname = fileDialog.GetPath()
			# print(pathname)
			self.SrcTxt.SaveFile(pathname)
		event.Skip()

	def closit(self, event):
		q = self.GetParent()
		q.Close()

	def cutit(self, event):
		self.SrcTxt.Cut()
		event.Skip()

	def copyit(self, event):
		self.SrcTxt.Copy()
		event.Skip()

	def pastit(self, event):
		self.SrcTxt.Paste()
		event.Skip()

	def slctal(self, event):
		self.SrcTxt.SelectAll()
		event.Skip()

	def clos_lin(self, event):
		self.py_view.AddText("\t\tq = self.GetParent()\n\t\tq.Close()\n")
		event.Skip()

	def get_lin(self, event):
		event.Skip()

	def put_lin(self, event):
		event.Skip()

	def null_lin(self, event):
		event.Skip()

	def impnum(self, event):
		pass

	def impmat(self, event):
		pass

	def impa3d(self, event):
		pass

	def impmlu(self, event):
		pass

	def toML(self, event):
		print(self.pnl.pyFile)
		ifil = self.pnl.pyFile.split('\\')[-1].replace(u'.py',u'')
		print(ifil)
		if self.pnl.pyFile == GUI_PATH+u'Temp\\untitle.py':
			wx.MessageBox(u'Please save your work then Do this perosse.')
			self.savasit(event)
		elif self.pnl.pyFile == GUI_PATH+u'MLPane\\Untitle.py':
			wx.MessageBox(u'Please save your work then Do this perosse.')
			self.savasit(event)
		else:
			print(self.DfDir)
			MLpnl = self.GetGrandParent()
			if self.DfDir == GUI_PATH+u'MLPane\\':
				mylstml = MLpnl.getMData.AllML(u'join MLPane on MLinfo.MLPid = MLPane.MLPid')
				print(mylstml)
				tclslct = MLpnl.TLC1.GetSelection()
				if MLpnl.getMData.MLPansFils(u" where MLPane.MLPfile = '%s' " %ifil ) != []:
					wx.MessageBox(u'File is exist please change it')
				else:
					lebls = [u'Par. Pane Name', u'Par. Pane code', u'Par. Pane file']
					data = [ifil]
					dlg = wx.Dialog(self.GetFrame(), -1)
					pnl = MyPanel4(dlg, lebls, data)
					dlg.SetSize((480, 190))
					dlg.SetLabel(u'Add ML to List')
					dlg.ShowModal()
					if pnl.acpt:
						algnm = pnl.fld1.GetValue()
						algcd = pnl.fld2.GetValue()
						algid = pnl.fld4.GetValue()
					dlg.Destroy()
					print(algid, algnm, algcd)
					print(MLpnl.codings)
					if algnm != u'' or algcd != u'' or algid != u'':
						if int(algid) > MLpnl.codings[0] and int(algid) < MLpnl.codings[1]:
							print(u'to database')
							#MLpnl.setMDate.Table = u'MLinfo'
							#MLpnl.setMDate.Additem(u' MLPid, MLname, MLcod', [int(algid), algnm, algcd])
							MLpnl.setMDate.Table = u'MLPane'
							MLpnl.setMDate.Additem(u' MLPid, MLPfile', [algid, ifil])
							wx.MessageBox(u'Your source Add to list Successfully.')
						else:
							wx.MessageBox(u'Please attend to coding range!')
					else:
						wx.MessageBox(u'Some fields is empty or wrong ! try again!')


			if self.DfDir == AI_PATH+u'ML\\':
				mylstml = MLpnl.getMData.AllML(u'join MLAlgo on MLAlgo.MLcod = MLinfo.MLcod')
				print(mylstml)
				tclslct = MLpnl.TLC1.GetSelection()
				#algnm = MLpnl.TLC1.GetItemText(tclslct, 0)
				#algcd = MLpnl.TLC1.GetItemText(tclslct, 1)
				if MLpnl.getMData.MLAlgoFils(u" where MLAlgo.MLAsrc = '%s' " %ifil ) != []:
					wx.MessageBox(u'File is exist please change it')
				else:
					lebls = [u'Algorithm Name', u'Algorithm Code', u'Algorithm file']
					data = [ifil]
					dlg = wx.Dialog(self.GetFrame(), -1)
					pnl = MyPanel4(dlg, lebls, data)
					dlg.SetSize((480, 190))
					dlg.SetLabel(u'Add ML to List')
					dlg.ShowModal()
					if pnl.acpt:
						algnm = pnl.fld1.GetValue()
						algcd = pnl.fld2.GetValue()
						algid = pnl.fld4.GetValue()
					dlg.Destroy()
					#print(algid,algnm,algcd)
					#print(MLpnl.codings)
					if algnm != u'' or algcd != u'' or algid != u'':
						if int(algid) > MLpnl.codings[0] and int(algid) < MLpnl.codings[1]:
							print(u'to database')
							MLpnl.setMDate.Table = u'MLinfo'
							MLpnl.setMDate.Additem(u' MLPid, MLname, MLcod',[int(algid), algnm, algcd])
							MLpnl.setMDate.Table = u'MLAlgo'
							MLpnl.setMDate.Additem(u' MLcod, MLAsrc',[algcd, ifil])
							wx.MessageBox(u'Your source Add to list Successfully.')
						else:
							wx.MessageBox(u'Please attend to coding range!')
					else:
						wx.MessageBox(u'Some fields is empty or wrong ! try again!')



			#print(MLpnl.getMData.AllML(u' join MLPane on MLinfo.MLPid = MLPane.MLPid join MLAlgo on MLAlgo.MLcod = MLinfo.MLcod'))
			#print(MLpnl.TLC1.GetSelection())
			#tclslct = MLpnl.TLC1.GetSelection()
			#print(MLpnl.TLC1.GetItemText(tclslct,0))
			#print(MLpnl.TLC1.GetItemText(tclslct, 1))
			print(MLpnl.ChsBok.GetChoiceCtrl())

			#lebls = [u'Par. Pane Name',u'Par. Pane code',u'Par. Pane file']
			#lebls = [u'Algorithm Name',u'Algorithm Code',u'Algorithm file']
			#data = []
			#dlg = wx.Dialog(self.GetFrame(), -1)
			#pnl = MyPanel4(dlg,lebls,data)
			#dlg.SetSize((480,190))
			#dlg.SetLabel(u'Add ML to List')
			#dlg.ShowModal()
			#dlg.Destroy()


	def tst(self, event):
		event.Skip()

###########################################################################
## Class MyPanel4
###########################################################################

class MyPanel4 ( wx.Panel ):

	def __init__( self, parent,lebls,data, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 481,188 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		Vsz1 = wx.BoxSizer( wx.VERTICAL )

		Hsz1 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl1 = wx.StaticText( self, wx.ID_ANY, lebls[0], wx.DefaultPosition, wx.Size( 110,-1 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.lbl1.Wrap( -1 )

		Hsz1.Add( self.lbl1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz1.Add( self.fld1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.lbl4 = wx.StaticText(self, wx.ID_ANY, u"Alg. id", wx.DefaultPosition, wx.DefaultSize, 0)
		self.lbl4.Wrap(-1)
		Hsz1.Add(self.lbl4, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		self.fld4 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(70, -1), 0)
		Hsz1.Add(self.fld4, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		Vsz1.Add( Hsz1, 1, wx.EXPAND, 5 )

		Hsz2 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl2 = wx.StaticText( self, wx.ID_ANY, lebls[1], wx.DefaultPosition, wx.Size( 110,-1 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.lbl2.Wrap( -1 )

		Hsz2.Add( self.lbl2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.fld2.SetToolTip(u"Example: GD  EN  GLM  MLE")
		Hsz2.Add( self.fld2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.lbl3 = wx.StaticText( self, wx.ID_ANY, lebls[2], wx.DefaultPosition, wx.Size( 95,-1 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.lbl3.Wrap( -1 )

		Hsz2.Add( self.lbl3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld3 = wx.TextCtrl( self, wx.ID_ANY, str(data[0]), wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz2.Add( self.fld3, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz1.Add( Hsz2, 1, wx.EXPAND, 5 )

		# Hsz3 = wx.BoxSizer( wx.HORIZONTAL )
		#
		# self.lbl4 = wx.StaticText( self, wx.ID_ANY, u"ML Algorithm Code", wx.DefaultPosition, wx.Size( 110,-1 ), wx.ALIGN_CENTER_HORIZONTAL )
		# self.lbl4.Wrap( -1 )
		#
		# Hsz3.Add( self.lbl4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		#
		# self.fld4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		# Hsz3.Add( self.fld4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		#
		# self.lbl5 = wx.StaticText( self, wx.ID_ANY, u"ML Algorithm File", wx.DefaultPosition, wx.Size( 95,-1 ), wx.ALIGN_CENTER_HORIZONTAL )
		# self.lbl5.Wrap( -1 )
		#
		# Hsz3.Add( self.lbl5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		#
		# self.fld5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		# Hsz3.Add( self.fld5, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		#
		#
		# Vsz1.Add( Hsz3, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		Hsz4 = wx.BoxSizer( wx.HORIZONTAL )

		self.btn1 = wx.Button( self, wx.ID_ANY, u"Cancle", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz4.Add( self.btn1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.btn2 = wx.Button( self, wx.ID_ANY, u"Apply", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz4.Add( self.btn2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz1.Add( Hsz4, 0, wx.ALIGN_RIGHT, 5 )


		self.SetSizer( Vsz1 )
		self.Layout()

		# Connect Events
		self.btn1.Bind( wx.EVT_BUTTON, self.cncl )
		self.btn2.Bind( wx.EVT_BUTTON, self.aply )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def cncl( self, event ):
		self.acpt = False
		q = self.GetParent()
		q.Close()

	def aply( self, event ):
		self.acpt = True
		q = self.GetParent()
		q.Close()


