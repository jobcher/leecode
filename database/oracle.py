#!/usr/bin/python3
"""
使用python 对oracle数据进行操作
提前安装好 cx_Oracle
pip3 install cx_Oracle
"""
import cx_Oracle

conn = cx_Oracle.connect('sj','sjjxc','193.0.0.77/mg01')
cursor = conn.cursor()
sql = 'SELECT to_char(wmsys.wm_concat(a.shopid)) FROM (SELECT shopid, MAX(sdate) sdate FROM dbusroms1.accountdatelist   where sdate>sysdate-10 GROUP BY shopid) a,(SELECT DISTINCT shopid, rjdate FROM dbusroms1.mktrjproc)b WHERE a.shopid = b.shopid    AND a.sdate <> rjdate - 1'
cursor.execute(sql)
res = cursor.fetchall()