#!/usr/bin/env python3
""" Caching System """

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO cache policy """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Add item to cache"""
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key not in self.cache_data:
                    # Get the first key
                    first_key = next(iter(self.cache_data))
                    self.cache_data.pop(first_key)
                    print(f"DISCARD: {first_key}")
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item for the key from the cache"""
        return self.cache_data.get(key) if key else None
