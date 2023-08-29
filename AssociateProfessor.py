import re
import urllib.request
#导入urllib.request模块
url=urllib.request.urlopen("https://sdmda.bupt.edu.cn/szdw/fjs.htm")
#得到学院教授资料信息官网
html = url.read().decode('utf-8')
#read获取所有信息，并decode()命令将网页的信息进行解码
DepartmentTuple = re.findall('<span class="iden">(.*?)</span>', html)
nameTuple = re.findall('<span class="name">(.*?)</span>', html)
imgTuple = re.findall('<img src="(.*?)" alt="">', html)
for i in range(len(imgTuple)):
    print(DepartmentTuple[i]+","+nameTuple[i]+","+"副教授,"+imgTuple[i])
