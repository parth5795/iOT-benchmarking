"""**Speedtest.net Usage Example:**"""
import core_speedtest
st = Speedtesting(custom = False)
for i in range(1,1000):
    print(f'Speed Test Iteration #{i}')
    result = st.test_upload_download(export = True)
    st.push_to_thingspeak(result)
