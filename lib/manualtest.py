import requests,time,paramiko,os

class ManualTest:
    def __init__(self):
        self._download_speed_list = []
        self._upload_speed_list = []
        self.latcs7_pass = os.environ['LATCS7_PASSWORD']
        self.latcs7_username = os.environ['LATCS7_USERNAME']


    def download_once(self, filesize):
        MB_SIZE = 1024000
        url = f"http://homepage.cs.latrobe.edu.au/20163715/{filesize}MB.txt"
        time_pre_connection = time.time()
        r = requests.get(url)
        time_post_connection = time.time()

        download_speed = round((MB_SIZE*filesize*0.001*0.001) / (time_post_connection-time_pre_connection), 3)
        return download_speed

    def download(self, filesize = 5, N= 10):
        for i in range(N):
            self._download_speed_list.append(self.download_once(filesize))
        avg = sum(self._download_speed_list)/len(self._download_speed_list)
        return avg
    def upload(self, filesize = 5, N= 10):
        for i in range(N):
            self._upload_speed_list.append(self.upload_once(filesize))
        avg = sum(self._upload_speed_list)/len(self._upload_speed_list)
        return avg
    def upload_once(self, filesize = 5):
        MB_SIZE = 1024000
        host = "latcs7.cs.latrobe.edu.au"
        port = 22
        password = self.latcs7_pass
        username = self.latcs7_username

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port, username, password)

        sftp = ssh.open_sftp()

        path = "/home/mcswk/20163715/public_html/uploads/5MB.txt"
        localpath = os.getcwd()+"/5MB.txt"
        time_pre_connection = time.time()
        sftp.put(localpath, path)
        time_post_connection = time.time()

        sftp.close()
        ssh.close()
        upload_speed = round((MB_SIZE*filesize*0.001*0.001) / (time_post_connection-time_pre_connection), 3)
        return upload_speed
