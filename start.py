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

st = Speedtesting()
while 1:
    try:
        st.test_all()
    except:
        print("Some error is happening. Are you sure you are in the right network?")

    print(f"sleeping for {int(sleep_inteval/MINUTE)} minutes")
    time.sleep(sleep_inteval) # 15 seconds
