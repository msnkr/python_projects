#!usr/bin/python

import os

output = os.system('/usr/bin/powerprofilesctl get')

print(output)
# if output == 'balanced':
#     print('')
# elif output == 'power saver':
#     print('')
# elif output == 'performance':
#     print('')