import boto3
import os
import shutil

from datapackage_pipelines.lib.dump.dumper_base import CSVDumper

class AWSDumper(CSVDumper):

    def initialize(self, params):
        super(AWSDumper, self).initialize(params)
        self.out_path = params.get('out-path', '.')
        self.bucket = params.get('bucket')
        self.s3 = boto3.resource('s3')

    def write_file_to_output(self, filename, path):
        path = os.path.join(self.out_path, path)
        self.s3.meta.client.upload_file(filename, self.bucket, path)

    @staticmethod
    def __makedirs(path):
        if not os.path.exists(path):
            os.makedirs(path)


AWSDumper()()
