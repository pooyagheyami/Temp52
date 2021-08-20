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
            if 'GUI' in im:
                return im[im.find('GUI'):].split(' ')[0]

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


def GetPamelImport(filewopy):
    f = filewopy+'.py'