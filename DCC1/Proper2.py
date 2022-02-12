# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################


import wx
import wx.aui as wxaui
import wx.adv
import wx.propgrid as pg
import os
import sys
import Database.MenuSet2 as MS
from Config.Init import *

_ = wx.GetTranslation

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

        self.AddPrivateChild( pg.IntProperty("X", value=value.x) )
        self.AddPrivateChild( pg.IntProperty("Y", value=value.y) )

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
# Check Property class
#
###########################################################################
#class checkProperty(pg.PGCheckBoxEditor)


###########################################################################
## Class MyPanel1
###########################################################################


class MyPanel1 ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,500 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        #self.panel = panel = wx.Panel(self, wx.ID_ANY)
        #print(panel.GetSize())
        self.MyMenu = MS.GetData(u'Menu2.db', u'')

        LAuiP = [ l[0] for l in self.MyMenu.ListPanes() ]

        Statu = [u'name',u'date',u'time']
        #print(LAuiP)

        language = [LANGUAGE_LIST[lan] for lan in LANGUAGE_LIST]
        DBtype   = [Database_type[dbt] for dbt in Database_type ]
        lan = [lan for lan in LANGUAGE_LIST ]
        DBt = [Dtyp for Dtyp in Database_type]

        Vsz1 = wx.BoxSizer( wx.VERTICAL )

        self.pgm = pg.PropertyGridManager(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.propgrid.PG_DESCRIPTION|wx.propgrid.PG_SPLITTER_AUTO_CENTER|wx.propgrid.PG_TOOLBAR|wx.TAB_TRAVERSAL)
        #self.pgm.SetExtraStyle( wx.propgrid.PG_EX_MODE_BUTTONS )
        self.pgm.ExtraStyle |= pg.PG_EX_HELP_AS_TOOLTIPS

        self.pgm.Bind(pg.EVT_PG_CHANGED, self.OnPropGridChange)
        self.pgm.Bind(pg.EVT_PG_PAGE_CHANGED, self.OnPropGridPageChange)
        self.pgm.Bind(pg.EVT_PG_SELECTED, self.OnPropGridSelect)
        self.pgm.Bind(pg.EVT_PG_RIGHT_CLICK, self.OnPropGridRightClick)

        self.config = wx.GetApp().GetConfig()


        PansLst = eval(self.config.Read("Panes"))
        StatLst = eval(self.config.Read("Status"))
        self.ifont = self.config.Read(u'Font')
        TBGname,self.TBGCol = self.config.Read(u'TBGColor').split(',')
        SBGname,self.SBGCol = self.config.Read(u'SBGColor').split(',')
        Winsize = wx.Size(eval(self.config.Read(u'WinSize')))
        #Winsize = (int(self.config.Read(u'WinSize').split(',')[0]),int(self.config.Read(u'WinSize').split(',')[1]))
        #print(Winsize)

        mw = wx.GetTopLevelWindows()

        fntis = self.config.Read(u'Font').split(',')
        #print(fntis)
        if fntis[4] == 'True':
            undr = True
        else:
            undr = False

        ifont = wx.Font(int(fntis[0]),int(fntis[1]),int(fntis[2]),int(fntis[3]),undr,faceName=fntis[5])


        conflst = {u"General properties":[(u'Enum',u"Language", u"Language",u"",language,lan,int(self.config.Read("Language")) ),
                                          (u"Image",u"Splash",u"Splash",u"Use this file for Splash",self.config.Read('Splash') ),
                                          (u"Enum",u"Database type",u"DBtype",u"",DBtype,DBt,int(self.config.Read('DBtype')) )
                                          ],
                   u"Main Window properties":[(u'String',u'Label of Window',u'Winname',u'Show label of Main window',self.config.Read(u'Winname')),
                                              (u'Size',u'Window Size',u'WinSize',u'Set Main Window Size start',Winsize),
                                              (u'Bool',u"Back Ground Active",u"BGActive",u"UseCheckbox",eval(self.config.Read('BGActive'))),
                                              (u"Image",u"Background",u"Background",u"If Active BackGround Use this file",self.config.Read('Background')),
                                              #(u"Enum",u"Type of Menu",u"Menu",u"",[u'Normal',u'Flat'],[1,2],int(self.config.Read("Menu"))),
                                              (u"Enum",u"Type of Toolbar",u"Toolbar",u"",[u'Normal',u'Aui'],[1,2],int(self.config.Read("Toolbar"))),
                                              (u"SysColor",u"Toolbar Background",u"TBGColor",u"Toolbar Background colour set",self.TBGCol),
                                              (u"MChoice",u"Start Panes",u"Panes",u"Start this panes in Main Window",LAuiP,PansLst),
                                              (u"Font",u"Main Window Font",u"Font",u"",ifont),
                                              (u"MChoice",u"Show in Status ",u"Status",u"",Statu,StatLst),
                                              (u"SysColor",u"Status Background Color",u"SBGColor",u"Status background colour set",self.SBGCol)]
        }

        self.P1 = self.pgm.AddPage( u"General Properties Page", wx.ArtProvider.GetBitmap( wx.ART_LIST_VIEW, wx.ART_MESSAGE_BOX ) );

        Items1 = []
        for con in conflst:
            Items1.append(self.P1.Append( pg.PropertyCategory(con, con)))
            for itm in conflst[con]:
                if itm[0] == u"Enum":
                    Items1.append(self.P1.Append( pg.EnumProperty(itm[1],itm[2],itm[4],itm[5],itm[6]) ))
                    Items1[-1].SetHelpString(itm[3])
                elif itm[0] == u"Image":
                    Items1.append(self.P1.Append( pg.ImageFileProperty(itm[1],itm[2],value=itm[4]) ))
                    Items1[-1].SetHelpString(itm[3])
                elif itm[0] == u"Bool":
                    Items1.append(self.P1.Append( pg.BoolProperty(itm[1],itm[2],value=itm[4]) ))
                    #Items1[-1].SetHelpString(itm[3])
                    self.pgm.SetPropertyAttribute(itm[2],itm[3],True )
                elif itm[0] == u"MChoice":
                    Items1.append(self.P1.Append( pg.MultiChoiceProperty(itm[1],itm[2],choices=itm[4],value=itm[5]) ) )
                    Items1[-1].SetHelpString(itm[3])
                elif itm[0] == u"Font":
                    Items1.append(self.P1.Append( pg.FontProperty(itm[1],itm[2],ifont) ) )
                    Items1[-1].SetHelpString(itm[3])
                elif itm[0] == u'SysColor':
                    Items1.append(self.P1.Append( pg.SystemColourProperty(itm[1],itm[2])))
                    Items1[-1].SetHelpString(itm[3])
                    Items1[-1].SetValue(wx.SystemSettings.GetColour(int(itm[4])))
                    #print(Items1[-1])
                elif itm[0] == u'String':
                    Items1.append(self.P1.Append( pg.StringProperty(itm[1],itm[2],itm[4])))
                    Items1[-1].SetHelpString(itm[3])
                elif itm[0] == u'Size':
                    Items1.append(self.P1.Append( SizeProperty(itm[1],itm[2],value=wx.Size(itm[4]))))
                else:
                    print("something error")



        MAP = os.getcwd()
        dirlst = {u'Main Directory and Path':[(u"Application Path",'AppPath',u"The Path of application and work program",MAP),
                                              (u"Database Path",u'DBPath',u'',MAP+u'\\Src\\DBF'),
                                              (u"API source path",u'APIPath',u"The path of application program interface ",MAP+u'\\Src\\API'),
                                              (u"Program of Menu Bar Path",u"PRGPath",u"",MAP+u"\\Src\\PRG"),
                                              (u"Menu Programs Path",u'MnuPath',u'',MAP+u'\\GUI\\Program')
                                              ],
                  u"Resouce and images":[(u"Fonts Path",u'Fonts',u'',MAP+u'\\Res\\Fonts'),
                                         (u"Icon Menu Path",u'MenuPath',u'',MAP+u'\\Res\\Icons\\Menu'),
                                         (u"Icon Toolbar Path",u'ToolPath',u'',MAP+u'\\Res\\Icons\\Toolbar'),
                                         (u"Image Path",u'ImgPath',u'',MAP+u'\\Res\\Images'),
                                         (u"Picture Path",u'PicPath',u'',MAP+u'\\Res\\Pics'),
                                         (u"Splash Path", u'SplshPath', u'', MAP + u'\\Res\\Splash')
                                         ],

                  u"Other Path":[(u"Temp Path",u'TmpPath',u'',MAP+u'\\Temps'),
                                 (u"Log Path",u'LogPath',u'',MAP+u'\\Logs'),
                                 (u"Utility Path",u'UtilPath',u'',MAP+u'\\Utility'),
                                 (u"Config Path",u'ConPath',u'',MAP+u'\\Config'),
                                 ],
                  u"Machin Learning Source":[(u"Machine Learning Algorithm",u'MLAPath',u'',MAP+u'\\Src\\MLA'),
                                             (u"Machine Learning Panel",u'MLPPath',u'',MAP+u'\\Src\\MLP')]
                  }
        self.Itms = []


        self.P2 = self.pgm.AddPage( u"Directory and Path Page", wx.ArtProvider.GetBitmap( wx.ART_FOLDER_OPEN, wx.ART_MESSAGE_BOX ) );
        for itm in dirlst:
            #print(itm)
            self.Itms.append(self.P2.Append(pg.PropertyCategory(itm,itm)))
            for tm in dirlst[itm]:
                self.Itms.append(self.P2.Append(pg.DirProperty(tm[0],tm[1],value=tm[3])))
                self.P2.SetPropertyHelpString(self.Itms[-1], tm[2])


        Vsz1.Add( self.pgm, 1, wx.ALL|wx.EXPAND, 5 )

        Hsz1 = wx.BoxSizer( wx.HORIZONTAL )

        self.btn1 = wx.Button( self, wx.ID_ANY, u"Cancle", wx.DefaultPosition, wx.DefaultSize, 0 )
        Hsz1.Add( self.btn1, 0, wx.ALL, 5 )

        self.btn2 = wx.Button( self, wx.ID_ANY, u"Apply", wx.DefaultPosition, wx.DefaultSize, 0 )
        Hsz1.Add( self.btn2, 0, wx.ALL, 5 )


        Vsz1.Add( Hsz1, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.SetSizer( Vsz1 )
        self.Layout()

        # Connect Events
        self.btn1.Bind( wx.EVT_BUTTON, self.cncl )
        self.btn2.Bind( wx.EVT_BUTTON, self.aply )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def cncl( self, event ):
        q = self.GetParent()
        q.Close()


    def aply( self, event ):
        d = self.pgm.GetPropertyValues(inc_attributes=True)
        v = self.pgm.GetPropertyValues(as_strings=True)
        #print(d)
        e = self.pgm.GetPropertyValues()
        #print(e)
        self.config = wx.GetApp().GetConfig()
        for itm in e:
            if itm == 'TBGColor':
                #print(e[itm])
                self.config.Write(itm,v[u'TBGColor']+','+str(self.TBGCol))
            elif itm == 'SBGColor':
                self.config.Write(itm,v[u'SBGColor']+','+str(self.SBGCol))
            elif itm == 'Font':
                self.config.Write('Font', self.ifont)
            else:
                self.config.Write(itm,str(e[itm]))

        self.config.Flush()
        wx.MessageBox("Config file changed. You must Start application again to see the change")
        q = self.GetParent()
        q.Close()


    def OnPropGridChange(self, event):
        p = event.GetProperty()
        v = self.pgm.GetPropertyValues(as_strings=True)
        #print('change',p.GetValue(),p.GetName(),p.GetLabel(),p.GetDisplayedString())
        if p.GetName() == 'Background':
            bmpwin = wx.GetTopLevelWindows()
            bmpwin[0].bmpwin.BGfile = p.GetValue()
            bmpwin[0].bmpwin.ChangeBackGround()
        if p.GetName() == u'Font':
            #print(v[u'Font'])
            wfont = p.GetValue()
            minwin = wx.GetTopLevelWindows()

            f1 = wfont.GetPointSize()
            f2 = wfont.GetFamily()
            f3 = wfont.GetStyle()
            f4 = wfont.GetWeight()
            f5 = wfont.GetUnderlined()
            f6 = wfont.GetFaceName()
            #print(f1,f2,f3,f4,f5,f6)
            self.ifont = str(f1)+','+str(f2)+','+str(f3)+','+str(f4)+','+str(f5)+','+f6
            #print(minwin[0],wfont)
            minwin[0].SetFont(wfont)
            minwin[0].SetOwnFont(wfont)
            minwin[0].Refresh()
            minwin[0].m_mgr.Update()

        if p.GetName() == u'TBGColor':
            #print(v[u'TBGColor'])
            wcolor = p.GetValue()
            self.TBGCol = wcolor.m_type
            minwin = wx.GetTopLevelWindows()
            #print(minwin[0].GetToolBar())
            minwin[0].GetToolBar().SetBackgroundColour(wx.SystemSettings.GetColour(wcolor.m_type))
            minwin[0].Refresh()



        if p.GetName() == u'SBGColor':
            #print(v[u'SBGColor'])
            wcolor = p.GetValue()
            #print(wcolor.m_type)
            self.SBGCol = wcolor.m_type
            minwin = wx.GetTopLevelWindows()
            #print(minwin[0].GetStatusBar().GetFieldsCount())
            minwin[0].GetStatusBar().SetBackgroundColour(wx.SystemSettings.GetColour(wcolor.m_type))
            minwin[0].Refresh()






    def OnPropGridSelect(self, event):
        p = event.GetProperty()
        #print('select',dir(p))

    def OnPropGridRightClick(self, event):
        p = event.GetProperty()
        #print('Right',p)

    def OnPropGridPageChange(self, event):
        index = self.pgm.GetSelectedPage()
        #print('Page N',index)
