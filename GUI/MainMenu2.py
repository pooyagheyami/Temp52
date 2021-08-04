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
    def menuItem2(self, i):
        bitm = self.MySql.AmenuItm(i)
        mitem = []
        for itm in bitm:
            if itm[-1] == 'S':
                sitem = []
                sitem.append(itm)
                sitem.append(self.menuItem2(itm[0]))
                mitem.append(sitem)
            else:
                mitem.append(itm)
        return mitem

    def menuDir(self):
        self.Bdir = self.MySql.DirBar()
        self.mdir = []
        for row in self.Bdir:
            self.mdir.append(row)
        # print self.mdir
        return self.mdir


class AppMenu(wx.MenuBar):
    Lstmnu = []
    Lstsub = []
    def __init__(self):
        wx.MenuBar.__init__(self, style=0)
        self.m = MenuData()
        #print(self.m.menuBar())
        self.createMenuBar()

    def createMenuBar(self):
        for eachmenu in self.m.menuBar():
            menutitle = eachmenu[1]
            #print('MenuItem 2:',self.m.menuItem2(eachmenu[0]))
            #self.Append(self.createMenuItem(self.m.menuItem(eachmenu[0])),menutitle)
            self.Append(self.createMenuItem2(self.m.menuItem2(eachmenu[0])), menutitle)
        return self

    def createMenuItem2(self, menudata):
        menu = wx.Menu()
        self.Lstmnu.append(menu)
        #print(menudata)
        for eachitem in menudata:
            if type(eachitem) != list:
                eachid, eachlabel, eachstatus, shortcut, eachicon, eachtype = eachitem
                if not eachlabel:
                    menu.AppendSeparator()
                    continue
                else:
                    itmlbl = eachlabel
                    if shortcut != '':
                        itmlbl += '\t' + shortcut
                if eachtype == 'C':
                    menuitem = menu.AppendCheckItem(eachid, itmlbl, eachstatus)
                elif eachtype == 'R':
                    menuitem = menu.AppendRadioItem(eachid, itmlbl, eachstatus)
                elif eachtype == 'N':
                    menuitem = menu.Append(eachid, itmlbl, eachstatus)
                #elif eachtype == 'S':
                #    self.menu.AppendSubMenu(self.createMenuItem2(eachitem), eachlabel, eachstatus)
                    #return self.menu
                else:
                    wx.MessageBox('Error In Menu Database. Please connect to Programmer')
                if eachicon != None and eachicon != '':
                    menuitem.SetBitmap(wx.Bitmap(ICON16_PATH + eachicon, wx.BITMAP_TYPE_ANY))

            elif type(eachitem) == list:
                #print('This list send:', eachitem[1])
                subroot = self.createMenuItem2(eachitem[1])
                menuitem = menu.AppendSubMenu(subroot, eachitem[0][1])
                self.Lstsub.append(subroot)
                #self.createMenuItem2(eachitem)
                pass
            else:
                wx.MessageBox('Error In Menu Database. Please connect to Programmer')
        return menu

    def Onmenu(self, event):
        self.mid = event.GetId()

    def GetItemId(self):
        return self.GetMenus()[0]

    def AddItem2(self, Mbar, Data, Bar=''):
        lbl = self.ChkShrtCut(Data)
        print(self.FindMenu(Mbar))
        if self.FindMenu(Mbar) != -1:
            imnu = self.GetMenu(self.FindMenu(Mbar))
        else:
            imnu = self._findmenu2(Mbar, Bar)
            #imnu = self.FindMenuItem(mb.GetMenu,Mbar)

        iitm = imnu.Append(int(Data[0]), lbl, Data[5])
        if Data[3] != '':
            iitm.SetBitmap(wx.Bitmap(ICON16_PATH + Data[3], wx.BITMAP_TYPE_ANY))

    def AddItem(self,Mbar,Data,Bar='B'):
        if Bar == 'B':
            imnu = self._BackMyMenu(Mbar)
        else:
            imnu = self._findsubmenu2(Mbar)
            #print(imnu)
        lbl = self.ChkShrtCut(Data)
        iitm = imnu.Append(int(Data[0]),lbl,Data[5])
        if Data[3] != '':
            iitm.SetBitmap(wx.Bitmap(ICON16_PATH + Data[3], wx.BITMAP_TYPE_ANY))
        #print(iitm)

    def AddSubMenu2(self,Mbar,Data,Bar=''):
        lbl = self.ChkShrtCut(Data)
        print(self.FindMenu(Mbar))
        if self.FindMenu(Mbar) != -1:
            imnu = self.GetMenu(self.FindMenu(Mbar))
        else:
            imnu = self._findmenu2(Mbar, Bar)
        iitm = imnu.AppendSubMenu(self.createSubmenu(Data[0],lbl),lbl)
        if Data[3] != '':
            iitm.SetBitmap(wx.Bitmap(ICON16_PATH + Data[3], wx.BITMAP_TYPE_ANY))


    def AddSubMenu(self,Mbar,Data,Bar='B'):
        if Bar == 'B':
            imnu = self._BackMyMenu(Mbar)
        else:
            imnu = self._findsubmenu2(Mbar)
        lbl = self.ChkShrtCut(Data)
        iitm = imnu.AppendSubMenu(self.createSubmenu(Data[0]),lbl)
        if Data[3] != '':
            iitm.SetBitmap(wx.Bitmap(ICON16_PATH + Data[3], wx.BITMAP_TYPE_ANY))

    def createSubmenu(self, mroot, title = '' ):
        mroot = wx.Menu()
        mroot.SetTitle(title)
        self.Lstsub.append(mroot)
        return mroot

    def AddSepar(self,title):
        imnubar = self.FindMenu(title)
        itmmnu = self.GetMenu(imnubar)
        #print(itmmnu)
        itmmnu.AppendSeparator()

    def AddCheck(self,Mbar,Data):
        imnu = self._BackMyMenu(Mbar)
        lbl = self.ChkShrtCut(Data)
        iitm = imnu.AppendCheckItem(int(Data[0]),lbl,Data[5])

    def AddRadio(self,Mbar,Data):
        imnu = self._BackMyMenu(Mbar)
        lbl = self.ChkShrtCut(Data)
        iitm = imnu.AppendRadioItem(int(Data[0]), lbl)

    def _findmenu2(self, Mbar, Bar):
        mw = self.FindWindowByName('main')
        mb = mw.GetMenuBar()
        if Bar != 'S':
            return mb.GetMenu(mb.FindMenu(Mbar))
        else:
            print(self.Lstsub)
            for m in self.Lstsub:
                print(m.GetTitle())
                if m.GetTitle() == '' or m.GetTitle() == Mbar:
                    print(m)
                    return m


    def _BackMyMenu(self,Mbar):
        imnubar = self.FindMenu(Mbar)
        itmmnu = self.GetMenu(imnubar)
        #print(itmmnu)
        return itmmnu

    def _findsubmenu(self,Sub):
        lstbar = self.GetMenus()
        for bar in lstbar:
            lst = bar[0].GetMenuItems()
            for l in lst:
                if l.IsSubMenu() and l.GetItemLabel() == Sub:
                    #print(l.GetSubMenu())
                    return l.GetSubMenu()

    def _findsubmenu2(self, Sub):
        for bar in self.Lstmnu:
            lst = bar.GetMenuItems()
            for l in lst:
                print(l.IsSubMenu(), l.GetItemLabel())
                if l.IsSubMenu() and l.GetItemLabel() == Sub:
                    return l.GetSubMenu()


    def ChkShrtCut(self,Data):
        if Data[4] != '':
            return Data[2]+'\t'+Data[4]
        else:
            return Data[2]