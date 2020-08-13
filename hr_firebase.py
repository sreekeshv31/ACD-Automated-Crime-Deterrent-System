from serial import *
import time
import requests
import simplejson as json
 
firebase_url = 'https://pulse-rate-aac0d.firebaseio.com' #Url for the Firebase database
 

ser = Serial("/dev/ttyACM0", 9600, timeout=0) #Port from which data is obtained 
 

fixed_interval = 10
 
while 1:
 try:
     hr_pulse = ser.readline() #Heart Rate Values 
     hr_pulse = hr_pulse.decode('utf-8')
     
     time_hhmmss = time.strftime('%H:%M:%S') #Time
     date_mmddyyyy = time.strftime('%d/%m/%Y') #Date
      
     print (hr_pulse) #Printing the values of HR reading
    
     data = {'date':date_mmddyyyy,'time':time_hhmmss,'value':hr_pulse.rstrip()} #Date values
    
     data1 = json.dumps(data)
     result = requests.post(firebase_url + '/' + 'pulse' + '/Data.json', data=data1) #post method to send data to firebase database
     
     print ('Record inserted. Result Code = ' + str(result.status_code) + ',' + result.text) #Status Code of Operation
     time.sleep(fixed_interval)
 except IOError:
     print('Error! Something went wrong.')
     time.sleep(fixed_interval)
