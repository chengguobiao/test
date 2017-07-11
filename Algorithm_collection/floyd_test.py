#!usr/bin/env python
#encoding:utf-8

'''
__Author__:沂水寒城
功能：使用floyd算法求最短路径距离
'''

import random
import time


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


def floyd(data_matrix):
    '''
    输入：原数据矩阵，即：一个二维数组
    输出：顶点间距离
    '''
    dist_matrix=[]
    path_matrix=[]
    vex_num=len(data_matrix)  
    for h in range(vex_num):
        one_list=['N']*vex_num
        path_matrix.append(one_list)
        dist_matrix.append(one_list)
    for i in range(vex_num):
        for j in range(vex_num):
            dist_matrix=data_matrix
            path_matrix[i][j]=j
    for k in range(vex_num):
        for i in range(vex_num):
            for j in range(vex_num):
                if dist_matrix[i][k]=='N' or dist_matrix[k][j]=='N':
                    temp='N'
                else:
                    temp=dist_matrix[i][k]+dist_matrix[k][j]
                if dist_matrix[i][j]>temp:
                    dist_matrix[i][j]=temp
                    path_matrix[i][j]=path_matrix[i][k]
    return dist_matrix, path_matrix
      
 

def main_test_func(vex_num=10):
    '''
    主测试函数
    '''
    data_matrix=random_matrix_genetor(vex_num)
    dist_matrix, path_matrix=floyd(data_matrix)
    for i in range(vex_num):
        for j in range(vex_num):
            print '顶点'+str(i)+'----->'+'顶点'+str(j)+'最小距离为:', dist_matrix[i][j]


if __name__ == '__main__':
    data_matrix=[['N',1,'N',4],[1,'N',2,'N'],['N',2,'N',3],[4,'N',3,'N']]
    dist_matrix, path_matrix=floyd(data_matrix)
    print dist_matrix
    print path_matrix

    time_list=[]

    print '------------------------------节点数为10测试情况------------------------------------'
    start_time0=time.time()
    main_test_func(10)
    end_time0=time.time()
    t0=end_time0-start_time0
    time_list.append(t0)
    print '节点数为10时耗时为：', t0


    # print '------------------------------节点数为50测试情况------------------------------------'
    # start_time1=time.time()
    # main_test_func(50)
    # end_time1=time.time()
    # t1=end_time1-start_time1
    # time_list.append(t1)
    # print '节点数为50时耗时为：', t1


    print '------------------------------节点数为100测试情况------------------------------------'
    start_time1=time.time()
    main_test_func(100)
    end_time1=time.time()
    t1=end_time1-start_time1
    time_list.append(t1)
    print '节点数为100时耗时为：', t1

    print '------------------------------节点数为1000测试情况------------------------------------'
    start_time1=time.time()
    main_test_func(1000)
    end_time1=time.time()
    t3=end_time1-start_time1
    time_list.append(t3)
    print '节点数为100时耗时为：', t3

    print '--------------------------------------时间消耗情况为：--------------------------------'
    for one_time in time_list:
        print one_time