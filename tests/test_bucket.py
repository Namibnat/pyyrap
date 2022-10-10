"""Test for the bucket module."""

from src.bucket import Bucket


class TestBucket(object):
    def test_add(self):
        bucket = Bucket()
        bucket.add('item')
        assert bucket.bucket[0].item == 'item'

    def test_remove(self):
        bucket = Bucket()
        bucket.add('item')
        bucket.remove('item')
        assert bucket.bucket == []
