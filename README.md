

# iOT-benchmarking
IoT Benchmarking of La trobe Campus WiFi Speeds using Raspberry Pi 4

## Non-docker installation and single time run:
- `pip install -r requirements.txt`
- `python ./speedtest.py`


## Usage
  - export LATCS7_PASSWORD=MY_PASS_WORD
  - export DEVICE_ID=1
  - python3 start.py

#Example

      st = Speedtesting()
	    while 1:
	      speed = st.test_all()
	      print(speed, 'Mbps')
	      time.sleep(15) # every 15 seconds
