#!usr/bin/env python
#encoding:utf-8

'''
__Author__:沂水寒城
功能：使用Kruskal算法求加权连通图的最小生成树
'''


import random
import time
import numpy


def random_matrix_genetor(vex_num=10):
    '''
    随机图顶点矩阵生成器
    输入：顶点个数，即矩阵维数
    '''
    data_matrix=[]
    for i in range(vex_num):
        one_list=[]
        for j in range(vex_num):
            one_list.append(random.randint(1, 100))
        data_matrix.append(one_list)
    return data_matrix


def Kruskal(data_matrix):
    '''
    Kruskal 算法
    输入：图矩阵
    输出：加权最小生成树总权重
    '''
    vex_num=len(data_matrix)
    kruskal=[]
    weights=[]
    start_set=[]
    end_set=[]
    for i in range(vex_num):
        kruskal.append([i])
        for j in range(i+1,vex_num):
            if data_matrix[i][j]!='N':
                start_set.append(i)
                end_set.append(j)
                weights.append(data_matrix[i][j])
    distance=0
    for i in range(vex_num):
        tmp=numpy.argsort(weights)[0]
        for j in range(vex_num):
            if start_set[tmp] in kruskal[j]:
                m=j
            if end_set[tmp] in kruskal[j]:
                n=j
        if m!=n:
            kruskal[m]=kruskal[m]+kruskal[n]
            kruskal[n]=[]
            distance+=weights[tmp]
        weights.pop(tmp)
        start_set.pop(tmp)
        end_set.pop(tmp)
    print '加权最小生成树总权重为：', distance
    return distance

    

def main_test_func(vex_num=10):
    '''
    主测试函数
    '''
    start_time=time.time()
    data_matrix=random_matrix_genetor(vex_num)
    distance=Kruskal(data_matrix)
    end_time=time.time()
    return end_time-start_time


 
if __name__=='__main__':
    data_matrix=[[0,3,1,'N'],[3,0,2,4],[1,2,0,5],['N',4,5,0]]
    print data_matrix
    Kruskal(data_matrix)   
    
    time_list=[]
    print '----------------------------10顶点测试-------------------------------------'
    time10=main_test_func(10)
    time_list.append(time10)

    print '----------------------------50顶点测试-------------------------------------'
    time50=main_test_func(50)
    time_list.append(time50)

    print '----------------------------100顶点测试-------------------------------------'
    time100=main_test_func(100)
    time_list.append(time100)

    print '----------------------------1000顶点测试-------------------------------------'
    time1000=main_test_func(1000)
    time_list.append(time1000)

    print '---------------------------------时间消耗对比--------------------------------'
    for one_time in time_list:
        print one_time


'''
[[0, 3, 1, 'N'], [3, 0, 2, 4], [1, 2, 0, 5], ['N', 4, 5, 0]]
加权最小生成树总权重为： 7
----------------------------10顶点测试-------------------------------------
加权最小生成树总权重为： 111
----------------------------50顶点测试-------------------------------------
加权最小生成树总权重为： 103
----------------------------100顶点测试-------------------------------------
加权最小生成树总权重为： 116
----------------------------1000顶点测试-------------------------------------
加权最小生成树总权重为： 834
---------------------------------时间消耗对比--------------------------------
0.0
0.010999917984
0.0670001506805
57.513999939
[Finished in 58.1s]
'''