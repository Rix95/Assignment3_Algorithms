# This is a sample Python script.
import math

import numpy as np
import numpy as py

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# For simplicity’s sake, 0 is added to keep 1 index consistency.
price_array_base = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]


def recursive_top_down(price_array: list, length_cut):
    if length_cut == 0:
        return 0

    max_price = -math.inf

    for idx in range(1, length_cut + 1):
        max_price = max(max_price, price_array[idx] + recursive_top_down(price_array, length_cut - idx))

    return max_price


def memoized_cut_rod(price_array: list, cut_length: int):
    result_array = np.empty(cut_length + 1)
    result_array.fill(-math.inf)
    #print(result_array)

    return memoized_cut_rod_aux(price_array, cut_length, result_array)


def memoized_cut_rod_aux(price_array, cut_length, result_array):
    if result_array[cut_length] >= 0:
        return result_array[cut_length]
    if cut_length == 0:
        max_result = 0
    else:
        max_result = -math.inf
        for idx in range(1, cut_length + 1):
            max_result = max(max_result,
                             price_array[idx] + memoized_cut_rod_aux(price_array, cut_length - idx, result_array))
    result_array[cut_length] = max_result

    return max_result


def extended_bottom_up_cut_rod(price_array, cut_length, counter=0):
    result_array = np.arange(0.0, cut_length + 1.0)
    choice_array = np.arange(1.0, cut_length + 1.0)

    #print(result_array)
    #print(choice_array)
    result_array[0] = 0

    for idx in range(1, cut_length + 1):
        max_profit = -math.inf
        for sub_idx in range(1, idx + 1):
            counter+=1
           # print(idx, sub_idx, "idx  & sub_idx")
            if max_profit < (price_array[sub_idx] + result_array[idx - sub_idx]):
                max_profit = price_array[sub_idx] + result_array[idx - sub_idx]
                choice_array[idx - 1] = sub_idx
        result_array[idx] = max_profit
    print("Hey i just met you, ", counter)
    return result_array, choice_array

def get_breakdown(choice_array: list, cut_length):
    left_rope = cut_length - 1
    print(type(left_rope))
    print(type(choice_array))
    break_down = []
    while left_rope > 0:
        print(type(left_rope))
        to_be_cut = int(choice_array[left_rope])
        break_down.append(to_be_cut)
        left_rope -= to_be_cut
    return break_down


if __name__ == '__main__':
    print(recursive_top_down(price_array_base, 7))
    print(memoized_cut_rod(price_array_base, 7))
    tupler = extended_bottom_up_cut_rod(price_array_base,7 )
    print(get_breakdown(tupler[1], 5))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
