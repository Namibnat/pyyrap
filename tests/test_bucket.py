"""Test for the bucket module."""

from src.bucket import Bucket


class TestBucket(object):
    def test_add(self):
        bucket = Bucket()
        bucket.add('item')
        assert bucket.bucket == ['item']
