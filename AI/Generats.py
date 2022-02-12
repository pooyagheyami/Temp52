#In the name of GOD
# -*- coding: utf-8 -*-

from .Analiz import *

class Genrate(object):
    def __init__(self,frmname):
        self.imp_pnl = {}
        self.frm_mak = frmname

        self.lin_wrt = ''

    def createFrm(self, filnam):
        self.filnam = filnam
        self.impfil = self.filnam.split('\\')[-1].replace('.py', '')
        #print(self.impfil)
        #pnlfil = Anlzfil(filnam)
        #self.imp_pnl = pnlfil.parsefil()
        #self.GUIpars = pnlfil.getGUIfil()
        #pnlfil.showParse()

        self.gnr_lins()
        with open(self.frm_mak, 'w') as fl:
            fl.writelines(self.lin_wrt)


    def gnr_lins(self):
        line1 = u"#In the name of GOD\n"
        line2 = u"# -*- coding: utf-8 -*-\n"
        line3 = u"#!usr/bin/env python\n\n"
        self.lin_wrt = line1 + line2 + line3
        self.lin_wrt += self.gnr_imps()
        self.lin_wrt += self.gnr_frm()
        self.lin_wrt += self.gnr_siz()
        self.lin_wrt += self.gnr_min()
        self.lin_wrt += self.gnr_if()


    def gnr_imps(self):
        imprtxt = u"import wx\n"
        imprtxt += u"from  Config.Init import *\n"
        imprtxt += u"import Src.api."+self.impfil+" as pnl\n\n"
        return imprtxt

    def gnr_frm(self):
        frmtxt = u"class telframe(wx.Frame):\n"
        frmtxt += u"\tdef __init__(self,parent):\n"
        frmtxt += u"\t\twx.Frame.__init__(self,parent,style=wx.FRAME_FLOAT_ON_PARENT|wx.DEFAULT_FRAME_STYLE)\n"
        frmtxt += u"\t\tself.parent= parent\n\n"

        frmtxt += u"\t\tself.Pnl = pnl.MyPanel1(self)\n\n"

        frmtxt += u"\tdef closeit(self):\n"
        frmtxt += u"\t\tself.Close(True)\n\n"

        return frmtxt

    def gnr_siz(self):
        sizdef = u"def size():\n"
        sizdef += u"\treturn (-1,-1)\n\n"
        return sizdef
    def gnr_min(self):
        mindef = u"def main(panel=None ):\n"
        mindef += u"\tparent =  panel.GetParent()\n\n"
        mindef += u"\tframe = telframe(parent )\n"
        mindef += u"\tframe.SetTitle(u'form')\n"
        mindef += u"\tframe.SetSize(size())\n"
        mindef += u"\tframe.Show()\n\n"
        return mindef

    def gnr_if(self):
        iffil = u"if __name__ == '__main__':\n"
        iffil += u"\tmain()\n"
        return iffil


class Genrate2(object):
    def __init__(self,pronam):
        self.pronam = pronam
        self.addlin = ''

    def appendFile(self):
        with open(self.pronam,'a+', encoding='utf-8') as Prg:
            Prg.writelines(self.addlin)

    def gnratLine(self, Frame=True, Size=True, Main=True, Ifit=True, Framname= 'telframe' , Title= 'Form'):
        if Frame:
            self.addlin += self.grplin1creat()

        if Size:
            self.addlin += self.grplin2creat()

        if Main:
            self.addlin += self.grplin3creat(Framname,Title)

        if Ifit:
            self.addlin += self.grplin4creat()

    def grplin1creat(self):
        frmtxt = u"class telframe(wx.Frame):\n"
        frmtxt += u"\tdef __init__(self,parent):\n"
        frmtxt += u"\t\twx.Frame.__init__(self,parent,style=wx.FRAME_FLOAT_ON_PARENT|wx.DEFAULT_FRAME_STYLE)\n"
        frmtxt += u"\t\tself.parent= parent\n\n"

        frmtxt += u"\t\tself.Pnl = pnl.MyPanel1(self)\n\n"

        frmtxt += u"\tdef closeit(self):\n"
        frmtxt += u"\t\tself.Close(True)\n\n"

        return frmtxt

    def grplin2creat(self):
        sizdef = u"def size():\n"
        sizdef += u"\treturn (-1,-1)\n\n"
        return sizdef

    def grplin3creat(self, Fram_name, Titel):
        mindef = u"def main(panel=None ):\n"
        mindef += u"\tparent =  panel.GetParent()\n\n"
        mindef += u"\tframe = %s(parent )\n"%Fram_name
        mindef += u"\tframe.SetTitle(u'%s')\n"%Titel
        mindef += u"\tframe.SetSize(size())\n"
        mindef += u"\tframe.Show()\n\n"
        return mindef

    def grplin4creat(self):
        iffil = u"if __name__ == '__main__':\n"
        iffil += u"\tmain()\n"
        return iffil


class GenrDemo(Genrate):
    def __init__(self,mypath):
        Genrate.__init__(self,mypath+'\\Demo.py')
        self.createFrm('SamPnl.py')



