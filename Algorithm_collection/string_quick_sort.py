#!usr/bin/env python
#encoding:utf-8

'''
__Author__:沂水寒城
功能：对字符串进行快速排序输出
'''

def get_string_quick_sorted(one_str_list, left, right):
    '''
    输入：待排序的字符串列表,起始位置下标
    输出：标志位下标位置，作为递归的划分界限
    '''
    start=left
    end=right
    tmp=one_str_list[start]
    while start<end:
        while one_str_list[end]>tmp and start<end:
            end-=1
        if start<end:
            one_str_list[start]=one_str_list[end]
            start+=1
        while one_str_list[start]<tmp and start<end:
            start+=1
        if start<end:
            one_str_list[end]=one_str_list[start]
            end-=1
    one_str_list[start]=tmp
    return start


def test(one_str_list, left, right):
    '''
    递归排序的测试函数
    '''
    if left<right:
        p=get_string_quick_sorted(one_str_list, left, right)
        test(one_str_list, left, p-1)
        test(one_str_list, p+1, right)


if __name__ == '__main__':
    i=0
    str_list=['bdsAFha','abcdf','mkjGSAid','hglopdm','mnsdgvjbn']
    for one_str in str_list:
        one_str_list=list(one_str)
        test(one_str_list, 0, len(one_str_list)-1)
        print i
        print 'original_string is:', one_str
        print 'sorted_string is:', ''.join(one_str_list)
        i+=1