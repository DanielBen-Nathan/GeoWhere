import pickle
import tensorflow as tf
import matplotlib.pyplot as plt
import cv2
import numpy as np
import os

IMG_SIZE=300

new_model=tf.keras.models.load_model('geoBrainModel1.model')
def read(path,fig):
    img_array=cv2.imread(os.path.join("test\\",path))
    img_array = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)
    img_array=cv2.resize(img_array,(IMG_SIZE,IMG_SIZE))
    
    x=[]

    for features in img_array:
        x.append(features)
          

    x=np.array(x).reshape(-1,IMG_SIZE,IMG_SIZE,3)
    pred=new_model.predict([x])

    #print(pred)
    plt.figure(fig)
    plt.imshow(img_array)
    
    #print(pred)
    #print(pred[0][0])
    lat=pred[0][0]*85
    long=pred[0][1]*180
    print(lat," ",long)
    
   

print("39.4523501,-8.9842991: ",read('39.4523501,-8.9842991\\gsv_0.jpg',1))

print("35.8031728,-106.2178936: ",read('35.8031728,-106.2178936\\gsv_0.jpg',2))

print("46.2318624,-69.2038995: ",read('46.2318624,-69.2038995\\gsv_0.jpg',3))
plt.show()
