"""Collect new ideas that could be projects or things to do."""

import os


class Bucket:
    def __init__(self, bucket_dir='.yrap', bucket_file='bucket.csv', delimiter='|', logging=True):
        self.bucket = []
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
        self.bucket.append(item)

    def remove(self, item):
        self.bucket.remove(item)
