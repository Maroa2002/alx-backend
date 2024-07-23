#!/usr/bin/env python3
""" Basic Cache """

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ caching system """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Add the item value for the specific key to the cache"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item for the key from the cache"""
        if key and key in self.cache_data:
            return self.cache_data.get(key)
        return None
