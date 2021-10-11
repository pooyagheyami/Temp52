#In The name of God
#!/usr/bin/env python
# -*- codnig: utf-8 -*-

from . import wxsq as sq


class GetData:
    def __init__(self, DBF, sends):
        self.DBF = DBF
        self.sends = sends

    def ShowItem(self, ibar=1):
        return sq.wxsqltxt(self.DBF, """select distinct mitem.extid, mitem.itemid,mitem.mbarid,mitem.itemname,handler.prgname,extended.acclvlid, mitem.itemtyp
                                        from mitem
                                        left join handler on handler.handlerid = mitem.handlerid
                                        left join extended on extended.extid = mitem.extid
                                        where mitem.mbarid = %d
                                        """ % ibar)

    def gItem(self, mbar=1, ext=''):
        return sq.wxsqltxt(self.DBF, """select mitem.itemname,mitem.itemid
                                        from mitem
                                        where mitem.mbarid = %d
                                         %s """ % (mbar, ext) )
    def gBarN(self, mbar=1):
        return sq.wxsqsnd(self.DBF,u'menubar',u'mbarname',u'mbarid',mbar)


    def AmenuBar(self, Access=u'FFFF',ext=''):
        return sq.wxsqltxt(self.DBF, """ SELECT distinct *
                                         FROM menubar,access
                                         where menubar.acclvlid = access.acclvlid
                                         and access.acclvl = '%s'
                                         %s order by menubar.mbarid""" % (Access,ext)
                           )
    def AmenuItm(self, barid=101):
        return sq.wxsqltxt(self.DBF, """SELECT DISTINCT mitem.itemid,mitem.itemname,extended.status,extended.shortcut,extended.icon,mitem.itemtyp
                     FROM mitem
                     left join extended on mitem.extid = extended.extid
                     WHERE mitem.mbarid = %d
                       """ % barid)  #ORDER BY mitem.itemid

    def getmItem(self, itmid=0):
        return sq.wxsqltxt(self.DBF, """ SELECT DISTINCT *
                     FROM mitem
                     left join extended on mitem.extid = extended.extid
                     left join access on extended.acclvlid = access.acclvlid
                     left join handler on mitem.handlerid = handler.handlerid
                     WHERE mitem.itemid = %d """ % itmid)

    def DirBar(self):
        return sq.wxsqltxt(self.DBF, """SELECT menubar.mbardir
                                        FROM menubar
                                        """)
    def AllBar(self,ext=''):
        return sq.wxsqltxt(self.DBF,"""SELECT * FROM menubar %s"""%ext)

    def AllSub(self, ext=''):
        return sq.wxsqltxt(self.DBF,"""SELECT * FROM mitem %s"""%ext)

    '''
    def RevItem(self):
        return sq.wxsqltxt(self.DBF,"""select mitem.itemname,mitem.itemid 
                                       from mitem
                                       where mitem.mbarid = (select menubar.mbarid
                                            from menubar
                                            where menubar.mbardir = 'GUI.Input')
        """)
    '''

    def MyProg(self,itemid=''):
        return sq.wxsqltxt(self.DBF,"""SELECT distinct mitem.handlerid, handler.prgname
            FROM mitem join handler on mitem.handlerid = handler.handlerid
            WHERE mitem.itemid = %s  """ %itemid)

    #def MnuDir(self,itemid=''):
    #    return  sq.wxsqltxt(self.DBF, """SELECT menubar.mbardir
    #          FROM mitem  JOIN menubar
    #          ON mitem.mbarid = menubar.mbarid
    #          WHERE mitem.itemid =  %s  """ %itemid)
    def MnuDir(self,itemid=''):
        return  sq.wxsqltxt(self.DBF, """SELECT menubar.mbardir
              FROM mitem  JOIN handler  ON mitem.handlerid = handler.handlerid
			  JOIN menubar ON handler.prgdir = menubar.mbarid
              WHERE mitem.itemid =  %s  """ %itemid)
    def MnuDir2(self,itemid=''):
        return sq.wxsqltxt(self.DBF, """SELECT Guidir.Dir
              FROM mitem  JOIN handler  ON mitem.handlerid = handler.handlerid
			  JOIN menubar ON menubar.mbarid = mitem.mbarid
			  JOIN Guidir ON menubar.mbardir = Guidir.prgdir
			  WHERE mitem.itemid = %s  """ %itemid)

    def SubDir(self,itemsub=''):
        return sq.wxsqltxt(self.DBF, """SELECT handler.prgdir
              FROM mitem  JOIN handler
              ON mitem.handlerid = handler.handlerid
              WHERE mitem.itemid = %s  """ %itemsub)

    def SubDir2(self, itemsub=''):
        return sq.wxsqltxt(self.DBF,"""SELECT Guidir.Dir
              FROM mitem  JOIN handler  ON mitem.handlerid = handler.handlerid
              JOIN Guidir ON Guidir.prgdir = handler.prgdir
              WHERE mitem.itemid = %s  """ %itemsub)

    def AllGuiDir(self, ext=''):
        return sq.wxsqltxt(self.DBF, """ SELECT * FROM Guidir %s""" %ext)

    def GetDirCod(self, idir=''):
        return sq.wxsqsnd(self.DBF,"Guidir", "hdddir", "prgdir", idir)

    def GetDirCod2(self, idir=''):
        return sq.wxsqsnd(self.DBF,"Guidir", "prgdir", "hdddir", idir)

    def DoHdnl(self):
        return sq.wxsqltxt(self.DBF,"""select handler.prgname
          from handler join mitem on mitem.handlerid = handler.handlerid
          WHERE  mitem.handlerid  notnull """)
    def RunHdnl(self, hndid = ''):
        return sq.wxsqltxt(self.DBF, """ select Guidir.Dir, handler.prgname
        from Guidir, handler
        where Guidir.prgdir = handler.prgdir
        and handler.handlerid = %s """ % hndid )

    def AllHndl(self, ext=''):
        return sq.wxsqltxt(self.DBF,""" select distinct * from handler %s """ % ext)

    def GetTB(self):
        return sq.wxsqltxt(self.DBF,"""select toolbar.toolid,toolbar.toolname,toolbar.toolicon,toolbar.shrttxt,handler.prgname 
                                       from toolbar left join handler
                                       on toolbar.handlerid = handler.handlerid """)

    def GetAllTB(self, ext=''):
        return sq.wxsqltxt(self.DBF,""" select * from toolbar %s""" % ext)

    def MyTogr(self,itolid=''):
        return sq.wxsqltxt(self.DBF,"""SELECT distinct toolbar.handlerid, handler.prgname
            FROM toolbar join handler on toolbar.handlerid = handler.handlerid
            WHERE toolbar.toolid = %s  """ %itolid)

    def TolDir(self,itolid=''):
        return sq.wxsqltxt(self.DBF, """ select distinct menubar.mbardir , mitem.handlerid
            from menubar, toolbar  inner join mitem on mitem.handlerid = toolbar.handlerid
            where menubar.mbarid = mitem.mbarid
            and toolbar.toolid =  %s  """ % itolid)
    def TolDir2(self,itolid=''):
        return sq.wxsqltxt(self.DBF, """select distinct Guidir.Dir , toolbar.handlerid
            from  toolbar  
			join handler on toolbar.handlerid = handler.handlerid
			join Guidir on handler.prgdir = Guidir.prgdir
            and toolbar.toolid = %s   """ % itolid)
    def Acclvl(self,accid=''):
        return sq.wxsqltxt(self.DBF, """ select * from access where access.acclvlid = '%s' """ % accid)
    def gBarItm(self,mbar=''):
        return  sq.wxsqltxt(self.DBF,""" select distinct mitem.mbarid , mitem.itemid , mitem.extid , extended.acclvlid
                                     from mitem,extended 
                                     where mitem.mbarid = %s""" % mbar)
    def getHndlr(self, prgnam = u''):
        return sq.wxsqltxt(self.DBF, """ select handler.handlerid, handler.prgdir 
                                    from handler     where handler.prgname = '%s'  """ %prgnam)

    def getHndid(self, mid=''):
        return sq.wxsqltxt(self.DBF, """ select handler.handlerid from handler where handler.prgdir = '%s' 
         order by handlerid """ % mid )

    def gethddir(self, dirct= u''):
        return sq.wxsqsnd(self.DBF,u'menubar',u'mbarid',u'mbardir',dirct)

    def AllPanes(self):
        return sq.wxsqltxt(self.DBF,""" select * from pans join panifo on pans.paninfoid = panifo.paninfoid """)

    def ListPanes(self):
        return sq.wxsqltxt(self.DBF," select pans.panname from pans ")

    def MLPansFils(self, ext=u''):
        return sq.wxsqltxt(self.DBF, ' select * from MLPane %s ' %ext)



class SetData:
    def __init__(self, Table,send, data):
        self.Table = Table
        self.send = send
        self.data = data

    def Additem(self, send, data):
        return sq.wxsqins('Menu2.db', self.Table, send, data)

    def Additem2(self, send, data):
        return sq.wxsqins2('Menu2.db', self.Table, send, data)

    def Upditem(self, send, data):
        return sq.wxsqlup('Menu2.db', self.Table, send, data)

    def Upditem2(self, send, data):
        return sq.wxsqlup2('Menu2.db', self.Table, send, data)

    def Delitem(self, data):
        return sq.wxsqdel('Menu2.db', self.Table, data)


