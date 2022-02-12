#In The name of God
#!/usr/bin/env python
# -*- codnig: utf-8 -*-

from . import wxsq as sq
from Config.Init import *

class Get:
    def __init__(self, DBF, Data, file):
        self.DBF = DBF
        self.Data = Data

        if file != '':
            #sqlfile = DATABASE_PATH + 'sqls' + SLASH + file
            sqlfile = Src_dbf + 'sqls' + SLASH + file
            self.SQLtxt = self.openSql(sqlfile)

    def openSql(self, sqlfile):
        with open(sqlfile) as f:
            alltxt = f.readlines()
        #print(alltxt)
        return alltxt[0]

    def GetFromDbf(self):
        return sq.wxsqltxt(self.DBF, self.SQLtxt)

    def GetFromDbfWithData(self):
        return sq.wxsqltxt(self.DBF, self.SQLtxt + self.Data )

    def GetFromString(self, string):
        return sq.wxsqltxt(self.DBF, string)

    def __del__(self):
        pass

    def __hash__(self):
        pass



class Post:
    def __init__(self, DBF, Tabel, Field, Data):
        self.DBF = DBF
        self.Tabel = Tabel
        #self.Field = Field
        #self.Data = Data

    def Addrecord(self,Field,Data):
        return sq.wxsqins(self.DBF, self.Tabel, Field, Data)

    def Addrecord2(self,Field,Data):
        return sq.wxsqins2(self.DBF, self.Tabel, Field, Data)

    def Updaterecord(self,Field,Data):
        return sq.wxsqlup(self.DBF, self.Tabel, Field, Data)

    def Updaterecord2(self,Field,Data):
        return sq.wxsqlup2(self.DBF, self.Tabel, Field, Data)

    def Deleterecord(self,Data):
        return sq.wxsqdel(self.DBF, self.Tabel, Data)

    def DeleteAllrecord(self,Field):
        return sq.wxsqdall(self.DBF, Field)


    def __del__(self):
        pass

    def __hash__(self):
        pass