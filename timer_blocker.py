#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 14:41:40 2018

@author: taimasuid
"""


import time
import re
import datetime



def sleeper():
    while True:
        #USER INPUT
        
        t = input('How long to wait? (h:mm:ss):  ')
        h,m,s = re.split(':',t)
        t = datetime.timedelta(hours=int(h),minutes=int(m),seconds=int(s)).total_seconds()  
 
    #ERROR PART  
       # try:
       #     t = float(t)
       # except ValueError:
       #     print('Error. Please enter in a number.\n')
       #     continue
 
       #TIME BEFORE/AFTER
        print('Time In: %s' % time.ctime())
        time.sleep(t)
        print('Time Out: %s\n' % time.ctime())
 
 
try:
    sleeper()
except KeyboardInterrupt:
    print('\n\nUm, ok. guess you want to leave. Now Exiting.')
    exit()
    

