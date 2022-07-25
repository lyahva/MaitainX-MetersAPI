import http.client
import json
from time import sleep
import os
def screen_clear():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')    

m_id: list[int] = ("Enter your list of Meter ID's without quotes ####, ####, ####")
for c_id in m_id:
  screen_clear()  
  print(c_id)
  meterID = c_id
  rVal = int(input("enter reading value: "))
  urla = '/v1/meters/'
  urlb = '/readings'
  urlx = urla + str(meterID) + urlb
  conn = http.client.HTTPSConnection("api.getmaintainx.com")
  payload = json.dumps({
    "readingValue": rVal
  })
  headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer "enter your API Key from MaintainX here without quotes"'
  }
  conn.request("POST", urlx, payload, headers)
  res = conn.getresponse()
  data = res.read()
  print(data.decode("utf-8"))
  sleep(2)

  #print(urlx,)
  #print(c_id, rVal, '\n')