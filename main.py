# This is a sample Python script.
import math
import numpy as np
import time
from tabulate import tabulate

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# For simplicity’s sake, 0 is added to keep 1 index consistency.
#                   0  1  2  3  4   5  6   7   8    9  10
price_array_base = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
# global counter variable used to count number of iter/calls
counter = 0


def recursive_top_down(price_array: list, cut_length):
    global counter
    #  print("First function ", cut_length)
    if cut_length == 0:
        return 0, counter

    max_price = -math.inf

    for idx in range(1, cut_length + 1):
        counter += 1
        max_price = max(max_price, price_array[idx] + (recursive_top_down(price_array, cut_length - idx)[0]))

    return max_price, counter


def memoized_cut_rod(price_array: list, cut_length: int):
    #  print("Second function ", cut_length)
    result_array = np.empty(cut_length + 1)
    result_array.fill(-math.inf)
    # print(result_array)

    return memoized_cut_rod_aux(price_array, cut_length, result_array)


def memoized_cut_rod_aux(price_array, cut_length, result_array):
    global counter

    if result_array[cut_length] >= 0:
        return result_array[cut_length], counter
    if cut_length == 0:
        max_result = 0
    else:
        max_result = -math.inf
        for idx in range(1, cut_length + 1):
            counter += 1
            max_result = max(max_result,
                             price_array[idx] + memoized_cut_rod_aux(price_array, cut_length - idx, result_array)[0])
    result_array[cut_length] = max_result

    return max_result, counter


def extended_bottom_up_cut_rod(price_array, cut_length, flag=False, counter=0):
    #  print("Third Function ", cut_length)
    result_array = np.arange(0.0, cut_length + 1.0)
    choice_array = np.arange(1.0, cut_length + 1.0)

    # print(result_array)
    # print(choice_array)
    result_array[0] = 0

    for idx in range(1, cut_length + 1):
        max_profit = -math.inf
        for sub_idx in range(1, idx + 1):
            counter += 1
            # print(idx, sub_idx, "idx  & sub_idx")
            if max_profit < (price_array[sub_idx] + result_array[idx - sub_idx]):
                max_profit = price_array[sub_idx] + result_array[idx - sub_idx]
                choice_array[idx - 1] = sub_idx
        result_array[idx] = max_profit
    # print(counter)

    if flag:
        return choice_array
    return result_array[-1], counter


def get_breakdown(cut_length):
    choice_array = extended_bottom_up_cut_rod(price_array_base, cut_length, True)
    left_rope = cut_length - 1
    break_down = []
    while left_rope > - 1:
        to_be_cut = int(choice_array[left_rope])
        break_down.append(to_be_cut)
        left_rope -= to_be_cut
    return break_down


# main function used to calculate most of the results for the 2D arrays.
def main():
    # number of entries for
    NUMBER_OF_ENTRIES = 5
    user_input_array = []
    function_array = [recursive_top_down, memoized_cut_rod, extended_bottom_up_cut_rod]
    optimal_revenue_array = [[] for i in range(len(function_array))]
    time_values_array = [[] for i in range(len(function_array))]
    break_down_array = []
    iteration_array = [[] for i in range(len(function_array))]

    def measure_time(user_input):
        global counter
        for i in range(len(function_array)):
            counter = 0
            start_time = time.perf_counter()
            current_function = function_array[i]
            results = current_function(price_array_base, user_input)
            # print("current i:", i)
            optimal_revenue = results[0]
            iteration_array[i].append(results[1])
            end_time = time.perf_counter()

            # Calculate elapsed time
            elapsed_time = end_time - start_time

            #  store result values for time, optimal revenue and the breakdown for the rope
            time_values_array[i].append(round(elapsed_time * 1000000, 2))  # store in microseconds
            optimal_revenue_array[i].append(optimal_revenue)

        return

    while NUMBER_OF_ENTRIES > 0:
        user_input = int(input("Please enter the desired length to be cut: "))
        user_input_array.append(user_input)
        measure_time(user_input)
        break_down_array.append(get_breakdown(user_input))
        NUMBER_OF_ENTRIES -= 1

    return user_input_array, optimal_revenue_array, time_values_array, break_down_array, iteration_array


def print_results(value_tuple):


    user_array = value_tuple[0]
    optimal_array = value_tuple[1]
    time_array = value_tuple[2]
    break_array = value_tuple[3]
    iteration_recursion_counter = value_tuple[4]

    print("Optimal Values per function")
    table_optimal = [[user_array] * 3, optimal_array]
    headers_optimal = ["Recursive Topdown", "Memoized Cut Rope", "Extended bottom up cut rod"]
    print(tabulate(table_optimal, headers_optimal, tablefmt="simple_grid"), "\n")

    print("Time allocated per function in microseconds: ")
    table_times = [["RTD"] + time_array[0], ["MCR"] + time_array[1], ["EBUCR"] + time_array[2]]
    headers_times = ["Function"] + user_array
    print(tabulate(table_times, headers_times, tablefmt="simple_grid"), "\n")

    print("Breakdown per desired cut")

    tables_breakdown = [break_array]
    headers_breakdown = user_array
    print(tabulate(tables_breakdown, headers_breakdown, tablefmt="simple_grid"), "\n")

    print("Recursion/Iteration Calls")
    table_counter = [["RTD"] + iteration_recursion_counter[0], ["MCR"] + iteration_recursion_counter[1], ["EBUCR"]
                     + iteration_recursion_counter[2]]
    headers_counter = ["Function"] + user_array
    print(tabulate(table_counter, headers_counter, tablefmt="simple_grid"), "\n")
    return


if __name__ == '__main__':
    print(
        "================================================================================================================")
    print("                                 Developer Ricardo Elizondo")
    print(
        "================================================================================================================")
    print("                              School name: Texas A&M San Antonio")
    print("                                          Algorithms")
    print("                                          Assignment 3")
    print("                                          Submitted  March 19, 2023")
    print("                                 Semester/Year: Spring 2023")
    print(
        "================================================================================================================")
    print("")

    print(
        "This project compares three algorithms to cut up a rope with the most optimal profit as a goal, the program \n"
        "has been designated to tabulate most of the results stored in 2d arrays, the time has been transformed \n"
        "to nano seconds to obtain meaningful results.\n\n")
    #  tester_function(price_array_base, 1)
    solution = main()
    print_results(solution)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
