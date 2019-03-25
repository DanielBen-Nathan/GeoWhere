import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout,Activation,Flatten,Conv2D,MaxPooling2D,Conv3D
import pickle
import os
import numpy as np
from tensorflow.keras.callbacks import TensorBoard
import time


NAME="geo-cnn-64x2-{}".format(int(time.time()))
tensorboard=TensorBoard(log_dir="logs/{}".format(NAME))


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

x=pickle.load(open("pictures.pickle","rb"))
y=pickle.load(open("locations.pickle","rb"))

x=x/255.0#scale between 0 and 1


model= Sequential()

model.add(Conv2D(32,(5,5),input_shape=x.shape[1:]))#conv layer nodes window size ignore -1 
model.add(Activation("relu"))#activation
model.add(MaxPooling2D(pool_size=(2,2)))#pooling

model.add(Conv2D(64,(5,5), padding='same'))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(128,(5,5), padding='same'))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(256,(5,5), padding='same'))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())#convert 3d feature map to 1d feature vectors
model.add(Dense(64))
model.add(Activation("tanh"))

model.add(Dense(64))
model.add(Activation("tanh"))

model.add(Dense(2))
#model.add(Activation('linear'))#relu's then tanh int output

#, sigs then tanh same output
#sigs then linear same out
#all tanh very simular result/same
#tanhs then lin same output
#tanhs no act in last
#relus in conv tanh in fl no last works :)



model.compile(loss="mean_squared_error",
              optimizer="adam",
              metrics=['accuracy'])

model.fit(x,np.array(y),batch_size=32,epochs=3, validation_split=0.1,callbacks=[tensorboard])
model.save('geoBrainModel1.model')

e=input("\n\ndone")
