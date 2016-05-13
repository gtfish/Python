#!/usr/bin/env python
#coding:utf8

"""
Author          :   Administrator
CreationDate    :   2016-05-11 22:50
Description     :
"""

import pdb


def merge_sorting(lis):
    """
    """
    if len(lis) == 1:
        return lis
    else:
        n_sublis = len(lis) / 2
        head_lis = lis[:n_sublis]
        tail_lis = lis[n_sublis:]
        sorted_head_lis = merge_sorting(head_lis)
        sorted_tail_lis = merge_sorting(tail_lis)
        merged_lis = merge_lis(sorted_head_lis, sorted_tail_lis)
        return merged_lis
#end_def

def merge_lis(lis_a, lis_b):
    """
    """
    len_a = len(lis_a)
    len_b = len(lis_b)
    i = 0
    j = 0
    merged_lis = []
    merge_ele = None
    while(i < len_a or j < len_b):
        if i >= len_a:
            merge_ele = lis_b[j]
            j += 1
        elif j >= len_b:
            merge_ele = lis_a[i]
            i += 1
        elif lis_a[i] < lis_b[j]:
            merge_ele = lis_a[i]
            i += 1
        else:
            merge_ele = lis_b[j]
            j += 1
        merged_lis.append(merge_ele)
    return merged_lis
#end_def

def main():
    """
    """
    #lis = raw_input()
    lis = [1,5,8,7,9,4,3,4,6]
    print merge_sorting(lis)
    
#end_main

if __name__ == "__main__":
   main()
#end_if

