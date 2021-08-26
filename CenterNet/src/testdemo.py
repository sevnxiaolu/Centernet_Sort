#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2021/8/4
# @Author  : Seven
'''

检测示例
python demo.py *** --demo ../images/ --load_model ../models/***

2D目标检测
python demo.py ctdet --demo ../images/ --load_model ../models/ctdet_coco_dla_2x.pth

人体姿态估计测试
python demo.py multi_pose --demo ../images/ --load_model ../models/multi_pose_dla_3x.pth

3D目标检测
python demo.py ddd --demo ../images/ --load_model ../models/ddd_3dop.pth

'''

#测试本地gpu是否能够正常启动
import torch
print(torch.__version__)
print(torch.cuda.is_available())
