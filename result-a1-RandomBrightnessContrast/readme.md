训练日期：2020/8/27  
基本参数：result6  
最后得分：  


数据增强参数：  
type='RandomBrightnessContrast',  
brightness_limit=[0.1, 0.3],  
contrast_limit=[0.1, 0.3],  
p=0.2),  


具体参数：  
resize = 1000,1000  
batchsize = 2  
lr = 0.01  
epoch = 36  
step = [24, 33] #  
aspp =(1,3,6,1)  
pretrain = resnet50 + detectors_cascade_rcnn_r50_1x_coco-32a10ba0.pth  
threshold=0.25/0.3  
