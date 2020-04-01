#! /usr/bin/python3

import os
import re
import time

basePath = '/sys/bus/w1/devices'
fname = 'w1_slave'

dirList = os.listdir(basePath)
#print(dirList)

while 1:
    for d in dirList:
        if d != 'w1_bus_master1':
            tempData = ''
            fPath = os.path.join(basePath, d, fname)
            #print(fPath)
            
            with open(fPath, 'r') as fo:
                for line in fo:
                    matchObj = re.search(r't=(\d{4,})', line, re.I)
                    if matchObj:
                        tempData = matchObj.group(1)
                        #print('The temp is', tempData)
            celsius = float(tempData) / 1000
            farenheit = (celsius * 1.8) + 32
            print('sensor: ',d)
            print('celsius: ',celsius)
            print('farenheit: ',farenheit)
            print('\n')
    time.sleep(15)            
        
                
            
            
            
    
    


#   /sys/bus/w1/devices/28-01191f1acd16 

#  98 01 4b 46 7f ff 0c 10 19 : crc=19 YES
#  98 01 4b 46 7f ff 0c 10 19 t=25500
