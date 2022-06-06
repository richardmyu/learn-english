# -*- coding: utf-8 -*-

"""根据父级目录，生成 md 文件

用法
  py create-file.py
"""

import os
import time

# linux 和 windows 下不同的文件路径，若项目路径变动，此处也需修改
LINUX_WORK_CWD = '/home/ym/Documents/githubproject/learn-english/'
WIN_WORKS_CWD = '/mywork/hubproject/learn-english/'

CURRENT_CWD = ''

# md 内容模板
MD_TITLE = '# '
MD_CONTENT = '''

## 1.近义词

## 2.意异词

## 3.僻意词

## 4.短语

## 5.习语

## 6.集合
'''


def check_env():
    """判断当前运行环境，选择合适的路径"""

    # heck env
    global CURRENT_CWD
    if os.name == 'nt':
        CURRENT_CWD = WIN_WORKS_CWD[:]
    else:
        CURRENT_CWD = LINUX_WORK_CWD[:]

    # check path
    if os.getcwd() != CURRENT_CWD:
        os.chdir(CURRENT_CWD)
        print('env: {}'.format(os.name))
        print('path: {}'.format(os.getcwd()))


def create_file():
    """生成 md 文件
    """
    print("--- creating problems files ---")
    local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print('--- now: {} ---'.format(local_time))
    file_menu = local_time[0:10].replace('-', os.path.sep)

    try:
        # menu year
        if not os.path.exists(file_menu[0:4]) and os.path.isdir(file_menu[0:4]):
            os.mkdir(file_menu[0:4])
        os.chdir(os.path.join(CURRENT_CWD, file_menu[0:4]))
        # menu month
        if not os.path.exists(file_menu[5:7]) and os.path.isdir(file_menu[5:7]):
            os.mkdir(file_menu[5:7])
        os.chdir(os.path.join(CURRENT_CWD, file_menu[0:7]))
        # menu day
        if not os.path.exists(os.path.join(CURRENT_CWD, file_menu[8:10])):
            with open(file_menu[8:10]+'.md', 'w', encoding='utf-8') as file:
                file.write(
                    MD_TITLE+str(file_menu[5:7])+"."+str(file_menu[8:10]))
                file.write(MD_CONTENT)
                print("--- file: {} create success ---".format(file_menu))
    except Exception as e:
        print("--- file: {} create fail ---".format(file_menu))
        print(e)

    print("--- end ---")


if __name__ == '__main__':
    check_env()
    create_file()
