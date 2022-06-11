1.先进入VOCdata，把图片和标注的xml文件分别放在imges和Anotations文件夹下，先运行split_train_val.py,
生成一个imageSets/main文件夹，且在其下生成 测试集、训练集、验证集，存放图片的名字。

2.运行text_to_yolo.py文件，运行后会生成如下 labels 文件夹和 dataSet_path 文件夹。其中 labels 中为不同
图像的标注文件。每个图像对应一个txt文件，文件每一行为一个目标的信息，包括class, x_center, y_center, width,
 height格式，这种即为 yolo_txt格式。

3.dataSet_path文件夹包含三个数据集的txt文件，train.txt等txt文件为划分后图像所在位置的路径，
如train.txt就含有所有训练集图像的路径。

4.在 yolov5 目录下的 data 文件夹下 新建一个 myvoc.yaml文件（可以自定义命名），用记事本打开。

内容是：

训练集以及验证集（train.txt和val.txt）的路径（可以改为相对路径）以及 目标的类别数目和类别名称。

5.下载预训练模型，这里可以下载yolov5s,m,l,x权重文件。打开models文件夹找到对应模型的yaml文件，把nc
改成自己需要训练的类别数。然后就可以开始训练了。

6.在runs文件夹下找到训练好的模型，复制文件路径，把路径放到detect.py下就可以用训练好的模型预测图片了。

