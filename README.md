

# iOT-benchmarking
IoT Benchmarking of La trobe Campus WiFi Speeds using Raspberry Pi 4



## Usage
### Manual
  - `pip install -r requirements.txt`
  - `export LATCS7_USERNAME=MY_LATCS7_USERNAME`
  - `export LATCS7_PASSWORD=MY_PASS_WORD`
  - `export DEVICE_ID=1`
  - `python3 start.py`
### docker
  - update Dockerfile with LATCS7_PASSWORD, LATCS7_USERNAME and DEVICE_ID values
  - `docker build . -t speedtester`
  - `docker run -it speedtester`

# Example

      st = Speedtesting()
	    while 1:
  	     responses = st.test_all()
  	     print(responses)
  	     time.sleep(15) # every 15 seconds
