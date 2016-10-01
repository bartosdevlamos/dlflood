import urllib2
from time import sleep
import argparse
import threading
import sys
import os
import datetime
import warnings
warnings.filterwarnings("ignore")

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

ap = argparse.ArgumentParser()
ap.add_argument("URL", nargs='?', default="")
ap.add_argument("threads", type=int, nargs='?', default="")

a = ap.parse_args()
thr = ap.parse_args()


cls()
def dostread(num):
    start = datetime.datetime.now()
    u = urllib2.urlopen(a.URL)
    end = datetime.datetime.now()
    diff = end - start
    cls()
    print "ping:", int(round(diff.microseconds / 1000))    
    meta = u.info()
    file_size = int(meta.getheaders("Content-Length")[0])
    file_size_dl = 0
    block_sz = 1
    
    print "polling file:" + str(a.URL) 
    print "using threads:" + str(thr.threads)
    print "current threads active", threading.activeCount()
    while True:
        buffer = u.read(block_sz)
        sleep(99999)
threads = []
for i in range(thr.threads):
    t = threading.Thread(target=dostread, args=(i,))
    t.start()
