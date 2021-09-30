from lib.core_speedtest import *


st = Speedtesting()
while 1:
    speed = st.test_all()
    print(speed, 'Mbps')
    time.sleep(15) # 15 seconds
