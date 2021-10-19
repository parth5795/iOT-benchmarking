# -*- coding: utf-8 -*-
"""speedtest.ipynb

# CSE5IDP Speedtest

**Downloading python package**

If you run it on your computer, you need to write the following command without the '!' before the pip command


You would need to execute the following command in your python enviornment/virtual enviornment:
```
pip install speedtest-cli
```

**GoogleColab-specific command:**
!pip install speedtest-cli

"""


"""**Speedtesting class**

Speedtesting class is designed to be scalable to do speedtest.net task and the custom speedtest task.
"""

import speedtest
from .manualtest import ManualTest
import json
import requests
import sys, time, os
import subprocess

class Speedtesting:
  def __init__(self):
      self.speed_test = speedtest.Speedtest()
      self.speed_test.get_servers()
      self.speed_test.get_best_server()
      self.api_key = 'MSYZ8L99JXGS7CUW'
      self.latcs7_test = ManualTest()
      self.device_id = self.get_device_id()
      print(f"DEVICE_ID {self.device_id}")



# will only work on Raspberry pi
  def get_device_id(self):
      # Extract serial from cpuinfo file
      cpuserial = "0000000000000000"
      try:
        f = open('/proc/cpuinfo','r')
        for line in f:
          if line[0:6]=='Serial':
            cpuserial = line[10:26]
        f.close()
      except:
        cpuserial = "ERROR000000000"

      return cpuserial
  #TODO to be implemented later
  def push_to_thingspeak(self, results_dictionary, custom = False):
    _json = json.dumps(results_dictionary, indent = 4)
    locations = {True:"Latcs7", False:"Speedtest.net"}
    url_str = f"https://api.thingspeak.com/update?api_key={self.api_key}&field1={results_dictionary['upload']}&field2={results_dictionary['download']}&field3={results_dictionary['ping']}&field4={self.device_id}&field5={locations[custom]}"
    # print(url_str)
    response = requests.get(url_str)
    return response

  def test_speedtest_net(self, export = False):
    self.speed_test.download()
    self.speed_test.upload()
    res = self.speed_test.results.dict()
    ret = {}
    ret["upload"] = res["upload"]*0.001*0.001
    ret["download"] = res["download"]*0.001*0.001
    ret["ping"] = res["ping"]

    if export:
      with open('results.json', 'w') as fp:
          json.dump(ret, fp)
    return ret

  def test_latcs7(self):
      ping = self.latcs7_test.ping()
      download = self.latcs7_test.download(filesize = 5)
      upload = self.latcs7_test.upload(filesize = 5)
      #TODO add ping
      results = {"download": download, "upload":upload, "ping": ping }
      return results
  def decode_dictionary(self,dict, debug=False):
      decoded = f"ping: {dict['ping']}, download: {dict['download']}, upload: {dict['upload']}"
      if print:
          print(decoded)
      return decoded

  def test_all(self):
      print("Checking Speedtest.net...")
      st_result = self.test_speedtest_net()
      self.decode_dictionary(st_result, debug = True)
      print("Pushing to Thingspeak...")
      response1 = self.push_to_thingspeak(st_result)
      print("Checking Latcs7 server...")
      if 'LATCS7_USERNAME' not in os.environ or 'LATCS7_PASSWORD' not in os.environ:
          print("Not latcs7 credentials found in env variables")
          return
      lc_result = self.test_latcs7()
      self.decode_dictionary(lc_result, debug = True)
      print("Pushing to Thingspeak...")
      response2 = self.push_to_thingspeak(lc_result, custom = True)
