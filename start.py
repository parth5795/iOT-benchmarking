from lib.core_speedtest import *


st = Speedtesting()
while 1:
    responses = st.test_all()
    print(responses)
    time.sleep(15) # 15 seconds
