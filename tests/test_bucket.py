"""Test for the bucket module."""

import datetime

from src.bucket import Bucket


class TestBucket(object):
    def test_add(self):
        bucket = Bucket()
        bucket.add('item')
        assert bucket.bucket[0].item == 'item'

    def test_date_created(self):
        bucket = Bucket()
        bucket.add('item')
        assert bucket.bucket[0].date_created is not None
        assert bucket.bucket[0].date_created.year == datetime.datetime.now().year

    def test_remove(self):
        bucket = Bucket()
        bucket.add('item')
        bucket.remove('item')
        assert bucket.bucket == []
