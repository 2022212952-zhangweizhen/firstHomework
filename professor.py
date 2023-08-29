import os
import re
import urllib.request
# 导入urllib.request模块
url = urllib.request.urlopen("https://sdmda.bupt.edu.cn/szdw/js.htm")
# 得到学院教授资料信息官网
html = url.read().decode('utf-8')
# read获取所有信息，并decode()命令将网页的信息进行解码
DepartmentTuple = re.findall('<span class="iden">(.*?)</span>', html)
nameTuple = re.findall('<span class="name">(.*?)</span>', html)
imgTuple = re.findall('<img src="(.*?)" alt="">', html)
# 可以写for循环记录img地址，并且保存到指定路径，通过元组的方式保存
# for i in range(len(imgTuple)):
#     file_path = os.path.join("D:\小学期第一次作业\爬虫得到的照片所存地", nameTuple[i]+".jpg")
#     urllib.request.urlretrieve("https://sdmda.bupt.edu.cn/szdw/js.htm"+imgTuple[i], file_path)
# 按照格式化输出或者用csv文件输出
for i in range(len(imgTuple)):
    print(DepartmentTuple[i]+","+nameTuple[i]+","+"教授,"+"https://sdmda.bupt.edu.cn/szdw/js.htm"+imgTuple[i])