#!usr/bin/python

import os

output = os.system('/usr/bin/powerprofilesctl get')

print(output)

#if output == 'balanced':
#     print('Hi, Balanced')
#elif output == 'power-saver':
#     print('Hi, Power Saver')
#elif output == 'performance':
#     print('Hi, Performace')
