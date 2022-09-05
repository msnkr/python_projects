# /usr/bin/vcgencmd measure_temp
import os 

temp = os.system('/usr/bin/vcgencmd measure_temp')
print(temp)