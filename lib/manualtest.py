import requests,time,os
from subprocess import call
import pexpect


from ping3 import ping, verbose_ping
class ManualTest:
    def __init__(self):
        self._download_speed_list = []
        self._upload_speed_list = []
        self._ping_list = []
        if 'LATCS7_USERNAME' in os.environ and 'LATCS7_PASSWORD' in os.environ:
            self.latcs7_pass = os.environ['LATCS7_PASSWORD']
            self.latcs7_username = os.environ['LATCS7_USERNAME']
            self.server = 'latcs7.cs.latrobe.edu.au'

    def ping_once(self, packet_size = 56):
        result = ping(self.server, size = packet_size)
        return round(result,5)/0.001
    def ping(self, N = 10):
        for i in range(N):
            self._ping_list.append(self.ping_once())
        avg = sum(self._ping_list)/len(self._ping_list)
        return avg
    def download_once(self, filesize):
        url = f"http://{self.server}/20163715/{filesize}MB.speedtest"
        MB_SIZE = 1024*1024*8 # 1 megabyte in bits
        time_pre_connection = time.time()
        r = requests.get(url)
        time_post_connection = time.time()
        download_speed = round((MB_SIZE*filesize*0.001*0.001)/ (time_post_connection-time_pre_connection), 3)
        return download_speed

    def download(self, filesize = 5, N= 10):
        self._download_speed_list = []
        for i in range(N):
            self._download_speed_list.append(self.download_once(filesize))
        avg = sum(self._download_speed_list)/N
        return round(avg,3)
    def upload(self, filesize = 5, N= 10):
        self._upload_speed_list = []
        for i in range(N):
            self._upload_speed_list.append(self.upload_once(filesize))
        avg = sum(self._upload_speed_list)/N
        return round(avg,3)
    def upload_once(self, filesize = 5):
        MB_SIZE = 1024*1024*8 # 1 megabyte in bits
        host = "latcs7.cs.latrobe.edu.au"
        port = 22
        password = self.latcs7_pass
        username = self.latcs7_username
        path = f"/home/mcswk/20163715/public_html/uploads/{filesize}MB.speedtest"
        localpath = os.getcwd()+f"/{filesize}MB.speedtest"
        time_pre_connection = time.time()
        cmd_str = f"curl --insecure --user {self.latcs7_username}:{self.latcs7_pass} -T \"{localpath}\" sftp://{host}{path}"
        # print(cmd_str)
        pexpect.run(cmd_str)
        time_post_connection = time.time()
        # print(time_post_connection-time_pre_connection)
        upload_speed = round((MB_SIZE*filesize*0.001*0.001) / (time_post_connection-time_pre_connection), 3)
        return upload_speed
