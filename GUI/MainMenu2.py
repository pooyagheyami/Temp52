# In the name of God
# Cearte Menu main Frame File
# ! /usr/bin/env python
# -*- coding: utf-8 -*-

import Database.MenuSet2 as MS
import wx
import os
from Config.Init import *


class MainMenu():
    def __init__(self):
        self.createMenuBar()
        #self.menuItem = self.menu.Append(0,'','')
        #M = MenuData()
        #self.m = M.menuBar()
        self.mid = 1001

    def createMenuBar(self):
        self.menuBar = wx.MenuBar()
        #self.mhand = []
        self.m = MenuData()
        for eachMenuData in self.m.menuBar():
            menuLabel = eachMenuData[1]
            menuItem = self.m.menuItem(eachMenuData[0])

            self.menuBar.Append(self.createMenu(menuItem), menuLabel)
            #if eachMenuData[3] == '31cd':
            #    print(self.menuBar)

        #print( self.menuBar )
        return self.menuBar

    def createMenu(self, menuData):
        self.menu = wx.Menu()
        #print(menuData)
        for echitem in menuData:
            #print(echitem)
            if type(echitem) != list:
                eachId, eachLabel, eachStatus, shrtcut, echicon, mtype = echitem

                if not eachLabel:
                    self.menu.AppendSeparator()
                    continue
                if shrtcut != None:
                    itmlebl = eachLabel + u'\t' + shrtcut
                else:
                    itmlebl = eachLabel

                if mtype == 'C':
                    self.menuItem = self.menu.AppendCheckItem(eachId, itmlebl, eachStatus)
                elif mtype == 'R':
                    self.menuItem = self.menu.AppendRadioItem(eachId, itmlebl)
                elif mtype == 'N':
                    self.menuItem = self.menu.Append(eachId, itmlebl, eachStatus)
                else:
                    print('mtype has a error')
                if echicon != None and echicon != '':
                    self.menuItem.SetBitmap(wx.Bitmap(ICON16_PATH + echicon, wx.BITMAP_TYPE_ANY))

            else:
                for ech in echitem:
                    eachId, eachLabel, eachStatus, shrtcut, echicon, mtype = ech
                    if mtype == 'S':
                        iroot = self.createSubmenu(eachId)
                        self.menuItem = self.menu.AppendSubMenu(iroot,eachLabel)
                    else:
                        self.menuItem =  iroot.Append(eachId,eachLabel,eachStatus)

        #print(self.menu)
        return self.menu

    def createSubmenu(self, mroot ):
        mroot = wx.Menu()
        return mroot

    #def createHandler(self):
        # print self.menu.GetEventHandler()
        #return self.menu.GetEventHandler

    def Onmenu(self, event):
        self.mid = event.GetId()
        # print self.GetItemId()

    def GetItemId(self):
        #print(self.menuItem)
        return self.menuItem


class MenuData(object):
    def __init__(self):
        self.MySql = MS.GetData(u'Menu2.db', u'')
        self.ToSql = MS.SetData(u'', u'',u'')

    def menuBar(self):
        self.mbar = []
        for row in self.MySql.AmenuBar(ext=' and menubar.mbarid < 9999  '):
            self.mbar.append(row)
        return self.mbar

    def menuItem(self, i):
        self.bitm = self.MySql.AmenuItm(i)
        self.mitem = []
        self.sitem = []
        for itm in self.bitm:
            #print(itm)
            if itm[-1] == 'S':
                self.sitem.append(itm)
                stm = self.MySql.AmenuItm(itm[0])
                for s in stm:
                    self.sitem.append(s)
                #self.mitem.append(itm)
                self.mitem.append(self.sitem)
            else:
                self.mitem.append(itm)
        #print( self.mitem)
        return self.mitem

    def menuDir(self):
        self.Bdir = self.MySql.DirBar()
        self.mdir = []
        for row in self.Bdir:
            self.mdir.append(row)
        # print self.mdir
        return self.mdir


class AuiMenu(wx.MenuBar):
    def __init__(self):
        wx.MenuBar.__init__(self, style=0)
        self.m = MenuData()
        print(self.m.menuBar())
        self.createMenuBar()


    def createMenuBar(self):
        for eachmenu in self.m.menuBar():
            menutitle = eachmenu[1]
            print(self.m.menuItem(eachmenu[0]))
            self.Append(self.createMenuItem(self.m.menuItem(eachmenu[0])),menutitle)

    def createMenuItem(self, menudata):
        self.menu = wx.Menu()

        return self.menu

    def AddItem(self):
        pass

    def AddSubMenu(self):
        pass

    def AddSepar(self):
        pass

    def AddCheck(self):
        pass

    def AddRadio(self):
        pass