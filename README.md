

# iOT-benchmarking
IoT Benchmarking of La trobe Campus WiFi Speeds using Raspberry Pi 4

## Running docker container on Raspberry Pi
  - `docker run --privileged -d --name cronspeed sudipta20449667/pythondocker:latest`
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
# Example

      st = Speedtesting()
	    while 1:
  	     st.test_all()
  	     time.sleep(15) # every 15 seconds
