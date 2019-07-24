# -*- coding: utf-8 -*-
# @Time : 2019/7/15 9:50
# @Author : Quantum_Ran
# @Email : ai.ei.ui@live.cn
# @File : server_post.py
# @Software: PyCharm
def postData_to_dict(s):
    list1 = s.split('&')
    ret = {L.split('=')[0]: L.split('=')[1] for L in list1}
    return ret

# str1 = 'udid=1b6ae2bcf7ef5283&openudid=1b6ae2bcf7ef5283&device_model=OPPO%20R11&os=Android&os_version=5.1.1&resolution=1440000&device_brand=OPPO%20&offset=0'
# postData_to_dict(str1)
