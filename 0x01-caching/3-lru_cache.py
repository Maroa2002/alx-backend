#!/usr/bin/env python3
""" Caching System """

from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRU cache policy """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add item to cache"""
        if key and item:
            if key in self.cache_data:
                self.cache_data.move_to_end(key)
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                oldest_key = next(iter(self.cache_data))
                self.cache_data.pop(oldest_key)
                print(f"DISCARD: {oldest_key}")

    def get(self, key):
        """Retrieve an item for the key from the cache"""
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None
