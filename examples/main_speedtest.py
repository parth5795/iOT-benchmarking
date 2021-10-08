"""**Speedtest.net Usage Example:**"""
from core_speedtest import *
st = Speedtesting(custom = False)
for i in range(1,1000):
    print(f'Speed Test Iteration #{i}')
    result = st.test_upload_download(export = True)
    st.push_to_thingspeak(result)


 
