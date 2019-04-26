import sys

sys.setrecursionlimit(10000)
# recursion_times = 0


def quick_sort(input_list):
    print(f'Start to sort list: {input_list}')
    # global recursion_times
    # recursion_times += 1
    # print(f'Current recursion times depth: {recursion_times}')
    if len(input_list) in [0, 1]:
        return input_list

    pivot = input_list[0]
    left_list = [item for item in input_list[1:] if item <= pivot]
    right_list = [item for item in input_list[1:] if item > pivot]
    return quick_sort(left_list) + [pivot] + quick_sort(right_list)
