# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 21:08:17 2020
Write a Spark program that reads your browser history file, then displays the top 5 websites you visited in the last week?
@author: user
"""
import os
import sqlite3
con = sqlite3.connect('C:\\Users\\X\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
c = con.cursor()
c.execute("select datetime(last_visit_time/1000000-11644473600,'unixepoch'),url from  urls order by last_visit_time desc") #Change this to your prefered query
results = c.fetchall()
for r in results:
 print(r)