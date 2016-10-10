import sqlite3 as lite
import os
databasePath = os.path.join(os.path.expanduser('~'),"grxAutosysTool.db")

tableName = 'EnvList'
conn = lite.connect(databasePath)

def checkTableExists(dbcon, tablename):
    dbcur = dbcon.cursor()
    dbcur.execute("""
        SELECT COUNT(*)
        FROM sqlite_master
        WHERE type = 'table' AND
         name = '{0}'
        """.format(tablename.replace('\'', '\'\'')))
    if dbcur.fetchone()[0] == 1:
        dbcur.close()
        return True

    dbcur.close()
    return False

if checkTableExists(conn,tableName) is False:
    crcur = conn.cursor()
    crcur.execute("Create table if not exists "+tableName+" (id integer)")
    crcur.close()
    conn.close()
    conn = lite.connect(databasePath)
    incur = conn.cursor()
    incur.execute("insert into "+ tableName + "(id) values (%d)" % (2))
    conn.commit()
    incur.close()

selcurr = conn.cursor()
selcurr.execute("select * from "+ tableName)
all_rows = selcurr.fetchall()
print('1):', all_rows)

selcurr.close()
conn.close()

