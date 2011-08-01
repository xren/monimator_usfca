import threading
import sys
import os
import base64
import httplib
import urllib 

url = '/~afedosov/labmon/index.cgi?s='
# https://www.cs.usfca.edu/~afedosov/labmon/index.cgi?s=umon

class labmonSignup(threading.Thread):
    def __init__(self,countdown):
        self.countdown = countdown
        threading.Thread.__init__(self)
        
    def run(self):
        while 1:
            time.sleep(self.countdown)
            
            

def getAuth(username,password):
    print 'building authentication info...'
    b64up = base64.b64encode('%s:%s' % (username,password))
    header = {}
    header['Authorization'] = 'Basic %s' % b64up
    
    return header
    
def sendSignupRequest(auth,url,slots):
    print 'auth: %s, url: %s, slot: %s' % (auth, url, slots)
    requests = []
    for slot in slots:
        requests.append(url + str(slot))
        print url + slot
    
    print 'building connection..'
    connection = httplib.HTTPSConnection('www.cs.usfca.edu:443')
    
    try:
        for request in requests:
            print request
            connection.request('GET',request,headers = auth)
            response = connection.getresponse()
            if response.status != 200:
                print 'sign up failed'
            else:
                print 'sign up succeed for' + request
                            
    except Exception,e:
        print e
    
def help():
    print 'here shows the helper'
    
    
def main():
    av = sys.argv
    
    if len(av) <= 1:
        help()
        sys.exit(1)
    
    username = av[1]
    password = av[2]

    print len(av)
    slots = []
    slots.append(av[3])
    slots.append(av[4])
    
    auth = getAuth(username,password)
    sendSignupRequest(auth,url,slots)
    
    
if __name__ == '__main__':
    main()