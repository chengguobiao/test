#!usr/bin/env python
#encoding:utf-8

'''
__Author__:沂水寒城
功能：计算字符串之间的最长公共子序列
'''

def get_lcs(string1, string2):
    '''
    输入：待比较的两个字符串
    输出：降序输出的（子序列长度，子序列）列表
    '''
    string1_list=list(string1)
    string2_list=list(string2)
    lcs_list=[]
    for i in range(len(string1_list)):
        flag=0
        lcs=''
        for j in range(i,len(string1_list)):
            for k in range(flag, len(string2_list)):
                if string1_list[j]==string2_list[k]:
                    lcs+=string1_list[j]
                    flag=k+1
        lcs_list.append((len(lcs), lcs))
    print len(lcs_list)
    return sorted(lcs_list, reverse=True)


if __name__ == '__main__':
    lcs_list=get_lcs("abcdjio7890bhsdjknyewhbnvd", "djio78347bvfdjbnknyew")
    print lcs_list

'''
结果：
26
[(11, 'io77bbknyew'), (10, 'o77bbknyew'), (9, 'ddjbknyew'), (9, 'ddjbknyew'), (9, '77bbknyew'), (8, 'jjbknyew'), 
(8, 'ddjknyew'), (8, 'ddjknyew'), (8, 'ddjknyew'), (8, '8bbknyew'), (7, 'jjknyew'), (7, 'bbknyew'), (7, 'bbknyew'),
 (7, 'bbknyew'), (7, 'bbknyew'), (7, 'bbknyew'), (5, 'nnyew'), (5, 'knyew'), (4, 'bbnn'), (4, 'bbnn'), (3, 'yew'),
  (2, 'vd'), (2, 'nn'), (2, 'ew'), (2, 'dd'), (1, 'w')]
[Finished in 0.5s]
'''