#!/usr/bin/env python3
"""simple helper function"""

from typing import Tuple


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
