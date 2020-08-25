# RS-result

1. rfp pretrain添加了预训练模型后效果都变得较差  

2. 修改aspp后，检测框略微少了一些，不是很明显，分值略微波动

3. 调整学习率和step的影响  

4. 调整SAC后，分值略微波动  





  
          结果            预训练模型                 aspp            epoch+step           lr        thr        mAP      

         result0      detectoRS+resnet50          (1,3,6,1)           36(14,25)          0.01       0.5       19.6  

         result1        detectoRS+RFP             (1,2,3,1)           51(20,38)          0.01       0.25      较差
 
         result2        detectoRS+RFP             (1,3,6,1)           51(20,38)          0.01       0.25      较差
    
         result3         resnet50 * 2             (1,3,6,1)           36(14,25)          0.01       0.25      18.3              
         
         result4         resnet50 * 2             (1,2,3,1)           36(14,25)          0.01       0.25      18.4

         result5         resnet50 * 2             (1,3,6,1)           36(14,25)          0.02       0.25      较差
 
         result6      detectoRS+resnet50          (1,3,6,1)           36(24,33)          0.01       0.25      18.86  
         
         result7      detectoRS+resnet50          (1,2,3,1)           36(24,33)          0.01       0.25      18.64
  
         result8      detectoRS+resnet50          (1,3,6,1)           36(24,33)          0.01       0.25      18.41
         
    
    
     
5. 数据增强的影响 (基本参数：result6)


         
         数据增强         RandomFlip      ShiftScaleRotate       RandomRotate      RandomCrop       Brightness       Contrast 
         
           map              18.86 

 





               
                  
