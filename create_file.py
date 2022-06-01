# -*- coding: utf-8 -*-
"""根据父级目录，生成 md 文件

用法
  py create-file.py
"""

import os
import sys
from threading import local
import time

# linux 和 windows 下不同的文件路径，若项目路径变动，此处也需修改
LINUX_WORK_CWD = '/home/ym/Documents/githubproject/learn-english/'
WIN_WORKS_CWD = '/mywork/hubproject/learn-english/'

# md 内容模板
md_content = '''
## 1.近义词

## 2.意异词

## 3.僻意词

## 4.短语

## 5.习语

## 6.集合
'''


current_cwd = ''
system_split_char = ''

custome_cwd = ''


def check_env():
    """判断当前运行环境，选择合适的路径"""
    print('env: {}'.format(os.name))
    print('path: {}'.format(os.getcwd()))

    # heck env
    global current_cwd
    if os.name == 'nt':
        current_cwd = WIN_WORKS_CWD[:]
        system_split_char ='\\'
    else:
        current_cwd = LINUX_WORK_CWD[:]
        system_split_char = '/'

    # check path
    if os.getcwd() != current_cwd:
        os.chdir(current_cwd)


def create_file():
    """生成指定语言类型文件
    """
    print("--- creating problems files ---")

    local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print('--- {} ---'.format(local_time))
    file_menu = local_time[0:10].replace('-', '/')
    print(file_menu)

    # if not os.path.exists(os.path.join(custome_cwd,file_year)):

    # 获取模板
    # case_txt, test_txt = read_template()
    # code_file = os.path.join(custome_cwd, 'case01.' +
    #                          script_config.lang_config[sys.argv[2][1:]]['code'])
    # test_file = os.path.join(custome_cwd, 'test.' +
    #                          script_config.lang_config[sys.argv[2][1:]]['code'])

    # if not os.path.exists(code_file):
    #     f_code = open(code_file, 'w')
    #     f_code.write(case_txt)
    #     f_code.close()

    # if not os.path.exists(test_file):
    #     f_test = open(test_file, 'w')
    #     f_test.write(test_txt)
    #     f_test.close()

    # print("--- end ---")


if __name__ == '__main__':
    check_env()
    create_file()
