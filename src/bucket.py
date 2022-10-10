"""Collect new ideas that could be projects or things to do."""

import datetime
from collections import namedtuple
import os

import pandas as pd


class Bucket:
    def __init__(self, bucket_dir='.yrap', bucket_file='bucket.csv', delimiter='|', logging=True):
        self.bucket = []
        self.item = namedtuple('Bucket', ['date_created', 'item'])
        self.bucket_dir = bucket_dir
        self.bucket_file = bucket_file
        self.delimiter = delimiter
        self.logging = logging
        self.home_directory = os.path.expanduser('~')
        self.bucket_path = os.path.join(self.home_directory, self.bucket_dir, self.bucket_file)

    def create_bucket_file(self):
        if not os.path.exists(self.bucket_path):
            os.makedirs(os.path.dirname(self.bucket_path), exist_ok=True)
            with open(self.bucket_path, 'w') as f:
                f.write('')

    def add(self, item):
        self.bucket.append(self.item(date_created=datetime.datetime.now(), item=item))

    def remove(self, item):
        for i in self.bucket:
            if i.item == item:
                self.bucket.remove(i)
            break

    def read(self):
        """Read the bucket from a csv file"""
        bucket_df = pd.read_csv(self.bucket_path, delimiter=self.delimiter)

    def save(self):
        """Save the bucket to a csv file

        Bucket items are saved with the date they were created.
        """
        pass
