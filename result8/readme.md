训练日期：2020/8/20  
数据集：htxt-ship (300张训练/300张测试)  
最后得分：  
  
具体参数：调整了sac   
resize = 1000,1000  
batchsize = 2  
lr = 0.01    
epoch = 36  
step = [24, 33]  
aspp = (1,3,6,1)  
sac = (T,T,T,T) * 2  #默认是(F,T,T,T)*2  
pretrain = resnet50 + detectors_cascade_rcnn_r50_1x_coco-32a10ba0.pth  
threshold=0.25/0.3  
