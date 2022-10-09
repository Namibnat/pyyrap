"""Collect new ideas that could be projects or things to do."""


class Bucket:
    def __init__(self, bucket_dir='.bucket', bucket_file='bucket.csv', delimiter='|', logging=True):
        self.bucket = []

    def add(self, item):
        self.bucket.append(item)
