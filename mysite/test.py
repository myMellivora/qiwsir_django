import os
# 获取当前文件的绝对路径，其中的__file__是内建变量，表示当前文件
print(os.path.abspath(__file__))
# 获取当前文件所在路径
print(os.path.dirname(os.path.abspath(__file__)))
