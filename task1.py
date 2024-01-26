import time
import sys
from functools import wraps
from typing import Callable
from random import randint


def show_time(func: Callable[..., any]) -> Callable[..., any]:
    @wraps(func)
    def wrapper(*args, **kwargs) -> any:
        start_time = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__}: {time.time() - start_time}")
        return result

    return wrapper


def insertion_sort(iterable: list[any]) -> list[any]:
    for i in range(1, len(iterable)):
        key = iterable[i]
        j = i - 1
        while j >= 0 and key < iterable[j]:
            iterable[j + 1] = iterable[j]
            j -= 1
        iterable[j + 1] = key
    return iterable


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def merge_sort(iterable) -> list[any]:
    if len(iterable) <= 1:
        return iterable

    mid = len(iterable) // 2
    left_half = iterable[:mid]
    right_half = iterable[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def timsort(iterable: list[any]) -> list[any]:
    return list(sorted(iterable))


SORTING_METHODS: dict[str, Callable[[list[any]], list[any]]] = {
    func.__name__: func for func in (insertion_sort, merge_sort, timsort)
}


if __name__ == "__main__":
    unsorted_data: list[int] = [randint(1, 50) for i in range(500)]
    # unsorted_data: list[int] = [randint(1, 50) for i in range(50000)]

    start_time = time.time()
    SORTING_METHODS[sys.argv[1]](unsorted_data)
    print(time.time() - start_time)
