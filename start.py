from lib.core_speedtest import *
import argparse
import time
parser = argparse.ArgumentParser(description='iotApp')
parser.add_argument('--sleep_minutes', required=False, help='Interval of speedtesting in minutes')
args = parser.parse_args()

MINUTE = 60
sleep_inteval = 15 * MINUTE
if args.sleep_minutes:
    sleep_inteval = int(args.sleep_minutes)  * MINUTE
file = open('5MB.speedtest', 'wb')
file.write(b"h"*(1024*1024*5))
file.close()
while 1:
    st = None
    st = Speedtesting()

    try:
        st.test_all()
    except  Exception as e:
        print("Some error is happening. Are you sure you are in the right network?")
        print(str(e))

    print(f"sleeping for {int(sleep_inteval/MINUTE)} minutes")
    time.sleep(sleep_inteval) # 15 seconds
