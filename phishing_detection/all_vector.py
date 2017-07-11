#!/usr/bin/python
#-*-coding:utf-8-*-
import json
from hash_path_builder import get_hash_dir_info
from os.path import join as pjoin
from result import get_html_vector
from url_svm import get_url_vector



def get_web_files_dir_info1(web_dir_info):
        '''
        获取 web_dir_info目录下存在 text.json文件的url，读取其中的 title，keyword，ICP到字典中
        格式为 {url：xxx, url:xxx}
        '''
        url_vector = []
        html_vector = []
        all_vector = []
        for url, web_file in web_dir_info.iteritems():
            for web_path, file_list in web_file.iteritems():
            	if 'url_file' in file_list:
            		with open(pjoin(web_path, 'url_file'), 'r') as f:
            			url = f.read()
            			url_vector = get_url_vector(url)
            	if 'main.txt' in file_list:
            		with open(pjoin(web_path, 'main.txt'), 'r') as f:
            			html = f.read()
            			html_vector = get_html_vector(html)
		        all_vector.extend(url_vector)
		        all_vector.extend(html_vector)
        return all_vector
        print '**************************************************************************'
        print url
        print html_vector
        print '*****************************************************************************'



def get_web_files_dir_info(web_dir_info):
        '''
        获取 web_dir_info目录下存在 text.json文件的url，读取其中的 title，keyword，ICP到字典中
        格式为 {url：xxx, url:xxx}
        '''
        url_vector = []
        html_vector = []
        
        all_result = open('all_result.txt', 'wb')
        for url, web_file in web_dir_info.iteritems():
            for web_path, file_list in web_file.iteritems():
            	all_vector = []
            	if 'url_file' in file_list:
            		with open(pjoin(web_path, 'url_file'), 'r') as f:
            			url = f.read()
            			url_vector = get_url_vector(url)
            	if 'main.txt' in file_list:
            		with open(pjoin(web_path, 'main.txt'), 'r') as f:
            			html = f.read()
            			html_vector = get_html_vector(html)
		        all_vector.extend(url_vector)
		        all_vector.extend(html_vector)
                heuristic_vector_str = [str(vector) for vector in all_vector]
                all_result.write(','.join(heuristic_vector_str)  + ',' + '0' + '\n')
        return all_vector
        print '**************************************************************************'
        print url
        print html_vector
        print '*****************************************************************************'

def get_web_info_dir_info(web_type):
        '''
        获取本地特征信息库中全部指定的web_type的目录信息
        '''
        structure_list = []
        web_info_root_path = pjoin('html/web_info/' + web_type + '_web')
        print 'web_info_root_path is :',web_info_root_path
        hash_dir_info = get_hash_dir_info(web_info_root_path, 4)
        print 'hash_dir_info is :',hash_dir_info
        structure_list = get_web_files_dir_info(hash_dir_info)
        print structure_list

        #print hash_dir_info

get_web_info_dir_info('protected')