from lib.core_speedtest import *
import argparse

parser = argparse.ArgumentParser(description='iotApp')
parser.add_argument('--sleep_minutes', required=True, help='Interval of speedtesting in minutes')
args = parser.parse_args()

MINUTE = 60
sleep_inteval = 15 * MINUTE
if args.sleep_minutes:
    sleep_inteval = int(args.sleep_minutes)  * MINUTE

st = Speedtesting()
while 1:
    responses = st.test_all()
    print(responses)
    time.sleep(sleep_inteval) # 15 seconds
