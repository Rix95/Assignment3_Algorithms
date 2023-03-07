# This is a sample Python script.
import math

import numpy as np
import numpy as py

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# For simplicity’s sake, 0 is added to keep 1 index consistency.
price_array_base = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]


def recursive_top_down(price_array: list, num_of_cuts):
    if num_of_cuts == 0:
        return 0

    max_price = -math.inf

    for idx in range(1, num_of_cuts + 1):
        max_price = max(max_price, price_array[idx] + recursive_top_down(price_array, num_of_cuts - idx))

    return max_price


def memoized_cut_rod(price_array: list, num_of_cuts: int):
    result_array = np.empty(num_of_cuts + 1)
    result_array.fill(-math.inf)
    print(result_array)

    return memoized_cut_rod_aux(price_array, num_of_cuts, result_array)


def memoized_cut_rod_aux(price_array, num_of_cuts, result_array):
    if result_array[num_of_cuts] >= 0:
        return result_array[num_of_cuts]
    if num_of_cuts == 0:
        max_result = 0
    else:
        max_result = -math.inf
        for idx in range(1, num_of_cuts + 1):
            max_result = max(max_result,
                             price_array[idx] + memoized_cut_rod_aux(price_array, num_of_cuts - idx, result_array))
    result_array[num_of_cuts] = max_result

    return max_result


def extended_bottom_up_cut_rod(price_array, num_of_cuts):
    result_array = np.arange(0.0, num_of_cuts + 1.0)
    choice_array = np.arange(1.0, num_of_cuts + 1.0)

    print(result_array)
    print(choice_array)
    result_array[0] = 0

    for idx in range(1, num_of_cuts + 1):
        max_profit = -math.inf
        for sub_idx in range(1, idx + 1):
            print(idx, sub_idx, "idx  & sub_idx")
            if max_profit < (price_array[sub_idx] + result_array[idx - sub_idx]):
                max_profit = price_array[sub_idx] + result_array[idx - sub_idx]
                choice_array[idx - 1] = sub_idx
        result_array[idx] = max_profit
    return result_array, choice_array


if __name__ == '__main__':
    print(recursive_top_down(price_array_base, 5))
    print(memoized_cut_rod(price_array_base, 5))
    print(extended_bottom_up_cut_rod(price_array_base, 5))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
