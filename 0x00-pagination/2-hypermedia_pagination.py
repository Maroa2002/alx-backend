#!/usr/bin/env python3
"""simple pagination"""

import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates the range of indexes to return in a list for
    particular pagination parameters.

    Args:
        page: page number
        page_size: size of each page
    Returns: tuple of size two containing index and end indexes
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns a page of the dataset.

        Args:
            page (int): Page number.
            page_size (int): Number of items per page.

        Returns:
            List[List]: A list of lists containing the data for requested page
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0

        dataset = self.dataset()
        start_index, end_index = index_range(page, page_size)
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10):
        """
        Hypermedia pagination
        Args:
            page (int): Page number.
            page_size (int): Number of items per page.
        Returns: a dictionary containing the hypermedia info key-value pairs
        """
        dataset = self.get_page(page, page_size)

        entire_dataset = self.dataset()
        total_items = len(entire_dataset)
        total_pages = math.ceil(total_items / page_size)

        prev_page = None
        next_page = None

        if page > 1:
            prev_page = page - 1
        if page < total_pages:
            next_page = page + 1

        hm_dict = {
                'page_size': page_size, 'page': page,
                'data': dataset, 'next_page': next_page,
                'prev_page': prev_page, 'total_pages': total_pages
                }
        return hm_dict
