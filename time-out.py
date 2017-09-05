import webbrowser
import time
from time import sleep
i=0
while(i<3):
    i=i+1
    sleep(1); webbrowser.open('goo.gl/bhoikQ', new=2);
    sleep(1); print("Chillax it's your %d break " "and time is " %i +time.ctime())
