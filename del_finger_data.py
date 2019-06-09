#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
'''laxz'''
"""
from pyfingerprint.pyfingerprint import PyFingerprint
import time
from sys import exit

## Deletes a finger from sensor

try:
    f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

    if ( f.verifyPassword() == False ):
        raise ValueError('The given fingerprint sensor password is wrong!')

except Exception as e:
    print('The fingerprint sensor could not be initialized!')
    print('Exception message: ' + str(e))
    exit(1)

used = f.getTemplateCount() #0,1,2,3 = 4
print('Currently used templates: ' + str(used) +'/'+ str(f.getStorageCapacity()))


try:
    print("Fingerprints deleting in 6 sec...")
    time.sleep(6)
    for i in range(len(used)):
        if(f.deleteTemplate(i) == True):
            print("Template deleted from position {0}".format(i))
        else:
            print("Internal Error")

except KeyboardInterrupt:
    print("-fingerprint delete- operation cancled")
    exit(0)

except Exception as e:
    print(str(e))
    print('Operation failed!')
    exit(1)

exit(0)
