#In the name of GOD
# -*- coding: utf-8 -*-


import wx
import wx.stc as stc

from Config import *

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
## Class MyPanel1
###########################################################################

class PyPanel(wx.Panel):

    def __init__(self, parent, pyFile, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(680, 465),
                 style=wx.TAB_TRAVERSAL, name=wx.EmptyString):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)

        self.pyFile = pyFile

        Vz1 = wx.BoxSizer(wx.VERTICAL)

        Hz1 = wx.BoxSizer(wx.HORIZONTAL)

        self.py_view = PythonSTC(self, pyFile)

        Hz1.Add(self.py_view, 1, wx.EXPAND | wx.ALL, 5)

        Vz2 = wx.BoxSizer(wx.VERTICAL)

        self.btn3 = wx.Button(self, wx.ID_ANY, u"SelectAll", wx.DefaultPosition, wx.DefaultSize, 0)
        Vz2.Add(self.btn3, 0, wx.ALL, 5)

        self.btn4 = wx.Button(self, wx.ID_ANY, u"Copy", wx.DefaultPosition, wx.DefaultSize, 0)
        Vz2.Add(self.btn4, 0, wx.ALL, 5)

        self.btn5 = wx.Button(self, wx.ID_ANY, u"Paste", wx.DefaultPosition, wx.DefaultSize, 0)
        Vz2.Add(self.btn5, 0, wx.ALL, 5)

        Vz2.Add((0, 0), 1, wx.EXPAND, 5)
        self.btn9 = wx.Button(self, wx.ID_ANY, u"Analyze", wx.DefaultPosition, wx.DefaultSize, 0)
        Vz2.Add(self.btn9, 0, wx.ALL, 5)

        Vz2.Add((0, 0), 1, wx.EXPAND, 5)

        self.btn6 = wx.Button(self, wx.ID_ANY, u"line-close", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btn6.SetToolTip(u"add close code to button function")
        Vz2.Add(self.btn6, 0, wx.ALL, 5)

        self.btn7 = wx.Button(self, wx.ID_ANY, u"line-getdata", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btn7.SetToolTip(u"get data from fields textctrl ")
        Vz2.Add(self.btn7, 0, wx.ALL, 5)

        self.btn8 = wx.Button(self, wx.ID_ANY, u"linr-putdata", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btn8.SetToolTip(u"put data to fields textctrl")
        Vz2.Add(self.btn8, 0, wx.ALL, 5)

        Vz2.Add((0, 0), 1, wx.EXPAND, 5)

        self.btn1 = wx.Button(self, wx.ID_ANY, u"save", wx.DefaultPosition, wx.DefaultSize, 0)
        Vz2.Add(self.btn1, 0, wx.ALL, 5)

        self.btn2 = wx.Button(self, wx.ID_ANY, u"close", wx.DefaultPosition, wx.DefaultSize, 0)
        Vz2.Add(self.btn2, 0, wx.ALL, 5)

        Hz1.Add(Vz2, 0, wx.EXPAND, 5)

        Vz1.Add(Hz1, 1, wx.EXPAND, 5)

        self.SetSizer(Vz1)
        self.Layout()

        # Connect Events
        self.btn3.Bind(wx.EVT_BUTTON, self.slctal)
        self.btn4.Bind(wx.EVT_BUTTON, self.cpyslct)
        self.btn5.Bind(wx.EVT_BUTTON, self.pstslct)
        self.btn1.Bind(wx.EVT_BUTTON, self.svefil)
        self.btn2.Bind(wx.EVT_BUTTON, self.clos)

        self.btn6.Bind(wx.EVT_BUTTON, self.line_clos)
        self.btn7.Bind(wx.EVT_BUTTON, self.line_gets)
        self.btn8.Bind(wx.EVT_BUTTON, self.line_puts)

        self.btn9.Bind(wx.EVT_BUTTON, self.analyzfil)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def slctal(self, event):
        self.py_view.SelectAll()
        event.Skip()

    def cpyslct(self, event):
        self.py_view.Copy()
        event.Skip()

    def pstslct(self, event):
        self.py_view.Paste()
        event.Skip()

    def svefil(self, event):
        if u'untitle.py' in self.pyFile:

            with wx.FileDialog(self, "Save new file", wildcard="Python files (*.py)|*.py",
                               style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:

                if fileDialog.ShowModal() == wx.ID_CANCEL:
                    return  # the user changed their mind

                # save the current contents in the file
                pathname = fileDialog.GetPath()
                print(pathname)
                self.py_view.SaveFile(pathname)
        else:
            self.py_view.SaveFile(self.pyFile)
            wx.MessageBox(u'You save to file change successful.')
        event.Skip()

    def clos(self, event):
        q = self.GetParent()
        q.Close()

    def line_clos(self, event):
        #print(self.getpos())
        self.py_view.AddText("\t\tq = self.GetParent()\n\t\tq.Close()\n")


    def line_gets(self, event):

        if self.ctltxt == [] and self.chosls == [] and self.chkbox == [] and self.rdobox == []:
            wx.MessageBox(u'No any part of Panel for get data! Please use one of this object: \
                          wx.TextCtrl wx.Choice wx.CheckBox wx.RadioBox')
        else:
            i = 1
            for obj in self.ctltxt:
                self.py_view.AddText("\t\tD%s = "%str(i)+obj+".GetValue()\n")
                i += 1
            for obj in self.chosls:
                self.py_view.AddText("\t\tD%s = "%str(i)+obj+".GetSelection()\n")
                i += 1
            for obj in self.chkbox:
                self.py_view.AddText("\t\tD%s = "%str(i)+obj+".GetValue()\n")
                i += 1
            for obj in self.rdobox:
                self.py_view.AddText("\t\tD%s = "%str(i)+obj+".GetSelection()\n")
                i += 1

        self.py_view.AddText("\t\t#### you can return data in your own format here ###\n")

    def line_puts(self, event):
        pass

    def analyzfil(self, event):
        self.ctltxt = []
        self.chkbox = []
        self.rdobox = []
        self.chosls = []
        lins = self.py_view.GetLineCount()
        for l in range(lins):
            if u'wx.TextCtrl' in self.py_view.GetLine(l):
                self.ctltxt.append(self.py_view.GetLineText(l).split('=')[0].lstrip('\t').rstrip(' '))
            if u'wx.Choice' in self.py_view.GetLine(l):
                self.chosls.append(self.py_view.GetLineText(l).split('=')[0].lstrip('\t').rstrip(' '))
            if u'wx.CheckBox' in self.py_view.GetLine(l):
                self.chkbox.append(self.py_view.GetLineText(l).split('=')[0].lstrip('\t').rstrip(' '))
            if u'wx.RadioBox' in self.py_view.GetLine(l):
                self.rdobox.append(self.py_view.GetLineText(l).split('=')[0].lstrip('\t').rstrip(' '))
        wx.MessageBox(u"We Successful Analyzing file for field and data")

    def getpos(self):
        return self.py_view.GetPosition()

