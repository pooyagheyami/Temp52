#In the name of God
# -*- coding: utf-8 -*-
#!usr/bin/env python

from wx.py import frame,filling,pseudo
import re

class Anlzfil(object):
    def __init__(self, pyFile):
        self.pyFile = pyFile
        self.imprts = []
        self.objcts = {}
        self.pmodls = {}

    def parsefil(self):
        with open(self.pyFile, 'r', encoding=u'utf-8') as fpy:
            linsred = fpy.readlines()
            d = 1
            for ln in linsred:
                if 'import' in ln:
                    #print(ln)
                    self.imprts.append(ln)
                if 'class' in ln:
                    #print(ln)
                    i = pseudo.PseudoFile.readline(self.pyFile)
                    #print(dir(i))
                    self.objcts['class'] = ln
                if 'def' in ln:

                    self.pmodls['def'+str(d)] = ln
                    d = d + 1

    def showParse(self):
        print(self.imprts,self.objcts,self.pmodls)

    def getGUIfil(self):
        for im in self.imprts:
            if 'Src' in im:
                return im[im.find('GUI'):].split(' ')[0]

    def checkSyntx(self):
        with open(self.pyFile, 'r') as f:
            whris = re.search(r"if\s__name__\s==\s\'__main__\':", f.read())
            whmis = re.search(r'(.+main.+)||[main]',f.read())
            #print(whris.group().split(' '))
            if whris:
                mainis = re.search(r'def\smain',f.read())
                mainis2= re.search(r'...\smain\s\(panel.+\)\:',f.read())
                #print(u'main found:',mainis,mainis2)
            #print(whmis)
            return whris


    def ishasmain(self):
        with open(self.pyFile, 'r') as f:
            whris = re.search(r'def\smain', f.read())
            if whris:
                #print(whris.group().split(' '))
                return whris.group().split(' ')[1]

    def ishasifin(self):
        with open(self.pyFile, 'r') as f:
            #whris = re.search(r"if\s__name__", f.read())
            whris = re.search(r"if\s__name__\s==\s\'__main__\':", f.read())
            if whris:
                #print(whris.group().split(' '))
                return whris.group().split(' ')[1]

    def ishasframe(self):
        with open(self.pyFile, 'r') as f:
            whris = re.search(r'class\s.+\s+(wx\.Frame).+', f.read())
            if whris:
                #print(whris.group().split(' ')[1])
                return whris.group().split(' ')[1]

    def ishaspanel(self):
        with open(self.pyFile, 'r' ) as f:
            whris = re.search(r"class\s+.+\s+(wx\.Panel)", f.read())
            if whris:
                #print(whris.group().split(' ')[1])
                return whris.group().split(' ')[1]

    def ishasimport(self, txt=''):
        with open(self.pyFile, 'r') as f:
            whris = re.findall(r'import\s+%s.+\s+'%txt, f.read())
            if whris :
                #print(whris)
                return whris
    def ishasfromim(self, txt=''):
        with open(self.pyFile, 'r') as f:
            whris2 = re.findall(r'from\s+%s.+\s+import\s+.+'%txt, f.read())
            if whris2:
                #print(whris2)
                return whris2


def GetPanelImport(filewopy):
    f = filewopy+'.py'

def AnalizdbText(dbdatatxt):
    Table_feild_dict = {}
    Index_List = []
    wtxt1 = re.sub(r'[\(\n\)]','',dbdatatxt)
    #print(wtxt1)
    wtxt = re.sub(r'\s+',' ',wtxt1)
    #print(wtxt)
    ltxt = wtxt.split(' ')
    #print(ltxt)
    Table_name = ltxt[ltxt.index('TABLE') + 1]

    t = dbdatatxt
    fld = t[t.find('(')+1:t.find(')')]
    t1 = re.sub(r'\s+',' ',fld)
    #print(t1.replace('\n','').split(','))
    t2 = t1.replace('\n','').split(',')
    #print(t2)
    ifilds = []
    for fll in t2:
        #Table_feild_dict[Table_name]=(fll.split(' ')[0],fll.split(' ')[1])
        ifilds.append(fll)
    Table_feild_dict[Table_name] = ifilds
    return Table_feild_dict

def AnalizdbText2(dbtext):
    Table_list = {}
    Index_list = {}
    for txt in dbtext:
        if txt[0] == 'table':
            f = txt[4][txt[4].index('(')+1:txt[4].index(')',-1)]
            #print(re.sub(r'\s+', ' ', f))
            sbf = re.sub(r'\s+', ' ', f)
            fields = []
            #print(sbf.split(','))
            for sfld in sbf.split(','):
                #print(sfld.strip(' ')[:7])
                if sfld.strip(' ')[:7] == 'PRIMARY' or ')' in sfld.strip(' ').split(' ')[0]:
                    print(sfld)
                else:
                    fields.append(sfld)
            #fields = re.split(',',re.sub('\s+',' ',f))
            #print(fields)
            lstfld = []
            for fl in fields:
                ssfl = ''
                ssfl = fl.strip(' ').split(' ')
                #print(ssfl)
                if len(ssfl) > 0:
                    namfld = ssfl[0]
                    if len(ssfl) > 1:
                        typfld = ssfl[1]
                        if len(ssfl) > 2:
                            stgfld = ssfl[2:]
                        else:
                            stgfld = []
                    else:
                        typfld = "TEXT"
                #print(namfld,typfld,stgfld)
                lstfld.append((namfld,typfld,stgfld))
            Table_list[txt[1]] = lstfld

        if txt[0] == 'index':
            #Index_list[txt[1]]
            pass
    return Table_list,Index_list