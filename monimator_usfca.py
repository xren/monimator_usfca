import threading
import sys
import os
import base64
import httplib
import urllib 
import time
import optparse
from datetime import datetime

# https://www.cs.usfca.edu/~afedosov/labmon/index.cgi?s=umon
url = '/~afedosov/labmon/index.cgi?s='
ending_time = datetime(2012,1,16,12,05,00)

parser = optparse.OptionParser()
parser.add_option('-i','--fetch_interval',dest='fetch_interval',default=1)
parser.add_option('-u','--username',dest='username')
parser.add_option('-p','--password',dest='password')
parser.add_option('-f','--first_slot',dest='first_slot')
parser.add_option('-s','--second_slot',dest='second_slot')
parser.add_option('-d','--debug',dest='debug',default='f')

options, args = parser.parse_args()

if not options.fetch_interval:
    parser.error('-i fetch_interval required')
if not options.username:
    parser.error('-u username required')
if not options.password:
    parser.error('-p password required')
if not options.first_slot:
    parser.error('-f first_slot required')
    
if options.debug == 't':
    debug = True
elif options.debug == 'f':
    debug = False

class monimator(threading.Thread):
    def __init__(self,username,password,fetch_interval,slot):
        self.countdown = fetch_interval
        self.auth_header = self.getAuth(username,password)
        self.slot = slot
        threading.Thread.__init__(self)
        
    def run(self):
        while 1:
            if datetime.now() > ending_time:
                print 'Times up, sign up finished'
                break
            self.sendSignupRequest(self.auth_header,url,self.slot)
            time.sleep(float(self.countdown))
            

    def getAuth(self,username,password):
        b64up = base64.b64encode('%s:%s' % (username,password))
        header = {}
        header['Authorization'] = 'Basic %s' % b64up
    
        return header
    
    def sendSignupRequest(self,auth,url,slot):
        request_url = url + str(self.slot)
        
        if debug:
            print 'auth: %s, url: %s, slot: %s' % (auth, url, slot)
            print 'url: ' + request_url
            print 'building connection..'
            
        connection = httplib.HTTPSConnection('www.cs.usfca.edu:443')
    
        try:
            connection.request('GET',request_url,headers = auth)
            response = connection.getresponse()
            result = response.read()
            if 'It%20is%20not%20time%20to%20apply%20yet' in result:
                print 'its not the time yet'
                if debug:
                    print result
            else:
                print '*******************'
                print 'sign up succeed for' + self.timeslot
                print '*******************'
                print result
        except Exception,e:
            print 'connection failed'
            if debug:
                print e
    
thread1 = monimator(options.username,options.password,options.fetch_interval,options.first_slot)
thread1.start()
if options.second_slot:
    thread2 = monimator(options.username,options.password,options.fetch_interval,options.second_slot)
    thread2.start()
