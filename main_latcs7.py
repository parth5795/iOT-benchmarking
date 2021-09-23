from core_speedtest import *

"""**custom speed test Usage Example:**"""

st = Speedtesting(custom = True)
for i in range(1,1000):
    print(f'Speed Test Iteration #{i}')
    speed = st.custom_upload_test()
    print(speed, 'Mbps')
