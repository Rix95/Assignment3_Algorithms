# This is a sample Python script.
import math

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

price_array_base = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]


def recursive_top_down(price_array: list, num_of_cuts):
    print(num_of_cuts, "numcuts")
    if num_of_cuts == 0:
        return 0

    max_price = -math.inf
    print("hbi")
   # lambda x: (max_price = max(max_price, price_array[x] + recursive_top_down(price_array, num_of_cuts - x)
    [(lambda x: max(max_price, price_array[x] + recursive_top_down(price_array, num_of_cuts - x))) for i in range(num_of_cuts + 1)]
    print(max_price)
    # for idx in range(1, num_of_cuts + 1):
    #
    #     max_price = max(max_price, price_array[idx] + recursive_top_down(price_array, num_of_cuts - idx))
    # for idx in range(1, num_of_cuts + 1):
    #
    #     max_price = max(max_price, price_array[idx] + recursive_top_down(price_array, num_of_cuts - idx))
    return max_price




if __name__ == '__main__':
    print(recursive_top_down(price_array_base, 4))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
