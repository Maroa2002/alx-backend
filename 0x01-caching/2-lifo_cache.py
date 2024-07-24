#!/usr/bin/env python3
""" Caching System """

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO cache policy """
    def __init__(self):
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """Add item to cache"""
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key not in self.cache_data:
                    if self.last_key:
                        self.cache_data.pop(self.last_key)
                        print(f"DISCARD: {self.last_key}")
            self.cache_data[key] = item
            self.last_key = key

    def get(self, key):
        """Retrieve an item for the key from the cache"""
        return self.cache_data.get(key) if key else None
