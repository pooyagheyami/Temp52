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
            sqlfile = DATABASE_PATH + 'sqls' + SLASH + file
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
        self.Field = Field
        self.Data = Data


    def Addrecord(self):
        return sq.wxsqins(self.DBF, self.Tabel, self.Field, self.Data)

    def Addrecord2(self):
        return sq.wxsqins2(self.DBF, self.Tabel, self.Field, self.Data)

    def Updaterecord(self):
        return sq.wxsqlup(self.DBF, self.Tabel, self.Field, self.Data)

    def Updaterecord2(self):
        return sq.wxsqlup2(self.DBF, self.Tabel, self.Field, self.Data)

    def Deleterecord(self):
        return sq.wxsqdel(self.DBF, self.Field, self.Data)

    def DeleteAllrecord(self):
        return sq.wxsqdall(self.DBF, self.Field)


    def __del__(self):
        pass

    def __hash__(self):
        pass