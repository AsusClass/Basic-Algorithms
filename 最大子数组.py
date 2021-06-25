# coding=utf-8
# @Time    : 2021/6/25 14:53
# @Author  : Leo
# @Email   : l1512102448@qq.com
# @File    : 最大子数组.py
import sys
sys.setrecursionlimit(20000)

"""
寻找和最大的非空连续子数组
"""


def find_max_crossing_subarray(arr:list, low:int, mid:int, high:int):
    """
    查找包含中点的最大子数组：
    左边最大+右边最大
    :param arr:list 数组
    :param low:int 第一个元素下标
    :param mid:int 中间元素下标
    :param high:int 最后一个元素下标
    :return:max_low, max_high, left_sum+right_sum  最大子数组的第一个元素, 最后一个元素的下标, 最大子数组的和
    """

    # 从中间元素往回遍历，查找左边最大子数组

    left_sum = float("-inf")
    current_sum = 0
    max_low = 0
    for i in range(mid, low-1, -1):
        current_sum += arr[i]
        if current_sum > left_sum:
            left_sum = current_sum
            max_low = i

    # 从中间元素往后遍历，查找右边最大子数组
    right_sum = float("-inf")
    current_sum = 0
    max_high = 0
    for i in range(mid+1, high+1, 1):
        current_sum += arr[i]
        if current_sum > right_sum:
            right_sum = current_sum
            max_high = i
    return max_low, max_high, left_sum+right_sum



def find_max_subarray(arr:list, low:int, high:int):
    """
    查找最大子数组递归实现(分治法)
    :param arr:list 数组
    :param low:int  第一个元素下标
    :param high:int  最后一个元素下标
    :return: 最大子数组第一个元素下标, 最大子数组最后一个元素下标, 最大子数组和
    """

    # 当数组只有一个元素
    if low >= high:
        return low, high, arr[(low+high)//2]
    else:
        # 中间元素下标
        mid = (low+high) // 2

        # 递归求左边最大子数组
        left_arr_low, left_arr_high, left_arr_sum = find_max_subarray(arr, low, mid-1)

        # 递归求右边最大子数组
        right_arr_low, right_arr_high, right_arr_sum = find_max_subarray(arr, mid+1, high)

        # 求包含中点的最大子数组
        mid_arr_low, mid_arr_high, mid_arr_sum = find_max_crossing_subarray(arr, low, mid, high)

        # 求最大子数组
        if max(left_arr_sum, right_arr_sum, mid_arr_sum) == left_arr_sum:
            return left_arr_low, left_arr_high, left_arr_sum
        elif max(left_arr_sum, right_arr_sum, mid_arr_sum) == right_arr_sum:
            return  right_arr_low, right_arr_high, right_arr_sum
        elif max(left_arr_sum, right_arr_sum, mid_arr_sum) == mid_arr_sum:
            return  mid_arr_low, mid_arr_high, mid_arr_sum




def find_max_subarray2(arr:list, low:int, high:int):
    """
    查找最大子数组暴力求解法
    :param arr:list 数组
    :param low:int  第一个元素下标
    :param high:int  最后一个元素下标
    :return: 最大子数组第一个元素下标, 最大子数组最后一个元素下标, 最大子数组和
    """
    max_sum = float("-inf")
    max_low = 0
    max_high = 0
    current_sum = 0
    for start in range(low, high+1):
        for stop in range(start, high+1):
            current_sum = sum(arr[start:stop+1])
            if current_sum > max_sum:
                max_sum = current_sum
                max_low = start
                max_high = stop
    return max_low, max_high, max_sum






arr = [13, -3, -25, 20, -3, -16,-23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
low, high = 0, len(arr)-1
mid_arr_low, mid_arr_high, mid_arr_sum = find_max_subarray2(arr, low, high)
print(find_max_subarray2(arr, low, high))