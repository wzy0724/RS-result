训练日期：2020/8/19  
数据集：htxt-ship (300张训练/300张测试)  
最后得分：  

具体参数：  
resize = 1000,1000  
batchsize = 2
lr = 0.01     
epoch = 36    
step = [24, 33]   
aspp =(1,2,3,1) #  
pretrain = resnet50 + detectors_cascade_rcnn_r50_1x_coco-32a10ba0.pth  
threshold=0.25/0.3  
