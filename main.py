import urllib.request
from notify_run import Notify 

notify = Notify() 


try:
  urllib.request.urlopen("https://onlineedlreg.dotm.gov.np/dlNewRegHome").getcode()
  notify.send('UP :)')
except:
  print("Unable to open the website")
  notify.send('DOWN :(')
   
