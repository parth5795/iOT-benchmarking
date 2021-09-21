

# iOT-benchmarking
IoT Benchmarking of La trobe Campus WiFi Speeds using Raspberry Pi 4

## Non-docker installation and single time run:
- `pip install -r requirements.txt`
- `python ./speedtest.py`

## Class methods
|Method| return | parameters  | comments |
|--|--|--|---|
| Speedtesting Constructor |  |  custom | True will connect to latcs7. False will connect to speedtest.net servers |
| test_upload_download| dictionary (network performance) |  export | True/False of exporting results to a results.json file |
| push_to_thingspeak| string (response)  |  results_dictionary | dictionary of results returned from test_upload_download to be parsed and appended to thingspeak REST API|

## Examples

  - check main_speetest.py for speedtest.net example

  - check main_latcs7.py for latcs7 example
