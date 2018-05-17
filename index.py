from datetime import datetime
from sys import platform
print(platform)
odds = [1,3,5,7,9,10]
right_this_minute = datetime.today().minute

if right_this_minute  in odds:
    print('This minute ...');
else :
    print('NO ..')