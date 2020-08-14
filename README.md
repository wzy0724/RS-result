# RS-result
rfp pretrain添加了预训练模型后效果都变得极差  
修改aspp后，检测框略微少了一些，不是很明显，影响不是很大

              预训练模型                 aspp              epoch+step          lr        mAP      

result0   detectoRS+resnet50          (1,3,6,1)           36(14,25)         0.01      19.6  

result1     detectoRS+RFP             (1,2,3,1)           51(20,38)         0.01    

result2     detectoRS+RFP             (1,3,6,1)           51(20,38)         0.01       
  
result3      resnet50 * 2             (1,3,6,1)           36(14,25)         0.01     

result4      resnet50 * 2             (1,2,3,1)           36(14,25)         0.01    

result5      resnet50 * 2             (1,2,3,1)           36(14,25)         0.02    
