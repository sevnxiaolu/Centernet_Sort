## Centernet_Sort
### Centernet+deepsort完成对行人检测计算跟踪
#### 基于Centernet完成目标检测，deepsort完成对行人的id分配及跟踪
### 配置说明
| cuda版本 | pytorch版本 | python版本 |gpu型号 |
| :-----: | :-----: | :------: | :------: |
| 10.2 | 1.7.0 | 3.7.0 | GTX2060 x 1 |
### 开始前准备工作
**项目检测框架使用Centernet，项目目录下有详细介绍[详见](https://github.com/sevnxiaolu/Centernet)**    

#### 项目部署
```
git clone https://github.com/sevnxiaolu/Centernet_Sort.git
pip install -r requirements.txt
```
##### 在demo_centernet_deepsort中修改主文件目录，检测过程需要调用centernet的2D检测器，默认参数一般不需要修改centernet已集成在项目内
```
#centernet检测器分为三种，在import时调用2D检测
CENTERNET_PATH = './CenterNet/src/lib/'
```
##### 项目运行修改demo_centernet_deepsort参数
```
python demo_centernet_deepsort.py
```
### 性能对比
**AP50 comparsion** 

| model  | (person) AP50 | (all classes) AP50 |
| ------------- | ------------- | ------------- |
| ctdet_coco_dla_2x | 77.30 | 55.13 |
| ctdet_coco_resdcn18 | 68.24 | 44.9 | 
| *yolov3 416 | 66.99 | 49.02 |     


### 说明此项目默认已经完成centernet学习，相较于yolo集成deepsort实现目标检测与跟踪在性能上有一定提升     
# Reference
[1] https://github.com/xingyizhou/CenterNet   
[2] https://github.com/ZQPei/deep_sort_pytorch   
[3] centernet论文链接：[arXiv 1904.07850](http://arxiv.org/abs/1904.07850)   
