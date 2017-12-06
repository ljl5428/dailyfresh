from django.core.files.storage import Storage
from django.conf import settings
from fdfs_client.client import Fdfs_client

class FDFSStorage(Storage):
    def __init__(self, client_conf=None, nginx_url=None):
        if client_conf is None:
            client_conf = settings.FDFS_CLIENT_CONF
        self.client_conf = client_conf
        if nginx_url is None:
            nginx_url = settings.FDFS_NGINX_URL
        self.nginx_url = nginx_url

    def _open(self, name, mode='rb'):
        pass


    def _save(self, name, content):
        client = Fdfs_client(self.client_conf)

        content = content.read()

        res = client.upload_by_buffer(content)

        if res['Status'] != 'Upload successed.':
            raise Exception('上传文件到fdfs失败')

        file_id = res['Remote file_id']

        return file_id


    def exists(self, name):
        return False

    def url(self, name):
        return self.nginx_url + name
