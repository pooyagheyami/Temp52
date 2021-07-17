select * from mitem left join menubar on menubar.mbarid = mitem.mbarid
 left join handler on handler.handlerid = mitem.handlerid
 left join extended on extended.extid = mitem.extid
 left join access on extended.acclvlid = access.acclvlid

