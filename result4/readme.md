训练日期：2020/8/12  
数据集：htxt-ship (300张训练/300张测试)  
最后得分：xx  
 
具体参数：  
resize = 1000,1000  
batchsize = 2  
lr = 0.01  
epoch = 36  
step = [14,25]  
aspp =(1,2,3,1)   
pretrain = torchvision://resnet50 * 2  
threshold=0.25/0.3  
