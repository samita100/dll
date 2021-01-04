import requests
import json


website = "https://onlineedlreg.dootm.gov.np/dlNewRegHome"
url = 'https://hooks.slack.com/services/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'
headers = {'content-type': 'application/json'}

try:
  try:
    page = requests.get(website, verify=False)
  except:
    print("Request to server failed")
  
  if page.status_code == 200:
    myobj = {"text":"<@U01HTKXTWBF>, UP :)"}
    x1 = requests.post(url, data=json.dumps(myobj), headers=headers)
    print("Website opened")
    print(x1.text)
  
  else:
    print("Another status code")
    myobj2 = {"text":f'Another SC:- {page.status_code}'}
    x2 = requests.post(url, data=json.dumps(myobj2), headers=headers)
    print(x2.text)
  
  
except:
  print("Unable to open the website")
  myobj3 = {"text":"DOWN :("}
  x3 = requests.post(url, data=json.dumps(myobj3), headers=headers)
  print(x3.text)
