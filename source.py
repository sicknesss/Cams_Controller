# from typing import re

import rtsp as r
import time
import requests as rq

print('Input web controller IP\n')
web_address = input()
print('Input presentation shortcut number\n')
input_number = input()
presentation_address = 'http://' + web_address + '/api/?Function=Cut&Input=' + input_number
return_to_address = 'http://' + web_address + '/api/?Function=Cut&Input=0'

while 1:
    case = int(input())
    if case == 1:
        print(rq.get(presentation_address))
        time.sleep(5)
        print(rq.get(return_to_address))
    else:
        break
