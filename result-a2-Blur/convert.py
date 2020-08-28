import six.moves.cPickle as pickle
import os
import cv2
#import  matplotlib.pyplot as plt

path = 'result5.pkl'
f = open(path,'rb')
data = pickle.load(f)
print(len(data))
k = 0

with open("./data/VOCdevkit/VOC2007_val/ImageSets/Main/val.txt","r")as f:
    lines = f.readlines()

#print(lines)
for da in data:
    index = lines[k].split()[0]
    name = index + ".png"
    k+=1
    image_dir = os.path.join("./data/VOCdevkit/VOC2007_val/JPEGImages",name)
    new_image_dir = image_dir.replace("JPEGImages","result")
    image = cv2.imread(image_dir)

    print(image_dir)
    with open("result/"+index+".txt","w") as f:
        for dd in da[0]:
            #res=""
            if dd[-1]<0.25:
                continue
            
            x1 = int(float(dd[0]))
            y1 = int(float(dd[1]))
            x2 = int(float(dd[2]))
            y2 = int(float(dd[3]))
            w = int(dd[2]) - int(dd[0])
            h = int(dd[3]) - int(dd[1])
            cv2.rectangle(image,(x1,y1),(x2,y2),(0,0,255),2)

            res = str(x1) + "," + str(y1) + "," + str(w) + "," + str(h) + "," + str(dd[4]) + ",1"
            #for index,d in enumerate(dd):
               # res +=str(d)
               # res +=","
            f.write(res)
            #f.write("1")
            f.write("\n")
    cv2.imwrite(new_image_dir,image)
     
