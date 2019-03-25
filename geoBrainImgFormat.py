import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import random
import pickle

PATH="data_set"
CATORGRIES=["Dog","Cat"]
IMG_SIZE=300

training_data=[]
def read_training_data():
    os.chdir(PATH)
    print(len(os.listdir()))
    for img in os.listdir():
        
        os.chdir(img)
        try:
            img_array=cv2.imread("gsv_0.jpg")
            img_array = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)
            img_array=cv2.resize(img_array,(IMG_SIZE,IMG_SIZE))
            #plt.imshow(new_array)
            #plt.show()
            lat,long=img.split(',')
            long=split_second(long)
            #print(long)
            loc_array=[float(lat)/85.0,float(long)/180.0]
            training_data.append([img_array,loc_array])
        except Exception:
            pass
        os.chdir('..')
    
    os.chdir('..')
def split_second(s):
    found=False
    target='.'
    counter=0
    for char in s:
        if(char=='.' and found):
            print(counter)
            return s[:counter]
        if(char=='.' and not found):
            found=True
        
        counter+=1
    return s

def format_data():
    x=[]
    y=[]
    for features,label in training_data:
        
        x.append(features)
        y.append(label)

    x=np.array(x).reshape(-1,IMG_SIZE,IMG_SIZE,3)
    #y=np.array(y).reshape(1,1)
    return x,y

def saveLoad():
    
    if (not os.path.isfile("pictures.pickle")and  not os.path.isfile("locations.pickle")):
        print("setup data")
        read_training_data()
        random.shuffle(training_data)
        x,y=format_data()
        print(x[0])


        pickle_out=open("pictures.pickle","wb")
        pickle.dump(x,pickle_out)
        pickle_out.close()

        pickle_out=open("locations.pickle","wb")
        pickle.dump(y,pickle_out)
        pickle_out.close()
    else:
        print("read in data")
        pickle_in=open("pictures.pickle","rb")
        x=pickle.load(pickle_in)
        
        pickle_in=open("locations.pickle","rb")
        y=pickle.load(pickle_in)
        print(np.array(y)[0])

saveLoad()
#print(split_second("3.42342.jpg"))
