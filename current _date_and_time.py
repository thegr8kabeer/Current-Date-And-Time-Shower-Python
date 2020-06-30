# A simple python project made by Thegr8kabeer to display the current date and time
# Easy to understand syntax for the person who knows the basics of Python by using the built-in Pyhton modules time and datetime
# Feel free to edit my code and do some experiments!!!
# Don't forget to follow me on instagram at https://instagram.com/thegr8kabeer/

import time,datetime
epochseconds = time.time()
print(epochseconds)

t = time.ctime(epochseconds)
print(t)

dt = datetime.datetime.today()
print('Current Date: {}/{}/{}'.format(dt.day,dt.month,dt.year))
print('Current Time: {}:{}:{}'.format(dt.hour,dt.minute,dt.second))
