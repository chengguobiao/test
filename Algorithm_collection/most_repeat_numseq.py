#!usr/binenv python
#encoding:utf-8

'''
__Author__:沂水寒城
统计一个给定字符串中重复模式数量得到最高重复模式串
'''

def slice(num_str,w):
    '''
    对输入的字符串滑窗切片返回结果列表
    '''
    result_list=[]
    for i in range(len(num_str)-w+1):
        result_list.append(num_str[i:i+w])
    return result_list


def get_repeat_num_seq(num_str):
    '''
    统计重复模式串数量
    '''
    result_dict={}
    result_list=[]
    for i in range(2,len(num_str)):
        one_list=slice(num_str, i)
        result_list+=one_list
    for i in range(len(result_list)):
        if result_list[i] in result_dict:
            result_dict[result_list[i]]+=1
        else:
            result_dict[result_list[i]]=1
    sorted_result_dict=sorted(result_dict.items(), key=lambda e:e[1], reverse=True)
    return sorted_result_dict[0:10]


if __name__ == '__main__':
    num_list=get_repeat_num_seq('4513785645121214545454545457894')
    print num_list

'''
结果：
[('45', 8), ('4545', 5), ('454', 5), ('545', 5), ('54', 5), ('5454', 4), ('454545', 4), ('45454', 4), 
('54545', 4), ('545454', 3)]
[Finished in 0.6s]
'''