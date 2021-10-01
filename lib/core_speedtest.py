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


class Speedtesting:
  def __init__(self):
      self.speed_test = speedtest.Speedtest()
      self.speed_test.get_servers()
      self.speed_test.get_best_server()
      self.api_key = 'MSYZ8L99JXGS7CUW'
      self.latcs7_test = ManualTest()
      self.device_id = os.environ['DEVICE_ID']



  #TODO to be implemented later
  def push_to_thingspeak(self, results_dictionary, custom = False):
    _json = json.dumps(results_dictionary, indent = 4)
    locations = {True:"Latcs7", False:"Speedtest.net"}
    print(f"pushing data from {locations[custom]}")
    print(f"data: {results_dictionary}")
    url_str = f"https://api.thingspeak.com/update?api_key={self.api_key}&field1={results_dictionary['upload']}&field2={results_dictionary['download']}&field3={self.device_id}&field4={locations[custom]}"
    print(url_str)
    response = requests.get(url_str)
    return response

  def test_speedtest_net(self, export = False):
    self.speed_test.download()
    self.speed_test.upload()
    res = self.speed_test.results.dict()
    res["upload"] = res["upload"]*0.001*0.001
    res["download"] = res["download"]*0.001*0.001
    if export:
      with open('results.json', 'w') as fp:
          json.dump(res, fp)
    return res

  def test_latcs7(self):
      download = self.latcs7_test.download(filesize = 5)
      upload = self.latcs7_test.upload(filesize = 5)
      #TODO add ping
      results = {"download": download, "upload":upload }
      return results
  def test_all(self):
      st_result = self.test_speedtest_net()
      response1 = self.push_to_thingspeak(st_result)
      lc_result = self.test_latcs7()
      response2 = self.push_to_thingspeak(lc_result, custom = True)
      return response1,response2
