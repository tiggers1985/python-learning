#-------------------------------------------------------------------------------------------------------------------------
# 跨包引用
# https://blog.csdn.net/zhili8866/article/details/52980924
# https://www.jianshu.com/p/61ed747680e2
#-------------------------------------------------------------------------------------------------------------------------


import sys
sys.path.append('..') #跨目录import  https://blog.csdn.net/zhili8866/article/details/52980924

from anz_proxy import ANZ_PROXIES

print(ANZ_PROXIES.HTTP_PROXY)