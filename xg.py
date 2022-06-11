import os #导入模块
filename = '/home/ccf_disk/newbzq/dzy/yolov5/VOCData/images' #文件地址
list_path = os.listdir(filename)  #读取文件夹里面的名字
for index in list_path:  #list_path返回的是一个列表   通过for循环遍历提取元素
    name = index.split('.')[0]   #split字符串分割的方法 , 分割之后是返回的列表 索引取第一个元素[0]
    kid = index.split('.')[-1]   #[-1] 取最后一个
    s=''
    for i in name:
        if i!=' ':
            s=s+i
    path = filename + '/' + index
    new_path = filename + '/'  +s+'.png'
    os.rename(path, new_path) #重新命名

print('修改完成')
