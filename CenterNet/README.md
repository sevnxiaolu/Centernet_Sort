# Objects as Points 项目在pytorch中实现
#### 基于中心点的检测框架 Centernet是一个端到端的快速目标检测器
#### 使用三元组的一级目标检测框架，检测器将目标定位到一个点上（目标中心点），检测器通过热力图寻找中心点然后回归其他属性（3D位置坐标，方向，姿态）。
#### 非此项目作者，仅作为学习所用
项目原代码地址：https://github.com/xingyizhou/CenterNet
论文链接：[arXiv 1904.07850](http://arxiv.org/abs/1904.07850)   
## 项目部署
### 环境说明
| cuda版本 | pytorch版本 | python版本 |gpu型号 |
| :-----: | :-----: | :------: | :------: |
| 10.2 | 1.7.0 | 3.7.0 | GTX2060 x 1 |
### 准备工作
**需要提前安装好vs2017，编译过程需要**    
**安装cocoapi:https://www.cnblogs.com/yihe/p/8467984.html**   
#### 项目下载安装
```
git clone https://github.com/sevnxiaolu/Centernet.git
pip install -r requirements.txt
```
#### 编译 nms
```
cd src\lib\external
python setup.py build_ext --inplace
```
#### 编译 DCNv2
##### 这里原作者项目内使用的是pytorch0.4版本的，这里以更换成适配1.7版本，所以可直接使用
```
cd src\lib\models\networks\DCNv2
python setup.py build develop
```
## 运行demo
### [下载模型](https://pan.baidu.com/s/1ZiDNR4kOuOrP_ZVPk2MZjA)     
提取码：qwer 
#### 模型下载后存放到models，models.txt内为模型下载地址  
| 模型名称 | 参数 | 说明 |
| :-----: | :-----: | :------: |
| ctdet_coco_dla_2x.pth| ctdet | 执行2D检测 |
| multi_pose_dla_3x.pth| multi_pose | 姿态估计 |
| ddd_3dop.pth| ddd | 执行3D检测 |
#### 使用预训练权重
```
python demo.py *** --demo ../images/ --load_model ../models/***
```
testdemo中写入了三种检测命令  
此处建议先运行testdemo测试本地环境版本
# 注意事项
   3D检测发生错误可能在cv.line划线3D框过程中需要将传入的参数坐标由原始的float转成int类型     
   项目中使用的[DCNv2](https://github.com/lbin/DCNv2/tree/pytorch_1.7)  DCNv2为最新版本(支持pytorch1.5-1.7)      
   执行3D检测时可能出现的错误，由于在cv.line划线（此处生成为3D检测框），需要把传入的坐标参数转换成int型，项目原始类型为float32
   






