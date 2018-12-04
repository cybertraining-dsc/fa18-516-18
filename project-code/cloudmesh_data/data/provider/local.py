from cloudmesh_data.data.provider.DataProvider import DataProvider
import os
import shutil
from os import listdir
from os.path import isfile, join


class LocalProvider(DataProvider):

    name = "local"

    def __init__(self, cloud=None):
        if cloud is None:
            self.cloud = "local"
        else:
            self.cloud = cloud

    def authenticate(self, config):
        pass

    def delete(self, filename):
        os.remove(filename)

    def copy(self, source, destination):
        shutil.copyfile(source, destination)

    def move(self, source, destination):
        os.rename(source, destination)

    def download(self, source):
        pass

    def upload(self, source):
        pass

    def list(self, path):
        files = [f for f in listdir(path) if isfile(join(path, f))]
        return files

    def authenticate(self, credentials):
        pass
