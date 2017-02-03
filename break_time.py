import time
import webbrowser
'''
time and webbrowser is in pyhton standard libaray
python std lib : https://docs.python.org/2/library/
'''

count = 0
LOOP_NUM = 3
while count < LOOP_NUM:
    time.sleep(3)
    print 'This is the {0} time'.format(count+1)
    #webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
    count = count + 1

def toHours(seconds):
    return seconds / 60 / 60

def toSeconds(hours):
    return hours * 60 * 60

