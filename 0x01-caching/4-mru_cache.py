#!/usr/bin/env python3
""" Caching System """

from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ MRU cache policy """
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
                most_recent_key = next(reversed(self.cache_data))
                self.cache_data.pop(most_recent_key)
                print(f"DISCARD: {most_recent_key}")

    def get(self, key):
        """Retrieve an item for the key from the cache"""
        if key in self.cache_data:
            # Move key to end to mark it as most recently used
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None
