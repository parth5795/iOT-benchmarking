


# iOT-benchmarking
IoT Benchmarking of La trobe Campus WiFi Speeds using Raspberry Pi 4

## Running docker container on Raspberry Pi
  - `docker run --privileged -d --name cronspeed --restart unless-stopped sudipta20449667/pythondocker:latest`
  - `crontab -e`
    - Add `* * * * * /home/pi/cron.sh >> /home/pi/speedtests.log` add the very bottom to check for updates every minute

## Building the code
### Manual
  - `pip install -r requirements.txt`
  - `export LATCS7_USERNAME=MY_LATCS7_USERNAME`
  - `export LATCS7_PASSWORD=MY_PASS_WORD`
  - `export DEVICE_ID=1`
  - `python3 start.py --sleep_minutes 15`
    - --sleep_minutes is optional
### deployment
  - Create a branch for your code
  - `git checkout -b arm32v7 myFeatureBranch`
  - push your work to your branch
  - merge with arm32v7
  - the updated container will run automatically on Raspberry pi after github workflow finished successfully by roughly a minute

# Speedtesing Class

## Methods

|Method	| return | parameters |
|--|--|--|
| Constructor | Speedtesting | - |
|get_device_id: Getting the serial number of a raspberry pi 4|id:string|-|
|test_speedtest_net: Getting metrincs measured with speedtest.net servers|metrics:dict of keys 'upload','download','ping'|-|
|test_latcs7: Getting download/upload/ping speed with latcs7 server|metrics:dict of keys 'upload','download','ping'|-|
| decode_dictionary: Format the values in the metrics dictionary into a readable string for debugging | readableText: str | metrics:dict|
| push_to_thingspeak : pushing metrics captured from any source to thingspeak channel | void | metrics:dict |
| test_all : A wrapper method that call | void | - |

## dependencies
### speedtest-cli
### pexpect
### requests
### ping3
### ManualTest class
Custom server testing was separated to a file to separate changes in code functionality.
|Method	| return | parameters |
|--|--|--|
| Constructor | ManualTest | - |
| ping_once: pings the custom server once | time in milliseconds: double | packet_size:int (optional) default is 56 |
| ping: calls the function ping_once N times (default is 10) | average_time_in_milliseconds: double |  N:int (optional) default is 10 |
| download_once: measures download speed once | speed: double |  filesize:int unit is Mb. For example 1 for 1Mb |
| download: calls the function download_once N times (default is 10) | average_speed: double |  N:int (optional) default is 10 |
| upload_once: measures upload speed once | speed: double |  filesize:int unit is Mb. For example 1 for 1Mb |
| upload: calls the function upload N times (default is 10) | average_speed: double |  N:int (optional) default is 10 |


# Out of the box usage example

      st = Speedtesting()
	    while 1:
  	     st.test_all()
  	     time.sleep(15) # every 15 seconds
