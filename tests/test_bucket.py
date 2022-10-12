"""Test for the bucket module."""

import datetime
import os

from src.bucket import Bucket

TEST_BUCKET_FILE = 'test_bucket.csv'


class TestBucket(object):
    @classmethod
    def teardown_class(cls):
        bucket = Bucket(bucket_file=TEST_BUCKET_FILE)
        os.remove(os.path.join(os.path.expanduser('~'), bucket.bucket_dir, TEST_BUCKET_FILE))

    def test_add(self):
        bucket = Bucket(bucket_file=TEST_BUCKET_FILE)
        bucket.add('item')
        assert bucket.bucket[0].item == 'item'

    def test_date_created(self):
        bucket = Bucket(bucket_file=TEST_BUCKET_FILE)
        bucket.add('item')
        assert bucket.bucket[0].date_created is not None
        assert bucket.bucket[0].date_created.year == datetime.datetime.now().year

    def test_remove(self):
        bucket = Bucket(bucket_file=TEST_BUCKET_FILE)
        bucket.add('item')
        bucket.remove('item')
        assert bucket.bucket == []

    def test_save(self):
        bucket = Bucket(bucket_file=TEST_BUCKET_FILE)
        bucket.add('item')
        bucket.save()
        with open(os.path.join(os.path.expanduser('~'), bucket.bucket_dir, TEST_BUCKET_FILE), 'r') as f:
            assert 'item' in f.read()

    def test_read(self):
        bucket = Bucket(bucket_file=TEST_BUCKET_FILE)
        bucket.add('item')
        bucket.save()
        bucket_df = bucket.read()
        assert bucket_df['item'][0] == 'item'
