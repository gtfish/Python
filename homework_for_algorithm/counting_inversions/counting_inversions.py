#!/usr/bin/env python
#coding:utf8

"""
Author          :   Administrator
CreationDate    :   2016-5-13 18:39:40
Description     :
"""

import pdb


def sort_and_count_inv(lis):
    """
    """
    if len(lis) == 1:
        return 0, lis
    else:
        n_sublis = len(lis) / 2
        head_lis = lis[:n_sublis]
        tail_lis = lis[n_sublis:]
        head_inv_cnt, sorted_head_lis = sort_and_count_inv(head_lis)
        tail_inv_cnt, sorted_tail_lis = sort_and_count_inv(tail_lis)
        cur_inv_cnt, merged_lis = merge_and_count_split_inv(sorted_head_lis, sorted_tail_lis)
        return head_inv_cnt + tail_inv_cnt + cur_inv_cnt, merged_lis
#end_def

def merge_and_count_split_inv(lis_a, lis_b):
    """
    """
    len_a = len(lis_a)
    len_b = len(lis_b)
    i = 0
    j = 0
    inv_cnt = 0
    merged_lis = []
    merge_ele = None
    while(i < len_a or j < len_b):
        if i >= len_a:
            merge_ele = lis_b[j]
            j += 1
        elif j >= len_b:
            merge_ele = lis_a[i]
            i += 1
        elif lis_a[i] <= lis_b[j]:
            merge_ele = lis_a[i]
            i += 1
        else:
            merge_ele = lis_b[j]
            inv_cnt += len_a - i
            j += 1
        merged_lis.append(merge_ele)
    return inv_cnt, merged_lis
#end_def

def main():
    """
    """
    #lis = raw_input()
    lis = [1,3,5,2,4,6]
    inv_cnt, sorted_lis = sort_and_count_inv(lis)
    print inv_cnt
    print sorted_lis
    
#end_main

if __name__ == "__main__":
   main()
#end_if

