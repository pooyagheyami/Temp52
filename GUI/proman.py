# In the name of God
#! /usr/bin/env python
# -*- coding: utf-8 -*-

import Database.MenuSet2 as MS
import importlib
import importlib.util
from Config.Init import *


class Mymenu(object):
    def __init__(self):
        self.MySql = MS.GetData(u'Menu2.db', u'')
        self.ToSql = MS.SetData(u'', u'',u'')

    def program(self, itemid):
        self.handler = self.MySql.MyProg(itemid=itemid)
        return self.handler[0][1]

    def toogram(self, itolid):
        self.handler = self.MySql.MyTogr(itolid)
        return self.handler[0][1]

    def menudir(self, itemid):
        self.directory = self.MySql.MnuDir2(itemid)
        if self.directory != [] :
            return self.directory[0][0]
        #else:
        #    return ''

    def submndir(self, itemsub):
        self.directory = self.MySql.SubDir(itemsub)
        return self.directory[0][0]

    def tooldir(self, itolid):
        self.directory = self.MySql.TolDir2(itolid)
        return self.directory[0][0]

    def Dohndlr(self):
        return self.MySql.DoHdnl()

    def Runhdlr(self, handlerid):
        return self.MySql.RunHdnl(handlerid)[0]

    #def Revitm(self):
    #    return self.MySql.RevItem()


def DoProgram2(itm,hndlr):
    M = Mymenu()
    #print(itm,hndlr)
    if itm > 1000 and itm < 9000:
        P = M.program(itm)
        d = M.menudir(itm)
        #print(P,d)
        if not d:
            d = M.submndir(itm)

    elif itm < 1000 and itm > 100:
        P = M.toogram(itm)
        d = M.tooldir(itm)
        #print(P, d)
    elif itm > 9000:
        P = M.program(itm)
        d = 'GUI.Main'
        #print(P, d)
    else:
        P = ''
        d = ''
        if hndlr != '':
            d,P = M.Runhdlr(hndlr)


    a = d+'.'+P
    #print(a)
    try:
        i = importlib.import_module(a)
    except ImportError as error:
        print(error)
        i = -1
    #print(dir(i))
    return i

