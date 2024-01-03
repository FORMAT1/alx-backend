#!/usr/bin/env python3
"""caching system
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """An object that allows storing and 
    retrieving items from a dcitionary.
    """
    def put(self, key, item):
        """To add an item in the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item by key.
        """
        return self.cache_data.get(key, None)
