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
## Class MyPanel1
###########################################################################


class MyPanel1 ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,500 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        #self.panel = panel = wx.Panel(self, wx.ID_ANY)
        #print(panel.GetSize())

        Vsz1 = wx.BoxSizer( wx.VERTICAL )

        self.pgm = pg.PropertyGridManager(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.propgrid.PG_DESCRIPTION|wx.propgrid.PG_SPLITTER_AUTO_CENTER|wx.propgrid.PG_TOOLBAR|wx.TAB_TRAVERSAL)
        #self.pgm.SetExtraStyle( wx.propgrid.PG_EX_MODE_BUTTONS )
        self.pgm.ExtraStyle |= pg.PG_EX_HELP_AS_TOOLTIPS

        self.pgm.Bind(pg.EVT_PG_CHANGED, self.OnPropGridChange)
        self.pgm.Bind(pg.EVT_PG_PAGE_CHANGED, self.OnPropGridPageChange)
        self.pgm.Bind(pg.EVT_PG_SELECTED, self.OnPropGridSelect)
        self.pgm.Bind(pg.EVT_PG_RIGHT_CLICK, self.OnPropGridRightClick)

        self.config = wx.GetApp().GetConfig()

        conflst = {u"General properties":[('Date',u"Date",u"Date",u"Contorl Date of system and program",wx.DateTime.Now()),
                                          (u'Enum',u"Language", u"Language",u"",[u'English',u'Turkish',u'Persian'],[1,2,3],1 ),
                                          (u"Image",u"Background",u"Background",u"",self.config.Read('Background'))],

        }

        self.P1 = self.pgm.AddPage( u"General Properties Page", wx.ArtProvider.GetBitmap( wx.ART_LIST_VIEW, wx.ART_MESSAGE_BOX ) );

        self.Item1 = self.P1.Append( pg.PropertyCategory( u"General properties", u"General properties" ) )
        self.Item2 = self.P1.Append( pg.DateProperty( u"Date", value=wx.DateTime.Now() ) )
        self.P1.SetPropertyHelpString( self.Item2, u"Contorl Date of system and program" )
        self.Item3 = self.P1.Append( pg.EnumProperty( u"Language", u"Language",[u'English',u'Turkish',u'Persian'],[1,2,3],1 ) )
        #self.Item4 = self.P1.Append( pg.ImageFileProperty( u"Background",value=os.getcwd()+u'\\Res\\Pics\\V19.jpg' ) )
        self.Item4 = self.P1.Append(pg.ImageFileProperty(u"Background", value=self.config.Read("Background")))
        self.Item5 = self.P1.Append( pg.EnumProperty( u"Type of Toolbar", u"Toolbar",[u'Normal',u'Aui'],[1,2],1 ) )
        self.Item6 = self.P1.Append( pg.EnumProperty( u"Type of Menu", u"Menu",[u'Normal',u'Flat'],[1,2],1 ) )
        self.Item7 = self.P1.Append( pg.MultiChoiceProperty( u"Start Panes",u"Panes",choices=[u'Pane 1',u'Pane 2',u'Pane 3']  ) )

        self.Item8 = self.P1.Append( pg.PropertyCategory( u"Form Properties", u"Form Properties" ) )
        self.Item9 = self.P1.Append( SizeProperty( u"Default size",u'FSize', value=wx.DefaultSize ) )

        self.Item10 = self.P1.Append(pg.EnumProperty(u"Form Type", u"FType", [u'',u'']))
        self.Item11 = self.P1.Append(pg.ImageFileProperty(u"Form Background", u"FormBackground"))
        self.Item12 = self.P1.Append(pg.PropertyCategory(u"Toolbar Properties", u"Toolbar Properties"))
        self.Item13 = self.P1.Append( SizeProperty(u"Icon Size", u"IconSize",value=wx.DefaultSize))
        self.Item14 = self.P1.Append(pg.EnumProperty(u"Text position", u"TextPos"))
        self.Item15 = self.P1.Append(pg.EnumProperty(u"Toolbar Type", u"TBType"))
        self.Item16 = self.P1.Append( pg.PropertyCategory( u"Panes Properties", u"Panes Properties" ) )
        self.Item17 = self.P1.Append( pg.IntProperty( u"Nomber of Leyer", u"NLeyer" ) )
        self.Item18 = self.P1.Append( pg.PropertyCategory( u"Status Properties", u"Status Properties" ) )
        self.Item19 = self.P1.Append( pg.MultiChoiceProperty( u"Choice parameter", u"Choice parameter" ) )

        self.pgm.SetPropertyAttribute("Date", pg.PG_DATE_PICKER_STYLE,wx.adv.DP_DROPDOWN | wx.adv.DP_SHOWCENTURY)
        MAP = os.getcwd()
        dirlst = {u'Main Directory and Path':[(u"Application Path",'AppPath',u"The Path of application and work program",MAP),
                                              (u"Database Path",u'DBPath',u'',MAP+u'\\Database'),
                                              (u"GUI API path",u'APIPath',u"The path of application program interface that each menu point to execute it",MAP+u'\\GUI'),
                                              (u"Menu Programs Path",u'MnuPath',u'',MAP+u'\\GUI\\Program')],
                  u"Resouce and images":[(u"Icon 32X32 Path",u'Icn32Path',u'',MAP+u'\\Res\\Icons\\32x32'),
                                         (u"Icon 16X16 Path",u'Icn16Path',u'',MAP+u'\\Res\\Icons\\16x16'),
                                         (u"Image and Pic Path",u'ImgPath',u'',MAP+u'\\Res\\Pics'),
                                         (u"Splash Path",u'SplshPath',u'',MAP+u'\\Res\\Splash')],

                  u"Other Path":[(u"Temp Path",u'TmpPath',u'',MAP+u'\\Temps'),
                                 (u"Log Path",u'LogPath',u'',MAP+u'\\Logs'),
                                 (u"Utility Path",u'UtilPath',u'',MAP+u'\\Utility'),
                                 (u"Config Path",u'ConPath',u'',MAP+u'\\Config'),
                                 (u"Machine Learning Path",u'MLPath',u'',MAP+u'\\AI\\ML')]}
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
        #print(d)
        e = self.pgm.GetPropertyValues()
        #print(e)
        self.config = wx.GetApp().GetConfig()
        for itm in e:
            self.config.Write(itm,str(e[itm]))
        self.config.Flush()
        wx.MessageBox("Config file changed. You must Start application again to see the change")
        q = self.GetParent()
        q.Close()


    def OnPropGridChange(self, event):
        p = event.GetProperty()
        #print('change',p.GetValue(),p.GetName(),p.GetLabel(),p.GetDisplayedString())
        if p.GetName() == 'Background':
            bmpwin = wx.GetTopLevelWindows()
            bmpwin[0].bmpwin.BGfile = p.GetValue()
            bmpwin[0].bmpwin.ChangeBackGround()

    def OnPropGridSelect(self, event):
        p = event.GetProperty()
        #print('select',dir(p))

    def OnPropGridRightClick(self, event):
        p = event.GetProperty()
        #print('Right',p)

    def OnPropGridPageChange(self, event):
        index = self.pgm.GetSelectedPage()
        #print('Page N',index)
